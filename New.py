from distutils.command import config
from pickle import TRUE
from aiohttp import BadContentDispositionHeader
import discord
from discord.ext import commands
import datetime
import time
import json

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)



@bot.listen()
async def on_message(message):
 if k == 1:
      x = datetime.datetime.now()
      y = message.channel.name
      channel = (message.channel.id)
      id = (message.author.id)

      myText = (str(x) + " : " + str(message.author) + ": " +"# "+ str(message.content) +" #" + " (" + message.guild.name + ")" + " : " + str(y) ) + " -> ->Message Id =  :():" + str(id) + ":():"#+ "  chanelID: " + str( channel) )

      print(myText)

      with open('Log.txt', 'a') as myFile:
        myFile.write(myText)
        myFile.write('\n')
      myFile.close()

@bot.command()
@commands.has_permissions(administrator=True)
async def Lon(ctx):
    global k
    k = 1
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def Loff(ctx):
    global k
    k = 0
    await ctx.message.delete()

Bad = ['Bad']

@bot.event
async def on_message(ctx, message):
    msg = message.content
    with open('Words.txt') as Words:
        if msg in Words.read():
            await message.delete()
            await ctx.send("Dont use that word!")
        else:
            await ctx.process_commands(message)



bot.run() #<- token goes here

