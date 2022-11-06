from dotenv import load_dotenv
import os
import discord

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

        if message.content.startswith("!ayame "):
            pass

    @client.event
    async def on_member_join(member):
        channel = client.get_channel(1038808903061872692)
        await channel.send(f"<@{member.id}> Konnakkiri!!")

    client.run(os.getenv("TOKEN"))
