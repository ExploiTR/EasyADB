import os
import json
import sys

def format_config(config):
    formatted_config = ""
    for key, value in config.items():
        formatted_config += f"{key}: {value}\n"
    return formatted_config

config_file = os.path.join(os.path.expanduser("~"), "config.json")

if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    print(f"Current configuration:\n{format_config(config)}")
    update = input("Do you want to update the configuration? (y/n/p): ")
    if update.lower() == "y":
        params = ["ip", "port", "platform_folder"]
        print("Select the parameter you want to update:")
        for i, param in enumerate(params):
            print(f"{i+1}. {param}: {config[param]}")
        print(f"{len(params)+1}. All")
        choice = int(input("Enter your choice: "))
        if choice == len(params)+1:
            config["ip"] = input("Enter the IP address: ")
            config["port"] = int(input("Enter the port number: "))
            config["platform_folder"] = input("Enter the platform folder: ")
        elif choice < 1 or choice > len(params):
            print("Invalid choice")
        else:
            param = params[choice-1]
            config[param] = input(f"Enter the new value for {param}: ")
    elif update.lower() == "p":
        config["port"] = int(input("Enter the new port number: "))
    else:
        pass
else:
    config = {}
    config["ip"] = input("Enter the IP address: ")
    config["port"] = int(input("Enter the port number: "))
    config["platform_folder"] = input("Enter the platform folder: ")

with open(config_file, 'w') as f:
    json.dump(config, f)

print(f"Current configuration:\n{format_config(config)}")

platform_folder = config["platform_folder"]
os.chdir(platform_folder)
print(f"Switched to platform folder: {platform_folder}")
command = f"adb connect {config['ip']}:{config['port']}"
output = os.popen(command).read()
print(output)

if "cannot connect" in output:
    while True:
        choice = input("Connection failed. Press r to retry, re to restart script or e to exit: ")
        if choice.lower() == "r":
            output = os.popen(command).read()
            print(output)
            if "connected to" in output:
                break
        if choice.lower() == "re":
            os.execv(sys.executable, ['python'] + sys.argv)
        elif choice.lower() == "e":
            exit()
        else:
            print("Invalid choice.")
else:
    print("Connected successfully.")
    os.system("adb devices")
    input("Press any key to exit...")
