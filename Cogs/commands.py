from discord.ext import commands
import discord
import random
import json
import re
import time

with open("tarot.json",'r') as t:
    t_json = json.load(t)
    t_list = list(t_json.keys())

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
    s_class = 'E','E-','E+','D','D-','D+','C','C-','C+','B','B-','B+','A','A-','A+','S','S-','S+'

    @commands.command()
    async def search(self,ctx,arg): 
        if re.search('[a-zA-Z]',arg):
            if arg not in s_class: # もし引数が予想以外なら警告で返す
                await ctx.send(f"脅威クラス**{arg}**は存在しません。")
                return

            users_c = [] # クラスが一致した人の情報を入れておく

            for info in r_json:  
                if arg in info["class"]: # 正規表現じゃなくてinにすればEならEとE-,E+も入るし、E+ならE+だけが入る
                    users_c.append([info["id"], info["value"]]) # usersに情報を一旦保管

            if users == []: # もし結果が空なら返す
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

    #タロット占い
    @commands.command()
    async def tarot(self,ctx):
        res_pic= random.choice(t_list)
        res_mean = t_json[res_pic]
        embed = discord.Embed(title='ワンオラクル・引かれたカード',color=0x90ee90)
        embed.set_image(url=res_pic)
        await ctx.send(embed=embed)
        await ctx.send(f'{res_mean}')

def setup(bot):
    return bot.add_cog(Commands(bot))
