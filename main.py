import discord
import os
import random

# Inserisci il tuo token del bot qui
TOKEN = "TUO_TOKEN_DISCORD"

# ID del canale in cui vuoi inviare le immagini (opzionale)
CHANNEL_ID = 1234567890

# Cartella contenente le immagini
IMAGE_FOLDER = "immagini/"

# Configura il bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Evita che il bot risponda ai propri messaggi

    if message.content.strip().lower() == "$brainrotCC":
        if not os.path.exists(IMAGE_FOLDER) or not os.listdir(IMAGE_FOLDER):
            await message.channel.send("Nessuna immagine disponibile!")
            return

        image_path = os.path.join(IMAGE_FOLDER, random.choice(os.listdir(IMAGE_FOLDER)))
        await message.channel.send(file=discord.File(image_path))

client.run(TOKEN)