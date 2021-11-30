from discord.ext import commands
import discord

class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Gcheck(self,ctx):
        if ctx.author.id == 854331482444267550:
            g_list = self.bot.guilds
            for info in g_list:
                Gid = info[0]
                Gname = info[1]
                await ctx.send(f'**{Gname}**\n(id:**{Gid}**)')

def setup(bot):
    return bot.add_cog(Status(bot))
