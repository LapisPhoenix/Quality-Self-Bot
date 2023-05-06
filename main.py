import os
import discord
import utils
import random
import discord_self_embed
import uwuify as uwu
import pyfiglet
from discord.ext import commands


# Customizable Prefix
prefix = utils.Settings().load(path='.env')["prefix"]


client = commands.Bot(command_prefix = prefix, case_insensitive=True, self_bot=True)
client.remove_command('help')


def main():
    TOKEN = utils.Settings().load(path='.env')["token"]

    client.run(TOKEN)

@client.event
async def on_ready():
    menu = utils.Menu(client)
    menu.main()


@client.command()
async def help(ctx, *args):
    """ Shows this message """

    if not args:
        commands_list = client.commands
        commands_dict = {command.name: command.help for command in commands_list}

        message = f">>> **Help**\n\n"
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
    embed = discord_self_embed.Embed(title="Pong!", description=f"Latency: {round(client.latency * 1000)}ms", colour="0x00ff00")
    url = embed.generate_url(hide_url=True, shorten_url=False)

    await ctx.send(url)

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

    await ctx.send(short_link)


@client.command()
async def uwuify(ctx, *, message):
    """ UwUify a message """

    await ctx.send(uwu.uwu(message))


@client.command()
async def reverse(ctx, *, message):
    """ Reverse a message """

    await ctx.send(message[::-1])


@client.command()
async def flip(ctx, *, message):
    """ Flip a message """

    await ctx.send(message[::-1].swapcase())


@client.command()
async def mock(ctx, *, message):
    """ Mock a message """

    await ctx.send(''.join([random.choice([letter.upper(), letter.lower()]) for letter in message]))


@client.command()
async def ascii(ctx, *, message):
    """ Creates an ascii art message """

    await ctx.send(f"```{pyfiglet.figlet_format(message)}```")


@client.command()
async def prefix(ctx, prefix):
    """ Change the prefix """

    new_settings = {"prefix": prefix, "token": utils.Settings().load(path='.env')["token"]}

    utils.Settings().save(path='.env', settings=new_settings)
    await ctx.send(f"Prefix changed to **`{prefix}`**!")
    client.command_prefix = prefix


if __name__ == "__main__":
    main()
