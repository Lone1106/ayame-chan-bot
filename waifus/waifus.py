import requests
import random


async def get_waifus(message):

    query = message.content.strip()

    async def get_type():

        types = [
            "waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry",
            "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet",
            "blush", "smile", "wave", "highfive", "handhold", "nom", "bite",
            "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance",
            "cringe"
        ]

        rand = random.randint(0, len(types))

        choice = types[rand]

        return choice

    if query == "!ayame waifu":

        choice = await get_type()

        try:
            img = requests.get(
                f"https://api.waifu.pics/sfw/{choice}").json()["url"]
            await message.channel.send(img)

        except Exception:
            await message.channel.send(
                "Hmmm hmm hmm, I couldn't find anything right now 人間.")
