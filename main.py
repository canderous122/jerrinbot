import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
from jerrin_random_phrases import *
# load the token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot instance with intents
intents = discord.Intents.default()
intents.message_content = True # Needed to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

# Event: bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# Event: When a message is sent
@bot.event
async def on_message(message):
    #dont respond to itself
    if message.author == bot.user:
        return
    
    #check if bot was mentioned
    if bot.user in message.mentions:
        await message.reply(random.choice(jerrin_phrases))


    # this line is important, it allows commands to still work
    await bot.process_commands(message)

# run the bot
bot.run(TOKEN)