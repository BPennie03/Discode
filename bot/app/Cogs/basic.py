import discord
from discord.ext import commands
from discord import app_commands


async def setup(bot: commands.Bot):
    await bot.add_cog(BotCommands(bot))


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sync')
    async def sync(self, ctx):
        await self.bot.tree.sync()
        self.bot.tree.copy_global_to(guild=ctx.guild)
        await ctx.send(f'All slash commands have been synced')

    @app_commands.command(description="Sends message containing Discord WebSocket protocol latency")
    async def ping(self, interaction: discord.Interaction):
        
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f'{latency} ms')
        
