import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def auti(ctx):
    await ctx.send(f"""Ciao, {bot.user}! Le istruzioni per attivare i comandi di questo bot sono i seguenti:\n
                   $brainrot per ricevere un meme casuale a tema riscaldamento globale""")

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao! Sono un bot {bot.user}!")

@bot.command()
async def brainrot(ctx):
    image_path = os.path.join("images", random.choice(os.listdir("images")))
    await ctx.send(file=discord.File(image_path))

bot.run("INSREISCI TOKEN")