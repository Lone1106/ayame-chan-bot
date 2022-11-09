import requests


async def quotes(message):

    question = message.content.strip()

    if question.startswith("!ayame quote -r"):
        try:
            query = requests.get(
                "https://animechan.vercel.app/api/random").json()
            anime, character, quote = query.values()
            response = f"{quote} ({character}, {anime})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(
                "I couldnt find a quote right now. Maybe try again later.")

    if question.startswith("!ayame quote -a $"):
        try:
            title = message.content.split(" ")[1].lower()
            query = requests.get(
                f"https://animechan.vercel.app/api/random/anime?title={title}"
            ).json()
            anime, character, quote = query.values()
            response = f"{quote} ({character}, {anime})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(
                "I couldnt find a quote from this anime.")

    if question.startswith("!ayame quote -c $"):
        try:
            char = message.content.split("$")[1].lower()
            query = requests.get(
                f"https://animechan.vercel.app/api/random/character?name={char}"
            ).json()
            anime, character, quote = query.values()
            response = f"{quote} ({character}, {anime})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(
                "I couldnt find a quote of that character.")
