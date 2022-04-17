from discord.ext import commands
import discord

class Settings(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    
def setup(bot):
   return bot.add_cog(Settings(bot))
