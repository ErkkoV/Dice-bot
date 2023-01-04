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
        print(message.author.name)

        await message.channel.send(message.author.name + " " + reply)

    if message.content.startswith("/help roll"):
        await message.channel.send(
            """
        Insert roll as: \n 
        `/roll 4d + 5` Roll 3 dice, take 2, add 5 skill\n
        `/roll 4n + 5` Roll 3 dice, take 2, add 5 skill\n
        `/roll -4n + 5` Roll 6 dice, worst 1, add 5 skill\n
        `/roll r3t2 + 3` Roll 3 dice, take 2, add 3 skill\n
        `/roll h3o2 + 5` Roll 3 dice, take 2, add 3 skill\n
        `/roll l4 + 5` Roll 4 dice, worst 1, add 3 skill\n
        add `[number]` to add diffciculty to the roll\n
        add `"reason"` to add reason to the roll\n
        `/roll r3t2 + 3 [25] "trying to sit down"`
        """
        )


client.run(DISCORD_TOKEN, log_handler=handler)
