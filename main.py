import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif ve hazır!")

@bot.command()
async def selam(ctx):
    await ctx.send("Aleykümselam cano! Bot buluttan 7/24 selam çakıyor.")

bot.run(os.getenv("TOKEN"))
