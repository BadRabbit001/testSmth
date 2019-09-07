# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
import time
from itertools import cycle
from discord.utils import get
from discord import Game
import os

client = commands.Bot(command_prefix='!')
#client = discord.Client()
Clientdiscord = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['web: www.rabbit001.cf', 'With BlackRabbit', 'discord.gg/cZ8GcPF', '!cmds for commands', '!cmds'])

client.remove_command('help')

@client.command()
async def clr(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx):
    check_role = get(ctx.message.guild.roles, name='BAN-SQUAD')
    if check_role in ctx.author.roles:
        await ctx.send("https://gifimage.net/wp-content/uploads/2017/07/ban-hammer-gif-14.gif")
    else:
        await ctx.send("You can't use this!")


@client.event
async def on_ready():
    print("=======================================")
    print()
    print("Hello BlackRabbit#3981")
    print("client id :", client.user.id)
    print()
    print("=======================================")
    game = discord.Game("")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    message.content = message.content.lower().replace(' ', '')
    if message.content.startswith("!hello"):
        print(message.author.name)
        embed = discord.Embed(color=0xFF09D7)
        embed.add_field(name="text", value="https://direct-link.net/27527/spotify3", inline=False)
        embed.add_field(name="Link #2:", value="https://direct-link.net/27527/spotify4", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        
    if message.content.startswith("!nord"):
        print(message.author.name)
        embed = discord.Embed(title="`NordVPN acc`", color=0xFF09D7)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/NordVPN", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)     
        
    if message.content.startswith("!cmds"):
        print(message.author.name)
        embed = discord.Embed(title="**COMMANDS**", color=0xFF09D7)
        embed.add_field(name="Visit my website for list of commands:", value="http://rabbit001.cf/commands.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        
    if message.content.startswith("!commands"):
        print(message.author.name)
        embed = discord.Embed(title="**COMMANDS**", color=0xFF09D7)
        embed.add_field(name="Visit my website for list of commands:", value="http://rabbit001.cf/commands.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)

        
    if message.content.startswith("!minecrafts"):
        print(message.author.name)
        embed = discord.Embed(title="`Minecraft acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://link-to.net/27527/Minecraft001", inline=False)
        embed.add_field(name="Link #2:", value="https://filemedia.net/27527/Minecraft", inline=False)
        embed.add_field(name="Link #3:", value="https://up-to-down.net/27527/minecrafts", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        

    if message.content.startswith("!hulu"):
        print(message.author.name)
        embed = discord.Embed(title="`Hulu acc`", color=0x40cc55)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/hulu2", inline=False)
        embed.add_field(name="Link #2:", value="https://filemedia.net/27527/hulu", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        
        
    if message.content.startswith("!origin"):
        print(message.author.name)
        embed = discord.Embed(title="`Origin acc`", color=668000)
        embed.add_field(name="Your link:", value="https://link-to.net/27527/Origin", inline=False)
        embed.add_field(name="Your link:", value="https://direct-link.net/27527/Origin3", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordappf.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("!uplay"):
        print(message.author.name)
        embed = discord.Embed(title="`Uplay acc`", color=0x666644)
        embed.add_field(name="Your link:", value="https://up-to-down.net/27527/uplay", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("!fortnite"):
        print(message.author.name)
        embed = discord.Embed(title="`Fortnite acc`", color=0x296666)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/fortnite", inline=False)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/fortnite2", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        
    if message.content.startswith("!steam"):
        print(message.author.name)
        embed = discord.Embed(title="`Steam acc`", color=0x796666)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/Steam", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed) 
        
    if message.content.startswith("!spotify"):
        print(message.author.name)
        embed = discord.Embed(title="`Spotify acc`", color=0x996666)
        embed.add_field(name="Your link:", value="https://direct-link.net/27527/spotify4", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed) 
        
    if message.content.startswith("!udemy"):
        print(message.author.name)
        embed = discord.Embed(title="`Udemy acc`", color=0x550000)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/udemy2", inline=False)
        embed.add_field(name="Your link:", value="https://up-to-down.net/27527/udemy", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        
    if message.content.startswith("!scribd"):
        print(message.author.name)
        embed = discord.Embed(title="`Scrib acc`", color=0x840055)
        embed.add_field(name="Your link:", value="https://direct-link.net/27527/Scribd", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        
    if message.content.startswith("!pinterest"):
        print(message.author.name)
        embed = discord.Embed(title="`Pinterest acc`", color=0x8400bb)
        embed.add_field(name="Your link:", value="https://link-to.net/27527/pinterest", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        
    if message.content.startswith("!familyowner"):
        print(message.author.name)
        embed = discord.Embed(title="`Spotify - family owner accs`", color=0xff8400)
        embed.add_field(name="Your link:", value="https://direct-link.net/27527/familyowner", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("!"):
        print(message.author.name)
        embed = discord.Embed(title="`Check your DMs man!`", color=0xaeff84)
        await message.channel.send(embed=embed)
   
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(os.getenv('BOT_TOKEN'))
