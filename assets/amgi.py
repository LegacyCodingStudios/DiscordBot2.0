import discord
from discord.ext import commands

import os
import random 

class AMGI(commands.Cog):
  def __init__(self, client):
    self.client = client

  def is_guild_amgi(ctx):
    return str(ctx.guild.id) in ["804633372948430878", "478952313562595329"]

  @commands.command(aliases=["rollin"], hidden=True)
  @commands.check(is_guild_amgi)
  async def alex(self, ctx, *args):
    await ctx.message.delete()

    path="./assets/imgs/Alex/"
    files=os.listdir(path)
    d=random.choice(files)
    file = discord.File(f"{path}{d}")
    await ctx.send(file=file)

def setup(client):
  client.add_cog(AMGI(client))

  # Go to the .env file and the username and password are there