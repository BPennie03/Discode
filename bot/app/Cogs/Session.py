import discord
from discord.ext import commands
from discord import app_commands


async def setup(bot: commands.Bot):
    await bot.add_cog(Session(bot))


class Session(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to begin/start a session

    # Command to end a session
