import datetime
import random
import discord
import utils
import uwuify as uwu
import pyfiglet
from discord.ext import commands
from revChatGPT.V1 import AsyncChatbot


# Customizable Prefix
prefix = utils.Settings().load(path='.env')["prefix"]


client = commands.Bot(command_prefix = prefix, case_insensitive=True, self_bot=True)
client.remove_command('help')


LOGGER = utils.Logger(True)
COLORS = utils.Colorization()
SPOTIFY = utils.Spotify()


def main():
    TOKEN = utils.Settings().load(path='.env')["token"]

    client.run(TOKEN)


###############################################################################################
###############################################################################################
######################################### COMMANDS  ###########################################
###############################################################################################
###############################################################################################



@client.command()
async def help(ctx, *args):
    """ Shows this message """

    if not args:
        commands_list = client.commands
        commands_dict = {command.name: command.help for command in commands_list}

        message = f">>> **Help**\n\n"
        message += f"**`{client.command_prefix}help <command>`** - Shows help for a specific command.\n\n"
        for command, help_text in commands_dict.items():
            message += f"**{command}** - {help_text if help_text else 'No Description Provided.'}\n"

        await ctx.send(message)
    else:
        command = client.get_command(args[0])
        if command is None:
            await ctx.send(f"Command '{args[0]}' not found.")
            return

        message = f">>> **Help for {args[0]}**\n\n"
        message += f"**{command.name}** - {command.help if command.help else 'No Description Provided.'}\n"
        message += f"**Usage:** `{utils.Settings().load(path='.env')['prefix']}{command.name} {command.signature if command.signature else ''}`\n"

        if isinstance(command, commands.Group) and command.commands:
            message += "\n**Subcommands:**\n"
            for subcommand in command.commands:
                message += f"  **{subcommand.name}** - {subcommand.help if subcommand.help else 'No Description Provided.'}\n"
            
            message += f"\n**Usage:** `{utils.Settings().load(path='.env')['prefix']}{command.name} {command.signature if command.signature else ''} <subcommand> {subcommand.signature if subcommand.signature else ''}`\n"

        await ctx.send(message)


@client.command()
async def ping(ctx):
    """ Get the latency of the bot """
    #title= "Pong!"
    #description= f"Latency: {round(client.latency * 1000)}ms"
    #embed = utils.embed.Embed(title=title, description=description)
#
    #url = await embed.generate()
#
    #await ctx.send(url)

    await ctx.send(f"Latency: {round(client.latency * 1000)}ms")

@client.command()
async def joke(ctx):
    """ Get a random joke """
    request = utils.Request()
    joke = request.get("https://official-joke-api.appspot.com/random_joke")
    setup = joke["setup"]
    punchline = joke["punchline"]
    type_ = joke["type"]

    message = f""">>> Type: {type_}\n\n**{setup}**...\n{punchline}"""

    await ctx.send(message)


@client.command()
async def animal(ctx):
    """ Get a random dog or cat image """
    request = utils.Request()
    try:
        dog = request.get("https://dog.ceo/api/breeds/image/random")
        cat = request.get("https://api.thecatapi.com/v1/images/search")
        dog_url = dog["message"]
        cat_url = cat[0]["url"]
    except Exception as e:
        dog_url = "Bark! Bark! (An error occured)"
        cat_url = "Meow! Meow! (An error occured)"

    if random.randint(0, 1) == 0:
        await ctx.send(dog_url)
    else:
        await ctx.send(cat_url)


@client.command()
async def dog(ctx):
    """ Get a random dog image """
    try:
        request = utils.Request()
        dog = request.get("https://dog.ceo/api/breeds/image/random")
        dog_url = dog["message"]
    except Exception as e:
        dog_url = "Bark! Bark! (An error occured)"
    
    await ctx.send(dog_url)


@client.command()
async def cat(ctx):
    """ Get a random cat image """
    try:
        request = utils.Request()
        cat = request.get("https://api.thecatapi.com/v1/images/search")
        cat_url = cat[0]["url"]
    except Exception as e:
        cat_url = "Meow! Meow! (An error occured)"
    
    await ctx.send(cat_url)


@client.command()
async def shortenlink(ctx, link):
    """ Shorten a link """
    request = utils.Request()
    short_link = request.post("https://cleanuri.com/api/v1/shorten", data={"url": link})["result_url"]

    await ctx.send(f"New Link --> {short_link}")


@client.command()
async def uwuify(ctx, *, message):
    """ UwUify a message """

    await ctx.send(f"```{uwu.uwu(message)}```")


@client.command()
async def reverse(ctx, *, message):
    """ Reverse a message """

    await ctx.send(f"```{message[::-1]}```")


@client.command()
async def flip(ctx, *, message):
    """ Flip a message """

    await ctx.send(f"```{message[::-1].swapcase()}```")


@client.command()
async def mock(ctx, *, message):
    """ Mock a message """

    await ctx.send(f"```{''.join([random.choice([letter.upper(), letter.lower()]) for letter in message])}```")


