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
    print("Bot Was Deployed Sucessfully !")
    while True:
        await client.change_presence(game=Game(name='with BadRabbit'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='with Generator'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='this Server', type = 3))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='Viktor Sheen', type = 2))
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel,'<@%s> visit #how-to-gen channel'  %(message.author.id))
    if message.content.startswith('!fortnite'):
        randomlist = ["https://filemedia.net/27527/fortnite","https://up-to-down.net/27832/1","https://up-to-down.net/27527/fortnite02"]
        await client.send_message(message.author,"Your link to Fortnite accounts: " + (random.choice(randomlist)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!minecraft'):
        randomlist1 = ["https://link-to.net/27527/Minecraft001","https://up-to-down.net/27527/minecrafts","https://filemedia.net/27527/Minecraft"]
        await client.send_message(message.author,"Your link to Minecraft accounts: " + (random.choice(randomlist1)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!nitro'):
        randomlist2 = ["We are sorry but we are currently out of Nitro codes."]
        await client.send_message(message.author,"Your link to Nitro codes: " + (random.choice(randomlist2)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content == '!spotify':
        randomlist3 = ["https://direct-link.net/27527/spotify4","https://direct-link.net/27527/spotify2"]
        await client.send_message(message.author,"Your link to Spotify accounts: " + (random.choice(randomlist3)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!nord'):
        randomlist4 = ["https://filemedia.net/27527/NordVPN"]
        await client.send_message(message.author,"Your link to NordVPN accounts: " + (random.choice(randomlist4)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!origin'):
        randomlist5 = ["https://link-to.net/27527/origin","https://up-to-down.net/27527/origin2","https://direct-link.net/27527/origin3"]
        await client.send_message(message.author,"Your link to Origin accounts: " + (random.choice(randomlist5)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!hulu'):
        randomlist6 = ["https://filemedia.net/27527/hulu","https://filemedia.net/27527/hulu2"]
        await client.send_message(message.author,"Your link to Hulu accounts: " + (random.choice(randomlist6)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!steam'):
        randomlist7 = ["https://filemedia.net/27527/steam"]
        await client.send_message(message.author,"Your link to Steam accounts: " + (random.choice(randomlist7)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!pinterest'):
        randomlist8 = ["https://link-to.net/27527/pinterest"]
        await client.send_message(message.author,"Your link to Pinterest accounts: " + (random.choice(randomlist8)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!udemy'):
        randomlist9 = ["https://up-to-down.net/27527/udemy","https://filemedia.net/27527/udemy2"]
        await client.send_message(message.author,"Your link to Udemy accounts: " + (random.choice(randomlist9)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!uplay'):
        randomlist10 = ["https://up-to-down.net/27527/uplay2","https://up-to-down.net/27527/uplay"]
        await client.send_message(message.author,"Your link to Uplay accounts: " + (random.choice(randomlist10)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!crunchyroll'):
        randomlist11 = ["https://up-to-down.net/27527/crunchyroll"]
        await client.send_message(message.author,"Your link to Crunchyroll accounts: " + (random.choice(randomlist11)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!scribd'):
        randomlist12 = ["https://direct-link.net/27527/Scribd"]
        await client.send_message(message.author,"Your link to Scribd accounts: " + (random.choice(randomlist12)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!grammarly'):
        randomlist13 = ["https://direct-link.net/27527/grammarly"]
        await client.send_message(message.author,"Your link to Grammarly accounts: " + (random.choice(randomlist13)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!fuckbook'):
        randomlist14 = ["https://filemedia.net/27527/fcbbook"]
        await client.send_message(message.author,"Your link to Fuckbook accounts: " + (random.choice(randomlist14)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith('!familyowner'):
        randomlist15 = ["https://direct-link.net/27527/familyowner"]
        await client.send_message(message.author,"Your link to Familyowner accounts: " + (random.choice(randomlist15)))
        await client.send_message(message.channel,"Check your DM's")
    if message.content.startswith("!spotifygen"):
        randomlist16 = ["https://direct-link.net/27527/SpotifyGenerator001"]
        await client.send_message(message.author,"Your link to download Spotify Generator is ready: " + (random.choice(randomlist16)))
        await client.send_message(message.channel,"Check your DM's")



client.run(os.getenv("BOT_TOKEN"))
