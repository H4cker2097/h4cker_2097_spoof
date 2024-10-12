import random
import time
import sys
import os

# Color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
LRED = "\033[91m"
LGREEN = "\033[92m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

def print_banner():
    banner = f"""
                  {CYAN}.---:                       :---.{RESET}                   
               {CYAN}.=++*+=+#+                    +#*=+*++=. {RESET}              
             {CYAN}=#*+++=++-=#                    #==++=+++*#= {RESET}            
           {CYAN}=%++**==**-*+#=   {RED}CALL{RESET}          =#+*-**==**++%={RESET}           
         {CYAN}.#*+***=+**-*+##+.   {GREEN}SPOOFING{RESET}   .+*%+*-**+=***+*%: {RESET}         
        {CYAN}-%=****-***=+*=%@+=            =+@%=*+=***-****=%- {RESET}       
       {CYAN}-%=****-****-***++@#.          .#@++***-****-****=%- {RESET}      
      {CYAN}.%=****=+***+=****-=%@=*:=#%=.*=@%=-****=+***+=****=%. {RESET}     
      {CYAN}*+*****-****=*****-+=#%*%#@@#%*%#=+-*****=****-*****=# {RESET}     
     {CYAN}.%=****=+****-*-..::%@@@+@@@@@@*@@@%-:..-*-****+=****=#. {RESET}    
     {CYAN}++*****-*+-:::.    @@@@@*%@@@@%*@@@@@    .:::-+*-*****++ {RESET}    
     {CYAN}*=***++-=         :@@@@@@##@@##@@@@@@:         =-++***=# {RESET}    
     {CYAN}*=+:               %@@%#@@@##@@@##@@%               :+=# {RESET}    
     {CYAN}+-            .... =@@@+@@@@@@@@+@@@= ....            -* {RESET}    
     {CYAN}=          *@@@@@@@+@@@=@@@@@@@@=@@@+@@@@@@@*          = {RESET}    
               {CYAN}:@@@@@@@@+@@%##%@@@@@###@@+@@@@@@@@: {RESET}              
               {CYAN}.@@@@##%@+@@%*@@@@@@@@*%@@+@%##@@@@. {RESET}              
                {CYAN}.*@@@@%#*+@@#%@@@@@@%#@@+*#%@@@@#: {RESET}               
                  {CYAN}.=#@@@@*%@@-*+--+*-@@%*@@@@#=. {RESET}                  
                      {CYAN}.=@+@@:.    .-@@+@#=: {RESET}                      
                          {CYAN}#*@=      =@*# {RESET}                          
                         {CYAN}:%=@+      +@=%: {RESET}                        
                       {CYAN}+****%*+=  =+*%****+ {RESET}                       
                        {CYAN}.-.=-        -=.-. {RESET}                         

    {LRED}[{LGREEN}+{LRED}] {GREEN}Channel : {LGREEN}@WOLFDOLLAR
    """
    print(banner)

def spoof_call(spoofed_number, target_number):
    """Simulates making a spoofed call."""
    print(f"{GREEN}Initiating call from {spoofed_number} to {target_number}...{RESET}")
    time.sleep(2)  # Simulate the call duration
    # Removed lines below
    # print(f"{GREEN}Call connected! You are now speaking with {target_number}.{RESET}")
    # print(f"{CYAN}... [Call in progress] ...{RESET}")
    time.sleep(5)  # Simulate a call duration
    print(f"{GREEN}Call ended.{RESET}")

def open_call_script():
    """Opens the CALL.PY script."""
    os.system('python call.py')  # This will run CALL.PY without displaying a message

def get_10_digit_number(prompt, allow_three=False):
    """
    Prompts the user to enter a 10-digit number and validates the input.
    If `allow_three` is True, the user can enter '3' to open call.py.
    """
    while True:
        number = input(prompt)
        if allow_three and number == '3':
            return number
        elif number.isdigit() and len(number) == 10:
            return number
        else:
            print(f"{RED}Invalid input. Please enter a valid 10-digit number.{RESET}")

def main():
    print_banner()  # Print the banner
    print(f"{CYAN}Welcome to the Call Spoofing 2097 Tool!{RESET}")

    while True:
        # Get user input for the target number, allowing "3" to open CALL.PY
        target_number = get_10_digit_number(f"{YELLOW}Enter the target number you want to call : {RESET}", allow_three=True)
        if target_number == '3':
            open_call_script()  # Open CALL.PY if the user enters '3'
            return  # Exit this script after opening CALL.PY
        
        # Get the spoofed number (10 digits only)
        spoofed_number = get_10_digit_number(f"{YELLOW}Enter the spoofed number: {RESET}")
        
        # Simulate the call
        spoof_call(spoofed_number, target_number)

        # Ask if the user wants to continue or open CALL.PY
        continue_choice = input(f"{YELLOW}Do you want to make another call? (yes/no): {RESET}")
        if continue_choice.lower() != 'yes':
            print(f"{CYAN}Opening the main menu...{RESET}")
            open_call_script()  # Opens CALL.PY instead of exiting
            return  # Exit this script and open CALL.PY

if __name__ == "__main__":
    main()
