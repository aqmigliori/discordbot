# Create a discord bot that you can send a message to like "start", which starts the server through AWS
# also add stop server function
# output server ip automatically
# If the time elapsed goes over time limit, stop the server automatically
# additional functions
import discord
from discord.ext import commands

DISCORD_TOKEN = 'MTM1Nzk4NDQ2MzU5MzY3MjgwNQ.GHU8_T.N5aMXa1sDUUmI3sczlBw_Tb04cduwL56s7h5js'

intents = discord.Intents.default()
intents.message_content = True


# bot = commands.Bot(command_prefix='$', intents=intents)


class Client(discord.Client):
    async def on_ready(self):  # will run whenever bot is connected to server successfully
        print(f'Logged on as {self.user}')

    async def on_message(self, message):  # event triggers for every message received
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello, ' + str(message.author))
        print(f'Message from {message.author}: {message.content}')


# @bot.command()
# async def test(ctx):
#     pass
#
#
# bot.add_command(test)

client = Client(intents=intents)
client.run(DISCORD_TOKEN)
