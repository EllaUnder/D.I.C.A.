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
Channel_ID4 = 865917109123809291 #サーバーステータス

@bot.event
async def on_ready():
    print('起動しました')
    channel = bot.get_channel(Channel_ID1)
    await channel.send('D.I.C.O.起動しました。')
    #注意ユーザーリスト更新
    channel = bot.get_channel(Channel_ID2)
    await channel.purge()
    embed = discord.Embed(title='⚠️注意ユーザーリスト',color=0xffff00)
    embed.add_field(name='<@523369028920541194>',value='事前告知のないeveryoneメンションでマジックショーの予告をする。\n配慮に欠けた行為であり、6サーバーでの同様の行為が報告されているが、確認したサーバーではeveryoneメンションの禁止がルールに規定されていなかったことを考慮して、注意Lv1に分類する。\nhttps://discord.com/channels/864768192399278110/864846073050431498/867049641232695336')
    await channel.send(embed=embed)
    #警戒ユーザーリスト更新
    channel = bot.get_channel(Channel_ID3)
    await channel.purge()
    embed = discord.Embed(title='⛔️警戒ユーザーリスト',color=0xff0000)
    embed.add_field(name='<@759520152655757374>',value='意味不明な文字列やGIF画像を連投するスパム行為。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/867759336641265674/image0.png)')
    embed.add_field(name='<@724918305948827689>',value='意味不明な文字列やGIF画像を連投するスパム行為。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/867759953283514368/image0.png)')
    embed.add_field(name='<@864016640143523850>',value='サーバー招待リンクのスパム。')
    embed.add_field(name='<@482484875794972692>',value='サーバー招待リンクのスパム。')
    embed.add_field(name='<@621546963963346956>',value='スパム行為による荒らし。')
    await channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def give(ctx):
    embed = discord.Embed(title=' ',description='[このチャンネルの上部へ](https://discord.com/channels/864768192399278110/864831620208656394/869026188805439488)')
    await ctx.send(embed=embed)


bot.run(token)
