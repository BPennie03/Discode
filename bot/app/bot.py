import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents(messages=True, guilds=True,
                          members=True, voice_states=True, message_content=True)
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """
    Initializes Discode Bot and loads all cogs in /Cogs
    """
    print(f'{bot.user} has connected to Discord!')

    for file in os.listdir('app/Cogs'):
        if file.endswith('.py'):
            try:
                print(f"Loading cog {file}")
                await bot.load_extension(f'Cogs.{file[:-3]}')
            except commands.errors.NoEntryPointError:
                pass

bot.run(DISCORD_BOT_TOKEN)
