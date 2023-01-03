import logging
import os

import discord
from dotenv import load_dotenv

from roller import roller

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/info"):
        await message.channel.send("Avaivable Commands: \n /coffee \n /roll")

    if message.content.startswith("/coffee"):
        await message.channel.send("ToniPal should drink more coffee.")

    if message.content.startswith("/roll"):
        reply = roller(message.content)
        await message.channel.send(reply)


client.run(DISCORD_TOKEN, log_handler=handler)
