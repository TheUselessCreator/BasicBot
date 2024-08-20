import os
import discord
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the token from the .env file
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a Discord client instance
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Event: Bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Run the bot
client.run(TOKEN)
