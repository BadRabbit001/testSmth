import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import asyncio
import time
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    activity = discord.Game(name="with Generator")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    author = '{0.author.mention}'.format(message)
    if message.content.startswith('!help'):
        msg = author + ' visit #how-to-gen channel'
        await message.channel.send(msg)
    if message.content.startswith('!fortnite'):
        randomlist = ["https://filemedia.net/27527/fortnite","https://up-to-down.net/27832/1","https://up-to-down.net/27527/fortnite02"]
        msg = 'Hello python ' + author 
        await message.channel.send(msg + (random.choice(randomlist)))

bot.run(NjAwNzMxNzUyNjA0MTA2Nzcx.XS7fEA.uyOPZ3SzQcks9TIf96dcV1ow4aw)
