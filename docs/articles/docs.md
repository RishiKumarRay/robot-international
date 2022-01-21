# Commands

Let's take a deep dive to each commands on Wholesomemaker, and which file is contains these commands or whatnot.

All sorted in Alphabetical order (A-Z)

## `./main.py` - Main Executable File

This file is the heart of the bot itself. Contains loggings, `./cogs` load/reload/unload commands, and more. Here's some breakdown on that file :

### Load Commands

> [!NOTE] 
> This `cogs` is the Part of Bot Owner Commands

Load a Module

To use it, type *slash commands* `/load extension: extension`

### Unload Commands

> [!NOTE] 
> This `cogs` is the Part of Bot Owner Commands

Unload a Module

To use it, type *slash commands* `/unload extension: extension`

### Reload Commands

> [!NOTE] 
> This `cogs` is the Part of Bot Owner Commands

Reload a Module

To use it, type *slash commands* `/reload extension: extension`

### Shutdown Commands

> [!NOTE] 
> This `cogs` is the Part of Bot Owner Commands

Shutdown the bot

To use it, type *slash commands* `/shutdown`

### Reboot Commands

> [!NOTE] 
> This `cogs` is the Part of Bot Owner Commands

Reboot the bot

To use it, type *slash commands* `/reboot`

## `./cogs` folder

This folder contains most functions of the bot itself, here's some breakdown on that folder : 

### `./cogs/avatar_unslash.py` - Avatar Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Check user Avatars.

To use it, type `!avatar member`

### `./cogs/avatar.py` - Avatar Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Check user Avatars.

To use it, type *slash commands* `/avatar member: member`

### `./cogs/ban.py` - Ban Commands

> [!NOTE] 
> This `cogs` is the Part Moderation Commands

> [!WARNING]
> This Commands is Limited to `dispatch` a.k.a Head Moderators Only.

Ban a User

To use it, type *slash commands* `/ban user_id: userid`

### `./cogs/banner_unslash.py` - Banner Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Check user Banner.

To use it, type `!banner member`

### `./cogs/banner.py` - Banner Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Check user Banner.

To use it, type *slash commands* `/banner member: member`

### `./cogs/bigemote.py` - Big emote Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Resize an Emote Instantly.

To use it, type *slash commands* `/bigemote emote: emote`

### `./cogs/boost.py` - `on_server_boost` Engine

This `cogs` is the Part of `on_server_boost` that sends a message if someone boost the server.

### `./cogs/coronavirus_unslash.py` - Coronavirus stats checks Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Check the Coronavirus Stats, (Possible search terms : `all`, `country name`)

To use it, type `!covid searchterm`

### `./cogs/coronavirus.py` - Coronavirus stats checks Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Check the Coronavirus Stats, (Possible search terms : `all`, `country name`)

To use it, type *slash commands* `/covid searchterm: possible search terms`

### `./cogs/dadjokes.py` - Dad Jokes Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

> [!WARNING]
> This Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.

Provide you with Dad Jokes

To use it, type `!dadjoke`

### `./cogs/deadchat.py` - Dead Chat Listener

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Counterattack `dead chat` words with some wise words.

To use it, type `dead chat`

### `./cogs/dog.py` - Dog pictures and facts Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you with dog pictures and facts

To use it, type *slash commands* `/dog`

### `./cogs/download_unslash.py` - Download Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you A Hentai manga from [`nhentai.com`](https://nhentai.com) 

To use it, type `!download codes`

### `./cogs/download.py` - Download Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you A Hentai manga from [`nhentai.com`](https://nhentai.com) 

To use it, type *slash commands* `/download codes: codes`

### `./cogs/ghostorg_unslash.py` - Ghost Org Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Moderation Commands

> [!WARNING]
> This Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.

Basically, assigning `#18191c` hex colored roles w/o any functionality to cover up their names 

*hidden in the shadows..*

To use it, type `!ghostorg member`

### `./cogs/ghostorg.py` - Ghost Org Commands

> [!NOTE] 
> This `cogs` is the Part of Moderation Commands

> [!WARNING]
> This Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.
:::

Basically, assigning `#18191c` hex colored roles w/o any functionality to cover up their names 

*hidden in the shadows..*

To use it, type *slash commands* `/ghostorg member: member`

### `./cogs/heartbeat.py` - Heartbeat Listener

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

The bot will post a random quote from Any Members Message.

Usually it's spawns between 1 hour to 3 hours.

### `./cogs/help.py` - Help Commands

