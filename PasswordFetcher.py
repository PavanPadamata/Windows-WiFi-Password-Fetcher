import subprocess

def get_wifi_passwords():
    # Run netsh command to get Wi-Fi profiles
    command = "netsh wlan show profile"
    output = subprocess.check_output(command, shell=True).decode("latin-1")
    
    # Extract profile names
    profiles = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]

    # Extract passwords for each profile
    for profile in profiles:
        profile_command = f'netsh wlan show profile name="{profile}" key=clear'
        profile_output = subprocess.check_output(profile_command, shell=True).decode("latin-1")

        # Extract password if available
        password_line = [line.split(":")[1].strip() for line in profile_output.split("\n") if "Key Content" in line]
        password = password_line[0] if password_line else "No Password"

        # Print the Wi-Fi profile and password
        print("Wi-Fi Profile:", profile)
        print("Password:", password)
        print()

# Main program
if __name__ == "__main__":
    get_wifi_passwords()
