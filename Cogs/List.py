import discord
from discord.ext import commands
import datetime
from datetime import timedelta,timezone

class list(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        @commands.command
        @commands.has_role(864846474399711253)
            async def regin(self,ctx):
                if ctx.channel.id == 867042310180962315:
                    channel = bot.get_channel(Channel_ID2)
                    await channel.purge()
                    embed = discord.Embed(title='⚠️注意ユーザーリスト',color=0xffff00)
                    embed.add_field(name='<@523369028920541194>',value='事前告知のないeveryoneメンションでマジックショーの予告をする。\n配慮に欠けた行為であり、6サーバーでの同様の行為が報告されているが、確認したサーバーではeveryoneメンションの禁止がルールに規定されていなかったことを考慮して、注意Lv1に分類する。\n[決議内容](https://discord.com/channels/864768192399278110/864846073050431498/867049641232695336)')
                    await channel.send(embed=embed)
                    JST = timezone(timedelta(hours=+9),'JST')
                    clock = datetime.datetime.now(JST)
                    time = clock.strftime('%Y年%m月%d日 %H:%M:%S')
                    await channel.send(f'更新日時　{time}')
                if ctx.channel.id == 864846769351294976:
                    channel = bot.get_channel(Channel_ID3)
                    await channel.purge()
                    embed = discord.Embed(title='⛔️警戒ユーザーリスト',color=0xff0000)
                    embed.add_field(name='<@759520152655757374>',value='意味不明な文字列やGIF画像を連投するスパム行為。\n警戒Lv1に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/867759336641265674/image0.png)')
                    embed.add_field(name='<@724918305948827689>',value='意味不明な文字列やGIF画像を連投するスパム行為。\n警戒Lv1に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/867759953283514368/image0.png)')
                    embed.add_field(name='<@864016640143523850>',value='サーバー招待リンクのスパム。\n警戒Lv1に分類する。')
                    embed.add_field(name='<@482484875794972692>',value='サーバー招待リンクのスパム。\n警戒Lv1に分類する。')
                    embed.add_field(name='<@621546963963346956>',value='スパム行為による荒らし。\n警戒Lv1に分類する。')
                    embed.add_field(name='<@839856314414137354>',value='スパム行為による荒らし。\n警戒Lv1に分類する。')
                    embed.add_field(name='<@716212058445709362>',value='Discordサーバー「荒らし連合」の招待リンクのスパム。\nしかし、荒らし連合との関連性は不明。\n警戒Lv1に分類。')
                    embed.add_field(name='<@371687418346340352>',value='スパム行為による荒らし。\nセルフbotによる全チャンネルへ同じメッセージをスパム。\n警戒Lv2に分類する。')
                    embed.add_field(name='<@871053537193386064>',value='複数回にわたる個人メンションと人種差別発言。\n私怨か無差別か判断が付きにくいが、脅威度分類により警戒Lv2に分類する。\n[詳細](https://discord.com/channels/864768192399278110/864846073050431498/871549370816929843)')
                    embed.add_field(name='<@874639558564786238>',value='アカウント売買やチートショップを運営するサーバーの招待リンクの貼り付け。\n調査の結果実際に売買していた為、脅威度分類規定に基づき警戒Lv2に分類する。\n[詳細](https://discord.com/channels/864768192399278110/864846073050431498/876231157904179210)')
                    embed.add_field(name='<@496981175038902273>',value='everyoneメンションと共に謎のURLをスパムする荒らし行為。\nURLの危険度が不明のため、警戒Lv1に分類する。')
                    embed.add_field(name='<@714065245181575230>',value='ゲームクランサーバーに執拗に荒らし行為を繰り返した。\n本人は荒らし連合軍を自称しているが、真偽は不明。\n規定に基づき警戒Lv2に分類。')
                    embed.add_field(name='<@715213698125529138>\n<@876669921185132636>\n<@877854246442254336>',value='荒らし共栄圏を讃えるような文と共に荒らしコミュニティサーバーの招待リンクをスパム。荒らし共栄圏との関係性は不明。\n脅威度規定に基づき、3名を警戒Lv3に分類する。')
                    embed.add_field(name='<@841568928571850752>',value='<@877854246442254336> へのサーバー招待リンクの提供。\n<@876669921185132636> のサブアカウント。\n規定に基づき警戒Lv2に分類。')
                    embed.add_field(name='<@878582493127794739>',value='<#864768192399278113> にて招待リンクのスパム。\nProbotの自動処理によってミュートにされると私と他のサーバー参加ユーザーに無差別にDM荒らしを実行。警戒Lv1に分類。')
                    embed.add_field(name='<@856857024155615253>',value='「情弱」などの暴言をメンションで書き込む。\nスパムには該当しないが荒らし共栄圏と悪辣さを考慮して荒らしと判断。警戒Lv1に分類。')
                    embed.add_field(name='<@347647394550251521>',value='everyoneメンションでサーバーの全チャンネルに渡って添付画像と同じ文を送信。\nリンク先はDiscordの公式が運営しているように見せかけたサイトであり、ニトロを取得しようとログインするとアカウントを乗っ取られる仕組みと思われる。\n脅威度規定に基づき警戒Lv3に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/878934418876678184/image0.png)')
                    embed.add_field(name='<@740192892093464586>',value='「障害乙ww」という暴言と共にサーバーの招待リンクをスパムする。\n規定に基づき警戒Lv1に分類。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/882086036946165850/image0.png)')
                    embed.add_field(name='<@277414484719697920>',value='everyoneメンションでサーバーの全チャンネルに渡って添付画像と同じ文を送信。\nリンク先はニトロプレゼントに見せかけたアカウント乗っ取りリンクだと思われる。\n規定に基づき警戒Lv3に分類する。\n備考:該当アカウントは乗っ取られたものである可能性があります。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/882770290864701531/image0.png)')
                    embed.add_field(name='<@787216130531393546>',value='everyoneメンションで添付画像と同じ文を送信。\nリンク先はニトロプレゼントに見せかけたアカウント乗っ取りリンクだと思われる。\n規定に基づき警戒Lv3に分類する。\n備考:該当アカウントはTwitterやTwitch、Battle.netのアカウントが接続されており、ほぼ確実に乗っ取られたアカウントであると思われる。\n[画像](https://cdn.discordapp.com/attachments/864846073050431498/883672303693619200/image0.png)')
                    embed.add_field(name='<@683230272543522867>',value='everyoneメンション、目が痛くなるGIF、どこかの国の言語文字、荒らし共栄圏・Freeze及び何らかのサーバー招待リンクを含む長文メッセージをスパム。\n規定に基づき警戒Lv2に分類する。')
                    await channel.send(embed=embed)
                    JST = timezone(timedelta(hours=+9),'JST')
                    clock = datetime.datetime.now(JST)
                    time = clock.strftime('%Y年%m月%d日 %H:%M:%S')
                    await channel.send(f'更新日時　{time}')
                if ctx.channel.id == 871581378234433586:
                    channel = bot.get_channel(Channel_ID4)
                    await channel.purge()
                    list = ['<@759520152655757374>','<@724918305948827689>','<@864016640143523850>','<@482484875794972692>','<@621546963963346956>','<@839856314414137354>','<@716212058445709362>','<@371687418346340352>','<@871053537193386064>','<@874639558564786238>','<@496981175038902273>','<@714065245181575230>','<@715213698125529138>','<@876669921185132636>','<@877854246442254336>','<@841568928571850752>','<@878582493127794739>','<@856857024155615253>','<@347647394550251521>','<@740192892093464586>','<@277414484719697920>','<@787216130531393546>','<@683230272543522867>']
                    for UID in list:
                        await ctx.send(UID)
                else:
                    pass

def setup(bot):
    bot.add_cog(list(bot))