import subprocess
import re
import logging
from time import sleep
import random

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#port
PORT = random.randint(49152, 65535)

def run_command(command,delay):
    sleep(delay)
    logging.info(f"Running command: {command}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    stdout, stderr = process.communicate()
    if stdout:
        logging.debug(f"Command output: {stdout.strip()}")
    if stderr:
        logging.error(f"Command error: {stderr.strip()}")
    return stdout.strip(), stderr.strip()

def list_devices():
    logging.info("Listing devices")
    devices_output, _ = run_command('adb devices',0)
    # Updated regex pattern to match the device ID correctly
    devices = re.findall(r'^([\w\.:-]+)\s+device$', devices_output, re.MULTILINE)
    if len(devices) == 1:
        return devices[0]
    if not devices:
        logging.warning("No devices found.")
        return None
    # Removed the condition that returns when only one device is found
    for index, device in enumerate(devices, start=1):
        logging.info(f"{index}. {device}")
    selected_index = int(input("Select the device by entering the corresponding number: ")) - 1
    return devices[selected_index]

def set_tcpip(device_id):
    logging.info(f"Setting TCP/IP on device {device_id}")
    command = f'adb -s {device_id} tcpip {PORT}'
    output, error = run_command(command,0.5)
    if "TCP mode port" in output:
        logging.info("TCP/IP set successfully")
        return True
    else:
        logging.error(f"Failed to set TCP/IP: {error}")
        return False

def get_device_ip(device_id):
    logging.info(f"Getting IP address for device {device_id}")
    ifconfig_output, ifconfig_err = run_command(f'adb -s {device_id} shell ifconfig wlan0',2)
    if ifconfig_err:
        logging.error(f"Failed to get IP address: {ifconfig_err}")
        return None
    inet_addr = re.search(r'inet addr:(\S+)', ifconfig_output)
    if inet_addr:
        logging.info(f"Device IP address: {inet_addr.group(1)}")
        return inet_addr.group(1)
    else:
        logging.error("IP address not found")
        return None

def connect_over_tcp(device_ip):
    logging.info(f"Connecting over TCP to {device_ip}")
    connect_output, connect_error = run_command(f'adb connect {device_ip}:{PORT}',0)
    if connect_error:
        logging.error(f"Failed to connect over TCP: {connect_error}")
    else:
        logging.info(connect_output)

logging.info("Starting ADBx")
device_id = list_devices()
if device_id:
    if set_tcpip(device_id):
        device_ip = get_device_ip(device_id)
        if device_ip:
            connect_over_tcp(device_ip)
            
input("Press any key to exit...")
