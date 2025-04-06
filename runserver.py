# Create a discord bot that you can send a message to like "start", which starts the server through AWS
# also add stop server function
# output server ip automatically
# If the time elapsed goes over time limit, stop the server automatically
# additional functions
import discord
import requests

DISCORD_TOKEN = 'MTM1Nzk4NDQ2MzU5MzY3MjgwNQ.GHU8_T.N5aMXa1sDUUmI3sczlBw_Tb04cduwL56s7h5js'

intents = discord.Intents.default()
intents.message_content = True

serverOnline = False


def start():
    global serverOnline
    requests.get('https://g7wp4wsopf.execute-api.us-west-1.amazonaws.com/start')
    if not serverOnline:
        serverOnline = True
        return "Starting server..."
    return "Server already started"


def stop():
    global serverOnline
    requests.get('https://2qfh7sff55.execute-api.us-west-1.amazonaws.com/stop')
    if serverOnline:
        serverOnline = False
        return "Stopping server..."
    return "Server already stopped"


class Client(discord.Client):
    async def on_ready(self):  # will run whenever bot is connected to server successfully
        print(f'Logged on as {self.user}')

    async def on_message(self, message):  # event triggers for every message received
        if message.author == client.user:
            return

        if message.content.startswith('$start'):
            await message.channel.send('Status: ' + start())
        elif message.content.startswith('$stop'):
            await message.channel.send('Status: ' + stop())
        # print(f'Message from {message.author}: {message.content}')


client = Client(intents=intents)
client.run(DISCORD_TOKEN)
