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
    
Twitch_Bot().run()

bot = dcommands.Bot(command_prefix=when_command_mentioned.or('!'))
bot.run(private.DISCORD_TOKEN)
