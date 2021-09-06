import discord
from discord.ext import commands
import random

@bot.event
async def on_message(message):
    if message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
        luck = random.random()
        if luck <= 0.3:
            await message.channel.send('おはようございます。')
        else:
            pass

    await bot.process_commands(message)
