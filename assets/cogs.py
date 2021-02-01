import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

class Cogs(commands.Cog):
  def __init__(self, client):
    self.client = client

  def is_dev(ctx):
    load_dotenv()
    dev = os.getenv("DEV")
    return str(ctx.author.id) in dev

  @commands.command()
  @commands.check(is_dev)
  async def load(self, ctx, ext, *args):
    try:
      self.client.load_extension(f"assets.{ext}")
      await ctx.message.reply("COG LOADED SUCCESSFULLY")
    except:
      await ctx.message.reply("COG NOT LOADED")

  @commands.command()
  @commands.check(is_dev)
  async def unload(self, ctx, ext, *args):
    try:
      self.client.UNload_extension(f"assets.{ext}")
      await ctx.reply("COG UNLOADED SUCCESSFULLY")
    except:
      await ctx.reply("COG NOT UNLOADED")

  @commands.command()
  @commands.check(is_dev)
  async def reload(self, ctx, ext, *args):
    try:
      self.client.reload_extension(f"assets.{ext}")
      await ctx.reply("COG RELOADED SUCCESSFULLY")
    except:
      await ctx.reply("COG NOT RELOADED")

def setup(client):
  client.add_cog(Cogs(client))