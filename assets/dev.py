import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

class IN_DEV(commands.Cog):
  def __init__(self, c):
    self.client = c

  def is_dev(ctx):
    load_dotenv()
    dev = os.getenv("DEV")
    return str(ctx.author.id) in dev



def setup(client):
  client.add_cog(IN_DEV(client))