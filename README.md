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
