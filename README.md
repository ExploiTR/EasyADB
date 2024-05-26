## EasyADB
This Python script allows you to connect to an Android device over ADB (Android Debug Bridge) by setting up and managing your configuration details.

### Overview
The script checks for an existing config.json file in your home directory. If it exists, it loads your configuration (IP address, port, platform folder) and offers the option to update it. If the file doesn't exist, it prompts you to enter these details.

Once the configuration details are set, the script attempts to connect to the specified IP and port using ADB. If the connection fails, you have options to retry, restart the script, or exit.

### How to use
* Run the script using Python 3.
* If config.json exists in your home directory, your current configuration will be displayed. You can choose to update it by entering 'y', update only the port number by entering 'p', or keep it the same by entering 'n'.
* If config.json does not exist, you will be prompted to enter your configuration details.
* The script will attempt to connect to the Android device using the specified IP and port.
* If the connection fails, you can choose to retry by entering 'r', restart the script by entering 're', or exit by entering 'e'.
* After a successful connection, the script lists all connected ADB devices.

> Ensure manually checking adb-wireless on the device once before using the script.
> The platform_folder is the directory where your ADB executable is located. Ensure this is correctly set in your configuration.

> # New
## ADBX Script : Dynamically connects to the device.
This Python script automates the process of setting up an Android device to connect over TCP/IP for ADB (Android Debug Bridge) communication. It is particularly useful for developers who frequently need to switch between devices or reconnect devices without physically connecting them via USB.

### Script Workflow
The script follows a structured workflow to establish a TCP/IP connection with an Android device:

1. **Port Selection**: A random port is chosen within the ephemeral port range (49152-65535) to avoid port conflicts.

2. **Device Detection**: The script executes the `adb devices` command and parses the output using a regular expression to list all connected devices in 'device' mode.

3. **Device Selection**: If multiple devices are detected, the user is prompted to select one by entering the corresponding number displayed in the console.

4. **TCP/IP Configuration**: The selected device is set to listen on the chosen port for TCP/IP connections using the `adb -s <device_id> tcpip <port>` command.

5. **IP Address Retrieval**: The script retrieves the IP address of the device by running the `adb -s <device_id> shell ifconfig wlan0` command and parsing the output for the 'inet addr' field.

6. **TCP/IP Connection**: Finally, the script attempts to connect to the device over TCP/IP using the `adb connect <device_ip>:<port>` command.
