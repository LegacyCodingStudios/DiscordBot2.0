import discord
from discord.ext import commands
import asyncio
#
from typing import Optional

import json

import random

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, ctx):
    if "malachi" in ctx.content.lower():
      await ctx.delete()

  @commands.command()
  async def AFK(self, ctx, *, message):
    await ctx.send("WIP")
    return

  @commands.command(aliases=["emojis", "em"])
  async def emotes(self, ctx, *args):
    await ctx.send("WIP")
    await ctx.send(ctx.emojis)

  @commands.command()
  async def roll(self, ctx, sides=6, amount=1,  *args):
    vals = []
    tot = 0
    
    for i in range(amount):
      dice = random.randint(1, sides)
      tot += dice
      vals.append(str(dice))
      
    vals.append(f"Total: {tot}")
    
    await ctx.send(" ".join(vals))
      

  @commands.command()
  async def rps(self, ctx, choice, *args):
    botsay = random.choice(["Rock", "Paper", "Scissors"])
    bot = botsay[0].lower()
    user = choice[0].lower()
    if (bot == "r" and user == "p") or (bot == "p" and user == "s") or (bot == "s" and user == "r"):
      await ctx.send(f"{botsay}! You Win!")
    elif (bot == "r" and user == "s") or (bot == "p" and user == "r") or (bot == "s" and user == "p"):
      await ctx.send(f"{botsay}! The Bot Wins!")
    else:
      await ctx.send(f"{botsay}! Its a Draw!")

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
      
      id = len(data)

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

  @commands.command(aliases=["rm", "reminders"])
  async def reminder(self, ctx, rm=None):
    with open("./assets/json/reminders.json", "r") as f:
        data = json.load(f)

    if rm != None:
      rm = rm.lower().capitalize()

      if rm in data:
        if ctx.author.id in data[rm]:
          data[rm].remove(ctx.author.id)
        else:
          data[rm].append(ctx.author.id)

      with open("./assets/json/reminders.json", "w") as f:
        json.dump(data, f, indent=2)
    else:
      embed = discord.Embed(title="Reminders")
      uid = ctx.author.id

      for i in data:
        if uid in data[i]:
          embed.add_field(name=i, value="ON", inline=False)
        else:
          embed.add_field(name=i, value="OFF", inline=False)

      await ctx.send(embed=embed)

  @commands.command()
  async def image(self, ctx, user: discord.Member=None):
    if user == None:
      embed = discord.Embed(title=f"{ctx.guild}'s icon")
      embed.set_image(url=ctx.guild.icon_url)
    else:
      embed = discord.Embed(title=f"{user}'s icon")
      embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)

  @commands.command(name="8ball")
  async def eight_ball(self, ctx, *, message):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

    choice = random.choice(responses)

    embed = discord.Embed(title=message.capitalize(), description=choice)
    await ctx.send(embed=embed)

  @commands.command()
  async def ship(self, ctx, name1=None, name2=None, *args):
    if name1 == None:
      users = ctx.guild.members
      name1 = random.choice(users).name
    if name2 == None:
      users = ctx.guild.members
      name2 = random.choice(users).name

    len1 = round(len(name1)/2)
    len2 = round(len(name2)/2)

    embed = discord.Embed(title=f"{name1} x {name2}", description=f"{name1[:len1]}{name2[len2:]}")

    await ctx.send(embed=embed)




def setup(client):
  client.add_cog(General(client))