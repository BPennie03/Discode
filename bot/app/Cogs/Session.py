import discord
from discord.ext import commands
from discord import app_commands


async def setup(bot: commands.Bot):
    await bot.add_cog(Session(bot))


class Session(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_users = {}

    # Command to begin/start a session
    @commands.command(name='start')
    async def start(self, ctx):
        id = self.get_id_from_ctx(ctx)
        
        self.active_users.add(id)
        await ctx.send(f"{ctx.author.name} (ID: {id}) has started a session")
    
    # Command to end a session
    @commands.command(name='stop')
    async def stop(self, ctx):
        id = self.get_id_from_ctx(ctx)
        
        try:
            self.active_users.remove(id)
        except KeyError:
            await ctx.send(f"ID {id} not found in active users")
            return
        
        await ctx.send(f"User {ctx.author.name} (ID: {id}) has ended their session")
        
    
    @staticmethod
    def get_id_from_ctx(ctx):
        return ctx.author.name
