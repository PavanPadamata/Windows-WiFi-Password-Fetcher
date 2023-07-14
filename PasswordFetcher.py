import subprocess
import os
import time
import webbrowser

def display_logo():
    logo = r"""
   __      __.__   _____.__       .__                         __               
  /  \    /  \__|_/ ____\__|______|__| ____    ____   _______/  |_  ___________ 
  \   \/\/   /  \   __\|  \_  __ \  |/    \  / ___\ /  ___/\   __\/  _ \_  __ \
   \        /|  ||  |  |  ||  | \/  |   |  \/ /_/  >\___ \  |  | (  <_> )  | \/
    \__/\  / |__||__|  |__||__|  |__|___|  /\___  /____  > |__|  \____/|__|   
         \/                              \//_____/     \/                   """

    print(logo)
    print("By Pavan Padamata\n")

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

    # Create output folder with loading animation
    print("Creating output folder...")
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        print(f"\r{animation[i % len(animation)]}", end="")
    print("\n")

    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save Wi-Fi information to a text file with loading animation
    print("Saving Wi-Fi information...")
    for i in range(20):
        time.sleep(0.1)
        print(f"\r{animation[i % len(animation)]}", end="")
    print("\n")

    output_file = os.path.join(output_folder, "wifi_info.txt")
    with open(output_file, "w") as file:
        for profile, password in wifi_info:
            file.write(f"Wi-Fi Profile: {profile}\n")
            file.write(f"Password: {password}\n\n")

    print(f"Wi-Fi information saved to: {output_file}")

    # Print additional message, wait for 2 seconds, and open GitHub repository link
    print("Follow me on GitHub and ⭐Star this Repository.")
    time.sleep(2)
    webbrowser.open("https://github.com/PavanPadamata")

# Main program
if __name__ == "__main__":
    display_logo()
    print("Fetching Wi-Fi information...")
    # Add loading animation
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        print(f"\r{animation[i % len(animation)]}", end="")
    print("\n")
    get_wifi_passwords()
