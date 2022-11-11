import requests

headers = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json"
}


async def get_recommend(message):

    query = message.content.strip()

    if query == "!ayame trending":

        try:
            trend = requests.get("https://kitsu.io/api/edge/trending/anime",
                                 headers=headers).json()
            title = trend["data"][0]["attributes"]["canonicalTitle"]
            anime_id = trend["data"][0]["id"]
            desc = trend["data"][0]["attributes"]["synopsis"]
            rating = trend["data"][0]["attributes"]["averageRating"]

            await message.channel.send(
                f"Title: {title} \n ID: {anime_id} \n average Rating: {rating} \n Synopsis: {desc}\n"
            )

        except Exception:
            await message.channel.send(
                "Hmmm hmm hmm, I couldn't find anything 人間.")
