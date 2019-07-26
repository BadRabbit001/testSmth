# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle
from discord.utils import get

client = commands.Bot(command_prefix='!')
#client = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['with BlackRabbit', 'with your connection', 'with other rabbits', 'with generator', 'www.rabbit001.cf'])

@client.command()
async def lala(ctx):
    check_role = get(ctx.message.guild.roles, name='Leader')
    if check_role in ctx.author.roles:
        await ctx.send("Yes, you are the leader.")

    else:
        await ctx.send("No, you are NOT the leader.")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def acc(ctx):
    check_role = get(ctx.message.guild.roles, name='Seller')
    if check_role in ctx.author.roles:
        await ctx.send("your account: andrew@gmail.com:andrew789")
    else:
        await ctx.send("No, you are NOT the leader.")
    
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
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.author.send(msg)

    if message.content.startswith('!fortnite'):
        randomlist = ['https://filemedia.net/27527/fortnite','https://up-to-down.net/27527/fortnite02','https://up-to-down.net/27527/fortnite02']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('?ban'):
        msg = 'https://gifimage.net/wp-content/uploads/2017/07/ban-hammer-gif-14.gif'.format(message)
        await message.channel.send(msg)
                
    if message.content.startswith('!Spotify'):
        randomlist = ['https://direct-link.net/27527/spotify2','https://direct-link.net/27527/spotify4','https://direct-link.net/27527/spotify2']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('rabbit'):
        msg = 'https://i.pinimg.com/originals/ea/5b/b4/ea5bb42b167972d4121152caded1bcf4.gif'.format(message)
        await message.channel.send(msg)  
            
    if message.content.startswith('!stock'):
        randomlist = ['visit #how-to-gen for commands','visit #how-to-gen for commands','visit #how-to-gen for commands']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!nord'):
        randomlist = ['https://filemedia.net/27527/NordVPN','https://filemedia.net/27527/NordVPN2','https://filemedia.net/27527/NordVPN3']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!spotify'):
        randomlist = ['https://direct-link.net/27527/spotify4','https://direct-link.net/27527/spotify4','https://direct-link.net/27527/spotify3']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('!origin'):
        randomlist = ['https://link-to.net/27527/origin','https://link-to.net/27527/origin','https://link-to.net/27527/origin']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!hulu'):
        randomlist = ['https://filemedia.net/27527/hulu2','https://filemedia.net/27527/hulu','https://filemedia.net/27527/hulu2']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!steam'):
        randomlist = ['https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!udemy'):
        randomlist = ['https://filemedia.net/27527/udemy2','https://up-to-down.net/27527/udemy','https://up-to-down.net/27527/udemy']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!uplay'):
        randomlist = ['https://up-to-down.net/27527/uplay2','https://up-to-down.net/27527/uplay2','https://up-to-down.net/27527/uplay']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!crunchyroll'):
        randomlist = ['https://up-to-down.net/27527/crunchyroll','https://up-to-down.net/27527/crunchyroll','https://up-to-down.net/27527/crunchyroll']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!scribd'):
        randomlist = ['https://direct-link.net/27527/Scribd','https://direct-link.net/27527/Scribd','https://direct-link.net/27527/Scribd']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                        
    if message.content.startswith('!familyowner'):
        randomlist = ['https://direct-link.net/27527/familyowner','https://direct-link.net/27527/familyowner','https://direct-link.net/27527/familyowner']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
                                
    if message.content.startswith('!minecraft'):
        randomlist = ['https://link-to.net/27527/Minecraft001','https://up-to-down.net/27527/minecrafts','https://filemedia.net/27527/Minecraft']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!help'):
        await message.author.send("https://rabbit001.cf/bot/commands.html")
        
        
    if message.content.startswith('!purge'):
        args = message.content.split(" ")
        a = int(args[1])
        await message.channel.purge(limit=a)

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
