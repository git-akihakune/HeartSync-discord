from pathlib import Path
from getpass import getpass
import configparser
import sys



def createConfig():
    input('[*] Creating config file...')
    print("[#] If you don't know what a Discord bot token is, please read https://discordpy.readthedocs.io/en/stable/discord.html")
    token = getpass('[?] Please enter a valid Discord bot token: ')
    configure = configparser.ConfigParser()
    configure['TOKEN'] = {'token': token}
    with open('config.ini', 'w') as configfile:
        configure.write(configfile)
    if Path('config.ini').is_file():
        print('[+] Config file created successfully')
        return None
    print('[-] Failed to create config file. Please run the program again, or report this incident to https://github.com/git-akihakune/HeartSync-discord/issues, or manually create a config file yourself.')
    sys.exit('Failed to create config file.')



def loadConfig():
    print('[*] Loading config file...')
    if Path('config.ini').is_file():
        print('[+] Config file found, loading its content')
    else:
        print('[-] Config file not found, please create a config file before proceed')
        createConfig()
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config