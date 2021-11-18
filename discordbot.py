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
import psycopg2

bot = commands.Bot(
    command_prefix='#d',
    strip_after_prefix = True,
    help_command=None,
    intents=discord.Intents().all(),
    activity=discord.Game('D.I.C.A.管制補佐システム')
)

token = os.environ['DISCORD_BOT_TOKEN']

#データベース
DATABASE_URL = os.environ.get('DATABASE_URL')

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()



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
        total_str = 9

        for r_info in r_json:
            total_str += len(str(r_info['id'])) + len(str(r_info['value']))

            if field_count >= 25 or total_str >= 6000: 
                await channel.send(embed=embed)
                embed = discord.Embed(title='報告ユーザーリスト',color=0xff0000)
                field_count, total_str = 0, 9
                r_user_id = str(r_info['id'])
                r_content = str(r_info['value'])
                embed.add_field(name=f'▼__{r_user_id}__',value=r_content)
                total_str += len(str(r_info['id'])) + len(str(r_info['value']))
                
            else:
                r_user_id = str(r_info['id'])
                r_content = str(r_info['value'])
                total_str += len(str(r_info['value'])) + len(str(r_info['id']))
                embed.add_field(name=f'▼__{r_user_id}__',value=r_content)
                field_count += 1

        if field_count != 0:
            await channel.send(embed=embed)
    else:
        pass


#セキュリティシステム
@bot.event
async def on_member_join(member):
    g_id = member.guild.id
    if g_id == 864768192399278110:
        channel = bot.get_channel(864846240428457994) #ロビー
        join_member_mention = f'<@{member.id}>'
        await channel.send(f'ようこそ、{join_member_mention}様。貴方の入館を歓迎します。\nここはDiscord安全情報機関 D.I.C.A. ロビーです。\nまずは<#{864831620208656394}>と<#{864849667114926141}>をお読み下さい。')
    
        user_id = str(member.id)
        for join in r_json:
            if user_id in join['id']:
                await member.ban()
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
s_class = 'E','E-','E+','D','D-','D+','C','C-','C+','B','B-','B+','A','A-','A+','S','S-','S+'

@bot.command()
async def search(ctx,arg): 
    if re.search('[a-zA-Z]',arg):
        if arg not in s_class: # もし引数が予想以外なら警告で返す
            await ctx.send(f"脅威クラス**{arg}**は存在しません。")
            return

        users_c = [] # クラスが一致した人の情報を入れておく

        for info in r_json:  
            if arg in info["class"]: # 正規表現じゃなくてinにすればEならEとE-,E+も入るし、E+ならE+だけが入る
                users_c.append([info["id"], info["value"]]) # usersに情報を一旦保管

        if users == []: # もし結果が空なら返す
            await ctx.send("Search result: **None**")
            await ctx.send('該当するユーザーは見つかりませんでした。')
            return

        embed = discord.Embed(title=f'脅威クラス**{arg}**の報告リスト',color=0xff0000) # 初期Embed
        field_count = 0

        for user in users_c:
            if field_count >= 25: # いつもの
                time.sleep(random.uniform(3.0,5.0))
                await ctx.send(embed=embed)
                embed = discord.Embed(title=f'驚異クラス"{arg}"の報告リスト',color=0xff0000)
                field_count = 0
                user_id = str(user[0])
                user_content = str(user[1])
                embed.add_field(name=f'▼__{user_id}__',value=user_content)

            else:
                user_id = str(user[0])
                user_content = str(user[1])
                field_count += 1
                embed.add_field(name=f'▼__{user_id}__',value=user_content)

        if field_count != 0:
            await ctx.send(embed=embed)
    
    elif re.search('[0-9]',arg):
        arg_digits = len(str(arg))
        if 1 <= arg_digits <= 3:
            users_d_value = []
            
    elif arg in r_list_txt:
        await ctx.send('ちょっと待ってくださいね…')
        time.sleep(random.uniform(0.5,1.5))
        await ctx.send('該当IDは報告リストに存在します。')
    
    elif arg in b_list_txt:
        await ctx.send('ちょっと待ってくださいね…')
        time.sleep(random.uniform(0.5,1.5))
        await ctx.send('該当IDはブラックリストに存在します。')

    elif not arg in r_list_txt and not arg in b_list_txt:
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
    await ctx.send('サーチイテレータ、開始します…')
    messages = await channel.history(limit=int(arg1)).flatten()
    for message in messages:
        if message.author.id == int(arg2):
            await message.delete() # 検索対象のIDと一緒ならの処理
    await ctx.send('悪いメッセージはドーン、ドン！💣💥')

    #ユーザー情報取得

    #システム・ノーチラス
