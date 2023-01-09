import logging
import os

import discord
from dotenv import load_dotenv

from probber import probber
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
        if not "prob" in message.content and not "roll" in message.content:
            await message.channel.send(
                "Avaivable Commands: \n `/coffee` `/roll` `/prob` \n`/info roll` `/info probs`"
            )

    if message.content.startswith("/coffee"):
        await message.channel.send("ToniPal should drink more coffee.")

    if message.content.startswith("/roll"):
        reply = roller(message.content)
        await message.channel.send(message.author.name + " " + reply)

    if message.content.startswith("/prob"):
        reply = probber(message.content)
        await message.channel.send(message.author.name + " " + reply)

    if message.content.startswith("/info roll"):
        await message.channel.send(
            """
Insert roll as: 
`/roll 4d + 5` Roll 3 dice, take 2, add 5 skill
`/roll 4n + 5` Roll 3 dice, take 2, add 5 skill
`/roll -4n + 5` Roll 6 dice, worst 1, add 5 skill
`/roll r3t2 + 3` Roll 3 dice, take 2, add 3 skill
`/roll h3o2 + 5` Roll 3 dice, take 2, add 3 skill
`/roll l4 + 5` Roll 4 dice, worst 1, add 3 skill
add `[number]` to add diffciculty to the roll
add `"reason"` to add reason to the roll
`/roll r3t2 + 3 [25] "trying to sit down"`
"""
        )

    if message.content.startswith("/info prob"):
        await message.channel.send(
            """
Probability calculator simulates 10000 rolls to calculate the probability.
Insert prob as: 
`/prob r4t3 + 15 vs r3t3 +7` or
`/prob h4o3 + 15 vs l6 +7` or
`/prob h4o3 + 15 vs [30]` or
`/prob h4o3 + 15
Syntax is `Defence vs Attack`
"""
        )


client.run(DISCORD_TOKEN, log_handler=handler)
