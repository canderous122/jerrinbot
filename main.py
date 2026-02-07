import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
from jerrin_random_phrases import *
from flask import Flask
from threading import Thread


# load the token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot instance with intents
intents = discord.Intents.default()
intents.message_content = True # Needed to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

# flask app for health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"


def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

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
        if message.author.id == 210459434416209920:
            await message.reply("Look at this loser he's swapped to the same hero as me!")
        elif "marvel rivals" in message.content.lower():
            await message.reply("Im literally top fragging, are you watching the stream?")
        else:
            await message.reply(random.choice(jerrin_phrases))


    # this line is important, it allows commands to still work
    await bot.process_commands(message)


# Run Flask in a separate thread
Thread(target=run_flask).start()

# run the bot
bot.run(TOKEN)