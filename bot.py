import discord
from discord.ext import commands as dcommands
import private
import asyncio
import json


bot = dcommands.Bot(command_prefix=dcommands.when_mentioned_or('!'))

@bot.event
async def on_ready():
  print('------------------------------------')
  print('THE BOT IS ONLINE')
  print('------------------------------------')
  print("Name: {}".format(bot.user.name))
  print('Author: shadeyg56')
  print("ID: {}".format(bot.user.id))
  print('DV: {}'.format(discord.__version__))
  await bot.change_presence(activity=discord.Streaming(name='Watching over the chat until next stream', url='https://www.twitch.tv/shadeyg56'))

async def is_live():
	await bot.wait_until_ready()
	await asyncio.sleep(1)
	with open("communication.json") as f:
		data = json.load(f)
	try:
		if data["is_live"] == True:
			await bot.change_presence(activity=discord.Streaming(name="Success!", url="https://twitch.tv/shadeyg56"))
	except:
		print("Daddy isn't live ;(")
	finally:
		await asyncio.sleep(5)


bot.loop.create_task(is_live())
bot.run(private.DISCORD_TOKEN)
