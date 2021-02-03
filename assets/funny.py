import discord
from discord.ext import commands

class EatDogs(commands.Cog):
  def __init__(self, client):
    self.client = client

  def trollers(ctx):
    return str(ctx.author.id) in ["428369959501168650", "310806196330168320", "572152846351597579"]

  @commands.command(hidden=True)
  @commands.check(trollers)
  async def spam(self, ctx, amount, *args):
    await ctx.message.delete()
    for i in range(0, int(amount)):
      await ctx.send(" ".join(args))

def setup(client):
  client.add_cog(EatDogs(client))