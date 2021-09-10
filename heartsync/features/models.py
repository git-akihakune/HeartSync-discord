from features.colourlogging import logging
import discord
import datetime

log = logging()

class MyClient(discord.Client):
    async def on_ready(self):
        log.success(f'Logged in as {self.user} at {datetime.datetime.now()}')
    
    async def on_message(self, message):
        log.info(f'Message from {message.author}: {message.content}') # for debugging