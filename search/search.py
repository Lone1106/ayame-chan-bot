import requests
import urllib.parse


async def get_data(msg):

    img_str = ""

    if msg.attachments:
        img = msg.attachments[0]
        img_str = str(img)

    if not msg.attachments:
        img = msg.content.strip().split("$")[1]
        img_str = img

    return img_str


async def search(message):
    msg_content = message.content.strip()

    if msg_content.startswith("!ayame search"):

        await message.channel.send("Yo Yo, I'm on it 人間!")

        try:
            search_data = await get_data(message)

            query = requests.get("https://api.trace.moe/search?url={}".format(
                urllib.parse.quote_plus(search_data))).json()

            response = query["result"][0]["filename"].replace(
                "]", "_").replace("(", "_").split("_")[1]

            await message.channel.send(response)

        except Exception:
            await message.channel.send(
                "Hmmm hmm hmm, I couldn't find anything 人間.")
