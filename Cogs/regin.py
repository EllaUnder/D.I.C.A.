class Regin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(864846474399711253)
    async def regin(ctx):
        if ctx.channel.id == 864846769351294976:
            channel =bot.get_channel(Channel_ID3)
            await channel.purge()
            embed = discord.Embed(title='報告ユーザーリスト',color=0xff0000)
            field_count = 0
            user_id_count = 0
            content_count = 0
            total_str = 9

            for r_info in r_json:
                total_str += len(str(r_info['id'])) + len(str(r_info['value']))

                if field_count >= 25 or total_str >= 6000: 
                    await channel.send(embed=embed)
                    embed = discord.Embed(title='報告ユーザーリスト',color=0xff0000)
                    field_count, total_str = 0, 9
                    r_user_id = str(r_info['id'])
                    r_content = str(r_info['value'])
                    embed.add_field(name=f'▼__{r_user_id}__',value=r_content)
                    total_str += len(str(r_info['id'])) + len(str(r_info['value']))
                
                else:
                    r_user_id = str(r_info['id'])
                    r_content = str(r_info['value'])
                    total_str += len(str(r_info['value'])) + len(str(r_info['id']))
                    embed.add_field(name=f'▼__{r_user_id}__',value=r_content)
                    field_count += 1

            if field_count != 0:
                await channel.send(embed=embed)
        else:
            pass
