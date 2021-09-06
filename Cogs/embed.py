import discord
from discord.ext import commands

class embed(commands.Cog)
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        @commands.has_role(864846474399711253)
        async def Elink(ctx,arg1,arg2):
            embed = discord.Embed(description=f'[{arg1}]({arg2})')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(embed(bot)) 
