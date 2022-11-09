# Ayame-chan discord bot

Ayame-chan is a discord bot that will help with your anime desires. She will use some apis to quote characters for you, search animes based on images as well as recommend new animes to you.

[Invite Link](https://discord.com/api/oauth2/authorize?client_id=1038809073652609145&permissions=534723950656&scope=bot)

### Used APIS
Quotes: [Animechan](https://animechan.vercel.app)

Search anime per picture: [trace.moe](https://soruly.github.io/trace.moe-api/#/)

### Requirements
- channel named ayame-quote
- channel named ayame-search


## Commands

### Help
- !help -> gets you basic help overview
- !help channel -> gives you info about what you can do in the channel
- !help reactions -> shows all of the current reactions

### Reactions
Write one of the following commands in any channel and ayame will give you a fitting reaction.
- !ayame dance
- !ayame yo
- !ayame cool
- !ayame swarm
- !ayame idol
- !ayame angry
- !ayame wondering


### Quote functionality

#### !ayame quote -r
Ayame-chan will get you a random anime quote as well as tell you which character and anime it's from. The channel has to be called **ayame-quote** for this command to trigger.

#### !ayame quote -a $"anime name"
Ayame-chan will get you a random character quote from the anime you specified after the _$_ sign. In case of misspelling or the anime not existing she will tell you she didn't find anything. **(no exclamation marks needed for the title)**

#### !ayame quote -c $"character name"
Ayame-chan will get you a random character quote from the character you specified after the _$_ sign. In case of misspelling or the character not existing she will tell you she didn't find anything. **(no exclamation marks needed for the title)**


### Search anime per picture
Send a image link or upload a image file to the **ayame-search** channel and ayame will search the anime for you. **No prefixes needed, only image file or link**

