from discord.ext import commands
import discord

class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

def setup(bot):
    return bot.add_cog(Status(bot))
