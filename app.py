# Work with Py xxx
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


msgg = '```Check your DMs man!```'

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
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
 
 
 if message.content.startswith("!invite"):
        print(message.author.name)
        msg = 'I sent invite link into your DMs man!'
        embed = discord.Embed(color=0xFF09D7)
        await message.channel.send('Check your DMs!')
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed) 
	
        
 if message.content.startswith("!stock"):
        print(message.author.name)
        msg = 'Check DMs!'
        embed = discord.Embed(color=0xFF09D7)
        embed.add_field(name="I can't display stock but you can check my #gen-announcmenets channel on my server, if you aren't on my server here is invite link tho", value="https://discord.gg/2ZnMK4m", inline=False)
        await message.author.send(embed=embed) 
        await message.channel.send('Check your DMs!')
        
 if message.content.startswith("!scribd"):
        print(message.author.name)
        msg = '```Check your DMs man!```'
        embed = discord.Embed(title="`Scrib acc`", color=0x840055)
        embed.add_field(name="Your link:", value="https://direct-link.net/27527/Scribd", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
        
 if message.content.startswith("!cmds"):
        print(message.author.name)
        embed = discord.Embed(title="**COMMANDS**", color=0xFF09D7)
        embed.add_field(name="Visit my website for list of commands:", value="http://rabbit001.cf/commands.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
		
        
 if message.content.startswith("!commands"):
        print(message.author.name)
        embed = discord.Embed(title="**COMMANDS**", color=0xFF09D7)
        embed.add_field(name="Visit my website for list of commands:", value="http://rabbit001.cf/commands.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
	        
 if message.content.startswith("!grammarly"):
        print(message.author.name)
        msg = '```Check your DMs man!```'
        embed = discord.Embed(title="`Grammarly acc`", color=0x840055)
        embed.add_field(name="Your link:", value="https://direct-link.net/27527/grammarly", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapfp.com/oauth2/authorize?client_id=60496724186339f7376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
        
 if message.content.startswith("!minecraft"):
        print(message.author.name)
        embed = discord.Embed(title="`Minecraft acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://link-to.net/27527/Minecraft001", inline=False)
        embed.add_field(name="Link #2:", value="https://filemedia.net/27527/Minecraft", inline=False)
        embed.add_field(name="Link #3:", value="https://up-to-down.net/27527/minecrafts", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
		
		        
 if message.content.startswith("!hulu"):
        print(message.author.name)
        embed = discord.Embed(title="`Hulu acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/hulu2", inline=False)
        embed.add_field(name="Link #2:", value="https://filemedia.net/27527/hulu", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
		
				        
 if message.content.startswith("!origin"):
        print(message.author.name)
        embed = discord.Embed(title="`Origin acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://link-to.net/27527/Origin", inline=False)
        embed.add_field(name="Link #2:", value="https://direct-link.net/27527/Origin3", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
		
						        
 if message.content.startswith("!uplay"):
        print(message.author.name)
        embed = discord.Embed(title="`Uplay acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://up-to-down.net/27527/uplay", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
								        
 if message.content.startswith("!steam"):
        print(message.author.name)
        embed = discord.Embed(title="`Steam acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/Steam", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
							        
				        
 if message.content.startswith("!fortnite"):
        print(message.author.name)
        embed = discord.Embed(title="`Fortnite acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/fortnite", inline=False)
        embed.add_field(name="Link #2:", value="https://filemedia.net/27527/fortnite2", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
		
				        
 if message.content.startswith("!spotify"):
        print(message.author.name)
        embed = discord.Embed(title="`Spotify acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://direct-link.net/27527/spotify4", inline=False)
        embed.add_field(name="Link #2:", value="https://direct-link.net/27527/spotify3", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
						        
 if message.content.startswith("!nord"):
        print(message.author.name)
        embed = discord.Embed(title="`NordVPN acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="https://filemedia.net/27527/NordVPN", inline=False)
        embed.add_field(name="__**Tutorial:**__", value="http://rabbit001.cf/tutorial/video.html", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')
   						        
 if message.content.startswith("!pinterest"):
        print(message.author.name)
        embed = discord.Embed(title="`Pinterest acc`", color=0x400cc1)
        embed.add_field(name="Your link:", value="ttps://link-to.net/27527/pinterest", inline=False)
        embed.add_field(name="Invite this bot on your server!", value="https://discordapp.com/oauth2/authorize?client_id=604967241863397376&permissions=8&scope=bot", inline=False)
        await message.author.send(embed=embed)
        await message.channel.send('Check your DMs!')   		

   
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(' ____  _            _    ____       _     _     _ _    ___   ___  _')
    print('| __ )| | __ _  ___| | _|  _ \ __ _| |__ | |__ (_) |_ / _ \ / _ \/ |')
    print('|  _ \| |/ _` |/ __| |/ / |_) / _` |  _ \|  _ \| | __| | | | | | | |')
    print('| |_) | | (_| | (__|   <|  _ < (_| | |_) | |_) | | |_| |_| | |_| | |')
    print('|____/|_|\__,_|\___|_|\_\_| \_\__,_|_.__/|_.__/|_|\__|\___/ \___/|_|')
    print('====================================================================')
    print('“Hacking is a talent. You will not learn it at school. It is like being Messi or C.Ronaldo.')
    print('If you were born to become a Hacker, it is your destiny. Otherwise, you will be Hacked.”')
    print('― Amine Essiraj')
    print('===========================================================================================')
    print('“Shvatio sam… Da nema čoveka, kompjuter ne bi postojao. Da nema kompjutera,')
    print('mnogi ljudi ne bi naučili šta znači biti čovek.”')
    print('― Tamara Kučan, PROFAJLER')
    print('===========================================================================')
    print('Never tell everything you know...')
    print('=================================')
    change_status.start()

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(os.getenv('BOT_TOKEN'))
