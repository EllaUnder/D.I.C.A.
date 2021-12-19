from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title='Laplaceのコマンド一覧',description='プレフィックスは`#l`です。\n引数`<>`は必須になります。引数`[]`はオプションです。',color=0x00ff8d)
        embed.add_field(name='__search <ユーザーID>["existence"or"e"]__',value='D.I.C.A.データベースを検索し、指定したユーザーの報告書を返します。\nオプション引数がある場合、「存在するかどうか」のみを返します。')
        embed.add_field(name='__search <脅威クラス>__',value='指定した脅威クラスの前後+-の報告書を返します。\n+か-まで指定されている場合、その脅威クラスのみを返します。\n("D"と検索すると"D-","D","D+"を返し、"D+"と検索すると"D+"のみ)')
        embed.add_field(name='__search <評価値>["just"or"j"]__',value='指定した評価値の+-5の範囲に認定された報告書を返します。\nオプション引数がある場合、「検索された評価値ピッタリ」の報告書を返します。')
        embed.add_field(name='__Elink <タイトル> <メッセージリンク>__',value='埋め込みメッセージを作成します。\n管理者専用です。')
        embed.add_field(name='__MsearchD <検索範囲> <ユーザーID>__',value='検索範囲の中に指定したユーザーのメッセージがあった場合全て削除します。\n課長・副課長専用です。')
        embed.add_field(name='__help__',value='コマンド一覧を表示します。')
        embed.set_footer(text='その他、お問い合わせは[D.I.C.A.サーバー](https://discord.gg/7HrFYFQR6p)まで')
        await ctx.send(embed=embed)

def setup(bot):
    return bot.add_cog(Help(bot))
