#imports 
import discord 
from discord.ext import commands,tasks
import os
import traceback
import random
import re
import time
import datetime
from datetime import timedelta,timezone
import json
import requests
import math

bot = commands.Bot(
    command_prefix='#d',
    strip_after_prefix = True,
    help_command=None,
    intents=discord.Intents().all(),
    activity=discord.Game('D.I.C.A.管制補佐システム')
)

token = os.environ['DISCORD_BOT_TOKEN']

#defs
def Travel_overwrites(p_key, channel_permissions, roles_dict):
    keys = list(p_key)
    for key in keys: # keysをforで回す
        try:
            # まずpermissionオブジェクトを取り出す
            permission = channel_permissions[key]

            # overwritesに移行先のロールをkeyにしたpermissionを代入
            channel_permissions[roles_dict[key]] = permission

            # 移行元の権限の要素は消す
            del channel_permissions[key]
        except:
            pass
    return channel_permissions

def rps(hand, res_hand):
    if hand == res_hand:
        return "あいこです"

    if hand == "✊":
        if res_hand == "✌":
            return "君の勝ち！"
        elif res_hand == "🖐":
            return "私の勝ち！"

    if hand == "✌":
        if res_hand == "✊":
            return "私の勝ち！"
        elif res_hand == "🖐":
            return "君の勝ち！"

    if hand == "🖐":
        if res_hand == "✌":
            return "私の勝ち！"
        elif res_hand == "✊":
            return "君の勝ち！"
    else:
        return "その手は無いよ！"

Channel_ID1 = 886972852979531786 #その他ログ
Channel_ID2 = 867042310180962315 #注意ユーザーリスト
Channel_ID3 = 864846769351294976 #警戒ユーザーリスト
Channel_ID4 = 871581378234433586 #IDコピー
Channel_ID5 = 886972769340903424 #ユーザー更新ログ
Channel_ID6 = 899500385788624906 #活動記録

#リスト系読み込み
with open("list.txt",encoding="UTF-8") as f:
    list_txt = f.read()
    list_rtxt = list_txt.split('\n')

with open("blacklist.json",encoding="UTF-8") as b:
    b_list_txt = b.read()

with open("report.json",'r') as r:
    r_json = json.load(r)
    r_list_txt = r.read()

with open("tarot.json",'r') as t:
    t_json = json.load(t)
    t_list = list(t_json.keys())

#タイムゾーン設定
JST = timezone(timedelta(hours=+9),'JST')


INITIAL_EXTENSIONS = [
    "cogs.Nautilus",
    "cogs.commands",
    "cogs.flame_event"
    "cogs.help",
    "cogs.invite_track",
    "cogs.join_left",
    "cogs.regin",
    "cogs.response",
    "cogs.timetasks"
]

class Laplace(commands.Bot):

    def __init__(self,command_prefix):
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(e)

bot.load_extension('Cogs')

if __name__ == "__main__":
    bot.run(token)
