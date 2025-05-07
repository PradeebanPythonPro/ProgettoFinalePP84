import discord
from discord.ext import commands
import os
import random
from info import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def aiuto(ctx):
    await ctx.send(f"""Le istruzioni per attivare i comandi di questo bot sono i seguenti:\n
                   $brainrot: per ricevere un meme casuale a tema riscaldamento globale
                   $sito: per ricevere un link ad un sito casuale che parla di impatto ambientale""")

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao! Sono un bot {bot.user}!")

@bot.command()
async def brainrot(ctx):
    image_path = os.path.join("images", random.choice(os.listdir("images")))
    await ctx.send(file=discord.File(image_path))

@bot.command()
async def sito(ctx):
    await ctx.send(str(get_random_link()))

bot.run("INSERISCI TOKEN")