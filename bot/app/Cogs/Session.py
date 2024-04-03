import discord
from discord.ext import commands
from discord import app_commands


async def setup(bot: commands.Bot):
    await bot.add_cog(Session(bot))


class Session(commands.Cog):
    def __init__(self, bot):
        """
        Setup the Session cog for use with bot instance.

        Parameters:
        - bot (commands.Bot): The bot instance the cog will be added to.
        """
        self.bot = bot
        self.active_users = set()

    # Command to begin/start a session
    @app_commands.command(description='Start Discode Session')
    async def start(self, interaction: discord.Interaction):
        """
        Start a code session with Discode
        
        Parameters:
        - interaction (discord.Interaction): Interaction object sent from user
        """
        id = self.get_id_from_xaction(interaction)
        name = interaction.user.global_name

        if id in self.active_users:
            await interaction.response.send_message(
                f"{name} already has an active session",
                ephemeral=True
            )
            return

        self.active_users.add(id)
        await interaction.response.send_message(f"{name} (ID: {id}) has started a session")

    # Command to end a session
    @app_commands.command(description='Stop Discode Session')
    async def stop(self, interaction: discord.Interaction):
        """
        End a code session with Discode
        
        Parameters:
        - interaction (discord.Interaction): Interaction object sent from user
        """
        id = self.get_id_from_xaction(interaction)
        name = interaction.user.global_name

        if id not in self.active_users:
            await interaction.response.send_message(
                f"{name} has no session to end", 
                ephemeral=True
            )

        try:
            self.active_users.remove(id)
        except KeyError:
            await interaction.response.send_message(
                f"ID {id} not found in active users", 
                ephemeral=True    
            )
            return

        await interaction.response.send_message(f"User {name} (ID: {id}) has ended their session")
        
    @app_commands.command(description='Check to see if you have an active session')
    async def check_session(self, interaction: discord.Interaction):
        """
        Check the status of the user's current discode session.
        In the future, this could potentially return more information pertaining to the sessions
        i.e. files ran, current lang, etc.
        
        Parameters:
        - interaction (discord.Interaction): Interaction object sent from user
        """
        id = self.get_id_from_xaction(interaction)
        status = id in self.active_users
        
        message = "Your session is currently active." if status else "You do not have an active session."
        
        await interaction.response.send_message(message, ephemeral=True)
        

    @staticmethod
    def get_id_from_xaction(interaction: discord.Interaction) -> discord.User:
        """
        Retrieves the user ID from discord interaction
        ID is currently just the user object, this is subject to change
        
        Parameters:
        - interaction (discord.Interaction): The interaction from which the user object is to be retrieved.

        Returns:
        - discord.User: The user object associated with the interaction. This object contains information about the user who initiated the interaction, such as their username, ID, and other relevant user details.

        """
        return interaction.user
