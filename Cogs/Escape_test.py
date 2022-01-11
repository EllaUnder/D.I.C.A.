from discord.ext import commands
import discord
import difflib

messages = {}

class Escape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.guild.id == 864768192399278110:
            m_s = messages.append(message.content)

            if len(m_s) = 2:
                m_s1 = m_s[0]
                m_s2 = m_s[1]
                res = difflib.ndiff(str_1.split(), str_2.split())
                print('\n'.join(res))

def setup(bot):
    return bot.add_cog(Escape(bot))
