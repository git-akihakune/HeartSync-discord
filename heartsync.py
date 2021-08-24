import discord
import datetime
import configparser

class MyClient(discord.Client):
    async def on_ready(self):
        print (f'Logged in as {self.user} at {datetime.datetime.now()}')
    
    async def on_message(self, message):
        print (f'Message from {message.author}: {message.content}')

if __name__ == '__main__':
    client = MyClient()

    # reading config and executing
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config['TOKEN']['token']
    client.run(token)