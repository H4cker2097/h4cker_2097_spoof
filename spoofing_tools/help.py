def print_banner():
    """Prints the banner with your name."""
    banner = f"""
\033[32m                  .---:                       :---.                   
               .=++*+=+#+                    +#*=+*++=.               
             =#*+++=++-=#                   #==++=+++*#=            
           =%++**==**-*+#=                =#+*-**==**++%=           
         .#*+***=+**-*+##+.              .+*%+*-**+=***+*%:         
        -%=****-***=+*=%@+=            =+@%=*+=***-****=%-       
       -%=****-****-***++@#.          .#@++***-****-****=%-      
      .%=****=+***+=****-=%@=*:=#%=.*=@%=-****=+***+=****=%.     
      *+*****-****=*****-+=#%*%#@@#%*%#=+-*****=****-*****=#     
     .%=****=+****-*-..::%@@@+@@@@@@*@@@%-:..-*-****+=****=#.    
     ++*****-*+-:::.    @@@@@*%@@@@%*@@@@@    .:::-+*-*****++    
     *=***++-=         :@@@@@@##@@##@@@@@@:         =-++***=#    
     *=+:               %@@%#@@@##@@@##@@%               :+=#    
     +-            .... =@@@+@@@@@@@@+@@@= ....            -*    
     =          *@@@@@@@+@@@=@@@@@@@@=@@@+@@@@@@@*          =    
               :@@@@@@@@+@@%##%@@@@@###@@+@@@@@@@@:               
               .@@@@##%@+@@%*@@@@@@@@*%@@+@%##@@@@.               
                .*@@@@%#*+@@#%@@@@@@%#@@+*#%@@@@#:                
                  .=#@@@@*%@@-*+--+*-@@%*@@@@#=.                  
                      .=@+@@:.    .-@@+@#=:                       
                          #*@=      =@*#                            
                         :%=@+      +@=%:                           
                       +****%*+=  =+*%****+                         
                        .-.=-        -=.-.                         
    """
    print(banner)

def display_help():
    """Displays help information including Telegram ID and group."""
    telegram_id = "@jeansonjemesancheta"  # Replace with your actual Telegram ID
    telegram_group = "https://t.me/addlist/NBNkoWhVh4hjMTFl"  # Replace with your actual group link

    print_banner()  # Print the banner with your name
    print(f"\n\033[36mFor assistance, you can reach me on Telegram:")
    print(f"\033[93mTelegram ID: {telegram_id}")
    print(f"\033[93mJoin our Telegram group: {telegram_group}")
    print("\033[35m\nThank you for using the Email Spoofing Tool!")

if __name__ == "__main__":
    display_help()
