import discord
from discord.ext import commands as dcommands
from twitchio import commands as tcommands
import private

class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'])
    
  @tcommands.twitch_command()
  async def test(self, ctx):
    await ctx.send('I am alive')
    
  async def event_ready(self):
    print('Logged into Twitch')
    
Twitch_Bot().run()

bot = dcommands.Bot(command_prefix=dcommands.when_command_mentioned_or('!'))
@bot.event()
async def on_ready():
  print('------------------------------------')
  print('THE BOT IS ONLINE')
  print('------------------------------------')
  print("Name: {}".format(bot.user.name))
  print('Author: shadeyg56')
  print("ID: {}".format(bot.user.id))
  print('DV: {}'.format(discord.__version__))
  await bot.change_presence(activity=discord.Streaming(name='watching over the chat until next stream', url='https://www.twitch.tv/shadeyg56'))
bot.run(private.DISCORD_TOKEN)
