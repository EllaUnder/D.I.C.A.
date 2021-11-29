from discord.ext import commands
import discord
import random
import json
import re

with open("files/report.json",'r') as r:
    r_json = json.load(r)

s_class = 'E','E-','E+','D','D-','D+','C','C-','C+','B','B-','B+','A','A-','A+','S','S-','S+'

def countarg(args):
    factor_len = len(args)

    if factor_len == 1:
        arg = args[0]
        if re.search('[a-zA-Z]',arg):
            if arg not in s_class:
                return "process1" #脅威クラスは存在しません
            elif arg in s_class:
                return "process2"
        elif re.search('[0-9]',arg): #評価値アバウト
            digits = len(arg)
            if not 1<=digits<=3:
                return "process5"
            elif 1<=digits<=3:
                return "process3"
            elif digits == 18: #ID報告書あり
                return "process4"
        else:
            return "process5"

    if factor_len == 2:
        arg1 = args[0]
        arg2 = args[1]
        if arg1 != ["just","j","existence","e"] or arg2 != ["just","j","existence","e"]: 
            return "process5" #想定されていない引数
        elif re.search('[0-9]',arg1) or re.search('[0-9]',arg2):
            digits1 = len(arg1)
            digits2 = len(arg2)
            if 1<=digits1<=3 or 1<=digits2<=3: #評価値ピッタリ
                if arg1 == ["just","j"] or arg2 == ["just","j"]:
                    return "process6"
                else:
                    return "process5"
            elif digits1 == 18 or digits2 == 18:
                if arg1 == ["existence","e"] or arg2 == ["existence","e"]: #ID存在のみ
                    return "process7"
                else:
                    return "process5"
        else:
            return "process5"

class Datasearch(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def search(self,ctx,*args):
        print(args)
        users_c = []
        tag = countarg(args)
        if tag == "process1":
            await ctx.send(f'脅威クラス{arg}は存在しません。')

        elif tag == "process5":
            await ctx.send('想定されていない引数です。')

        elif tag == "process2":
            arg = args[0]
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

        elif tag == "process3":
            arg = int(args[0])
            min = int(arg-5)
            max = int(arg+5)
            for info in r_json:
                d_value = int(info["d_value"])
                if min<=d_value<=max:
                    users_c.append([info["id"], info["value"]]) # usersに情報を一旦保管
            if users_c == []: # もし結果が空なら返す
                await ctx.send("Search result: **None**")
                await ctx.send('該当するユーザーは見つかりませんでした。')
                return
            embed = discord.Embed(title=f'評価値**{min}~{max}**の報告書リスト',color=0xff0000) # 初期Embed
            field_count = 0
            for user in users_c:
                if field_count >= 25: # いつもの
                    time.sleep(random.uniform(3.0,5.0))
                    await ctx.send(embed=embed)
                    embed = discord.Embed(title=f'評価値**{min}~{max}**の報告書リスト',color=0xff0000)
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
        
        elif tag == "process4":
            arg = args[0]
            for info in r_json:  
                if arg in info["id"]: # 正規表現じゃなくてinにすればEならEとE-,E+も入るし、E+ならE+だけが入る
                    users_c.append([info["id"], info["value"]]) # usersに情報を一旦保管
            if users_c == []: # もし結果が空なら返す
                await ctx.send("Search result: **None**")
                await ctx.send('該当するユーザーは見つかりませんでした。')
                return
            embed = discord.Embed(title=f'<@{arg}>の報告書',color=0xff0000) # 初期Embed
            field_count = 0
            for user in users_c:
                if field_count >= 25: # いつもの
                    time.sleep(random.uniform(3.0,5.0))
                    await ctx.send(embed=embed)
                    embed = discord.Embed(title=f'<@{arg}>の報告書',color=0xff0000)
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
        
        elif tag == "process6":
            arg = args[0]
            for info in r_json:
                d_value = int(info["d_value"])
                if arg == d_value:
                    users_c.append([info["id"], info["value"]]) # usersに情報を一旦保管
            if users_c == []: # もし結果が空なら返す
                await ctx.send("Search result: **None**")
                await ctx.send('該当するユーザーは見つかりませんでした。')
                return
            embed = discord.Embed(title=f'評価値**{min}~{max}**の報告書リスト',color=0xff0000) # 初期Embed
            field_count = 0
            for user in users_c:
                if field_count >= 25: # いつもの
                    time.sleep(random.uniform(3.0,5.0))
                    await ctx.send(embed=embed)
                    embed = discord.Embed(title=f'評価値**{min}~{max}**の報告書リスト',color=0xff0000)
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

def setup(bot):
    return bot.add_cog(Datasearch(bot))
