from discord.ext import commands
import discord

class Escape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    return bot.add_cog(Escape(bot))