@bot.command()
@commands.has_any_role(864846474399711253,899474219623129168)
async def Nautilus(ctx,arg):
    await ctx.send('実行許可を確認しました。')
    time.sleep(random.uniform(0.5,1.5))
    await ctx.send('システム・ノーチラス、フルドライブ。') #電子の海を旅する装置としてその名は決定された。「システム・ノーチラス」。
    time.sleep(0.5)
    await ctx.send('ギルド観測儀・ラプラスアイ、展開します。')
    c_guild = bot.get_guild(ctx.guild.id)
    to_guild_id = int(arg)
    to_guild = bot.get_guild(to_guild_id)
    c_guild_cate = c_guild.categories
    to_guild_cate = to_guild.categories
    c_guild_chan = c_guild.channels
    to_guild_chan = to_guild.channels
    c_guild_roles = c_guild.roles
    to_guild_roles_bef = to_guild.roles
    await ctx.send('ギルド情報を取得しました。')

    await ctx.send('初期化開始')
    for channel in to_guild.channels:
        await channel.delete()
    for category in to_guild.categories:
        await category.delete()
    for d_role in to_guild_roles_bef:
        if not d_role in to_guild.get_member(bot.user.id).roles:
            await d_role.delete()
    await ctx.send('初期化完了')

    cc_guild_roles = list(reversed(c_guild_roles))
    await ctx.send('ロールセット。複製します。')
    roles_dict = {}
    for role in cc_guild_roles:
        if not role.is_default():
            role_name = role.name
            role_permissions = role.permissions
            role_color = role.color.value
            role_mentionable = role. mentionable
            role_hoist = role.hoist
            to_role = await to_guild.create_role(name=role_name,color=role_color,permissions=role_permissions,mentionable=role_mentionable,hoist=role_hoist)
            roles_dict[role] = to_role
        else:
            roles_dict[role] = to_guild.default_role
    await ctx.send('ロール、複製完了しました。')

    messages_dict = {}
    await ctx.send('ノアズ・メジャー、観測起動します。')
    time.sleep(random.uniform(1.0,3.0))
    await ctx.send('__定礎複写、開始__')
    time.sleep(random.uniform(0.5,1.5))
    await ctx.send('複写と並行して観測、実行します。')
    time.sleep(random.uniform(0.5,1.0))
    await ctx.send('コピースケール、400で固定。')
    for category in c_guild_cate:
        category_name = category.name
        to_category = await to_guild.create_category(category_name)
        for channel_category in category.channels:
            channel_name = channel_category.name
            channel_permissions = channel_category.overwrites
            p_key = channel_permissions.keys()
            channel_overwrites = Travel_overwrites(p_key,channel_permissions,roles_dict)
            if channel_category.type.name == 'text':
                messages = await channel_category.history(limit=400).flatten()
                messages_log = list(reversed(messages))
                to_text_channel = await to_category.create_text_channel(channel_name,overwrites=channel_overwrites) 
                messages_dict[str(to_text_channel.id)] = messages_log
            if channel_category.type.name == 'voice':
                await to_category.create_voice_channel(channel_name,overwrites=channel_overwrites)
            if channel_category.type.name == 'stage_voice':
                await to_category.create_stage_channel(channel_name,overwrites=channel_overwrites)
    await ctx.send('ギルド外殻の複製、完了しました。')
    await ctx.send('ノアズ・メジャー、観測停止。')
    time.sleep(random.uniform(1.0,1.5))
    await ctx.send('スレッドセット。観測データ、実証転写します。')
    time.sleep(0.7)
    await ctx.send('ノアズ・メジャー、モード・ライティング。測定針にスレッド装填。')
    dict_length = len(messages_dict)
    per_count = 0
    for channel in to_guild.channels:
        if channel.type.name == 'text':
            webhook = await channel.create_webhook(name = "CopyWebHook")
            webhook_url = webhook.url
            for message in messages_dict[str(channel.id)]:
                header = { "Content-type": "application/json" }
                try:
                    url = message.attachments[0].url
                except:
                    url = None
                if url != None:
                    data = {
                        "content" : f"{message.content}",
                        "username" : f"{message.author.name}",
                        "avatar_url": str(message.author.avatar_url).replace(".webp", ".png"),
                        "embeds": [{
                            "image":{
                            "url":message.attachments[0].url}
                        }]
                    }
                    requests.post(webhook_url, json = data, headers=header)
                    time.sleep(2.0)
                    per_count += 1
                    progress_per = math.floor(per_count/dict_length)
                    if random.random() <= 0.03:
                        await ctx.send(f'転写率**{progress_per}**%です。')
                    else:
                        pass
                else:
                    data = {
                        "content" : f"{message.content}",
                        "username" : f"{message.author.name}",
                        "avatar_url": str(message.author.avatar_url).replace(".webp", ".png")
                    }
                    requests.post(webhook_url, json = data, headers=header)
                    time.sleep(2.0)
                    per_count += 1
                    progress_per = math.floor(per_count/dict_length)
                    if random.random() <= 0.03:
                        await ctx.send(f'転写率**{progress_per}**%です。')
                    else:
                        pass
    per_count = 0
    await ctx.send('メジャーコンプリート。')
    await ctx.send('全工程オールクリア。')
    time.sleep(random.uniform(0.5,1.0))
    await ctx.send('ギルド複製、完了を確認。\nお疲れ様でした。')

    #タロット占い
