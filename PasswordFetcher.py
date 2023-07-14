import subprocess

def get_wifi_passwords():
    # Run netsh command to get Wi-Fi profiles and passwords
    command = "netsh wlan show profile key=clear"
    output = subprocess.check_output(command, shell=True).decode("latin-1")
    
    # Extract profile names and passwords
    profiles = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]
    passwords = []
    for profile in profiles:
        command = f"netsh wlan show profile name=\"{profile}\" key=clear"
        profile_output = subprocess.check_output(command, shell=True).decode("latin-1")
        password_line = [line.split(":")[1].strip() for line in profile_output.split("\n") if "Key Content" in line]
        if password_line:
            passwords.append(password_line[0])

    # Print the Wi-Fi profiles and passwords
    for profile, password in zip(profiles, passwords):
        print("Wi-Fi Profile:", profile)
        print("Password:", password)
        print()

# Main program
if __name__ == "__main__":
    get_wifi_passwords()
