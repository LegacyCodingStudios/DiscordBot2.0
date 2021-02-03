import discord
from discord.ext import commands

import json

class Economy(commands.Cog):
  def __init__(self, c):
    self.client = c

  @commands.command()
  async def withdraw(self, ctx, amount):
    with open("assets/json/economy.json", "r") as f:
      data = json.load(f)

    data[str(ctx.guild.id)][f"{ctx.author.name}#{ctx.author.discriminator}"]["bank"] -= amount

    data[str(ctx.guild.id)][f"{ctx.author.name}#{ctx.author.discriminator}"]["hand"] += amount

  @commands.command()
  async def deposit(self, ctx, amount):
    with open("assets/json/economy.json", "r") as f:
      data = json.load(f)

    data[str(ctx.guild.id)][f"{ctx.author.name}#{ctx.author.discriminator}"]["bank"] += amount

    data[str(ctx.guild.id)][f"{ctx.author.name}#{ctx.author.discriminator}"]["hand"] -= amount

  @commands.command()
  async def balance(self, ctx, user: discord.Member=None):
    if user == None:
      user = ctx.author

    embed = discord.Embed(title=f"{user.mention}'s balance")
    embed.add_field(name="Bank")

def setup(client):
  client.add_cog(Economy(client))