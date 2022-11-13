import requests

headers = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json"
}


async def get_recommend(message):

    async def get_data(endpoint):
        try:
            trend = requests.get(endpoint, headers=headers).json()["data"][0]
            cover = trend["attributes"]["coverImage"]["small"]
            title = trend["attributes"]["canonicalTitle"]
            anime_id = trend["id"]
            desc = trend["attributes"]["synopsis"]
            rating = trend["attributes"]["averageRating"]

            await message.channel.send(
                f"Title: {title} \nID: {anime_id} \naverage Rating: {rating} \nSynopsis: {desc}\n {cover}"
            )

        except Exception:
            await message.channel.send(
                "Hmmm hmm hmm, I couldn't find anything 人間.")

    query = message.content.strip()

    if query == "!ayame trending -a":
        await get_data("https://kitsu.io/api/edge/trending/anime")

    if query == "!ayame trending -m":
        await get_data("https://kitsu.io/api/edge/trending/manga")
