hand_list = ['✊','✌','🖐']

@bot.event
async def on_message(message):
    if message.author.bot:
            return

    if message.content == 'おはよう' or message.content == 'オハヨウ' or 'おは' in message.content or 'オハヨー' in message.content:
        if not message.channel.id == 898360112824066079:
            luck = random.random()
            if luck <= 0.3:
                await message.channel.send('おはようございます。')
            else:
                return

    if message.content == 'ねこ' or 'ねこ、' in message.content:
        luck = random.random()
        list_ = ['にゃん','にゃぁん','にゃ','ฅ^•ω•^ฅ？']
        if luck <= 0.3:
            res_ = random.choice(list_)
            await message.channel.send(f'{res_}')
        else:
            return
    
    if message.content.startswith('Laplace') or message.content.startswith('ラプラス'):
        await message.channel.send('お呼びでしょうか？')
        await bot.process_commands(message)
        return

    if message.content == 'じゃんけん✊' or message.content == 'じゃんけん✌️' or message.content == 'じゃんけん🖐':
        hand = message.content[5]
        res_hand = random.choice(hand_list)
        if not hand in hand_list:
            await message.channel.send(f'{rps(hand,res_hand)}')
        elif hand in hand_list:
            await message.channel.send(f"ポン！{res_hand}\n{rps(hand, res_hand)}")

    await bot.process_commands(message)
