from discord.ext import commands
import discord
import json

Channel_ID3 = 864846769351294976 #警戒ユーザーリスト

with open("files/report.json",'r') as r:
    r_json = json.load(r)

with open("files/trolling_way.json",'r') as t:
    t_json = json.load(t)

class Regin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(864846474399711253)
    async def regin(self,ctx):
        if ctx.channel.id == 864846769351294976:
            channel = self.bot.get_channel(Channel_ID3)
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

        elif ctx.channel.id == 913253599994339358:
            channel = self.bot.get_channel(913253599994339358)
            await channel.purge()
            
            count = 0
            for t_info in t_json:
                count += 1
                way_info = str(t_info["case"])
                counter_info = str(t_info["counter"])
                picture = str(t_info["pic"])
                embed = discord.Embed(title=f'**Case{count}**',description=f'{way_info}',color=0x18ff3a)
                embed.add_field(name='__【対処法】__',value=f'{counter_info}')
                embed.set_image(url=picture)
                await channel.send(embed=embed)
        else:
            pass

def setup(bot):
    return bot.add_cog(Regin(bot))
