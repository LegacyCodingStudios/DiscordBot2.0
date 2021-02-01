import discord
from discord.ext import commands
import asyncio

from typing import Optional

import json

import random

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def AFK(self, ctx, *, message):
    await ctx.send("WIP")
    return

  @commands.command(aliases=["emojis", "em"])
  async def emotes(self, ctx, *args):
    await ctx.send("WIP")
    await ctx.send(ctx.emojis)

  @commands.command()
  async def roll(self, ctx, sides=6, *args):
    await ctx.send(random.randint(1, sides))

  @commands.command()
  async def rps(self, ctx, choice, *args):
    bot = random.choice(["r", "p", "s"])
    user = choice[0].lower()
    if (bot == "r" and user == "p") or (bot == "p" and user == "s") or (bot == "s" and user == "r"):
      await ctx.send("You Win!")
    elif (bot == "r" and user == "s") or (bot == "p" and user == "r") or (bot == "s" and user == "p"):
      await ctx.send("The Bot Wins!")
    else:
      await ctx.send("Its a Draw!")

  @commands.command()
  async def flip(self, ctx, *args):
    res = random.choice(["Heads", "Tails"])
    await ctx.send(f"{res}!")

  @commands.command()
  async def poll(self, ctx, option1, option2, duration: Optional[int]=60, channel: Optional[discord.TextChannel]=None):
    if channel == None:
      channel = ctx.channel

    await ctx.message.delete()

    msg = await channel.send(f"{option1} OR {option2}")

    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")

    await asyncio.sleep(duration)

    msg = await msg.channel.fetch_message(msg.id)  # Can be None if msg was deleted
    
    embed = discord.Embed(title=f"{option1} V {option2}")
    embed.add_field(name=option1, value=msg.reactions[0].count - 1, inline=True)
    embed.add_field(name=option2, value=msg.reactions[1].count - 1, inline=True)

    await msg.delete()
    await channel.send("POLL FINISHED", embed=embed)

  @commands.command()
  async def suggestion(self, ctx, *, message):
    with open("./assets/json/suggestions.json", "r") as f:
      data = json.load(f)
      
      id = len(data)+1

      data.update({
        id:{
          "user": f"{ctx.author.name}#{ctx.author.discriminator}",
          "guild": ctx.guild.id,
          "suggestion": message,
          "resolved": False
        }
      })

    with open("./assets/json/suggestions.json", "w") as f:
      json.dump(data, f, indent=2)


def setup(client):
  client.add_cog(General(client))