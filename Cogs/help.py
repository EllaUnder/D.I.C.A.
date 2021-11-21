from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title='Laplaceのコマンド一覧',description='プレフィックスは`#d`です。\n引数`<>`は必須になります。引数`[]`はオプションです。',color=0x00ff8d)
        embed.add_field(name='__search <ユーザーID>__',value='報告リスト、ブラックリストに指定したユーザーが存在するかどうか検索します。')
        embed.add_field(name='__Elink <タイトル> <メッセージリンク>__',value='埋め込みメッセージを作成します。\n管理者専用です。')
        embed.add_field(name='__MsearchD <検索範囲> <ユーザーID>__',value='検索範囲の中に指定したユーザーのメッセージがあった場合全て削除します。\n課長・副課長専用です。')
        embed.add_field(name='__record <タイトル> <内容> [写真]__',value='荒らし対策の活動記録を残します。\nオフィサー専用です。')
        embed.add_field(name='__help__',value='コマンド一覧を表示します。')
        await ctx.send(embed=embed)

def setup(bot):
    return bot.add_cog(Help(bot))
