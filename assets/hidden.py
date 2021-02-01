import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

import json

class BotManagementCommands(commands.Cog, name='Dev Commands'):
  def __init__(self, c):
    self.client = c

  def is_dev(ctx):
    load_dotenv()
    dev = os.getenv("DEV")
    return str(ctx.author.id) in dev

  @commands.command(aliases=["code", "dev", "edit"], hidden=True)
  @commands.check(is_dev)
  async def repls(self, ctx, repl=None):
    embed = discord.Embed(title="REPL.IT bot files")
    if repl == None:
      embed.add_field(name="main", value="https://repl.it/@DanHowe/DiscordBot20#main.py", inline=False)
      for i in os.listdir("./assets"):
        if i.endswith(".py"):
          embed.add_field(name=i[:-3], value=f"https://repl.it/@DanHowe/DiscordBot20#assets/{i}", inline=False)

    await ctx.send(embed=embed)

  @commands.command()
  @commands.check(is_dev)
  async def sug_todo(self, ctx):
    with open("./assets/json/suggestions.json", "r") as f:
      data = json.load(f)

    embed = discord.Embed(description="Unresolved Suggestions")

    empty = True

    for i in data:
      if not data[i]["resolved"]:
        empty = False
        embed.add_field(name=f"{i}\n{data[i]['user']}\n{data[i]['guild']}", value=data[i]["suggestion"], inline=False)

    if empty:
      embed.add_field(name="You are all caught up!", value="You are a good person.")

    await ctx.send(embed=embed)


  @commands.command()
  @commands.check(is_dev)
  async def sug_resolve(self, ctx, id):
    with open("./assets/json/suggestions.json", "r") as f:
      data = json.load(f)

    data[id]["resolved"] = True

    with open("./assets/json/suggestions.json", "w") as f:
      json.dump(data, f, indent=2)




def setup(client):
  client.add_cog(BotManagementCommands(client))