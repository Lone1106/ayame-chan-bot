import requests


async def quotes(message):

    if message.content.startswith("!ayame quote -r"):
        try:
            query = requests.get(
                "https://animechan.vercel.app/api/random").json()
            response = f"{query['quote']} ({query['character']}, {query['anime']})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(
                "I couldnt find a quote right now. Maybe try again later.")

    if message.content.startswith("!ayame quote -a $"):
        try:
            title = message.content.split("$")[1].lower()
            query = requests.get(
                f"https://animechan.vercel.app/api/random/anime?title={title}"
            ).json()
            response = f"{query['quote']} ({query['character']})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(
                "I couldnt find a quote from this anime. Try checking your spelling."
            )

    if message.content.startswith("!ayame quote -c $"):
        try:
            char = message.content.split("$")[1].lower()
            query = requests.get(
                f"https://animechan.vercel.app/api/random/character?name={char}"
            ).json()
            response = f"{query['quote']} ({query['character']}, {query['anime']})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(
                "I couldnt find a quote of that character. Try checking your spelling."
            )
