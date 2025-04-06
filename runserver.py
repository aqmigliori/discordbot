# Create a discord bot that you can send a message to like "start", which starts the server through AWS
# also add stop server function
# output server ip automatically
# If the time elapsed goes over time limit, stop the server automatically
# additional functions
import discord
import requests
import time

DISCORD_TOKEN = 'MTM1Nzk4NDQ2MzU5MzY3MjgwNQ.GzGofw.QvGHVfNeHMrZ8CdPnfApc2m1JBJz0euAemVmD8'

intents = discord.Intents.default()
intents.message_content = True

serverOnline = null


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


def get_ip():
    global serverOnline
    r = requests.get('https://u7qhfk7zg0.execute-api.us-west-1.amazonaws.com/getIP')
    return str(r.json()['ip'])


class Client(discord.Client):
    async def on_ready(self):  # will run whenever bot is connected to server successfully
        print(f'Logged on as {self.user}')

    async def on_message(self, message):  # event triggers for every message received
        if message.author == client.user:
            return

        if message.content.startswith('$start'):
            await message.channel.send('Status: ' + start())
            time.sleep(10)
            await message.channel.send('IP: ' + get_ip())

        elif message.content.startswith('$stop'):
            await message.channel.send('Status: ' + stop())

        elif message.content.startswith('$ip'):
            await message.channel.send('IP: ' + get_ip())
        # print(f'Message from {message.author}: {message.content}')

# def status
# def players_online

client = Client(intents=intents)
client.run(DISCORD_TOKEN)
