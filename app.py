import discord
from discord.ext import commands, tasks
import random
from discord import Game
import os
from itertools import cycle
from discord.utils import get
import asyncio
import time

bot = commands.Bot(command_prefix='', case_insensitive=True)


#BlackRabbit001

@bot.event
async def on_ready():
    status = cycle(['Type "help" to my DM!'])
    await bot.change_presence(activity=discord.Game(next(status)))
    print('Logged in as')
    print(bot.user.name)
    print("client id :", bot.user.id)
    print(bot.user.id)
    print('------')
#client now isn't defined like client but like bot so correct type is: await ctx.send(msg)


sfw_message = '*hint: bot sending sfw commands only into "#memes" channel! check #memes if this is #memes channel it is ok*'


@bot.command()
async def contact(ctx):
  embed = discord.Embed(color=0xfc0303)
  embed.add_field(name="**Contact:**", value="If you want contact me just make ticket on my server or contact semeone with @staff role or @helpers role they will let me know", inline=False)
  embed.add_field(name="Email:", value="You can also use email help@rabbit001.cf", inline=False)
  await ctx.send(embed=embed)
  
@bot.command()
async def test(ctx):
  embed = discord.Embed(color=0xfc0303)
  embed.add_field(name="**Contact:**", value="If you want contact me just make ticket on my server or contact semeone with @staff role or @helpers role they will let me know", inline=False)
  embed.add_field(name="Email:", value="You can also use email help@rabbit001.cf", inline=False)
  await ctx.send(embed=embed)


@bot.command()
async def advertise(ctx):
  msg = 'If you want advertise something take a look on the price list.'
  await ctx.send(msg)
  embed = discord.Embed(title="__**Price list:**__", description="", color=0xfc0303)
  embed.add_field(name="**Website:**", value="-", inline=False)
  embed.add_field(name="Option 1:", value="1x @here ping in announcements 0,8€", inline=False)
  embed.add_field(name="Option 2:", value="1x @everyone ping in announcements 1,2€", inline=False)
  embed.add_field(name="-**YouTube channel**", value="1x @here ping in announcements 1€", inline=False)
  embed.add_field(name="Option 1:", value="1x @everyone ping in announcements 1,2€", inline=False)
  embed.add_field(name="**Discord server**", value="1x @here ping in announcements 1,5€", inline=False)
  embed.add_field(name="Option 1:", value="1x @here ping in announcements 1,7€", inline=False)
  embed.add_field(name="Option 2:", value="1x @everyone ping in announcements 2,0€", inline=False)
  embed.add_field(name="__**Description:**__", value="If anything isn't relavant please make a ticket on my server!", inline=False)
  await ctx.send(embed=embed)
  

  
@bot.command()
async def Buy(ctx):
  embed = discord.Embed(color=0xfc0303)
  embed.add_field(name="**__Shop details:__**", value="You can visit my shop w accounts here: https://shoppy.gg/@BadRabbit001", inline=False)
  embed.add_field(name="**More questins?**", value="If you have more questions make a ticket or talk with my helpers", inline=False)
  await ctx.send(embed=embed)


#problem solved - imported random

 
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Website", description="http://rabbit001.cf", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Blackrabbit001#7046")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"189")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=601785377593753601&permissions=8&scope=bot")

    await ctx.send(embed=embed)
    
@bot.command()
async def faq(ctx):
    embed = discord.Embed(title="FAQ", color=0xeee657)
    embed.add_field(name="Where are accounts from?", value="Accounts are alts, google what does it mean")
    embed.add_field(name="How we get that alts?", value="just from our sponsors or from frineds etc.")
    embed.add_field(name="Can i have your bot on my own server?", value="Sure! you can here is invite link:https://discordapp.com/api/oauth2/authorize?client_id=601785377593753601&permissions=8&scope=bot")

    await ctx.send(embed=embed)

bot.remove_command('help')

# NSFW #https://cdn.discordapp.com/attachments/622754558862688256/622755203153920020/Hnet-image_1.gif

@bot.command()
async def nsfw(ctx):
    if ctx.message.channel.is_nsfw():
       randomlist = ['https://cdn.someecards.com/posts/imagefromios-42-m6fQfC.jpg ', ' https://cdn.someecards.com/posts/imagefromios-39-N59YZ9.jpg ', ' https://cdn.discordapp.com/attachments/622754558862688256/622755203153920020/Hnet-image_1.gif ', '  https://cdn.discordapp.com/attachments/622754558862688256/622755203153920020/Hnet-image_1.gif ', ' https://img-9gag-fun.9cache.com/photo/aZ7ppwW_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a5Rr7YN_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a2R5mBe_460swp.webp', 'https://img-9gag-fun.9cache.com/photo/aY7LwV7_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aV0eXww_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/avonL0n_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aPRWy1Q_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/avonZ8d_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a1RXZeD_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a2R5NAD_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aO0vqwv_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/am5zX94_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a7wdLmx_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aMY91Ax_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a0Rj8OO_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/a0Rj8YB_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aV0ez38_460swp.webp ', ' https://img-9gag-fun.9cache.com/photo/aGgDK0K_460swp.webp ']
       await ctx.send(random.choice(randomlist))
       await ctx.send('*hint: bot sending nsfw commands only into nsfw ctx! check #nsfw*')
       
    else:
       await ctx.send("This is not nsfw channel!")

 #bot will send message to definned channel iahve to find how someone can it define by command like !nsfw-set-(CHANNEL_ID)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__**Commands:**__", description="", color=0xeee657)
    embed.add_field(name="advertise", value="type if you want advertise something on my server", inline=False)
    embed.add_field(name="buy", value="Type if you want buy something from me", inline=False)
    embed.add_field(name="contact", value="Type if you want ask me something or just contact me", inline=False)
    embed.add_field(name="NothingFromThese", value="Type if no option is appropriate", inline=False)
    embed.add_field(name="restock", value="Type if you need somethning about gen restock", inline=False)
    embed.add_field(name="FAQ", value="Type if you wanna list with FAQ", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def NothingFromThese(ctx):
    embed = discord.Embed(title="Then conatct me on:", description="help@rabbit001.cf", color=0xeee657)
    await ctx.send(embed=embed)

        
@bot.command()
async def Restock(ctx):
    embed = discord.Embed(title="**Restock info**", description="If you want ask when gonna be restock please type `fill_time`")
    embed.add_field(name="Gift accounts", value="If you want gift me some accs please make a ticket on my server", inline=False)
    await ctx.send(embed=embed)      
            
@bot.command()
async def Fill_Time(ctx):
    embed = discord.Embed(title="**Fill time**", description="I do not know when we will fill the gen but usually it takes like 3 days", color=0xeee657)
    await ctx.send(embed=embed) 


#discord.Embed(title="INFO", description="type `help`", color=0xeee657)
  
@bot.command()
async def Hi(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
        
        
@bot.command()
async def Hello(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
        
        
@bot.command()
async def Yo(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
            
@bot.command()
async def rabbit(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
        
        
@bot.command()
async def hola(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
            
@bot.command()
async def gay(ctx):
    msg_help = '__You are gay you fucking idiot! Suck me!__'
    await ctx.send(msg_help)
    
        
@bot.command()
async def are(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
        
@bot.command()
async def man(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
        
@bot.command()
async def morning(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
        
@bot.command()
async def good(ctx):
    msg_help = 'type `help`'
    await ctx.send(msg_help)
     



bot.run(os.getenv('BOT_TOKEN'))
