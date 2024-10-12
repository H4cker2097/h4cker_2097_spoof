import os
import time
import re

# Color codes
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"

def print_banner():
    banner = f"""
                  {CYAN}.---:                       :---.{RESET}                   
               {CYAN}.=++*+=+#+                    +#*=+*++=. {RESET}              
             {CYAN}=#*+++=++-=#                    #==++=+++*#= {RESET}            
           {CYAN}=%++**==**-*+#=   {RED}EMAIL{RESET}          =#+*-**==**++%={RESET}           
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

    {YELLOW}[+]{CYAN} Channel : @WOLFDOLLAR
    """
    print(banner)

def spoof_email(spoofed_email, target_email, message):
    """Simulates sending a spoofed email."""
    print(f"{GREEN}Sending email from {spoofed_email} to {target_email}...{RESET}")
    print(f"{GREEN}Message: {message}{RESET}")
    time.sleep(2)  # Simulate email sending duration
    print(f"{GREEN}Email sent successfully!{RESET}")

def get_email(prompt):
    """Prompts the user to enter an email and validates the input."""
    while True:
        email = input(prompt)
        # Check if email matches the pattern: starts with any character followed by @gmail.com
        if re.match(r'^[a-zA-Z0-9].+@gmail\.com$', email):
            return email
        else:
            print(f"{RED}Invalid email. Please enter a valid Gmail address starting with a letter or digit.{RESET}")

def get_work_email(prompt):
    """Prompts the user to enter a work email and validates the input."""
    while True:
        email = input(prompt)
        if "@" in email and "." in email:
            return email
        else:
            print(f"{RED}Invalid email. Please enter a valid work email address.{RESET}")

def get_message(prompt):
    """Prompts the user to enter a message."""
    return input(prompt)

def email_main():
    print_banner()  # Print the banner
    print(f"{CYAN}Welcome to the Email Spoofing Tool!{RESET}")

    while True:
        # Get the spoofed email (must be Gmail and start with a letter or digit)
        spoofed_email = get_email(f"{YELLOW}Enter the spoofed email address : {RESET}")

        # Get the target email (work email)
        target_email = get_work_email(f"{YELLOW}Enter the target email address : {RESET}")

        # Get the message to send
        message = get_message(f"{YELLOW}Enter your message: {RESET}")

        # Simulate sending the email
        spoof_email(spoofed_email, target_email, message)

        # Ask if the user wants to send another email
        continue_choice = input(f"{YELLOW}Do you want to send another email? (yes/no): {RESET}")
        if continue_choice.lower() != 'yes':
            print(f"{CYAN}Exiting Email Spoofing Tool...{RESET}")
            break

    # After exiting the loop, open call.py
    os.system('python call.py')  # Adjust the path if necessary

if __name__ == "__main__":
    email_main()
