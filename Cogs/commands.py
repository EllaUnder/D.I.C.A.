from discord.ext import commands
import discord
import random
import json
import re
import time

with open("files/report.json",'r') as r:
    r_json = json.load(r)
    r_list_txt = r.read()

s_class = 'E','E-','E+','D','D-','D+','C','C-','C+','B','B-','B+','A','A-','A+','S','S-','S+'
users_c = []

def searcharg(args):
    factor_len = len(args)

    if factor_len == 1:
        arg = ','.join(args)[0]
        if re.search('[a-zA-Z]',arg):
            if arg not in s_class:
                return await ctx.send(f'脅威クラス{arg}は存在しません。')
            elif re.search('[0-9]',arg): #評価値アバウト
                return tag = process1
            elif len(arg) == 18: #ID報告書あり
                return

    if factor_len == 2:
        arg1 = ','.join(args)[0]
        arg2 = ','.join(args)[1]
        if arg1 != ["just","j","existence","e"] or arg2 != ["just","j","existence","e"]: 
            return await ctx.send('想定されていない引数です。')
        elif re.search('[0-9]',arg1) or re.search('[0-9]',arg2): 
            if arg1 = ["just","j"] or arg2 = ["just","j"]: #評価値ピッタリ
                return
        elif len(arg1) == 18 or len(arg2) == 18:
            if arg1 = ["existence","e"] or arg2 = ["existence","e"]: #ID存在のみ
                return

class Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #Embedリンク
    @commands.command()
    @commands.has_any_role(865029743173828608,864846474399711253)
    async def Elink(self,ctx,arg1,arg2):
        embed = discord.Embed(description=f'[{arg1}]({arg2})')
        await ctx.send(embed=embed)

    #検索
    @commands.command()
    async def search(self,ctx,arg):
        if re.search('[a-zA-Z]',arg):
            if arg not in s_class: # もし引数が予想以外なら警告で返す
                await ctx.send(f"脅威クラス**{arg}**は存在しません。")
                return

            for info in r_json:  
                if arg in info["class"]: # 正規表現じゃなくてinにすればEならEとE-,E+も入るし、E+ならE+だけが入る
                    users_c.append([info["id"], info["value"]]) # usersに情報を一旦保管

            if users_c == []: # もし結果が空なら返す
                await ctx.send("Search result: **None**")
                await ctx.send('該当するユーザーは見つかりませんでした。')
                return

            embed = discord.Embed(title=f'脅威クラス**{arg}**の報告リスト',color=0xff0000) # 初期Embed
            field_count = 0

            for user in users_c:
                if field_count >= 25: # いつもの
                    time.sleep(random.uniform(3.0,5.0))
                    await ctx.send(embed=embed)
                    embed = discord.Embed(title=f'驚異クラス"{arg}"の報告リスト',color=0xff0000)
                    field_count = 0
                    user_id = str(user[0])
                    user_content = str(user[1])
                    embed.add_field(name=f'▼__{user_id}__',value=user_content)

                else:
                    user_id = str(user[0])
                    user_content = str(user[1])
                    field_count += 1
                    embed.add_field(name=f'▼__{user_id}__',value=user_content)

            if field_count != 0:
                await ctx.send(embed=embed)
    
        elif re.search('[0-9]',arg):
            arg_digits = len(str(arg))
            if 1 <= arg_digits <= 3:
                users_d_value = []
            
        elif arg in r_list_txt:
            await ctx.send('ちょっと待ってくださいね…')
            time.sleep(random.uniform(0.5,1.5))
            await ctx.send('該当IDは報告リストに存在します。')
    
        elif arg in b_list_txt:
            await ctx.send('ちょっと待ってくださいね…')
            time.sleep(random.uniform(0.5,1.5))
            await ctx.send('該当IDはブラックリストに存在します。')

        elif not arg in r_list_txt and not arg in b_list_txt:
            await ctx.send('ちょっと待ってくださいね…')
            time.sleep(random.uniform(0.5,1.5))
            await ctx.send('該当IDは報告リスト・ブラックリストに存在しません。')

        else:
            return

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
