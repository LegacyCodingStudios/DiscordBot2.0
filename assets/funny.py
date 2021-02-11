import discord
from discord.ext import commands
#
import asyncio

from dotenv import load_dotenv
import os

class EatDogs(commands.Cog):
  def __init__(self, client):
    self.client = client

    self.spam = False

  def trollers(self, ctx):
    return self.spam
    return str(ctx.author.id) in ["428369959501168650", "310806196330168320", "572152846351597579", "363614905607389186"]

  def is_dev(ctx):
    load_dotenv()
    dev = os.getenv("DEV")
    return str(ctx.author.id) in dev

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
  @commands.check(is_dev)
  async def stop_spam(self, ctx, *args):
    self.spam = False

  @commands.command(hidden=True)
  @commands.check(is_dev)
  async def allow_spam(self, ctx):
    self.spam = True
    

  

def setup(client):
  client.add_cog(EatDogs(client))