from dotenv import load_dotenv
import os
import discord

from quotes.quotes import quotes

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

    @client.event
    async def on_member_join(member):
        channel = client.get_channel(os.getenv("WELCOME_CHANNEL"))
        await channel.send(f"<@{member.id}> Konnakkiri!!")

    client.run(os.getenv("TOKEN"))
