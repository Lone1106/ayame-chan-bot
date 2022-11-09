import requests
import urllib.parse

img_str = ""


async def get_data(message):

    global img_str

    if message.attachments:
        img = message.attachments[0]
        img_str = str(img)

    if not message.attachments:
        img = message.content.strip()
        img_str = img


async def search(msg):
    try:
        await get_data(msg)

        query = requests.get("https://api.trace.moe/search?url={}".format(
            urllib.parse.quote_plus(img_str))).json()

        # Format request
        # Send answer as chat message
        print(query)

    except Exception:
        await msg.channel.send(
            "I couldn't find anything. Maybe try a different image?")
