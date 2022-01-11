from discord.ext import commands
import discord
import difflib

class Escape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        pass

def setup(bot):
    return bot.add_cog(Escape(bot))
