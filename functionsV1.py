import discord
import re
import asyncio

async def send_command(channel, command):
    member = discord.utils.get(channel.guild.members, name='IdleRPG', discriminator='THE_BOT_IDENTIFIER_HERE')
    if member:
        await channel.send(f'{member.mention} {command}')
        await asyncio.sleep(1)

async def send_date(channel):
    await send_command(channel, 'date')

async def send_fe(channel):
    await send_command(channel, 'fe')

async def send_pray(channel):
    await send_command(channel, 'pray')

async def send_daily(channel):
    await send_command(channel, 'daily')

async def send_xp(channel):
    await send_command(channel, 'xp')

async def send_a(channel, level):
    await send_command(channel, f'a {level}')

async def send_s_a(channel, difficulty, time_left):
    await asyncio.sleep(get_seconds(time_left))
    await send_command(channel, f'a {difficulty}')

def get_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s
