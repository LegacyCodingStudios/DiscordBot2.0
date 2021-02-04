import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
import os, json, datetime, nacl, threading

import BotGui

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="-", intents=intents)
  
@client.event
async def on_ready():
  print("BOT IS ONLINE")
  # online = client.get_channel(804633372948430881)
  # await online.send("The bot is now online")
  
  botgui = BotGui.DeveloperGui(client)

  x = threading.Thread(target=botgui.main)

  x.start()
  

@client.event
async def on_guild_join(guild):
  with open("assets/json/sanctions.json", "r") as f:
    data = json.load(f)

  tb = data["tempbans"]
  tb.update({guild.id: {}})

  data.update({str(guild.id): {"warnings": {}}})

  with open("assets/json/sanctions.json", "w") as f:
    json.dump(data, f, indent=2)

  with open("assets/json/economy.json", "r") as f:
    data = json.load(f)

  data.update({str(guild.id): {}})

  with open("assets/json/economy.json", "w") as f:
    json.dump(data, f, indent=2)

  
  
for i in os.listdir("./assets"):
  if i.endswith(".py"):
    client.load_extension(f"assets.{i[:-3]}")
  
load_dotenv()
token = os.getenv("TOKEN")

client.run(token)