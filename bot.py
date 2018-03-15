import discord
from discord.ext import commands as dcommands
import private
import asyncio


bot = dcommands.Bot(command_prefix=dcommands.when_mentioned_or('!'))

@bot.event()
async def on_ready():
  print('------------------------------------')
  print('THE BOT IS ONLINE')
  print('------------------------------------')
  print("Name: {}".format(bot.user.name))
  print('Author: shadeyg56')
  print("ID: {}".format(bot.user.id))
  print('DV: {}'.format(discord.__version__))
  await bot.change_presence(activity=discord.Streaming(name='Watching over the chat until next stream', url='https://www.twitch.tv/shadeyg56'))

bot.run(private.DISCORD_TOKEN)
bot.load_extension('twitch')
