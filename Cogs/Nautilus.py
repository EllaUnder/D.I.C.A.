from discord.ext import commands
import discord
import time
import requests
import math

def Travel_overwrites(p_key,channel_permissions, roles_dict):
    keys = list(p_key)
    for key in keys: # keysをforで回す
        try:
            # まずpermissionオブジェクトを取り出す
            permission = channel_permissions[key]

            # overwritesに移行先のロールをkeyにしたpermissionを代入
            channel_permissions[roles_dict[key]] = permission

            # 移行元の権限の要素は消す
            del channel_permissions[key]
        except:
            pass
    return channel_permissions


class Nautilus(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Nautilus(self,ctx,arg):
        a_id = ctx.author.id
        if not a_id == 854331482444267550:
            return
    
        c_guild = self.bot.get_guild(ctx.guild.id)
        to_guild_id = int(arg)
        to_guild = self.bot.get_guild(to_guild_id)
        c_guild_name = c_guild.name
        to_guild_name = to_guild.name

        await ctx.send(f'__コピー元__:{c_guild_name}\n__コピー先__:{to_guild_name}')
        req_m = await ctx.send('上記で実行許可をリクエストします。')
        def rep_check(m): # Nautilusの中に置くこと
            if m.reference is not None:
                if m.reference.message_id == req_m.id and m.content in ["Y", "y", "Yes", "yes", "はい", "許可"]:
                    return True
            return False
        try:
            reply = await self.bot.wait_for("message",check=rep_check,timeout=60.0)
        except:
            await ctx.send('タイムアウトによりリクエストを棄却しました。')
            return
        await ctx.send('実行許可を確認しました。')
        time.sleep(random.uniform(0.5,1.5))
        await ctx.send('システム・ノーチラス、フルドライブ。') #電子の海を旅する装置としてその名は決定された。「システム・ノーチラス」。
        time.sleep(0.5)
        await ctx.send('ギルド観測儀・ラプラスアイ、展開します。')
        c_guild_cate = c_guild.categories
        to_guild_cate = to_guild.categories
        c_guild_chan = c_guild.channels
        to_guild_chan = to_guild.channels
        c_guild_roles = c_guild.roles
        to_guild_roles_bef = to_guild.roles
        await ctx.send('ギルド情報を取得しました。')

        await ctx.send('初期化開始')
        for channel in to_guild.channels:
            await channel.delete()
        for category in to_guild.categories:
            await category.delete()
        for d_role in to_guild_roles_bef:
            if not d_role in to_guild.get_member(bot.user.id).roles:
                await d_role.delete()
        await ctx.send('初期化完了')

        cc_guild_roles = list(reversed(c_guild_roles))
        await ctx.send('ロールセット。複製します。')
        roles_dict = {}
        for role in cc_guild_roles:
            if not role.is_default():
                role_name = role.name
                role_permissions = role.permissions
                role_color = role.color.value
                role_mentionable = role. mentionable
                role_hoist = role.hoist
                to_role = await to_guild.create_role(name=role_name,color=role_color,permissions=role_permissions,mentionable=role_mentionable,hoist=role_hoist)
                roles_dict[role] = to_role
            else:
                roles_dict[role] = to_guild.default_role
        await ctx.send('ロール、複製完了しました。')

        messages_dict = {}
        await ctx.send('ノアズ・メジャー、観測起動します。')
        time.sleep(random.uniform(1.0,3.0))
        await ctx.send('__定礎複写、開始__')
        time.sleep(random.uniform(0.5,1.5))
        await ctx.send('複写と並行して観測、実行します。')
        time.sleep(random.uniform(0.5,1.0))
        await ctx.send('コピースケール、400で固定。')
        for category in c_guild_cate:
            category_name = category.name
            to_category = await to_guild.create_category(category_name)
            for channel_category in category.channels:
                channel_name = channel_category.name
                channel_permissions = channel_category.overwrites
                p_key = channel_permissions.keys()
                channel_overwrites = Travel_overwrites(p_key,channel_permissions,roles_dict)
                if channel_category.type.name == 'text':
                    messages = await channel_category.history(limit=400).flatten()
                    messages_log = list(reversed(messages))
                    to_text_channel = await to_category.create_text_channel(channel_name,overwrites=channel_overwrites) 
                    messages_dict[str(to_text_channel.id)] = messages_log
                if channel_category.type.name == 'voice':
                    await to_category.create_voice_channel(channel_name,overwrites=channel_overwrites)
                if channel_category.type.name == 'stage_voice':
                    await to_category.create_stage_channel(channel_name,overwrites=channel_overwrites)
        await ctx.send('ギルド外殻の複製、完了しました。')
        await ctx.send('ノアズ・メジャー、観測停止。')
        time.sleep(random.uniform(1.0,1.5))
        await ctx.send('スレッドセット。観測データ、実証転写します。')
        time.sleep(0.7)
        await ctx.send('ノアズ・メジャー、モード・ライティングで再起動。\n測定針にスレッド装填。')
        time.sleep(random.uniform(1.0,3.5))
        per_message = await ctx.send('転写率**0**%で開始。')
        dict_length = len(messages_dict)
        per_count = 0
        old_per_content = ""
        for channel in to_guild.channels:
            if channel.type.name == 'text':
                webhook = await channel.create_webhook(name = "CopyWebHook")
                webhook_url = webhook.url
                for message in messages_dict[str(channel.id)]:
                    header = { "Content-type": "application/json" }
                    try:
                        url = message.attachments[0].url
                    except:
                        url = None
                    if url != None:
                        data = {
                            "content" : f"{message.content}",
                            "username" : f"{message.author.name}",
                            "avatar_url": str(message.author.avatar_url).replace(".webp", ".png"),
                            "embeds": [{
                                "image":{
                                "url":message.attachments[0].url}
                            }]
                        }
                    else:
                        data = {
                            "content" : f"{message.content}",
                            "username" : f"{message.author.name}",
                            "avatar_url": str(message.author.avatar_url).replace(".webp", ".png")
                        }
                    requests.post(webhook_url, json = data, headers=header)
                    time.sleep(2.0)
                    per_count += 1
                    progress_per = math.floor(per_count/dict_length)
                    if random.random() <= 0.1:
                        per_content = f'転写率**{progress_per}**%です。'
                        if not per_content == old_per_content:
                            await per_message.edit(content=per_content)
                        old_per_content = f'転写率**{progress_per}**%です。'
        per_count = 0
        await ctx.send('メジャーコンプリート。')
        await ctx.send('全工程オールクリア。')
        time.sleep(random.uniform(0.5,1.0))
        await ctx.send('ギルド複製、完了を確認。\nお疲れ様でした。')

def setup(bot):
    return bot.add_cog(Nautilus(bot))
