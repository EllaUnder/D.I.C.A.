from discord.ext import commands
import discord

class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channel = self.bot.get_channel(886972852979531786) #その他ログ
        Gname = guild.name
        Gid = guild.id
        Gicon_url = guild.icon_url
        embed = discord.Embed(title='Botが以下のサーバーに招待されました。',color=0x00ff8d))
        embed.add_field(name=f'サーバー名:{Gname}',value=f'サーバーID:**{Gid}**')
        embed.set_image(url=Gicon_url)
        await channel.send(embed=embed)

    @commands.command()
    async def Gcheck(self,ctx):
        if ctx.author.id == 854331482444267550:
            g_list = self.bot.guilds
            for info in g_list:
                Gid = info.id
                Gname = info.name
                await ctx.send(f'{Gname}(id:**{Gid}**)')

    @commands.command()
    async def leave(self,ctx,arg):
        if ctx.author.id == 854331482444267550:
            guild = self.bot.get_guild(int(arg))
            await guild.leave()
            await ctx.send(f'{guild.name}(id:**{guild.id}**)を去りました。')
            
def setup(bot):
    return bot.add_cog(Status(bot))
