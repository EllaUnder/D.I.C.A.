class InviteTrack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_invite_create')
    async def invite_create(self,invite):
        g_id = invite.guild.id
        if g_id == 864768192399278110:
            i_creator = invite.inviter.id
            i_creator_mention = f'<@{i_creator}>'
            i_c_time = invite.created_at
            i_url = invite.url
            i_channel = invite.channel
            embed = discord.Embed(title='招待リンクが作成されました。',description=f'__作成者__:{i_creator_mention}',color=0xff6c00)
            embed.add_field(name='__作成時刻__',value=f'{i_c_time}')
            embed.add_field(name='__招待チャンネル__',value=f'{i_channel}')
            embed.add_field(name='__招待リンク__',value=f'{i_url}')
            channel = self.bot.get_channel(Channel_ID1)
            await channel.send(embed=embed)

def setup(bot)
    bot.add_cog(InviteTrack(bot))
