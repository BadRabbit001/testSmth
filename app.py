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

client = commands.Bot(command_prefix='+')
#client = discord.Client()

#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['with BadRabbit', 'with your connection', 'with other rabbits', 'with generator'])


@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!fortnite'):
        randomlist = ['test','test','test']
        msg = 'Hello ' + author + '. Your link: '
        await message.channel.send(msg + (random.choice(randomlist)))
                
    if message.content.startswith('!Spotify'):
        randomlist = ['https://direct-link.net/27527/spotify4','https://direct-link.net/27527/spotify2']
        msg = 'Hello ' + author + '. Your link: '
        await message.channel.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!nord'):
        randomlist = ['https://filemedia.net/27527/NordVPN','https://filemedia.net/27527/NordVPN2','https://filemedia.net/27527/NordVPN3']
        msg = 'Hello ' + author + '. Your link: '
        await message.channel.send(msg + (random.choice(randomlist)))
        
    if message.content.startswith('!spotify'):
        randomlist = ['https://direct-link.net/27527/spotify4','https://direct-link.net/27527/spotify2']
        msg = 'Hello ' + author + '. Your link: '
        await message.channel.send(msg + (random.choice(randomlist)))
		        
    if message.content.startswith('!netflix'):
        randomlist = ['For netflix account we need some danate ;) http://PayPal.me/Badrabbit001']
        msg = 'Hello ' + author + '. Your link: '
        await messag
				        
    if message.content.startswith('!origin'):
        randomlist = ['https://link-to.net/27527/origin','https://up-to-down.net/27527/origin2','http://direct-link.net/27527/orogin3']
        msg = 'Hello ' + author + '. Your link: '
        await messag
				        
    if message.content.startswith('!hulu'):
        randomlist = ['https://filemedia.net/27527/hulu','https://filemedia.net/27527/hulu2']
        msg = 'Hello ' + author + '. Your link: '
        await messag
						        
    if message.content.startswith('!steam'):
        randomlist = ['https://filemedia.net/27527/steam']
        msg = 'Hello ' + author + '. Your link: '
        await messag
						        
    if message.content.startswith('!udemy'):
        randomlist = ['https://up-to-down.net/27527/udemy','https://filemedia.net/27527/udemy2']
        msg = 'Hello ' + author + '. Your link: '
        await messag
		
    if message.content.startswith('!pinterest'):
        randomlist = ['https://link-to.net/27527/pinterest','https://link-to.net/27527/pinterest']
        msg = 'Hello ' + author + '. Your link: '
        await messag
				
    if message.content.startswith('!uplay'):
        randomlist = ['https://up-to-down.net/27527/uplay','https://up-to-down.net/27527/uplay2']
        msg = 'Hello ' + author + '. Your link: '
        await messag
						        
    if message.content.startswith('!crunchyroll'):
        randomlist = ['https://up-to-down.net/27527/crunchyroll','https://up-to-down.net/27527/crunchyroll']
        msg = 'Hello ' + author + '. Your link: '
        await messag
						        
    if message.content.startswith('!scribd'):
        randomlist = ['https://direct-link.net/27527/Scribd	']
        msg = 'Hello ' + author + '. Your link: '
        await messag
						        
    if message.content.startswith('!grammarly'):
        randomlist = ['https://direct-link.net/27527/grammarly','https://direct-link.net/27527/grammarly']
        msg = 'Hello ' + author + '. Your link: '
        await messag
		
    if message.content.startswith('!fuckbook'):
        randomlist = ['https://filemedia.net/27527/fcbbook','https://filemedia.net/27527/fcbbook']
        msg = 'Hello ' + author + '. Your link: '
        await messag
				
    if message.content.startswith('!familyowner'):
        randomlist = ['https://direct-link.net/27527/familyowner','https://direct-link.net/27527/familyowner']
        msg = 'Hello ' + author + '. Your link: '
        await messag
        
             
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
