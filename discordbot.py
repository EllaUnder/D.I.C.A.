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

bot = commands.Bot(
    command_prefix='#d',
    strip_after_prefix = True,
    help_command=None,
    intents=discord.Intents().all(),
    activity=discord.Game('D.I.C.O.管制補佐システム')
)

token = os.environ['DISCORD_BOT_TOKEN']


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

with open("report.json",'r') as f:
    r_json = json.load(f)
print(type(r_json))

#タイムゾーン設定
JST = timezone(timedelta(hours=+9),'JST')


@bot.event
async def on_ready():
    print('起動しました')
    channel = bot.get_channel(Channel_ID1)
    await channel.send('ブラックリストの読み込みが完了しました。')
    time.sleep(random.uniform(0.5,1.5))
    await channel.send('報告リストの読み込みが完了しました。')
    time.sleep(random.uniform(0.5,1.5))
    await channel.send('💚**System All Green**' if random.random() <= 0.1 else '🟢**System All Green**')
    time.sleep(random.uniform(0.5,1.5))
    await channel.send('安全保障機関 D.I.C.A.管制補佐システムLaplace、起動します。\nreginの実行を忘れないでください。')
    timeloop.start()

@bot.event
async def on_command_error(ctx,error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    channel = bot.get_channel(Channel_ID1)
    await channel.send(error_msg)
    await ctx.send('コマンドエラーです。')

#リスト
@bot.command()
@commands.has_role(864846474399711253)
async def regin(ctx):
    if ctx.channel.id == 864846769351294976:
        channel =bot.get_channel(Channel_ID3)
        await channel.purge()
        embed = discord.Embed(title='報告ユーザーリスト',color=0xff0000)
        field_count = 0
        user_id_count = 0
        content_count = 0

        for r_info in r_json:
            user_id_count += len(str(r_info['name']))
            content_count += len(str(r_info['value']))

            if field_count = 25 or (user_id_count + content_count) >= 6000:
                print(user_id_count + content_count)
                print(field_count)
                await channel.send(embed=embed)
                embed = discord.Embed(title='報告ユーザーリスト',color=0xff0000)
                field_count,user_id_count,content_count = 0,0,0
                r_user_id = str(r_info['name'])
                r_content = str(r_info['value'])
                embed.add_field(name=f'▼__{r_user_id}__',value=r_content)
                user_id_count += len(str(r_info['name']))
                content_count += len(str(r_info['value']))

            else:
                r_user_id = str(r_info['name'])
                r_content = str(r_info['value'])
                embed.add_field(name=f'▼__{r_user_id}__',value=r_content)
                field_count += 1

        if field_count != 0:
            await channel.send(embed=embed)
    else:
        pass


#セキュリティシステム
@bot.event
async def on_member_join(member):
    user_id = str(member.id)
    if user_id in list_txt:
        reason = ''.join([s for s in list_rtxt if user_id in s]).split(',')[1]
        await member.ban(reason = reason)
        channel = bot.get_channel(Channel_ID5)
        await channel.send('BANしました')
        return
    #コンディションシステム
    now = datetime.datetime.now()
    c_time = now - member.created_at
    u_name = member.name
    if c_time.total_seconds() <= 2628002.88:
        channel = bot.get_channel(Channel_ID1)
        role = member.guild.get_role(884218829151043594)
        await member.add_roles(role)
        await channel.send('コンディション更新、カラーオレンジです。')
    elif '共栄圏' in u_name or 'ワッパステイ' in u_name or '荒らし' in u_name or 'サウロン' in u_name:
        await member.ban()
        await channel.send('コンディション更新、カラーレッドです。')
    else:
        return

#コマンド
    #Embed
@bot.command()
@commands.has_any_role(865029743173828608,864846474399711253)
async def Elink(ctx,arg1,arg2):
    embed = discord.Embed(description=f'[{arg1}]({arg2})')
    await ctx.send(embed=embed)

    #検索機能
@bot.command()
async def search(ctx,arg): 
    if arg in list_txt:
        await ctx.send('ちょっと待ってくださいね…')
        time.sleep(random.uniform(0.5,1.5))
        await ctx.send('検索ヒットしました。\n該当IDは報告リストに存在します。')
    elif arg in b_list_txt:
        await ctx.send('ちょっと待ってくださいね…')
        time.sleep(random.uniform(0.5,1.5))
        await ctx.send('検索ヒットしました。\n該当IDはブラックリストに存在します。')
    elif not arg in list_txt and not arg in b_list_txt:
        await ctx.send('ちょっと待ってくださいね…')
        time.sleep(random.uniform(0.5,1.5))
        await ctx.send('該当IDは報告リスト・ブラックリストに存在しません。')
    else:
        return

    #特定ユーザーのメッセージを削除
@bot.command()
@commands.has_any_role(864846474399711253,865029743173828608)
async def MsearchD(ctx,arg1,arg2):
    channel = bot.get_channel(ctx.message.channel.id)
    messages = await channel.history(limit=int(arg1)).flatten()
    await ctx.send('サーチイテレータ、開始します…')
    for message in messages:
        if message.author.id == int(arg2):
            await message.delete() # 検索対象のIDと一緒ならの処理
    await ctx.send('悪いメッセージはドーン、ドン！💣💥')

    #ユーザー情報取得

    #ヘルプ
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Laplaceのコマンド一覧',description='プレフィックスは`#d`です。\n引数`<>`は必須になります。引数`[]`はオプションです。',color=0x00ff8d)
    embed.add_field(name='__search <ユーザーID>__',value='報告リスト、ブラックリストに指定したユーザーが存在するかどうか検索します。')
    embed.add_field(name='__Elink <タイトル> <メッセージリンク>__',value='埋め込みメッセージを作成します。\n管理者専用です。')
    embed.add_field(name='__MsearchD <検索範囲> <ユーザーID>__',value='検索範囲の中に指定したユーザーのメッセージがあった場合全て削除します。\n課長・副課長専用です。')
    embed.add_field(name='__record <タイトル> <内容> [写真]__',value='荒らし対策の活動記録を残します。\nオフィサー専用です。')
    embed.add_field(name='__help__',value='コマンド一覧を表示します。')
    await ctx.send(embed=embed)


#レスポンスコマンド
@bot.event
async def on_message(message):
    if message.content.startswith('Laplace') or message.content.startswith('ラプラス'):
        channel = message.channel
        await message.channel.send('お呼びでしょうか？')
    
    await bot.process_commands(message)


#レスポンス
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
        luck = random.random()
        if luck <= 0.3:
            await message.channel.send('おはようございます。')
        else:
            return

    await bot.process_commands(message)

#監察官補佐システム
@bot.command()
@commands.has_any_role(865030088477900811,865029743173828608,864846474399711253)
async def record(ctx,arg1,arg2):
    r_operator_mention = f"<@{ctx.author.id}>"
    now = datetime.datetime.now(JST)
    embed = discord.Embed(title=f'{arg1}',description=f'{arg2}',color=0x00FF7F)
    embed.add_field(name='__記録者__',value=f'{r_operator_mention}')
    embed.add_field(name='__記録時刻__',value=f'{now}')

    try:
        url = ctx.message.attachments[0].url
    except:
        url = None
    if url != None: #画像があった場合の処理
        embed.set_image(url=url)
    else: # 画像がないときの処理
        pass

    channel = bot.get_channel(Channel_ID6)
    await channel.send(embed=embed)
    
#招待リンク追跡
@bot.event
async def on_invite_create(invite):
    i_creator = invite.inviter.id
    i_creator_mention = f'<@{i_creator}>'
    i_c_time = invite.created_at
    i_url = invite.url
    i_channel = invite.channel
    embed = discord.Embed(title='招待リンクが作成されました。',description=f'__作成者__:{i_creator_mention}',color=0xff6c00)
    embed.add_field(name='__作成時刻__',value=f'{i_c_time}')
    embed.add_field(name='__招待チャンネル__',value=f'{i_channel}')
    embed.add_field(name='__招待リンク__',value=f'{i_url}')
    channel = bot.get_channel(Channel_ID1)
    await channel.send(embed=embed)

    


#時報
@tasks.loop(seconds=60)
async def timeloop():
    channel = bot.get_channel(881121615339986964) #ラウンジ
    Greeting_List = ['今日も一日頑張りましょう。','オフィサーの皆さん、おはようございます。']
    Dish_List = ['キャンディ','ドーナツ','バームクーヘン']
    JST = timezone(timedelta(hours=+9),'JST')
    now = datetime.datetime.now(JST).strftime('%H:%M')
    if now == '09:00':
        Today_Greeting = random.choice(Greeting_List)
        await channel.send(f'Laplaceが9時をお知らせします。\n{Today_Greeting}')
    if now == '12:00':
        p = random.random()
        if p <= 0.1:
            await channel.send('Laplaceが正午をお知らせします。\n今日の私のランチはきなこもちです。\n午後の業務も頑張っていきましょう。')
        else:
            Today_Lunch = random.choice(Dish_List)
            await channel.send(f'Laplaceが正午をお知らせします。\n今日の私のランチは{Today_Lunch}です。\n午後の業務も頑張っていきましょう。')
    if now == '18:00':
        await channel.send('PM6時をお知らせします。業務終了です。\n監察官各位、お疲れ様でした。')

bot.run(token)
