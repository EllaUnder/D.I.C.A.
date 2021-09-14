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
async def on_command_error(ctx,error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    channel = bot.get_channel(Channel_ID1)
    await channel.send(error_msg)

#リスト
@bot.command()
@commands.has_role(864846474399711253)
async def regin(ctx):
    if ctx.channel.id == 867042310180962315:
        channel = bot.get_channel(Channel_ID2)
        await channel.purge()
        embed = discord.Embed(title='⚠️注意ユーザーリスト',color=0xffff00)
        embed.add_field(name='<@523369028920541194>',value='事前告知のないeveryoneメンションでマジックショーの予告をする。\n配慮に欠けた行為であり、6サーバーでの同様の行為が報告されているが、確認したサーバーではeveryoneメンションの禁止がルールに規定されていなかったことを考慮して、注意Lv1に分類する。\n[決議内容](https://discord.com/channels/864768192399278110/864846073050431498/867049641232695336)')
        await channel.send(embed=embed)
        JST = timezone(timedelta(hours=+9),'JST')
        clock = datetime.datetime.now(JST)
        time = clock.strftime('%Y年%m月%d日 %H:%M:%S')
        await channel.send(f'更新日時　{time}')
    if ctx.channel.id == 864846769351294976:
        channel = bot.get_channel(Channel_ID3)
        await channel.purge()
        embed = discord.Embed(title='⛔️警戒ユーザーリスト1',color=0xff0000)
        embed.add_field(name='<@759520152655757374>',value='意味不明な文字列やGIF画像を連投するスパム行為。\n警戒Lv1に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/867759336641265674/image0.png)')
        embed.add_field(name='<@724918305948827689>',value='意味不明な文字列やGIF画像を連投するスパム行為。\n警戒Lv1に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/867759953283514368/image0.png)')
        embed.add_field(name='<@864016640143523850>',value='サーバー招待リンクのスパム。\n警戒Lv1に分類する。')
        embed.add_field(name='<@482484875794972692>',value='サーバー招待リンクのスパム。\n警戒Lv1に分類する。')
        embed.add_field(name='<@621546963963346956>',value='スパム行為による荒らし。\n警戒Lv1に分類する。')
        embed.add_field(name='<@839856314414137354>',value='スパム行為による荒らし。\n警戒Lv1に分類する。')
        embed.add_field(name='<@716212058445709362>',value='Discordサーバー「荒らし連合」の招待リンクのスパム。\nしかし、荒らし連合との関連性は不明。\n警戒Lv1に分類。')
        embed.add_field(name='<@371687418346340352>',value='スパム行為による荒らし。\nセルフbotによる全チャンネルへ同じメッセージをスパム。\n警戒Lv2に分類する。')
        embed.add_field(name='<@871053537193386064>',value='複数回にわたる個人メンションと人種差別発言。\n私怨か無差別か判断が付きにくいが、脅威度分類により警戒Lv2に分類する。\n[詳細](https://discord.com/channels/864768192399278110/864846073050431498/871549370816929843)')
        embed.add_field(name='<@874639558564786238>',value='アカウント売買やチートショップを運営するサーバーの招待リンクの貼り付け。\n調査の結果実際に売買していた為、脅威度分類規定に基づき警戒Lv2に分類する。\n[詳細](https://discord.com/channels/864768192399278110/864846073050431498/876231157904179210)')
        embed.add_field(name='<@496981175038902273>',value='everyoneメンションと共に謎のURLをスパムする荒らし行為。\nURLの危険度が不明のため、警戒Lv1に分類する。')
        embed.add_field(name='<@714065245181575230>',value='ゲームクランサーバーに執拗に荒らし行為を繰り返した。\n本人は荒らし連合軍を自称しているが、真偽は不明。\n規定に基づき警戒Lv2に分類。')
        embed.add_field(name='<@715213698125529138>\n<@876669921185132636>\n<@877854246442254336>',value='荒らし共栄圏を讃えるような文と共に荒らしコミュニティサーバーの招待リンクをスパム。荒らし共栄圏との関係性は不明。\n脅威度規定に基づき、3名を警戒Lv3に分類する。')
        embed.add_field(name='<@841568928571850752>',value='<@877854246442254336> へのサーバー招待リンクの提供。\n<@876669921185132636> のサブアカウント。\n規定に基づき警戒Lv2に分類。')
        embed.add_field(name='<@878582493127794739>',value='<#864768192399278113> にて招待リンクのスパム。\nProbotの自動処理によってミュートにされると私と他のサーバー参加ユーザーに無差別にDM荒らしを実行。警戒Lv1に分類。')
        embed.add_field(name='<@856857024155615253>',value='「情弱」などの暴言をメンションで書き込む。\nスパムには該当しないが荒らし共栄圏と悪辣さを考慮して荒らしと判断。警戒Lv1に分類。')
        embed.add_field(name='<@347647394550251521>',value='everyoneメンションでサーバーの全チャンネルに渡って添付画像と同じ文を送信。\nリンク先はDiscordの公式が運営しているように見せかけたサイトであり、ニトロを取得しようとログインするとアカウントを乗っ取られる仕組みと思われる。\n脅威度規定に基づき警戒Lv3に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/878934418876678184/image0.png)')
        embed.add_field(name='<@740192892093464586>',value='「障害乙ww」という暴言と共にサーバーの招待リンクをスパムする。\n規定に基づき警戒Lv1に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/882086036946165850/image0.png)')
        embed.add_field(name='<@277414484719697920>',value='everyoneメンションでサーバーの全チャンネルに渡って添付画像と同じ文を送信。\nリンク先はニトロプレゼントに見せかけたアカウント乗っ取りリンクだと思われる。\n規定に基づき警戒Lv3に分類する。\n備考:該当アカウントは乗っ取られたものである可能性があります。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/882770290864701531/image0.png)')
        embed.add_field(name='<@787216130531393546>',value='everyoneメンションで添付画像と同じ文を送信。\nリンク先はニトロプレゼントに見せかけたアカウント乗っ取りリンクだと思われる。\n規定に基づき警戒Lv3に分類する。\n備考:該当アカウントはTwitterやTwitch、Battle.netのアカウントが接続されており、ほぼ確実に乗っ取られたアカウントであると思われる。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/883672303693619200/image0.png)')
        embed.add_field(name='<@683230272543522867>',value='everyoneメンション、目が痛くなるGIF、どこかの国の言語文字、荒らし共栄圏・Freeze及び何らかのサーバー招待リンクを含む長文メッセージをスパム。\n規定に基づき警戒Lv2に分類する。')
        await channel.send(embed=embed)
        del embed
        embed = discord.Embed(title='⛔️警戒ユーザーリスト2',color=0xff0000)
        embed.add_field(name='<@886477238386708541>\n<@886295586591088641>\n<@886477272092123207>\n<@886477290756788224>\n<@886477418146197514>\n<@886477322759340072>\n<@886477247085690930>\n<@886477266283008020>\n<@886295571873296445>\n<@886477315507380234>',value='以下に記載')
        embed.add_field(name='<@886477244648787998>\n<@886477282259116082>\n<@886295472770261054>\n<@886688572697108611>\n<@886688543861264395>\n<@886688583891714069>\n<@886688586366341140>\n<@886688599666462811>\n<@886688526341640193>',value='同じサーバーに参加しているユーザーに不審な短縮URLを送信。\n被害と悪質さは大きいと判断し、警戒Lv3に分類。\n[画像](https://cdn.discordapp.com/attachments/801123681312309310/886756270781128704/image0.png)')
        await channel.send(embed=embed)
        JST = timezone(timedelta(hours=+9),'JST')
        clock = datetime.datetime.now(JST)
        time = clock.strftime('%Y年%m月%d日 %H:%M:%S')
        await channel.send(f'更新日時　{time}')
    if ctx.channel.id == 871581378234433586:
        channel = bot.get_channel(Channel_ID4)
        await channel.purge()
        list = ['<@759520152655757374>','<@724918305948827689>','<@864016640143523850>','<@482484875794972692>','<@621546963963346956>','<@839856314414137354>','<@716212058445709362>','<@371687418346340352>','<@871053537193386064>','<@874639558564786238>','<@496981175038902273>','<@714065245181575230>','<@715213698125529138>','<@876669921185132636>','<@877854246442254336>','<@841568928571850752>','<@878582493127794739>','<@856857024155615253>','<@347647394550251521>','<@740192892093464586>','<@277414484719697920>','<@787216130531393546>','<@683230272543522867>','<@886477238386708541>','<@886295586591088641>','<@886477272092123207>','<@886477290756788224>','<@886477418146197514>','<@886477322759340072>','<@886477247085690930>','<@886477266283008020>','<@886295571873296445>','<@886477315507380234>','<@886477244648787998>','<@886477282259116082>','<@886295472770261054>','<@886688572697108611>','<@886688543861264395>','<@886688583891714069>','<@886688586366341140>','<@886688599666462811>','<@886688526341640193>']
        for UID in list:
            await ctx.send(UID)
    else:
        pass

#Embed
@bot.command()
@commands.has_role(864846474399711253)
async def Elink(ctx,arg1,arg2):
    embed = discord.Embed(description=f'[{arg1}]({arg2})')
    await ctx.send(embed=embed)

   
#レスポンス
@bot.event
async def on_message(message):
    if message.author == message.author.bot:
        return

    if message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
        luck = random.random()
        if luck <= 0.7:
            await message.channel.send('おはようございます。')
        else:
            pass

    await bot.process_commands(message)

#時報
@tasks.loop(seconds=60)
async def timeloop():
    channel = bot.get_channel(881121615339986964) #ラウンジ
    Greeting_List = ['今日も一日頑張りましょう。','オペレーターの皆さん、おはようございます。']
    Dish_List = ['キャンディ','ドーナツ','バームクーヘン']
    JST = timezone(timedelta(hours=+9),'JST')
    now = datetime.datetime.now(JST).strftime('%H:%M')
    if now == '09:00':
        Today_Greeting = random.choice(Greeting_List)
        await channel.send(f'D.I.C.O.が9時をお知らせします。\n{Today_Greeting}')
    if now == '12:00':
        p = random.random()
        if p <= 0.1:
            await channel.send('D.I.C.O.が正午をお知らせします。\n今日の私のランチはきなこもちです。\n午後の業務も頑張っていきましょう。')
        else:
            Today_Lunch = random.choice(Dish_List)
            await channel.send(f'D.I.C.O.が正午をお知らせします。\n今日の私のランチは{Today_Lunch}です。\n午後の業務も頑張っていきましょう。')

bot.run(token)
