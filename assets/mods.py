import discord
from discord.ext import commands

import asyncio
#
import json
import datetime

class Moderator(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user : discord.Member, *, reason="Ban Hammer Has Spoken"):
    if user.id == ctx.author.id:
      await ctx.send("You cant ban yourself silly!")
      return
    await user.ban(reason = reason)
    await ctx.send(f"{user.name}#{user.discriminator} has been banned for {reason}")

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unban(self, ctx, user):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user : discord.Member, *, reason):
    await user.kick(reason=reason)
    
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def tempban(self, ctx, user: discord.Member, duration: int, *, reason="Ban Hammer has spoken"):
    await user.ban(reason=reason)
    with open("assets/json/sanctions.json", "r") as f:
      data = json.load(f)

    time = datetime.datetime.today() + datetime.timedelta(minutes=duration)

    tb = data["tempbans"][str(ctx.guild.id)]

    tb.update({f"{user.name}#{user.discriminator}": {"year": time.year, "month": time.month, "day": time.day, "hour": time.hour, "mins": time.minute}})

    with open("assets/json/sanctions.json", "w") as f:
      json.dump(data, f, indent=2)

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def warn(self, ctx, user: discord.Member, *, reason="You Have Been Warned!"):
    with open("assets/json/sanctions.json", "r") as f:
      data = json.load(f)

    gdata = data[str(ctx.guild.id)]
    wdata = gdata["warnings"]

    id = 0

    for i in wdata:
      if int(i) >= id:
        id = int(i)+1
        

    wdata.update({id: [f"{user.name}#{user.discriminator}", reason, str(datetime.datetime.now())]})

    with open("assets/json/sanctions.json", "w") as f:
      json.dump(data, f, indent=2)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def view_warns(self, ctx, user: discord.Member = None):
    with open("assets/json/sanctions.json", "r") as f:
      data = json.load(f)

    embed = discord.Embed(title="Warnings")
    warns = data[str(ctx.guild.id)]["warnings"]

    for i in warns:
      if user == None:
        embed.add_field(name=f"{i}: {warns[i][0]}", value=f"Reason: {warns[i][1]}\nTimestamp: {warns[i][2][:19]}\n.", inline=False)
      else:
        if warns[i][0] == f"{user.name}#{user.discriminator}":
          embed.add_field(name=f"{i}: {warns[i][0]}", value=f"Reason: {warns[i][1]}\nTimestamp: {warns[i][2][:19]}\n.", inline=False)
    
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def del_warn(self, ctx, id, *args):
    with open("assets/json/sanctions.json", "r") as f:
      data = json.load(f)

    wdata = data[str(ctx.guild.id)]["warnings"]

    if id in wdata:
      del wdata[id]

    with open("assets/json/sanctions.json", "w") as f:
      json.dump(data, f, indent=2)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, amount=10, user: discord.Member = None):
    channel = ctx.channel
    amount += 1
    if user == None:
      await channel.purge(limit=amount)
    else:
      await channel.purge(limit=amount, check=lambda message: message.author == ctx.author)
      

def setup(client):
  client.add_cog(Moderator(client))