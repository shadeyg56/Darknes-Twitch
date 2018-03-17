from twitchio import commands as tcommands
import discord
from discord.ext import commands as dcommands
import private
import json

class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'])
    
  @tcommands.twitch_command()
  async def test(self, ctx):
    await ctx.send('I am alive')
    
  async def event_ready(self):
    print('Logged into Twitch')
   
  async def is_live('shadeyg56'):
    print('Daddy is live')
    with open('communication.json') as f:
      data = json.load(f)
    data["is_live"] = True
    data = json.dumps(data, indent=4)
    with open('communication.json', 'w') as f:
      f.write(data)
  
Twitch_Bot().run()
