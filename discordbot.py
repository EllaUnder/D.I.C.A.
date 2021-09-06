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

@bot.event
async def on_ready():
    print('起動しました')
    channel = bot.get_channel(Channel_ID1)
    await channel.send('D.I.C.O.起動しました。\nreginの実行を忘れないでください。')
    timeloop.start()
    

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    channel = bot.get_channel(Channel_ID1)
    await channel.send(error_msg)

#コマンド
@bot.command()
@commands.has_role(864846474399711253)
async def Elink(ctx,arg1,arg2):
    embed = discord.Embed(description=f'[{arg1}]({arg2})')
    await ctx.send(embed=embed)
   
#時報
@tasks.loop(seconds=60)
async def timeloop():
    channel = bot.get_channel(881121615339986964) #ラウンジ
    Greeting_List = ['今日も一日頑張りましょう。','オペレーターの皆さん、おはようございます。']
    JST = timezone(timedelta(hours=+9),'JST')
    now = datetime.datetime.now(JST).strftime('%H:%M')
    if now == '09:00':
        Today_Greeting = random.choice(Greeting_List)
        await channel.send(f'D.I.C.O.が9時をお知らせします。\n{Today_Greeting}')
    
#レスポンス
@bot.event
async def on_message(message):
    if message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
        luck = random.random()
        if luck <= 0.3:
            await message.channel.send('おはようございます。')
        else:
            pass

    await bot.process_commands(message)

#Cogファイル読み込み
bot.load_extension('Cogs.List')


#動作確認
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
bot.run(token)
