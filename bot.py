import os
import discord
from discord.ext import commands

# Get the Discord bot token from environment variables
TOKEN = os.getenv("TOKEN")

# Bot prefix
bot = commands.Bot(command_prefix=".", intents=discord.Intents.default())

# Items and their prices
items = {
    "airpods": "$35",
    "sp5der": "$55"
}

# Bot ready event
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

# Handle messages dynamically based on items
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore bot messages

    if message.content.startswith("."):
        cmd = message.content[1:].lower()  # Remove the dot
        if cmd in items:
            await message.channel.send(items[cmd])

    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)
