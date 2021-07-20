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
    #警戒ユーザーリスト更新
    channel = bot.get_channel(Channel_ID2)
    await channel.purge()
    embed = discord.Embed(title='⚠️注意ユーザーリスト',color=0xffff00)
    embed.add_field(name='<@523369028920541194>',value='事前告知のないeveryoneメンションでマジックショーの予告をする。\n配慮に欠けた行為であり、6サーバーでの同様の行為が報告されているが、確認したサーバーではeveryoneメンションの禁止がルールに規定されていなかったことを考慮して、注意Lv1に分類する。\nhttps://discord.com/channels/864768192399278110/864846073050431498/867049641232695336')
    await channel.send(embed=embed)
    #注意ユーザーリスト更新
    channel = bot.get_channel(Channel_ID3)
    await channel.purge()
    embed = discord.Embed(title='⛔️警戒ユーザーリスト',color=0xff0000)
    await channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
