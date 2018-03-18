from twitchio import commands as tcommands
import discord
from discord.ext import commands as dcommands
import private
import json
import asyncio
import random

class Twitch_Bot(tcommands.TwitchBot):
  def __init__(self):
    super().__init__(prefix='!', nick='Darkness', token=private.TWITCH_TOKEN, initial_channels=['shadeyg56'], client_id=private.TWITCH_CLIENT_ID)
    self.loop.create_task(self.live())
    self.answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
                     'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
                     'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                     'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
                     'Very doubtful']
  @tcommands.twitch_command()
  async def test(self, ctx):
    await ctx.send('I am alive')
    
  async def event_ready(self):
    print('Logged into Twitch')

  @tcommands.twitch_command()
  async def discord(self, ctx):
    await ctx.send(f"{ctx.message.author} here is a list of Shade's discord servers: The United Republic of Dragons and Kats (Main): https://discord.gg/ahhJYjJ\n Darkness Support: https://discord.gg/fGV8jR2\n Fortnite: https://discord.io/fortnite2")

  @tcommands.twitch_command()
  async def eightball(self, ctx, *, question:str):
    if question:
      await ctx.send(f"{ctx.message.author.name}, Question: {question}, Answer: {random.choice(self.answers)}")
    else:
      await ctx.send(f"{ctx.message.author.name}, you must provide a question")

  async def live(self):
    with open('communication.json') as f:
      data = json.load(f)
    await asyncio.sleep(10)
    while not self.loop.is_closed():
      x = await self.is_live('shadeyg56')
      if x == True:
        print('Daddy is live :)')
        print(type(data))
        if data["is_live"] == "False":
          data['is_live'] = 'True'
        else:
          pass
        data = json.dumps(data, indent=4)
        with open('communication.json', 'w') as f:
          f.write(data)
      else:
        print("Daddy isn't live ;(")
        data["is_live"] = "False"
        data = json.dumps(data, indent=4)
        with open('communication.json', 'w') as f:
          f.write(data)
        await asyncio.sleep(5)

  
  
Twitch_Bot().run()
