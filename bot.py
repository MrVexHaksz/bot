import os
import discord
from discord.ext import commands

# Use environment variable for token (safer for GitHub/Railway)
TOKEN = os.getenv("TOKEN")

# Bot prefix
bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())

# Dictionary of items and prices
items = {
    "airpods": "35",
    "sp5der": "55"
}

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

# Dynamic command handler
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message starts with the prefix
    if message.content.startswith("."):
        cmd = message.content[1:].lower()  # Remove "." and make lowercase
        if cmd in items:
            await message.channel.send(items[cmd])

    # Needed to process other commands if you add them
    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)
