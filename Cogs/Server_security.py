from discord.ext import commands
import discord
import re

pattern1 = re.compile([\w-]{24}\.[\w-]{6}\.[\w-]{27})
pattern2 = re.compile(mfa\.[\w-]{84})

class SSecurity(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        m_ = message.content
        if pattern1.search(pattern1,m_) or pattern2.search(pattern2,m_):
            await message.delete()
            print ('fire')

def setup(bot):
    return bot.add_cog(SSecurity(bot))

    