> [!NOTE] 
> This `cogs` is the Main Help Commands

To use it, type *slash commands* `/help category: category (optional)`

### `./cogs/hug_unslash.py` - Hug Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Give Hug to a User.

To use it, type `!hug member`

### `./cogs/hug.py` - Hug Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Give Hug to a User.

To use it, type *slash commands* `/hug member: member`

### `./cogs/impersonate.py` - Impersonate Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Impersonate as bot to say something.

To use it, type *slash commands* `/impersonate input: input`

### `./cogs/kick.py` - Kick Commands

> [!NOTE] 
> This `cogs` is the Part Moderation Commands

> [!WARNING]
> This Commands is Limited to `dispatch` a.k.a Head Moderators Only.

Kick a User

To use it, type *slash commands* `/kick member: member reason: reason (optional)`

### `./cogs/kiss_unslash.py` - Kiss Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Kiss someone OwO.

To use it, type `!kiss member`

### `./cogs/kiss.py` - Kiss Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Kiss someone OwO.

To use it, type *slash commands* `/kiss member: member`

### `./cogs/konesyntees.py` - Konesyntees Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Use superior Estonian technology to express your feelings like you've never before!

To use it, type *slash commands* `/konesyntees input: input voice: int[0-3] (optional) speed: int[-9 - 9] (optional)`

### `./cogs/levelsys_unslash.py` - Levelling Systems (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Economic Commands

So, this cogs contains all of economics commands. 

I'll split this section into 4 things:

- `!mytop member` = Know your or someone Rank.

- `!top` = Rankings for most messages sent.

- `!givexp member exp` = Give you or this User some XP Rewards.

- `!setxp member exp` = Set you or this User XP.

- `!resetxp member` = Reset this User XP.

### `./cogs/levelsys.py` - Levelling Systems

> [!NOTE] 
> This `cogs` is the Part of Economic Commands

So, this cogs contains all of economics commands. 

I'll split this section into 4 things:

- *slash commands* `/mytop member: member` = Know your or someone Rank.

- *slash commands* `/top` = Rankings for most messages sent.

- *slash commands* `/givexp member: member exp: exp` = Give you or this User some XP Rewards.

- *slash commands* `/setxp member: member exp: exp` = Set you or this User XP.

- *slash commands* `/resetxp member: member` = Reset this User XP.

### `./cogs/logging.py` - Logging Engine

This `cogs` is the Part of Economic Commands that Logs everything at the Server.

### `./cogs/mute.py` - Mute Commands

> [!NOTE] 
> This `cogs` is the Part Moderation Commands

> [!WARNING]
> This Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.

Mute a user

To use it, type *slash commands* `/mute member: member reason: reason (optional)`

### `./cogs/neko_unslash.py` - Neko pics Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you with some Neko Pics.

To use it, `!neko`

### `./cogs/neko.py` - Neko pics Commands 

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you with some Neko Pics.

To use it, type *slash commands* `/neko`

### `./cogs/pat_unslash.py` - Pat Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Pat Someone OwO

To use it, type `!pat member`

### `./cogs/pat.py` - Pat Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Pat Someone OwO

To use it, type *slash commands* `/pat member: member`

### `./cogs/ping_unslash.py` - Ping Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Check the Bot Latency.

To use it, type `!ping`

### `./cogs/ping.py` - Ping Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Check the Bot Latency.

To use it, type *slash commands* `/ping`

### `./cogs/prune.py` - Prune Commands

> [!NOTE] 
> This `cogs` is the Part Moderation Commands

> [!WARNING]
> This Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.

Clear Messages from a Channel.

To use it, type *slash commands* `/prune amount: amount`

### `./cogs/punch_unslash.py` - Punch Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Punch Someone.

To use it, type `!punch member`

### `./cogs/punch.py` - Punch Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Punch Someone.

To use it, type *slash commands* `/punch member: member`

### `./cogs/readme.py` - Readme Fetcher Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

> [!WARNING]
> This Commands is Limited to `Bot Owner` or in my case it's `Bot Owner/Server Owner`.

Fetch Github Gist contains Server Rules and FAQ

To use it, type `!readme`

### `./cogs/rep_unslash.py` - Rep Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

- `!rep` = Know how many Wholesome react you give to someone message.

- `!toprep` = Rankings for most Wholesome emojis sent.


### `./cogs/rep.py` - Rep Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Wholesome React Counter Systems.

I'll split this section into 2 things:

    - *slash commands* `/rep` = Know how many Wholesome react you give to someone message.

    - *slash commands* `/toprep` = Rankings for most Wholesome emojis sent.

