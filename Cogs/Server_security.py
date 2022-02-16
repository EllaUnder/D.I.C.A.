from discord.ext import commands
import discord
import re
import json
import time
import datetime
from datetime import timedelta,timezone

JST = timezone(timedelta(hours=+9),'JST')

with open("files/report.json",'r') as r:
    r_json = json.load(r)

with open("files/TTA.txt",encoding="UTF-8") as t:
    TTA_txt = t.read()

with open("files/kick.txt",encoding="UTF-8") as k:
    kick_txt = k.read()
    
Channel_ID1 = 915410788641042483 #専用ログ
Channel_ID5 = 886972769340903424 #ユーザー更新ログ

pattern1 = r"[\w-]{20,28}\.[\w-]{3,10}\.[\w-]{22,30}"
pattern2 = r"mfa\.[\w-]{80,90}"
pattern3 = r"[a-zA-Z0-9]{15}"

class SSecurity(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        g_id = member.guild.id
        g_name = member.guild.name
        user_id = str(member.id)
        if g_id == 864768192399278110:
            for join in r_json:
                if user_id in join["id"]:
                    await member.ban()
                    channel = self.bot.get_channel(Channel_ID1)
                    await channel.send('報告リストに情報のあるユーザーをBANしました')
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

        elif user_id in TTA_txt:
            channel = self.bot.get_channel(Channel_ID1)
            await member.kick()
            await channel.send(f'TTAによるサーバーへの参加が確認された為、該当アカウントを自動kickしました。\n発生場所:{g_name}(id:{g_id})')
            
        elif user_id in kick_txt:
            channel = self.bot.get_channel(Channel_ID1)
            await member.kick()
            await channel.send(f'D.I.C.A.に危険人物と認定されたユーザーのサーバーへの参加が確認された為、該当アカウントを自動kickしました。\n発生場所:{g_name}(id:{g_id})')

    #荒らし文字列削除アルゴリズム
    @commands.Cog.listener()
    async def on_message(self,message):
        m_ = message.content
        md_ = len(m_)
        c_ = re.findall(r'[^|~*`]',m_)
        c = "".join(c_)

        if re.search(pattern1,c) or re.search(pattern2,c): #トークン文字列
            await message.delete()
            await message.channel.send('トークンの恐れがある文字列を削除しました。')
            m_author = message.author.id
            mg_ = message.guild.id
            mg_n = message.guild.name
            channel = self.bot.get_channel(915410788641042483)
            await channel.send(f'<@{m_author}> がトークンメッセージを送信しました。')
            await channel.send(f'発生場所:{mg_n}(id:{mg_})')

        if 'https://imgur.com/ehxMcVy' in message.content: #白GIF
            await message.delete()
        if re.search(pattern3,m_) and md_ == 15: #スパム回避
            await message.delete()

    #時間経過 メッセージ編集トークン化対策
    @commands.Cog.listener()
    async def on_message_edit(self,befoer,after):
        m_ = after.content
        m_author = befoer.author.id
        mg_ = befoer.guild.id
        mg_n = befoer.guild.name
        if re.search(pattern1,m_) or re.search(pattern2,m_):
            channel = self.bot.get_channel(915410788641042483) #専用ログ
            await after.delete()
            await channel.send(f'<@{m_author}> がメッセージを編集しトークン化しました。')
            await channel.send(f'発生場所:{mg_n}(id:{mg_})')
            
def setup(bot):
    return bot.add_cog(SSecurity(bot))
