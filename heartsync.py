from features import loadconfig
import discord
import datetime

class MyClient(discord.Client):
    async def on_ready(self):
        print (f'[+] Logged in as {self.user} at {datetime.datetime.now()}')
    
    async def on_message(self, message):
        print (f'[#] Message from {message.author}: {message.content}') # for debugging

if __name__ == '__main__':
    client = MyClient()

    # reading config and executing
    config = loadconfig.loadConfig()
    token = config['TOKEN']['token']
    client.run(token)