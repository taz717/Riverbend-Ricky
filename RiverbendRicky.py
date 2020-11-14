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


bot = commands.Bot(command_prefix='pls ')


@bot.command(name='ape', help="this makes monkey noises!")
async def plsText(ctx):

    response = "ooh ooh ahh EEEEEEE"
    await ctx.send(response)


@bot.command(name="dab", help="*dab*")
async def plsDab(ctx):

    response = "___Bitch___ *DAB!!!*"
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice. (# of dice, # of sides)')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='blackjack', help='Simulates blackJack. (playername)')
async def deal(ctx, playername):
    values = {
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
        'Six': 6,
        'Seven': 7,
        'Eight': 8,
        'Nine': 9,
        'Ten': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }
    cards = [['Ace', 'Two', 'Three', 'Four', 'Five', "Six", 'Seven', 'Eight',
              'Nine', 'Ten', 'Jack', 'Queen', 'King'],
             ['Spades', 'Diamonds', 'Hearts', 'Clubs']
             ]

    def arrayRandPick(array):
        return random.randrange(0, len(array))

    def generateCard(cards, values):
        card = cards[0][arrayRandPick(
            cards[0])], cards[1][arrayRandPick(cards[0])]
        value = values[card[0]]

        return card, value

    await ctx.send(generateCard(cards, values))


# client.run(TOKEN)
bot.run(TOKEN)
