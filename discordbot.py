import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(
    command_prefix='#d',
    strip_after_prefix = True,
)
token = os.environ['DISCORD_BOT_TOKEN']


Channel_ID1 = 864848975139700736
Channel_ID2 = 864846769351294976

@bot.event
async def on_ready():
    print('起動しました')
    channel = bot.get_channel(Channel_ID1)
    await channel.send('D.I.C.O.起動しました。')
    channel = bot.get_channel(Channel_ID2)
    embed = discord.Embed(title='注意ユーザーリスト',color=0xff0000)
    embed.add_field(name='<@482484875794972692>',value='サーバーに参加して「助けて」「人間関係の修復を手伝って欲しい」などの文言を連投。\n「自分では力になれそうにない」「どこか別のサーバーを探した方が良い」と助言しても「探すのが面倒臭い」という旨の主張をし、サーバーに居座り続ける。\n2サーバー以上の被害報告を確認。いずれも言動に特に変わりがない為、荒らしと判断。')
    embed.add_field(name='<@621546963963346956>',value='招待リンク及び怪しいURLのスパム。')
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
