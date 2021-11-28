from discord.ext import commands
import discord
import random
import json
import re
import time

class Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #Embedリンク
    @commands.command()
    @commands.has_any_role(865029743173828608,864846474399711253)
    async def Elink(self,ctx,arg1,arg2):
        embed = discord.Embed(description=f'[{arg1}]({arg2})')
        await ctx.send(embed=embed)

    #特定ユーザーのメッセージを削除
    @commands.command()
    @commands.has_any_role(864846474399711253,865029743173828608,899474219623129168)
    async def MsearchD(self,ctx,arg1,arg2):
        channel = self.bot.get_channel(ctx.message.channel.id)
        await ctx.send('サーチイテレータ、開始します…')
        messages = await channel.history(limit=int(arg1)).flatten()
        for message in messages:
            if message.author.id == int(arg2):
                await message.delete() # 検索対象のIDと一緒ならの処理
        await ctx.send('悪いメッセージはドーン、ドン！💣💥')

def setup(bot):
    return bot.add_cog(Commands(bot))
