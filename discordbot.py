import discord
from discord.ext import commands
import os
import traceback

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
    await channel.send('D.I.C.O.起動しました。')
    #注意ユーザーリスト更新
    channel = bot.get_channel(Channel_ID2)
    await channel.purge()
    embed = discord.Embed(title='⚠️注意ユーザーリスト',color=0xffff00)
    embed.add_field(name='<@523369028920541194>',value='事前告知のないeveryoneメンションでマジックショーの予告をする。\n配慮に欠けた行為であり、6サーバーでの同様の行為が報告されているが、確認したサーバーではeveryoneメンションの禁止がルールに規定されていなかったことを考慮して、注意Lv1に分類する。\n[決議内容](https://discord.com/channels/864768192399278110/864846073050431498/867049641232695336)')
    await channel.send(embed=embed)
    #警戒ユーザーリスト更新
    channel = bot.get_channel(Channel_ID3)
    await channel.purge()
    embed = discord.Embed(title='⛔️警戒ユーザーリスト',color=0xff0000)
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
    embed.add_field(name='<@714065245181575230>\n<@876832334865911808>',value='ゲームクランサーバーに執拗に荒らし行為を繰り返した。\n本人は荒らし連合軍を自称しているが、真偽は不明。\n規定に基づき警戒Lv2に分類。')
    await channel.send(embed=embed)

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

@bot.command()
@commands.has_role(864846474399711253)
async def sign(ctx):
    channel = bot.get_channel(Channel_ID4)
    await channel.purge()
    list = ['<@759520152655757374>','<@724918305948827689>','<@864016640143523850>','<@482484875794972692>','<@621546963963346956>','<@839856314414137354>','<@716212058445709362>','<@371687418346340352>','<@871053537193386064>','<@874639558564786238>','<@496981175038902273>','<@714065245181575230>','<@876832334865911808>']
    for UID in list:
        await ctx.send(UID)
        
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
bot.run(token)
