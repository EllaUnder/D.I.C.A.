from discord.ext import commands
import discord
import random
import json
import re

with open("files/report.json",'r') as r:
    r_json = json.load(r)

s_class = 'E','E-','E+','D','D-','D+','C','C-','C+','B','B-','B+','A','A-','A+','S','S-','S+'
users_c = []

def countarg(args):
    factor_len = len(args)

    if factor_len == 1:
        arg = ','.join(args)[0]
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
        arg1 = ','.join(args)[0]
        arg2 = ','.join(args)[1]
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

def setup(bot):
    return bot.add_cog(Datasearch(bot))
