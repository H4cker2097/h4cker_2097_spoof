import os
import sys

# Color codes for terminal output
RESET = "\033[0m"
BOLD = "\033[1m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"

def print_title():
    title = f"""
{BLUE}{BOLD}        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/\\
    \\___)=(___/

{MAGENTA}               {BOLD}H4CKER_2097 TOOL{RESET}
{YELLOW}==================================================
    {CYAN}{BOLD}Welcome to the H4CKER_2097 TOOL!{RESET}
"""
    print(title)

def print_menu():
    menu_options = [
        "Call Spoofing",
        "Email Spoofing",
        "Help",
        "Exit"
    ]
    print(f"{MAGENTA}{BOLD}Choose an option:{RESET}")
    for i, option in enumerate(menu_options, 1):
        print(f"{i}. {CYAN}{BOLD}{option}{RESET}")
    print()  # Add a blank line for better spacing

def run_tool(script_name):
    """Runs the specified script."""
    if not os.path.isfile(script_name):
        print(f"{YELLOW}Error: The script '{script_name}' was not found.{RESET}")
        return
    
    try:
        # Execute the script in a separate context
        with open(script_name) as f:
            code = f.read()
            exec(code, globals())
    except Exception as e:
        print(f"{YELLOW}Error while executing '{script_name}': {e}{RESET}")

def main():
    print_title()
    while True:
        print_menu()
        choice = input(f"{YELLOW}Enter your choice (1-4): {RESET}")

        # Map choices to script paths
        script_map = {
            '1': 'spoofing_tools/call_spoofing.py',
            '2': 'spoofing_tools/email_spoofing.py',
            '3': 'help.py'
        }

        if choice in script_map:
            run_tool(script_map[choice])
        elif choice == '4':
            print(f"{CYAN}Exiting...{RESET}")
            sys.exit(0)
        else:
            print(f"{YELLOW}Invalid choice. Please select a number between 1 and 4.{RESET}")

if __name__ == "__main__":
    main()
