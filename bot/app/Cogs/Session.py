import discord
from datetime import datetime, timedelta
from discord.ext import commands, tasks
from discord import app_commands


async def setup(bot: commands.Bot):
    await bot.add_cog(Session(bot))


class Session(commands.Cog):
    def __init__(self, bot):
        """
        Setup the Session cog for use with bot instance.

        Parameters:
        - bot (commands.Bot): The bot instance the cog will be added to.
        - active_sessions (dict): A dictionary containing the active sessions of the bot. The key is the user ID and the value is the start time of the session.
        - session_checker (tasks.loop): A loop that checks the active sessions every minute to see if any have timed out.
        - TIME_LIMIT (int): The time limit in minutes for a session to be active.
        """
        self.bot = bot
        self.active_sessions = {}
        self.session_checker.start()
        self.TIME_LIMIT = 30  # time limit in minutes

    # Cancel the session checker loop when the cog is unloaded
    def cog_unload(self):
        self.session_checker.cancel()

    # Loop to check the active sessions
    @tasks.loop(minutes=1)
    async def session_checker(self):
        """
        Check the active sessions every minute to see if any have timed out.
        If a session has timed out, the user will be notified that their session has ended.
        """

        # Get the current time and the timeout duration
        current_time = datetime.now()
        timeout_duration = timedelta(minutes=self.TIME_LIMIT)

        for id, start_time in list(self.active_sessions.items()):
            # If the session has timed out, remove the session from the active sessions and notify the user
            if current_time - start_time >= timeout_duration:
                self.active_sessions.pop(id)
                user = await self.bot.fetch_user(id)
                if user:
                    try:
                        # Nofiying the user via DM that their session has timed out
                        await user.send(f'Your Discode session has timed out after {self.TIME_LIMIT} minutes of inactivity.')
                    except discord.Forbidden:
                        pass

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

        if id in self.active_sessions:
            await interaction.response.send_message(
                f"{name} already has an active session",
                ephemeral=True
            )
            return

        self.active_sessions[id] = datetime.now()
        await interaction.response.send_message(f"{name} (ID: {id}) has started a session")

    # Command to end a session
    @app_commands.command(description='Stop Discode Session')
    async def end(self, interaction: discord.Interaction):
        """
        End a code session with Discode

        Parameters:
        - interaction (discord.Interaction): Interaction object sent from user
        """
        id = self.get_id_from_xaction(interaction)
        name = interaction.user.global_name

        if id not in self.active_sessions:
            await interaction.response.send_message(
                f"{name} has no session to end",
                ephemeral=True
            )
            return

        try:
            self.active_sessions.pop(id, None)
        except KeyError:
            await interaction.response.send_message(
                f"ID {id} not found in active users",
                ephemeral=True
            )
            return

        self.active_sessions.pop(id, None)
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
        status = id in self.active_sessions

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
        return interaction.user.id
