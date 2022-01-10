from discord.ext import commands
import discord
import traceback
import random
import time

Channel_ID1 = 915410788641042483 #ラプラス・takt専用ログ

class Flame_Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('起動しました')
        channel = self.bot.get_channel(Channel_ID1)
        await channel.send('ブラックリストの読み込みが完了しました。')
        time.sleep(random.uniform(0.5,1.5))
        await channel.send('報告リストの読み込みが完了しました。')
        time.sleep(random.uniform(0.5,1.5))
        await channel.send('💚**System All Green**' if random.random() <= 0.1 else '🟢**System All Green**')
        time.sleep(random.uniform(0.5,1.5))
        await channel.send('Discord安全情報機関 D.I.C.A.管制補佐システム【ディーカ】、起動します。\nreginの実行を忘れないでください。')

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        orig_error = getattr(error, "original", error)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        channel = self.bot.get_channel(Channel_ID1)
        g_id = ctx.guild.id
        g_name = ctx.guild.name
        await channel.send(error_msg)
        await channel.send(f'サーバー名:{g_name}(id:{g_id})\n上記のサーバーでコマンドエラーが発生しました。')
        await ctx.send(f'コマンドエラーです。')

def setup(bot):
    return bot.add_cog(Flame_Event(bot))
