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

    #invite
    @commands.command()
    async def invite(self,ctx):
        embed = discord.Embed(title='招待リンク一覧',color=0x00ff8d)
        embed.add_field(name='Laplace',value='[招待リンク](https://discord.com/api/oauth2/authorize?client_id=865086071636623370&permissions=124928&scope=bot)')
        embed.add_field(name='Discord安全情報機関 D.I.C.A.',value='[招待リンク](https://discord.gg/7HrFYFQR6p)')
        await ctx.send(embed=embed)

def setup(bot):
    return bot.add_cog(Commands(bot))
