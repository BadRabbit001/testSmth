# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle

client = commands.Bot(command_prefix='.')
#client = discord.Client()


# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle

#TOKEN = process.env.BOT_TOKEN
#TOKEN = 'NjAwMjgyODA2MzQxNDY4MTYx.XSxhug.CdE5SULghOlZyKIg7GvCmbxm-z8'

client = commands.Bot(command_prefix='.')
#client = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['with the &help command.', 'with the developers console', 'with some code', 'with JavaScript'])

@client.event
async def on_message(message):
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!fortnite'):
        randomlist = ['opt1','opt2','opt3']
        msg = 'Hello ' + author + '. Your link: '
        await message.channel.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!Spotify'):
        randomlist = ['opt1','opt2','opt3']
        msg = 'Hello ' + author + '. Your link: '
        await message.channel.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!nord'):
        randomlist = ['opt1','opt2','opt3']
        msg = 'Hello ' + author + '. Your link: '
        await message.channel.send(msg + (random.choice(randomlist)))
        
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(os.getenv('BOT_TOKEN'))
