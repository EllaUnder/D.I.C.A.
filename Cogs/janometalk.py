from discord.ext import commands
import discord
from janome.tokenizer import Tokenizer

class Talk(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
def setup(bot):
    return bot.add_cog(Status(bot))
