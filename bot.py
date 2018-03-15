import discord
from discord.ext import commands as dcommands
from twitchio import commands as tcommands
import private

class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'])
    
  async def test(ctx):
    await ctx.send('I am alive')
