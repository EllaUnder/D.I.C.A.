from discord.ext import commands
import discord

Channel_ID1 = 886972852979531786 #その他ログ

class Flame_Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_ready')
    async def ready(self):
        print('起動しました')
        channel = self.bot.get_channel(Channel_ID1)
        await channel.send('ブラックリストの読み込みが完了しました。')
        time.sleep(random.uniform(0.5,1.5))
        await channel.send('報告リストの読み込みが完了しました。')
        time.sleep(random.uniform(0.5,1.5))
        await channel.send('💚**System All Green**' if random.random() <= 0.1 else '🟢**System All Green**')
        time.sleep(random.uniform(0.5,1.5))
        await channel.send('安全保障機関 D.I.C.A.管制補佐システムLaplace、起動します。\nreginの実行を忘れないでください。')
        timeloop.start()

    @commands.Cog.listener(name='on_command_error')
    async def command_error(self,ctx,error):
        orig_error = getattr(error, "original", error)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        channel = self.bot.get_channel(Channel_ID1)
        await channel.send(error_msg)
        await ctx.send('コマンドエラーです。')

def setup(bot):
    return bot.add_cog(Flame_Event(bot))
