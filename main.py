import os
import discord
from discord.ext import commands
from PyCharacterAI import Client
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')
USER_TOKEN = config('USER_TOKEN')
CHARA_ID = config('CHARA_ID')


intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
client = Client()

# log in
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name='24-Strike Plum Blossom Sword Style'))
    await client.authenticate_with_token(USER_TOKEN)

@bot.command()
async def hi(ctx):
    await ctx.send('Use !cm to talk to me or die.')

@bot.command()
async def cm(ctx):
    chat = await client.create_or_continue_chat(CHARA_ID)
    ctx.message.content = ctx.message.content.replace('!cm ','')
    answer = await chat.send_message(ctx.message.content)
    await ctx.send(answer)

bot.run(BOT_TOKEN)