import discord
from discord.ext import commands as dcommands
import private
import asyncio

async def discord_start():
  bot = Bot
  bot.start(private.DISCORD_TOKEN)

class Bot(dcommands.Bot):
  def __init__(self):
    super().__init__(command_prefix=dcommands.when_mentioned_or('!'))
  self.load_extension('twitch.twitch')
  async def on_ready():
      print('------------------------------------')
      print('THE BOT IS ONLINE')
      print('------------------------------------')
      print("Name: {}".format(bot.user.name))
      print('Author: shadeyg56')
      print("ID: {}".format(bot.user.id))
      print('DV: {}'.format(discord.__version__))
      await bot.change_presence(activity=discord.Streaming(name='Watching over the chat until next stream', url='https://www.twitch.tv/shadeyg56'))
loop = asyncio.get_event_loop()
loop.run_until_complete(discord_start())
