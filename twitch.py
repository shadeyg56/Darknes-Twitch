from twitchio import commands as tcommands
import discord
from discord.ext import commands as dcommands
import private
from discord.ext.commands import Bot as bot
class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'])
    
  @tcommands.twitch_command()
  async def test(self, ctx):
    await ctx.send('I am alive')
    await self.bot.change_presence(activity=discord.Game(name='testing succesful!'))
    
  async def event_ready(self):
    print('Logged into Twitch')
    
Twitch_Bot().run()
