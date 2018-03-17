from twitchio import commands as tcommands
import discord
from discord.ext import commands as dcommands
import private
import json
import asyncio

class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'])
    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.live())

  @tcommands.twitch_command()
  async def test(self, ctx):
    await ctx.send('I am alive')
    
  async def event_ready(self):
    print('Logged into Twitch')
   
  async def live(self):
    with open('communication.json') as f:
      data = json.load(f)
    x = await self.is_live("shadeyg56")
    if x == True:
      print('Daddy is live')
      print(self.get_streams("shadeyg56"))
      data["is_live"] = True
      data = json.dumps(data, indent=4)
      with open('communication.json', 'w') as f:
        f.write(data)

  
  self.loop.run_forever()
Twitch_Bot().run()
