import os
import re
import discord
import asyncio
from datetime import datetime
from discord.ext import tasks
from functions import *
from keep_alive import *

intents = discord.Intents.all()
client = discord.Client(intents=intents)

run_autorun = False


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    for guild in client.guilds:
        print(f"{client.user} is connected to the following guild:\n"
              f"{guild.name} (id: {guild.id})\n")
        channels = guild.channels
        for channel in channels:
            print(f"    {channel} (id: {channel.id})")


@tasks.loop(minutes=1)
async def autorun():
    await client.wait_until_ready()  # wait for on_ready event to finish
    channel = client.get_channel(YOUR_CHANNEL_ID_HERE)
    if not channel:
        print("Channel not found.")
        return

    user = await client.fetch_user(YOUR_USER_ID_HERE)
    await send_command(channel, 'date', user)
    await send_command(channel, 'fe', user)
    await send_command(channel, 'pray', user)
    await send_command(channel, 'daily', user)
    await send_command(channel, 'xp', user)

    now = datetime.now()
    if now.hour % 12 == 0 and now.minute == 0:
        await send_command(channel, 'date')

    if now.minute % 30 == 0:
        await send_command(channel, 'fe')

    if now.hour == 9 and now.minute == 0:
        await send_command(channel, 'pray')

    if now.hour == 0 and now.minute == 0:
        await send_command(channel, 'daily')
        await send_command(channel, 'xp')

    if now.hour % 2 == 0 and now.minute == 0:
        await send_command(channel, 'xp')


@client.event
async def on_message(message):
    global run_autorun
    if message.content == '$autorun':
        run_autorun = True
        await message.channel.send('Bot will now run automatically.')
        autorun.start()
    elif message.content == '$autostop':
        run_autorun = False
        await message.channel.send('Bot will stop running automatically.')
        autorun.stop()
    elif message.author.name == 'IdleRPG':
        content = message.content.lower()
        if 'you are on cooldown' in content:
            cooldown_time = re.findall(r'\d+:\d+:\d+', content)[0]
            if any(keyword in content for keyword in ['date', 'fe', 'pray', 'daily']):
                await asyncio.sleep(get_seconds(cooldown_time))
                user = await client.fetch_user(YOUR_USER_ID_HERE)
                await send_command(channel, content, user)
        elif 'you currently have' in content:
            xp_match = re.search(r'you currently have (\d+) xp, which means you are on level (\d+)\. missing to next level: (\d+)', content)
            if xp_match:
                await asyncio.sleep(1)
                await send_command(channel, f'a {xp_match.group(2)}', user)
            elif 'you are already on an adventure.' in content:
                status_match = re.search(r'adventure status\nyou are currently on an adventure with difficulty (\d+)\.\ntime until it completes: (\d+:\d+:\d+)\nadventure name: (.+)\n', content)
                if status_match:
                    await asyncio.sleep(get_seconds(status_match.group(2)))
                    await send_command(channel, f'a {status_match.group(1)}', user)

keep_alive()
client.run(os.getenv("TOKEN"))
