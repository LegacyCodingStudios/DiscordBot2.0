import discord
from discord.ext import commands
#
import asyncio

class EatDogs(commands.Cog):
  def __init__(self, client):
    self.client = client

    self.spam = True

  def trollers(ctx):
    return str(ctx.author.id) in ["428369959501168650", "310806196330168320", "572152846351597579", "363614905607389186"]

  @commands.command(hidden=True)
  @commands.check(trollers)
  async def spam(self, ctx, amount=10, *args):
    if int(amount) > 100:
      amount = 100

    if "malachi" in args:
      return

    i = 0

    await ctx.message.delete()
    while self.spam and i < amount:
      await ctx.send(" ".join(args))
      i += 1

  @commands.command(hidden=True)
  @commands.check(trollers)
  async def stop_spam(self, ctx, *args):
    self.spam = False
    await asyncio.sleep(10)
    self.spam = True

  

def setup(client):
  client.add_cog(EatDogs(client))