import discord
from discord.ext import commands

import json
#
class Info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def info(self, ctx, *args):
    with open(".json", "r") as f:
      data = json.load(f)

    embed = discord.Embed(title="BOT INFO")

    for i in data:
      embed.add_field(name=i, value=data[i], inline=False)

    await ctx.send(embed=embed)

  @commands.command()
  async def ping(self, ctx):
    await ctx.send('Pong! {0}'.format(self.client.latency))

def setup(client):
  client.add_cog(Info(client))