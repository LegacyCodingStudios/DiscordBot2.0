import discord
from discord.ext import commands

from googletrans import Translator

class Languages(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def translate(self, ctx, *args):
    trans = Translator()

    print(type(" ".join(args)))
    trans = trans.translate(f"{' '.join(args)}")

    print(trans)

def setup(client):
  client.add_cog(Languages(client))