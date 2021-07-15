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
    embed = discord.Embed(title='注意ユーザーリスト',description='<@482484875794972692>/n<@621546963963346956>',color=0xff0000)
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
