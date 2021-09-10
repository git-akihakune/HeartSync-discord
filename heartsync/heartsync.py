#!/usr/bin/env python3

import sys
import datetime

try:
    import discord
except ImportError:
    sys.stderr.write('Impoting discord.py returned error. Please go to https://discordpy.readthedocs.io/en/stable/intro.html for a full documentation or run "pip install -r requirements.txt"')
    sys.exit()

try:
    from features import loadconfig
    from features import colourlogging
except ImportError:
    sys.stderr.write("Feature packages cannot be loaded. Please check if you've got a broken installation.")
    sys.exit()



def boot():
    """ For initializing at startups """
    global log, token

    log = colourlogging.logging()

    config = loadconfig.loadConfig()
    token = config['TOKEN']['token']



class MyClient(discord.Client):
    async def on_ready(self):
        log.success(f'Logged in as {self.user} at {datetime.datetime.now()}')
    
    async def on_message(self, message):
        log.info(f'Message from {message.author}: {message.content}') # for debugging



if __name__ == '__main__':
    boot()
    client = MyClient()
    client.run(token)