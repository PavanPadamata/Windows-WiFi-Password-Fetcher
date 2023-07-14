import subprocess
import os

def get_wifi_passwords():
    # Run netsh command to get Wi-Fi profiles
    command = "netsh wlan show profile"
    output = subprocess.check_output(command, shell=True).decode("latin-1")
    
    # Extract profile names
    profiles = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]

    # Extract passwords for each profile
    wifi_info = []
    for profile in profiles:
        profile_command = f'netsh wlan show profile name="{profile}" key=clear'
        try:
            profile_output = subprocess.check_output(profile_command, shell=True).decode("latin-1")
        except subprocess.CalledProcessError:
            continue

        # Extract password if available
        password_line = [line.split(":")[1].strip() for line in profile_output.split("\n") if "Key Content" in line]
        password = password_line[0] if password_line else "No Password"

        # Append Wi-Fi profile and password to the list
        wifi_info.append((profile, password))

    # Create output folder if it doesn't exist
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write Wi-Fi information to a text file
    output_file = os.path.join(output_folder, "wifi_info.txt")
    with open(output_file, "w") as file:
        for profile, password in wifi_info:
            file.write(f"Wi-Fi Profile: {profile}\n")
            file.write(f"Password: {password}\n\n")

    print(f"Wi-Fi information saved to: {output_file}")

# Main program
if __name__ == "__main__":
    get_wifi_passwords()
