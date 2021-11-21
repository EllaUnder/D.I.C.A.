bot.event
async def on_ready():
    print('起動しました')
    channel = bot.get_channel(Channel_ID1)
    await channel.send('ブラックリストの読み込みが完了しました。')
    time.sleep(random.uniform(0.5,1.5))
    await channel.send('報告リストの読み込みが完了しました。')
    time.sleep(random.uniform(0.5,1.5))
    await channel.send('💚**System All Green**' if random.random() <= 0.1 else '🟢**System All Green**')
    time.sleep(random.uniform(0.5,1.5))
    await channel.send('安全保障機関 D.I.C.A.管制補佐システムLaplace、起動します。\nreginの実行を忘れないでください。')
    timeloop.start()
