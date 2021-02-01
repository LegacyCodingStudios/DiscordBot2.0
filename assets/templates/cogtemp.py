import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

class TEMPLATE(commands.Cog):
  def __init__(self, client):
    self.client = client

  def checktemp(ctx):
    load_dotenv()
    checkvar = os.getenv("CHECK_STORE")  # checks ".env" for the data andthen checks if the user meets the reqirements
    return str(ctx.author.id) in checkvar

  @commands.command()
  @commands.check(checktemp)
  async def func(self, ctx, *args):
    return # do something here

def setup(client):
  client.add_cog(TEMPLATE(client))