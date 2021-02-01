import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
import os

import json

import datetime

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="-", intents=intents)

@tasks.loop(minutes=1)
async def unban_loop():
  print("unban loop")

  with open("assets/json/sanctions.json", "r") as f:
    data = json.load(f)
    
  bans = data["tempbans"]
  
  
  for i in bans:
    guild = client.get_guild(int(i))
    for j in bans[i]:
      banned_users = await guild.bans()
      member_name, member_discriminator = j.split("#")

      userdata = bans[i][j]
      year = userdata["year"]
      month = userdata["month"]
      day = userdata["day"]
      hour = userdata["hour"]
      minute = userdata["mins"]


      for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator) and datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute) <= datetime.datetime.now():
            await guild.unban(user)
            del data["tempbans"][i][j]
            with open("assets/json/sanctions.json", "w") as f:
              json.dump(data, f, indent=2)
            return
  

@client.event
async def on_ready():
  print("BOT IS ONLINE")
  unban_loop.start()

@client.event
async def on_guild_join(guild):
  with open("assets/json/sanctions.json", "r") as f:
    data = json.load(f)

  data.update({"tempbans": {guild.id: {}}})

  with open("assets/json/sanctions.json", "r") as f:
    data = json.load(f)

  
  
for i in os.listdir("./assets"):
  if i.endswith(".py"):
    client.load_extension(f"assets.{i[:-3]}")
  
load_dotenv()
token = os.getenv("TOKEN")

client.run(token)