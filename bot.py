import discord
from discord.ext import commands as dcommands
from twitchio import commands as tcommands
import private
import asyncio

async def twitch():
  Twitch_Bot().run()

class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'])
    
  @tcommands.twitch_command()
  async def test(self, ctx):
    await ctx.send('I am alive')
    
  async def event_ready(self):
    print('Logged into Twitch')
    

async def run():
  bot = Bot
  bot.start(private.DISCORD_TOKEN

class Bot(dcommands.Bot):
  def __init__(self):
    super().__init__(command_prefix=dcommands.when_command_mentioned_or('!'))
    
  async def on_ready():
      print('------------------------------------')
      print('THE BOT IS ONLINE')
      print('------------------------------------')
      print("Name: {}".format(bot.user.name))
      print('Author: shadeyg56')
      print("ID: {}".format(bot.user.id))
      print('DV: {}'.format(discord.__version__))
      await bot.change_presence(activity=discord.Streaming(name='watching over the chat until next stream', url='https://www.twitch.tv/shadeyg56'))
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.run_until_complete(twitch())
