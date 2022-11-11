from dotenv import load_dotenv
import os
import discord

from quotes.quotes import quotes
from reactions.reactions import reactions
from reactions.help_me import help_me
from search.search import search
from waifus.waifus import get_waifus
from recommend.recommend import get_recommend

load_dotenv()


def run_ayame():

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} ready to go")

    @client.event
    async def on_message(message):

        if message.author == client.user:
            return

        if message.channel.name == "ayame-quote":
            await quotes(message)

        if message.channel.name == "ayame-search":
            await search(message)

        if message.channel.name == "ayame-waifus":
            await get_waifus(message)

        if message.channel.name == "ayame-recommend":
            await get_recommend(message)

        await reactions(message)
        await help_me(message)

    client.run(os.getenv("TOKEN"))
