import requests


async def quotes(message):

    error_msg = "Hmmm hmm hmm, I couldn't remember anything at the moment 人間."
    question = message.content.strip()

    async def get_random_quote(endpoint):
        try:
            query = requests.get(endpoint).json()
            anime, character, quote = query.values()
            response = f"{quote} ({character}, {anime})"
            await message.channel.send(response)
        except Exception:
            await message.channel.send(error_msg)

    async def get_specified_quote(endpoint):
        search = message.content.split("$")[1].lower()
        search_query = f"{endpoint}{search}"
        await get_random_quote(search_query)

    if question == "!ayame quote":
        await get_random_quote("https://animechan.vercel.app/api/random")

    if question.startswith("!ayame quote -a $"):
        await get_specified_quote(
            "https://animechan.vercel.app/api/random/anime?title=")

    if question.startswith("!ayame quote -c $"):
        await get_specified_quote(
            "https://animechan.vercel.app/api/random/character?name=")
