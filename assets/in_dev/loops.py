import discord
from discord.ext import commands, tasks

import json, datetime

from dotenv import load_dotenv
import os
#
class Loops(commands.Cog):
  def __init__(self, c):
    self.client = c

    self.unban.start()
  
  def cog_unload(self):
    self.unban.cancel()

  @tasks.loop(minutes=1)
  async def unban(self):
    print("unban loop")

    with open("assets/json/sanctions.json", "r") as f:
      data = json.load(f)
      
    bans = data["tempbans"]
    
    
    for i in bans:
      guild = self.client.get_guild(int(i))
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

  @unban.before_loop
  async def before_unban(self):
    await self.client.wait_until_ready()

  def is_dev(ctx):
    load_dotenv()
    dev = os.getenv("DEV")
    return str(ctx.author.id) in dev

  @commands.command()
  @commands.check(is_dev)
  async def start(self, ctx, loop, *args):
    try:
      self.__getattribute__(loop).start()
      await ctx.reply(f"{loop} successfully started")
    except RuntimeError as e:
      await ctx.reply(e)
    except AttributeError as e:
      await ctx.reply(e)

  @commands.command()
  @commands.check(is_dev)
  async def stop(self, ctx, loop, *args):
    try:
      self.__getattribute__(loop).stop()
      await ctx.reply(f"{loop} successfully stopped")
    except AttributeError as e:
      await ctx.reply(e)

def setup(client):
  client.add_cog(Loops(client))