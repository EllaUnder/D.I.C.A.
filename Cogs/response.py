from discord.ext import commands
import discord
import random

hand_list = ['✊','✌','🖐']

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

class Response(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
            if not message.channel.id == 898360112824066079:
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
            
        if message.content == 'じゃんけん✊' or message.content == 'じゃんけん✌️' or message.content == 'じゃんけん🖐':
            hand = message.content[5]
            res_hand = random.choice(hand_list)
            if not hand in hand_list:
                await message.channel.send(f'{rps(hand,res_hand)}')
            elif hand in hand_list:
                await message.channel.send(f"ポン！{res_hand}\n{rps(hand, res_hand)}")

        await self.bot.process_commands(message)

def setup(bot):
    return bot.add_cog(Response(bot))
