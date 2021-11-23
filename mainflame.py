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

#タイムゾーン設定
JST = timezone(timedelta(hours=+9),'JST')


INITIAL_EXTENSIONS = [
    "Cogs.Nautilus",
    "Cogs.commands",
    "Cogs.flame_event",
    "Cogs.help",
    "Cogs.invite_track",
    "Cogs.join_left",
    "Cogs.regin",
    "Cogs.response"
]

class Laplace(commands.Bot):

    def __init__(self,command_prefix):
        super().__init__(command_prefix)
        self.remove_command('help')
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(e)

bot = Laplace(command_prefix='#d ')

token = os.environ['DISCORD_BOT_TOKEN']

if __name__ == "__main__":
    bot.run(token)
