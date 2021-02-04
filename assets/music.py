import discord
from discord.ext import commands

import nacl
#
class Music(commands.Cog):
  def __init__(self, c):
    self.client = c

  @commands.command()
  async def join(self, ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
  @commands.command()
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()

def setup(client):
  client.add_cog(Music(client))