class Join_Left(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener(name='on_member_join')
    async def on_join(self,member):
    g_id = member.guild.id
    if g_id == 864768192399278110:
        channel = self.bot.get_channel(864846240428457994) #ロビー
        join_member_mention = f'<@{member.id}>'
        await channel.send(f'ようこそ、{join_member_mention}様。貴方の入館を歓迎します。\nここはDiscord安全情報機関 D.I.C.A. ロビーです。\nまずは<#{864831620208656394}>と<#{864849667114926141}>をお読み下さい。')
    
        user_id = str(member.id)
        for join in r_json:
            if user_id in join['id']:
                await member.ban()
                channel = self.bot.get_channel(Channel_ID5)
                await channel.send('BANしました')
                return

        #コンディションシステム
        now = datetime.datetime.now()
        c_time = now - member.created_at
        u_name = member.name
        channel = self.bot.get_channel(Channel_ID1)
        if c_time.total_seconds() <= 2628002.88:
            role = member.guild.get_role(884218829151043594)
            await member.add_roles(role)
            await channel.send('コンディション更新、カラーオレンジです。')
        elif '共栄圏' in u_name or 'ワッパステイ' in u_name or '荒らし' in u_name or 'サウロン' in u_name:
            await member.ban()
            await channel.send('コンディション更新、カラーレッドです。')
        else:
            return

bot.event
async def on_member_remove(member):
    g_id = member.guild.id
    if g_id == 864768192399278110:
        channel = bot.get_channel(864846240428457994) #ロビー
        await channel.send(f'**{member.name}**様が退館しました。\nまたのご訪問お待ちしております。')
