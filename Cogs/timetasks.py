from discord.ext import commands,tasks
import discord
import datetime
from datetime import timedelta,timezone

class TimeTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop.start()

    @tasks.loop(seconds=60)
    async def loop(self):
        channel = self.bot.get_channel(898235395203018752) #twitter2
        tweet_List = ['にゃるらさんありがとう','ふん…','オラの武器はでっかい岩塩さ','群馬の暴力型侵略装置','富士そばの裏メニューって知ってる？']
        JST = timezone(timedelta(hours=+9),'JST')
        now = datetime.datetime.now(JST).strftime('%H:%M')
        if now == '09:00':
            Today_tweet = random.choice(tweet_List)
            await channel.send(f'{Today_tweet}')

def setup(bot):
    return bot.add_cog(TimeTasks(bot))
