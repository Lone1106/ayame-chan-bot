# Ayame-chan discord bot

Ayame-chan is a discord bot that will help with your anime desires. She will use some apis to quote characters for you, search animes based on images as well as recommend new animes to you.

[Invite Link](https://discord.com/api/oauth2/authorize?client_id=1038809073652609145&permissions=534723950656&scope=bot)

### Used APIS
Quotes: [Animechan](https://animechan.vercel.app)

Search anime per picture: [trace.moe](https://soruly.github.io/trace.moe-api/#/)

Waifus: [waifu.pics](https://waifu.pics/)

### Requirements
- channel named ayame-quote
- channel named ayame-search
- channel named ayame-waifu
- channel named ayame-recommend


## Commands

### Help
- !ayame-> gets you basic help overview (works in any channel)
- !ayame channel -> gives you info about what you can do in the current channel
- !ayame reactions -> shows all of ayames reactions (works in any channel)

### Reactions
Write one of the following commands in any channel and ayame will react!
- !ayame dance
- !ayame yo
- !ayame cool
- !ayame swarm
- !ayame idol
- !ayame angry
- !ayame wondering
- !ayame want
- !ayame blink


### Quote functionality

#### !ayame quote
Ayame-chan will try to get you a random anime quote as well as tell you which character and anime it's from. The channel has to be called **ayame-quote** for this command to trigger.

#### !ayame quote -a $"anime name"
Ayame-chan will try to get you a random character quote from the anime you specified after the _$_ sign. In case of misspelling or the anime not existing she will tell you she didn't find anything. **(no exclamation marks needed for the title)**

#### !ayame quote -c $"character name"
Ayame-chan will try to get you a random character quote from the character you specified after the _$_ sign. In case of misspelling or the character not existing she will tell you she didn't find anything. **(no exclamation marks needed for the title)**


### Search anime per picture
In case you upload an image to the channel please add **!ayame search** into the message field.
If you want to use a link to an image please prefix the link with **!ayame search $"LINK"** _(please dont put quotations around the link)_
After doing so ayame will reply to you with the anime and episode number or tell you she didnt find anything.


### Anime Waifu Images and GIF
Type **!ayame waifu** into the ayame-waifus channel and I will send you a SFW image or gif of a random anime waifu out of preset categories.


### Anime recommendations
Write one of the following comands into the ayame-recommend channel.

#### Trending anime
Type !ayame trending to get info of the latest trending anime (Name, ID, average Rating, Synopsis)

