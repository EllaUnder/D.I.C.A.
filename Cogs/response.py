import discord
from discord.ext import commands
import random

class response(commands.Cog):
    def __init__(self,bot):
        self.bot =bot

        @commands.Cog.listener()
        async def on_message(self,message):
            if message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
                luck = random.random()
                if luck <= 0.3:
                    await message.channel.send('おはようございます。')
                else:
                    pass

        await bot.process_commands(message)

def setup(bot):
    bot.add_cog(response(bot))
