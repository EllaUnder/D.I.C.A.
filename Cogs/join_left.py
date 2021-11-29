from discord.ext import commands
import discord

class Join_Left(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        g_id = member.guild.id
        if g_id == 864768192399278110:
            channel = self.bot.get_channel(864846240428457994) #ロビー
            join_member_mention = f'<@{member.id}>'
            await channel.send(f'ようこそ、{join_member_mention}様。貴方の入館を歓迎します。\nここはDiscord安全情報機関 D.I.C.A. ロビーです。\nまずは<#{864831620208656394}>と<#{864849667114926141}>をお読み下さい。')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        g_id = member.guild.id
        if g_id == 864768192399278110:
            channel = self.bot.get_channel(864846240428457994) #ロビー
            await channel.send(f'**{member.name}**様が退館しました。\nまたのご訪問お待ちしております。')

def setup(bot):
    return bot.add_cog(Join_Left(bot))