This systems also contain `on_raw_reaction_add` functions, which is the main part of this systems.

### `./cogs/role.py` - Self Role Dropdowns

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

> [!WARNING]
> This Commands is Limited to `Bot Owner` or in my case it's `Bot Owner/Server Owner`.

Post Embed to Roles Channel, Contains Role Descriptions and Self Role Dropdowns.

To use it, type `!role`

### `./cogs/sad_unslash.py` - Sad Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Express your sadness to everyone else 😔

To use it, type `!sad`

### `./cogs/sad.py` - Sad Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Express your sadness to everyone else 😔

To use it, type *slash commands* `/sad`

### `./cogs/server_avatar_unslash.py` - Server Avatar Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Provide you with a user Server Avatar.

To use it, type `!serveravatar member`

### `./cogs/serveravatar.py` - Server Avatar Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Provide you with a user Server Avatar.

To use it, type *slash commands* `/serveravatar member: member`

### `./cogs/serverinfo_unslash.py` - Server Info Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Provide you with this Server Info.

To use it, type `!serverinfo`

### `./cogs/serverinfo.py` - Server Info Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Provide you with this Server Info.

To use it, type *slash commands* `/serverinfo`

### `./cogs/slap_unslash.py` - Slap Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Slap Someone.

To use it, type `!slap member`

### `./cogs/slap.py` - Slap Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Slap Someone.

To use it, type *slash commands* `/slap member: member`

### `./cogs/slowmode.py` - Slow Mode Commands

> [!NOTE] 
> This `cogs` is the Part Moderation Commands

> [!WARNING]
> This Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.

Slow down the chats.

To use it, type *slash commands* `/slowmode seconds: seconds`

### `./cogs/smug_unslash.py` - Smug pics Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you with some Smug Pics.

To use it, type `!smug`

### `./cogs/smug.py` - Smug pics Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you with some Smug Pics.

To use it, type *slash commands* `/smug`

### `./cogs/unban.py` - Unban Commands

> [!NOTE] 
> This `cogs` is the Part Moderation Commands

> [!WARNING]
> This Commands is Limited to `dispatch` a.k.a Head Moderators Only.

Unban a user.

To use it, type *slash commands* `/unban id: userid`

### `./cogs/unmute.py` - Unmute Commands

> [!NOTE] 
> This `cogs` is the Part Moderation Commands

> [!WARNING]
> This Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.

Unmute a user.

To use it, type *slash commands* `/unmute member: member`

### `./cogs/urban_unslash.py` - Urban Dictionary Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you with some meaning of something, straight from Urban Dictionary.

To use it, type `!urban searchterm`

### `./cogs/urban.py` - Urban Dictionary Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Provide you with some meaning of something, straight from Urban Dictionary.

To use it, type *slash commands* `/urban searchterm: searchterm`

### `./cogs/userinfo.py` - User Info Commands

> [!NOTE] 
> This `cogs` is the Part of Tools Commands

Provide you with your/another member User Info.

To use it, type `!userinfo member(optional)`

### `./cogs/user.py` - Levelling Engine

This `cogs` is the Part of Economic Commands that counts Experience per message.

### `./cogs/uwu.py` - UwU Listener

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Counterattack `uwu` words :3

To use it, type `:3`

### `./cogs/warnsys.py` - Warning Systems

> [!NOTE] 
> This `cogs` is the Part of Moderation Commands

> [!WARNING]
> `/warn` Commands is Limited to `operator` a.k.a Moderators Only, It's flexible since Head Moderators can use it use they have the `operator` roles.
:::

> [!WARNING]
> `/resetwarn` Commands is Limited to `dispatch` a.k.a Head Moderators Only.

So, this cogs contains all of warning systems.

I'll split this section into 3 things:

- *slash commands* `/warn member: member reason: reason` = Give a User some Warnings.

- *slash commands* `/resetwarn member: member` = Reset this User Warnings.

- *slash commands* `/warnings` = Know your warnings. Anyone can use this commands.

The rest is only `on_message` events, to log things to Warning Databases, feel free to check out ✌

### `./cogs/wheelspin_unslash.py` - Wheelspin Commands (Unslashed Commands)

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Spin the wheel and Get some Prize!

To use it, type `!wheelspin`

### `./cogs/wheelspin.py` - wheelspin Commands

> [!NOTE] 
> This `cogs` is the Part of Fun Commands

Spin the wheel and Get some Prize!

To use it, type *slash commands* `/wheelspin`
