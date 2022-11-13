async def help_me(message):

    c = message.channel.name
    m = message.content.strip()

    if m == "!ayame":
        await message.channel.send(
            "To get help on channel specific commands please type **!help channel** in any of my channels. If you want to know about my reactions please use **!help reactions**."
        )

    if m == "!ayame reactions":
        await message.channel.send(
            "To make me react please write **!ayame [reaction name]**. All of my current reactions are dance, yo, cool, swarm, idol, angry, wondering, want, blink."
        )

    if m == "!ayame channel":
        if c == "ayame-search":
            await message.channel.send(
                "Upload an image to the channel or link an image and I will search the anime and episode for you! If you use a link please perfix it with **!ayame search $[LINK]**. If you upload an image to the channel put **!ayame search** into the message of the image. (Please dont use square brackets for the link!)"
            )

        if c == "ayame-quote":
            await message.channel.send(
                "Write one of the following commands to get a quote from me. **!ayame quote** for a random quote, **!ayame quote -a $[anime name]** for a random quote from the named anime, **!ayame quote -c $[character name]** for a random quote from the named character. (Please dont use square brackets for the names!)"
            )

        if c == "ayame-waifus":
            await message.channel.send(
                "Type **!ayame waifu** into the ayame-waifus channel and I will send you a SFW image or gif of a random anime waifu out of preset categories."
            )

        if c == "ayame-recommend":
            await message.channel.send(
                "Type **!ayame trending -a** to get info of the latest trending anime from me and **!ayame trending -m** for manga!"
            )
