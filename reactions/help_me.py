async def help_me(message):

    c = message.channel.name
    m = message.content.strip()

    if m == "!help":
        await message.channel.send(
            "To get help on channel specific commands please type '!help channel' in the corresponding channel. If you want to know about my reactions please use '!help reactions'. You can always check my readme here https://github.com/Lone1106/ayame-chan-bot"
        )

    if m == "!help channel" and c == "ayame-quote":
        await message.channel.send(
            "This is my quote channel. Write one of the following commands to get a anime quote from me. !ayame quote -r for a random quote, !ayame quote -a [anime name] for a random quote from an anime, !ayame quote -c [character name] for a random quote from your character. (Please dont use square brackets when you write!)"
        )

    if m == "!help channel" and c == "ayame-search":
        await message.channel.send("Coming soon")

    if m == "!help reactions":
        await message.channel.send(
            "To make me react please write !ayame [reaction].All of my current reactions are dance, yo, cool, swarm, idol, angry, wondering."
        )
