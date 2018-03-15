import discord
from discord.ext import commands as dcommands
from twitchio import commands as tcommands
import subprocess

scripts = ['/home/pi/Desktop/Darkness-Twitch/bot.py', 'home/pi/Desktop/Darkness-Twitch/twitch.py']
for script in scripts:
  #calls startup functions from bots
  p = subprocess.Popen([script, "ArcView"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  output = p.communicate()
  print(output[0])

