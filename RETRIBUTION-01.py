import os
import time

# Define Matrix theme commands
matrix_commands = [
    "Accessing mainframe...",
    "Decrypting security protocols...",
    "Hacking into database...",
    "Bypassing firewalls...",
    "Executing code injection...",
    "Downloading classified files..."
]

# Define Matrix color scheme
MATRIX_GREEN = '\033[92m'
MATRIX_BLACK = '\033[30m'
MATRIX_RESET = '\033[0m'

# Display Matrix theme with loading messages
def display_matrix_theme():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    for command in matrix_commands:
        print(f"{MATRIX_GREEN}{command}{MATRIX_RESET}")
        time.sleep(1)  # Add a delay for effect
    print("\nLoading complete. Initiating system...\n")  # Additional message
    time.sleep(1)  # Delay before displaying ASCII art logo

# ASCII art logo
logo = f"""
{MATRIX_GREEN}
░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓██████▓▒░    ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░  """

# Command system
def command_system():
    while True:
        command = input("\nEnter a command ('exit' to quit): ")
        if command.lower() == 'exit':
            break
        elif command.lower() == 'shutdown':
            print("Shutting down the system...")
            time.sleep(2)
            break
        elif command.lower() == 'help':
            print(f"{MATRIX_GREEN}List of available commands:{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}1. shutdown - Shutdown the system{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}2. help - Display this help message{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}3. run program - Execute a program{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}4. open file - Open a file{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}5. check status - Check system status{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}6. infect server - Infect a server with Retribution{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}7. scan network - Scan the network for vulnerabilities{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}8. launch attack - Enact Retribution{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}9. Initiate FailSafe - Initiate FailSafe sequence{MATRIX_RESET}")
            print(f"{MATRIX_GREEN}10. hide traces - Hide traces of Retribution{MATRIX_RESET}")
        elif command.lower() == 'run program':
            print("Running program...")
            time.sleep(2)
        elif command.lower() == 'open file':
            print("Opening file...")
            time.sleep(2)
        elif command.lower() == 'check status':
            print("Checking system status...")
            time.sleep(2)
            print("Antivirus Detection: Undetected")
            time.sleep(2)
            print("Retribution.EXE: Growing")
            time.sleep(2)
            print("Nexus servers: BREACHED")
            time.sleep(2)
            print("EST Time until full corruption: 4 days")
            time.sleep(2)
        elif command.lower() == 'infect servers':
            print("Infecting nexus servers with Retribution...")
            time.sleep(2)
        elif command.lower() == 'scan network':
            print("Scanning the nexus for vulnerabilities...")
            time.sleep(2)
        elif command.lower() == 'launch attack':
            print("Enacting Retribution...")
            time.sleep(2)
        elif command.lower() == 'initiate failsafe':
            print("Initiating full-system wipe sequence...")
            time.sleep(2)
        elif command.lower() == 'hide traces':
            print("Hiding traces of Retribution...")
            time.sleep(2)
        else:
            print(f"{MATRIX_GREEN}Command '{command}' not recognized. Type 'help' for a list of commands.{MATRIX_RESET}")
# Main function
def main():
    display_matrix_theme()  # Display loading messages
    display_logo_with_delay(logo, delay=0.01)  # Display ASCII art logo character by character
    command_system()  # Enter the command system

# Function to display logo character by character with delay
def display_logo_with_delay(logo, delay):
    for char in logo:
        print(char, end='', flush=True)
        time.sleep(delay)

if __name__ == "__main__":
    main()  # Call the main function
