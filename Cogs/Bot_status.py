from discord.ext import commands
import discord

with open("files/invite_ban_servers.txt",encoding="UTF-8") as b:
    ibs_txt = b.read()

class Status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channel = self.bot.get_channel(915410788641042483) #専用ログ
        Gname = guild.name
        Gid = guild.id
        Gicon_url = guild.icon_url

        embed = discord.Embed(title='Botが以下のサーバーに招待されました。',color=0x00ff8d)
        embed.add_field(name=f'サーバー名:{Gname}',value=f'サーバーID:**{Gid}**')
        embed.set_image(url=Gicon_url)
        await channel.send('<@854331482444267550>')
        await channel.send(embed=embed)

        if str(Gid) in ibs_txt:
            await guild.leave()
            await channel.send(f'__禁止指定サーバーに招待されたため自動退去しました。__\n【D座標】\nサーバー名:{Gname}\nID:{Gid}')

    @commands.command()
    async def Gcheck(self,ctx):
        if ctx.author.id == 854331482444267550:
            embed = discord.Embed(title='現在Laplaceが導入されているサーバー',color=0x00ff8d)
            g_list = self.bot.guilds
            gd_ = len(g_list)
            field_count,total_str = 0,21

            for info in g_list:
                Gid = info.id
                Gname = info.name
                total_str += len(str(Gid)) + len(Gname)

                if field_count >= 25 or total_str >= 6000:
                    await ctx.send(embed=embed)

                    field_count, total_str = 0,21
                    embed = discord.Embed(title='現在Laplaceが導入されているサーバー',color=0x00ff8d)
                    embed.add_field(name=f'サーバー名:{Gname}',value=f'(id:{Gid})')

                    total_str += len(str(Gid)) + len(Gname)

                else:
                    total_str += len(str(Gid)) + len(Gname)
                    embed.add_field(name=f'サーバー名:{Gname}',value=f'(id:{Gid})')
                    field_count += 1

            if field_count != 0:
                await ctx.send(embed=embed)

            await ctx.send(f'合計{gd_}サーバーに導入されています。')

    @commands.command()
    async def leave(self,ctx,arg):
        if ctx.author.id == 854331482444267550 or ctx.author.id == 791171026238308352:
            guild = self.bot.get_guild(int(arg))
            await guild.leave()
            await ctx.send(f'{guild.name}(id:**{guild.id}**)を去りました。')
            
def setup(bot):
    return bot.add_cog(Status(bot))
