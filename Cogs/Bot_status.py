from discord.ext import commands
import discord

class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Gcheck(self,ctx):
        if ctx.author.id == 854331482444267550:
            g_list = self.bot.guilds
            await ctx.send(g_list)

def setup(bot):
    return bot.add_cog(Status(bot))
