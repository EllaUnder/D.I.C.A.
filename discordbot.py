import discord
from discord.ext import commands,tasks
import os
import traceback
import random
import re
import datetime
from datetime import timedelta,timezone

bot = commands.Bot(
    command_prefix='#d',
    strip_after_prefix = True,
)
token = os.environ['DISCORD_BOT_TOKEN']


Channel_ID1 = 864848975139700736 #ログ
Channel_ID2 = 867042310180962315 #注意ユーザーリスト
Channel_ID3 = 864846769351294976 #警戒ユーザーリスト
Channel_ID4 = 871581378234433586 #IDコピー

INITIAL_EXTENSIONS = [
    'Cogs.list',
    'Cogs.embed',
    'Cogs.response'
]

class Laplace(commands.Bot):
    def __init__(self):
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                print('エラーが発生しました。')


    async def on_ready(self):
        print('起動しました')
        channel = bot.get_channel(Channel_ID1)
        await channel.send('D.I.C.O.起動しました。\nreginの実行を忘れないでください。')
        timeloop.start()
    
    async def on_command_error(self,ctx, error):
        orig_error = getattr(error, "original", error)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        channel = bot.get_channel(Channel_ID1)
        await channel.send(error_msg)
   
#時報
    @tasks.loop(seconds=60)
        async def timeloop(self):
            channel = bot.get_channel(881121615339986964) #ラウンジ
            Greeting_List = ['今日も一日頑張りましょう。','オペレーターの皆さん、おはようございます。']
            JST = timezone(timedelta(hours=+9),'JST')
            now = datetime.datetime.now(JST).strftime('%H:%M')
            if now == '09:00':
                Today_Greeting = random.choice(Greeting_List)
                await channel.send(f'D.I.C.O.が9時をお知らせします。\n{Today_Greeting}')


if __name__ == '__main__':
    bot = Laplace(self)
    bot.run(token)
