from discord.ext import commands
import discord
import re

pattern1 = "[\w-]{24}\.[\w-]{6}\.[\w-]{27}"
pattern2 = "mfa\.[\w-]{84}"

class SSecurity(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        m_ = message.content
        if re.search(pattern1,m_) or re.search(pattern2,m_):
            await message.delete()
    
