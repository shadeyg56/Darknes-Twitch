from twitchio import commands as tcommands
import discord
from discord.ext import commands as dcommands
import private

class Twitch():
  def __init___(self, bot):
    self.bot = bot
class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self, bot):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'])
    self.bot = bot
  @tcommands.twitch_command()
  async def test(self, ctx):
    await ctx.send('I am alive')
    
  async def event_ready(self):
    print('Logged into Twitch')
    
    

Twitch_Bot().run()
def setup(bot):
  bot.add_cog(Twitch_Bot(bot))
