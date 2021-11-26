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

#タイムゾーン設定
JST = timezone(timedelta(hours=+9),'JST')


INITIAL_EXTENSIONS = [
    "Cogs.Nautilus",
    "Cogs.Server_security"
    "Cogs.commands",
    "Cogs.flame_event",
    "Cogs.help",
    "Cogs.invite_track",
    "Cogs.join_left",
    "Cogs.regin",
    "Cogs.response"
]

class Laplace(commands.Bot):

    def __init__(self,command_prefix,intents,help_command,strip_after_prefix):
        super().__init__(command_prefix,
                          intents=intents,
                          strip_after_prefix=True)
        self.remove_command('help')
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(e)

token = os.environ['DISCORD_BOT_TOKEN']

if __name__ == "__main__":
    intents=discord.Intents.all()
    bot = Laplace(command_prefix='#d',intents=intents,help_command=None,strip_after_prefix=True)
    bot.run(token)
