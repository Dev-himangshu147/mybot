import discord
from discord.ext import commands

bot = commnads.Bot(command_prefix="your prefix")

@bot.event 
async def on_ready()
  print(f"logged in as {bot.user.name}")

@bot.command()
async def ping(ctx):
  await ctx.send(f"**pong** {round(bot.latency * 1000)} ms")

bot.run("your bot token")

