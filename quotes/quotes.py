import requests


async def quotes(message):

    error_msg = "Hmmm hmm hmm, I couldn't remember anything at the moment 人間."
    question = message.content.strip()

    if question == "!ayame quote":
        try:
            query = requests.get(
                "https://animechan.vercel.app/api/random").json()
            anime, character, quote = query.values()
            response = f"{quote} ({character}, {anime})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(error_msg)

    if question.startswith("!ayame quote -a $"):
        try:
            title = message.content.split("$")[1].lower()
            query = requests.get(
                f"https://animechan.vercel.app/api/random/anime?title={title}"
            ).json()
            anime, character, quote = query.values()
            response = f"{quote} ({character}, {anime})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(error_msg)

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
            await message.channel.send(error_msg)
