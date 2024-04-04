import discord
from discord.ext import commands
from discord import app_commands


async def setup(bot: commands.Bot):
    """
    Setup the BotCommands cog for use with bot instance.

    Parameters:
    - bot (commands.Bot): The bot instance the cog will be added to.
    """
    await bot.add_cog(BotCommands(bot))


class BotCommands(commands.Cog):
    """
    A discord.py cog class for basic util commands for Discode bot 
    """

    def __init__(self, bot):
        """
        init the BotCommands cog with a reference to the bot.

        Parameters:
        - bot (commands.Bot): The bot instance
        """
        self.bot = bot

    @commands.command(name='sync')
    async def sync(self, ctx):
        """
        Syncs all global slash commands to the guild of the context.

        Parameters:
        - ctx (commands.Context): The context of command is called, 
                    which provides the guild
        """
        await self.bot.tree.sync()
        self.bot.tree.copy_global_to(guild=ctx.guild)
        await ctx.send(f'All slash commands have been synced')

    @app_commands.command(description="Sends message containing Discord WebSocket protocol latency")
    async def ping(self, interaction: discord.Interaction):
        """
        (slash) command to send detect bot latency from any given interation
        
        Parameters:
        - interaction (discord.Interaction): The interaction object that 
                                            encapsulates the context of the slash command.
        """

        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f'{latency} ms')
