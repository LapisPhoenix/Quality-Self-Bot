import os
from colorama import Fore, Style, init
from discord.ext import commands

class Menu:
    def __init__(self, user: commands.Bot):
        init(autoreset=True)
        self.logo = f'''{Fore.LIGHTBLUE_EX + Style.BRIGHT}     _,ggg,_                                                          
    d8P"""Y8b,                           ,dPYb,        I8             
    88,    "8b,                          IP'`Yb        I8             
     "Y8baaa`8b                          I8  8I  gg 88888888          
        `""" Y8                          I8  8'  ""    I8             
             d8  gg      gg    ,gggg,gg  I8 dP   gg    I8   gg     gg 
,ad8888b,   ,8P  I8      8I   dP"  "Y8I  I8dP    88    I8   I8     8I 
I8P'  `"Y8a,8P'  I8,    ,8I  i8'    ,8I  I8P     88   ,I8,  I8,   ,8I 
I8b,,___,,888b,_,d8b,  ,d8b,,d8,   ,d8b,,d8b,_ _,88,_,d88b,,d8b, ,d8I 
 `"Y88888P"' "Y88P'"Y88P"`Y8P"Y8888P"`Y88P'"Y888P""Y88P""Y8P""Y88P"888
                                                                 ,d8I'
                                                               ,dP'8I 
                                                              ,8"  8I 
                                                              I8   8I 
                                                              `8, ,8I 
                                                               `Y8P"  '''
        
        self.user_data = self.user_info(user=user)
    
    def user_info(self, user: commands.Bot) -> list[str, int, int, str]:
        """ Gets the user info of whoever is logging into the bot."""

        name = user.user
        servers = len(user.guilds)
        friends = len(user.friends)
        prefix = user.command_prefix
        commands = len(user.commands)

        return [name, servers, friends, prefix, commands]
    
    def main(self):
        print(self.logo)
        print(f"{Fore.LIGHTBLUE_EX + Style.BRIGHT}Welcome to A Quality Discord Self Bot!{Fore.RESET + Style.RESET_ALL}".center(35))
        print(f"Logging in as {Fore.LIGHTBLUE_EX + Style.BRIGHT}{self.user_data[0]}{Fore.RESET + Style.RESET_ALL}")
        print(f"Servers: {Fore.LIGHTBLUE_EX + Style.BRIGHT}{self.user_data[1]}{Fore.RESET + Style.RESET_ALL}")
        print(f"Friends: {Fore.LIGHTBLUE_EX + Style.BRIGHT}{self.user_data[2]}{Fore.RESET + Style.RESET_ALL}")
        print(f"Loaded: {Fore.LIGHTBLUE_EX + Style.BRIGHT}{self.user_data[4]}{Fore.RESET + Style.RESET_ALL} commands""")
        print(f"Prefix: {Fore.LIGHTBLUE_EX + Style.BRIGHT}{self.user_data[3]}{Fore.RESET + Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX + Style.BRIGHT}Welcome!{Fore.RESET + Style.RESET_ALL}".center(35))

