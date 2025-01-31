import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os

# Get data env
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
APPLICATION_ID = os.getenv('DISCORD_APLICATION_ID')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

# Set up Intents
intents = discord.Intents.default()
intents.members = True  # Enable member-related events
intents.voice_states = True  # Enable voice state events
bot = Bot(command_prefix="!", intents=intents, application_id=APPLICATION_ID)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        # Sync slash commands with Discord
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Function to load all cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')  # Remove the .py extension
                print(f"Loaded cog: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load cog {filename[:-3]}: {e}")

# Run the bot
async def main():
    await load_cogs()  # Load all cogs before starting the bot
    await bot.start(TOKEN)

# Start the bot
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())