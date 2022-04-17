from discord.ext import commands
import discord
import psycopg2
import os

DATABASE_URL = os.environ.get('postgres://xgprjinrwrytuk:b50b58e259d2c8522288bd5e231f745b032c0a1ede21942ae1ea74900d6487a2@ec2-54-157-79-121.compute-1.amazonaws.com:5432/d6cp4jtgd4mlj4')
con = None

class Settings(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    
def setup(bot):
   return bot.add_cog(Settings(bot))