@client.command()
async def ascii(ctx, *, message):
    """ Creates an ascii art message """

    await ctx.send(f"```{pyfiglet.figlet_format(message)}```")


@client.command()
async def prefix(ctx, prefix):
    """ Change the prefix """
    global COLORS
    global LOGGER

    new_settings = {
        "prefix": prefix,
        "token": utils.Settings().load(path='.env')["token"],
        "channels_to_monitor": utils.Settings().load(path=".env")["channels_to_monitor"],
        "spotify_client_id": utils.Settings().load(path=".env")["spotify_client_id"],
        "spotify_client_secret": utils.Settings().load(path=".env")["spotify_client_secret"],
    }

    utils.Settings().save(path='.env', settings=new_settings)
    await ctx.send(f"Prefix changed to **`{prefix}`**!")
    LOGGER.log(LOGGER.LogLevel.INFO, f"Prefix changed to {COLORS.colorize(COLORS.Colors.BLUE, prefix)}")
    client.command_prefix = prefix

@client.command()
async def prompt(ctx, *, prompt: str = f"Say 'Hello, how may I serve you **{client.user}**?'"):
    """ Prompt chatGPT with a message (⚠CURRENTLY DISABLED⚠)."""

    # timer = time.perf_counter()
    # differ_message = await ctx.send("Please wait, I'm thinking...")
# 
    # config = {
    #     "paid": False   # Just assume it's false
    # }
# 
    # loaded_settings = utils.Settings().load(path='.env')
    # if loaded_settings.get("OPENAI_EMAIL", "") != "" and loaded_settings.get("OPENAI_PASSWORD", "") != "":
    #     config["email"] = loaded_settings["openAI_email"]
    #     config["password"] = loaded_settings["openAI_password"]
    #     config["access_token"] = utils.Settings().load(path='.env')["openAI_session"]
    # else:
    #     config["email"] = None
    #     config["password"] = None
    #     config["access_token"] = utils.Settings().load(path='.env')["openAI_session"]
    # 
# 
    # chatbot = AsyncChatbot(config=config)
    # async for item in chatbot.ask(prompt):
    #     response = item
# 
    # await differ_message.edit(content=response)

    await ctx.send("This command is currently a work in progress. Please try again later.")


@client.command()
async def randnum(ctx, min: int, max: int):
    """ Generate a random number between two numbers """

    await ctx.send(random.randint(min, max)) if min < max else await ctx.send("The minimum number must be less than the maximum number.")


@client.command()
async def define(ctx, *, word: str):
    """ Get the meaning of a word """

    URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    request = utils.Request(False)
    response = request.get(URL)
    try:
        phonetic = response[0]["phonetic"]
    except Exception as e:
        phonetic = "⚠__Error getting phonetic.__⚠"
    meanings = response[0]["meanings"]
    type_ = meanings[0]["partOfSpeech"]
    
    definitions = list()

    i = 1
    for definition in meanings[0]["definitions"]:
        definitions.append(f"**{i}**. {definition['definition']}")
        i += 1
    
    message = f"**{word.title()}** ({type_})\n\n*{phonetic}*\n\nDefinitons:\n" + "\n".join(definitions)
    await ctx.send(message)


@client.command()
async def whois(ctx, user: discord.User):
    """ Get information about a user."""
    name = user.name
    id = user.id
    avatar = user.avatar.url
    created_at = user.created_at.strftime("%B %d, %Y")

    if user.bot:
        bot = "Yes"
    else:
        bot = "No"
    
    if ctx.guild:
        member = ctx.guild.get_member(user.id)
        if member:
            joined_at = member.joined_at.strftime("%B %d, %Y")
            roles = ", ".join([role.name for role in member.roles])
    else:
        joined_at = "N/A"
        roles = "N/A"
    
    message = f">>> **{name}**\nID: *`{id}`*\nBot: *{bot}*\n\nCreated At: *`{created_at}`*\nJoined At: *`{joined_at}`*\nRoles: *`{roles}`*"

    await ctx.send(message)
    await ctx.send(avatar)

@client.group(invoke_without_command=True)
async def spotify(ctx):
    """ Spotify controller, play, pause, resume, etc. Full Spotify Control from Discord! """

    await ctx.send("Please specify a subcommand. Use `help spotify` for a list of subcommands.")

@spotify.command()
async def play(ctx, *, query: str):
    """ Play a song on Spotify """
    global SPOTIFY

    SPOTIFY.play_track(query)
    song_name = SPOTIFY.get_current_track()["item"]["name"]

    await ctx.send(f">>> Now playing **{song_name}**!")

@spotify.command()
async def pause(ctx):
    """ Pause the current song """
    global SPOTIFY

    SPOTIFY.pause_track()

    await ctx.send(">>> Paused playback.")

@spotify.command()
async def resume(ctx):
    """ Resume the current song """
    global SPOTIFY

    SPOTIFY.resume_track()

    await ctx.send(">>> Resumed playback.")

@spotify.command()
async def skip(ctx):
    """ Skip to the next song """
    global SPOTIFY

    SPOTIFY.skip_track()

    await ctx.send(">>> Skipped to the next song.")

