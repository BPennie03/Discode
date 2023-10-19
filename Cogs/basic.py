import discord
from discord.ext import commands
from discord import app_commands

async def setup(bot:commands.Bot):
    await bot.add_cog(StudentCommands(bot))


class StudentCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Sends message containing Discord WebSocket protocol latency")
    async def ping(self, interaction:discord.Interaction):

        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f'{latency} ms')