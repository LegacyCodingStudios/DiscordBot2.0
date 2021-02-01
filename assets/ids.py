import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

class Ids(commands.Cog):
  def __init__(self, client):
    self.client = client

  def is_dev(ctx):
    load_dotenv()
    dev = os.getenv("DEV")  # checks ".env" for the data andthen checks if the user meets the reqirements
    return str(ctx.author.id) in dev

  @commands.command()
  @commands.check(is_dev)
  async def userid(self, ctx, user=None, *args):

    if user == None:
      userid = ctx.author.id
    else:
      userid = discord.utils.get(self.client.get_all_members(), id=int(user[3:-1]))
      if userid == None:
        userid = ctx.guild.get_member_named(user)

    if userid == None:
      await ctx.reply("No user found")
    else:
      await ctx.reply(userid)

  @commands.command()
  @commands.check(is_dev)
  async def channelid(self, ctx, channel=None, *args):
    if channel == None:
      channel = ctx.channel
    else:
      print(channel)
      print(channel[2:-1])
      channel = discord.utils.get(self.client.get_all_channels(), id=int(channel[2:-1]))

    if channel == None:
      await ctx.reply("No channel found")
    else:
      await ctx.reply(channel.id)

  @commands.command()
  @commands.check(is_dev)
  async def guildid(self, ctx, *args):
    await ctx.reply(ctx.guild.id)

def setup(client):
  client.add_cog(Ids(client))