@spotify.command()
async def previous(ctx):
    """ Skip to the previous song """
    global SPOTIFY

    SPOTIFY.previous_track()

    await ctx.send(">>> Skipped to the previous song.")

@spotify.command()
async def search(ctx, *, query: str):
    """ Plays a song from a query """
    global SPOTIFY

    results = SPOTIFY.search_and_play(query)

    if results.lower() != query.lower():
        await ctx.send(f">>> Couldn't find that song; Playing first result: **{results}**!")
        return

    await ctx.send(f">>> Now playing **{query}**!")

@spotify.command()
async def playing(ctx):
    """ Get the current song """
    global SPOTIFY

    song_name = SPOTIFY.get_current_track()["item"]["name"]

    await ctx.send(f">>> Currently playing **{song_name}**!")

@client.command()
async def time(ctx):
    """ Get the current time """

    time = datetime.datetime.now().strftime("%I:%M %p")
    await ctx.send(f">>> It is currently **{time}**.")

@client.command()
async def generate_readme(ctx):
    """ DEVELOPER COMMAND: Generate the README.md file """
    if client.user.id != 966515900100538390:
        return
    
    await ctx.send("Generating README.md...")
    utils.generate_readme.generate(client, utils.generate_readme.inital_text)
    await ctx.send("README.md generated!")


###############################################################################################
###############################################################################################
################################## COMMAND ERROR HANDLING  ####################################
###############################################################################################
###############################################################################################

@client.event
async def on_command_error(ctx, error):
    global COLORS
    global LOGGER
    if isinstance(error, commands.CommandNotFound):
        cmds = client.commands
        for command in cmds:
            if f"**{command.name}**" in ctx.message.content:
                return

        await ctx.send(f"Command not found. Use `{utils.Settings().load(path='.env')['prefix']}help` for a list of commands.")
        LOGGER.log(LOGGER.LogLevel.WARN, f"Command not found: {ctx.message.content}")
    elif isinstance(LOGGER, commands.MissingRequiredArgument):
        missing_args = error.param.name
        await ctx.send(f"Missing required argument: `{', '.join(missing_args)}`. Use `{utils.Settings().load(path='.env')['prefix']}help` for a list of commands.")
        LOGGER.log(LOGGER.LogLevel.WARN, f"Missing required argument: {error}")
    elif isinstance(LOGGER, commands.MissingPermissions):
        missing_perms = error.missing_permissions
        await ctx.send(f"Missing required permissions: `{', '.join(missing_perms)}`. Use `{utils.Settings().load(path='.env')['prefix']}help` for a list of commands.")
        LOGGER.log(LOGGER.LogLevel.WARN, f"Missing required permissions: {error}")
    elif isinstance(error, commands.BotMissingPermissions):
        missing_perms = error.missing_permissions
        await ctx.send(f"Missing required permissions: `{', '.join(missing_perms)}`. Use `{utils.Settings().load(path='.env')['prefix']}help` for a list of commands.")
        LOGGER.log(LOGGER.LogLevel.WARN, f"Missing required permissions: {error}")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Command on cooldown. Try again in {round(error.retry_after, 2)} seconds.")
        LOGGER.log(LOGGER.LogLevel.WARN, f"Command on cooldown: {error}")
    else:
        # Discord is weird
        if "is a required argument that is missing." in str(error):
            await ctx.send(f"Missing required argument. Use `{utils.Settings().load(path='.env')['prefix']}help` for a list of commands.")
            LOGGER.log(LOGGER.LogLevel.WARN, f"Missing required argument: {error}")
            return
        if "NO_ACTIVE_DEVICE" in str(error):
            await ctx.send(f"Please load Spotify and play a song before using this command.")
            LOGGER.log(LOGGER.LogLevel.WARN, f"Spotify not active: {error}")
            return
        if "Invalid device ID" in str(error):
            await ctx.send(f"Please load Spotify and play a song before using this command.")
            LOGGER.log(LOGGER.LogLevel.WARN, f"Spotify not active: {error}")
            return
        await ctx.send(f"An error occured. Please try again later.")
        LOGGER.log(LOGGER.LogLevel.WARN, f"An error occured: {error}")


@client.event
async def on_raw_message_delete(payload):
    global COLORS
    global LOGGER
    try:
        channels = utils.Settings().load(path='.env')["channels_to_monitor"].split(",")

        channels = [int(channel) for channel in channels]
    except Exception as e:
        channels = []

    channel = client.get_channel(payload.channel_id)
    message = payload.cached_message

    if message is None:
        return

    if message.author.bot:
        return

    if message.content == "":
        return

    if not channels:
        return

    if channel.id in channels:
        LOGGER.log(LOGGER.LogLevel.INFO, f"Message deleted in {COLORS.colorize(COLORS.Colors.BLUE, channel.name)} by {COLORS.colorize(COLORS.Colors.BLUE, message.author.name)}: {COLORS.colorize(COLORS.Colors.BLUE, message.content)}")


@client.event
async def on_ready():
    menu = utils.Menu(client)
    menu.main()


if __name__ == "__main__":
    main()
