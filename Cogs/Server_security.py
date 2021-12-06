from discord.ext import commands
import discord
import re
import json
import time
import datetime
from datetime import timedelta,timezone

with open("files/report.json",'r') as r:
    r_json = json.load(r)

#辞書
moderater_members = {
    854331482444267550,
    791171026238308352,
    689349292879642684,
    567332302544306207,
    720917729376337970,
    422004181625339904,
    745816395530633248,
    890987400204017705
}

secure_categorys = {
    

Channel_ID1 = 886972852979531786 #その他ログ
Channel_ID5 = 886972769340903424 #ユーザー更新ログ

pattern1 = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}"
pattern2 = r"mfa\.[\w-]{84}"

class SSecurity(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        g_id = member.guild.id
        if g_id == 864768192399278110:
            user_id = str(member.id)
            for join in r_json:
                if user_id in join["id"]:
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

    #トークン自動削除
    @commands.Cog.listener()
    async def on_message(self,message):
        m_ = message.content
        if re.search(pattern1,m_) or re.search(pattern2,m_):
            await message.delete()
        if 'https://imgur.com/ehxMcVy' in message.content:
            await message.delete()

    #チャンネルロック
    @tasks.loop(seconds=60)
    async def timeloop():
    JST = timezone(timedelta(hours=+9),'JST')
    now = datetime.datetime.now(JST).strftime('%H:%M')
    if now == '09:00':
        
    @commands.Cog.listener()
    async def on_member_update(befoer,after):

def setup(bot):
    return bot.add_cog(SSecurity(bot))

    
