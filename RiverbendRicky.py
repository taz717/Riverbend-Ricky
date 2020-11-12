'''
Moataz Khallaf(Taz)
Riverbend Ricky
12-11-2020
'''

# Riverbend Ricky.py
# imports
import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
# this is to snag the discord bot info and server name
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord! Get ready for a shit show!')


bot = commands.Bot(command_prefix='!')


@bot.command(name='ape', help="this makes monkey noises!")
async def plsText(ctx):

    response = "ooh ooh ahh EEEEEEE"
    await ctx.send(response)

client.run(TOKEN)
bot.run(TOKEN)
