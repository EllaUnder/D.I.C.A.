from discord.ext import commands
import discord
import random

hand_list = ['โ','โ','๐']

def rps(hand, res_hand):
    if hand == res_hand:
        return "ใใใใงใ"

    if hand == "โ":
        if res_hand == "โ":
            return "ๅใฎๅใก๏ผ"
        elif res_hand == "๐":
            return "็งใฎๅใก๏ผ"

    if hand == "โ":
        if res_hand == "โ":
            return "็งใฎๅใก๏ผ"
        elif res_hand == "๐":
            return "ๅใฎๅใก๏ผ"

    if hand == "๐":
        if res_hand == "โ":
            return "็งใฎๅใก๏ผ"
        elif res_hand == "โ":
            return "ๅใฎๅใก๏ผ"
    else:
        return "ใใฎๆใฏ็กใใ๏ผ"

class Response(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if not message.guild.id == 864768192399278110:
            return

        if message.content == 'ใใฏใใ' or message.content == 'ใชใใจใฆ' or 'ใใฏ' in message.content or 'ใชใใจใผ' in message.content:
            if not message.channel.id == 898360112824066079:
                luck = random.random()
                if luck <= 0.3:
                    await message.channel.send('ใใฏใใใใใใพใใ')
                else:
                    return

        if message.content == 'ใญใ' or 'ใญใใ' in message.content:
            luck = random.random()
            list_ = ['ใซใใ','ใซใใใ','ใซใ','เธ^โขฯโข^เธ๏ผ']
            if luck <= 0.3:
                res_ = random.choice(list_)
                await message.channel.send(f'{res_}')
            else:
                return
    
        if message.content.startswith('Laplace') or message.content.startswith('ใฉใใฉใน'):
            await message.channel.send('ใๅผใณใงใใใใ๏ผ')
            
        if message.content == 'ใใใใใโ' or message.content == 'ใใใใใโ๏ธ' or message.content == 'ใใใใใ๐':
            hand = message.content[5]
            res_hand = random.choice(hand_list)
            if not hand in hand_list:
                await message.channel.send(f'{rps(hand,res_hand)}')
            elif hand in hand_list:
                await message.channel.send(f"ใใณ๏ผ{res_hand}\n{rps(hand, res_hand)}")

def setup(bot):
    return bot.add_cog(Response(bot))