@bot.command()
async def tarot(ctx):
    res_pic= random.choice(t_list)
    res_mean = t_json[res_pic]
    embed = discord.Embed(title='ワンオラクル・引かれたカード',color=0x90ee90)
    embed.set_image(url=res_pic)
    await ctx.send(embed=embed)
    await ctx.send(f'{res_mean}')

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

#レスポンス
hand_list = ['✊','✌','🖐']

@bot.event
async def on_message(message):
    if message.author.bot:
            return

    if message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
        luck = random.random()
        if luck <= 0.3:
            await message.channel.send('おはようございます。')
        else:
            return

    if message.content == 'ねこ' or 'ねこ、' in message.content:
        luck = random.random()
        list_ = ['にゃん','にゃぁん','にゃ','ฅ^•ω•^ฅ？']
        if luck <= 0.3:
            res_ = random.choice(list_)
            await message.channel.send(f'{res_}')
        else:
            return
    
    if message.content.startswith('Laplace') or message.content.startswith('ラプラス'):
        await message.channel.send('お呼びでしょうか？')
        await bot.process_commands(message)
        return

    if message.content == 'じゃんけん✊' or message.content == 'じゃんけん✌️' or message.content == 'じゃんけん🖐':
        hand = message.content[5]
        res_hand = random.choice(hand_list)
        if not hand in hand_list:
            await message.channel.send(f'{rps(hand,res_hand)}')
        elif hand in hand_list:
            await message.channel.send(f"ポン！{res_hand}\n{rps(hand, res_hand)}")

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
        channel = bot.get_channel(Channel_ID1)
        await channel.send(embed=embed)

#適当なことを呟く
@tasks.loop(seconds=60)
async def timeloop():
    channel = bot.get_channel(898235395203018752) #twitter2
    tweet_List = ['にゃるらさんありがとう','ふん…','オラの武器はでっかい岩塩さ','群馬の暴力型侵略装置','富士そばの裏メニューって知ってる？']
    JST = timezone(timedelta(hours=+9),'JST')
    now = datetime.datetime.now(JST).strftime('%H:%M')
    if now == '09:00':
        Today_tweet = random.choice(tweet_List)
        await channel.send(f'{Today_tweet}')

bot.run(token)
