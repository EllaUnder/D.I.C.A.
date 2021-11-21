bot.command()
@commands.has_any_role(865029743173828608,864846474399711253)
async def Elink(ctx,arg1,arg2):
    embed = discord.Embed(description=f'[{arg1}]({arg2})')
    await ctx.send(embed=embed)
