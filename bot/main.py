import datetime
import logging  # for logging things (on testing mode)
import os
import sys

import aiohttp
import nextcord
import nextcord.utils
from dotenv import load_dotenv
from nextcord import Webhook
from nextcord.ext import commands

load_dotenv()
intents = nextcord.Intents().all()
intents.members = True
client = commands.Bot(
    commands.when_mentioned_or("!"), intents=intents, case_insensitive=True
)
# client.remove_command("help")
invites = {}


class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = nextcord.Embed(description=page, color=0x7289DA)
            emby.timestamp = datetime.datetime.utcnow()
            await destination.send(embed=emby)


client.help_command = MyNewHelp()


@client.command(description="Load a Cogs", hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded **{extension}** module.")


@client.command(description="Unload a Cogs", hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded **{extension}** module.")


@client.command(description="Reload a Cogs", hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded **{extension}** module.")


@client.command(description="Shutdown the bot", hidden=True)
@commands.is_owner()
async def shutdown(ctx):
    embed = nextcord.Embed(
        description=f":wave: The bot has been Shutdowned, Goodbye World.",
        colour=nextcord.Colour.red(),
    )
    await ctx.send(embed=embed)
    await ctx.bot.close()


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


@client.command(description="Reboot the bot", hidden=True)
@commands.is_owner()
async def reboot(ctx):
    embed = nextcord.Embed(
        description=f":wave: The bot has been Rebooting, Please Wait..",
        colour=nextcord.Colour.red(),
    )
    await ctx.send(embed=embed)
    restart_program()


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# New member join message


@client.event
async def on_member_join(member):
    # Gets the member role as a `role` object
    if member.guild.id == 922523614828433419:
        if member.bot:
            embed = nextcord.Embed(
                color=nextcord.Colour.green(),
                description=f"**Bot Joined**\n{member.mention} {member.name}#{member.discriminator}",
            )
            embed.set_author(
                name=f"{member.name}#{member.discriminator}",
                icon_url=member.display_avatar,
            )
            embed.add_field(
                name="Account Age:",
                value=f"<t:{int(member.created_at.timestamp())}:F> (<t:{int(member.created_at.timestamp())}:R>)",
                inline=False,
            )
            embed.set_footer(text=f"ID: {member.id}")
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(os.getenv("WEBHOOK_TOKEN"), session=session)
                await webhook.send(embed=embed)

        invites_before_join = invites[922523614828433419, 806949608349106197]
        invites_after_join = await member.guild.invites()
        for invite in invites_before_join:
            if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:
                embed = nextcord.Embed(
                    color=nextcord.Colour.green(),
                    description=f"**Member Joined**\n{member.mention} {member.name}#{member.discriminator}",
                )
                embed.set_author(
                    name=f"{member.name}#{member.discriminator}",
                    icon_url=member.display_avatar,
                )
                embed.add_field(
                    name="Account Age:",
                    value=f"<t:{int(member.created_at.timestamp())}:F> (<t:{int(member.created_at.timestamp())}:R>)",
                    inline=False,
                )
                embed.add_field(
                    name="Inviter:",
                    value=f"{invite.inviter} | [discord.gg/{invite.code}](https://discord.gg/{invite.code})",
                    inline=False,
                )
                embed.set_footer(text=f"ID: {member.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)
                invites[922523614828433419, 806949608349106197] = invites_after_join
                return

    if member.guild.id == 806949608349106197:
        if member.bot:
            embed = nextcord.Embed(
                color=nextcord.Colour.green(),
                description=f"**Bot Joined**\n{member.mention} {member.name}#{member.discriminator}",
            )
            embed.set_author(
                name=f"{member.name}#{member.discriminator}",
                icon_url=member.display_avatar,
            )
            embed.add_field(
                name="Account Age:",
                value=f"<t:{int(member.created_at.timestamp())}:F> (<t:{int(member.created_at.timestamp())}:R>)",
                inline=False,
            )
            embed.set_footer(text=f"ID: {member.id}")
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    os.getenv("WM_WEBHOOK_TOKEN"), session=session
                )
                await webhook.send(embed=embed)

        invites_before_join = invites[922523614828433419, 806949608349106197]
        invites_after_join = await member.guild.invites()
        for invite in invites_before_join:
            if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:
                embed = nextcord.Embed(
                    color=nextcord.Colour.green(),
                    description=f"**Member Joined**\n{member.mention} {member.name}#{member.discriminator}",
                )
                embed.set_author(
                    name=f"{member.name}#{member.discriminator}",
                    icon_url=member.display_avatar,
                )
                embed.add_field(
                    name="Account Age:",
                    value=f"<t:{int(member.created_at.timestamp())}:F> (<t:{int(member.created_at.timestamp())}:R>)",
                    inline=False,
                )
                embed.add_field(
                    name="Inviter:",
                    value=f"{invite.inviter} | [discord.gg/{invite.code}](https://discord.gg/{invite.code})",
                    inline=False,
                )
                embed.set_footer(text=f"ID: {member.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)
                invites[922523614828433419, 806949608349106197] = invites_after_join
                return
    else:
        return


# Logging if a user leaves


@client.event
async def on_member_remove(member):
    if member.guild.id == 922523614828433419:
        embed = nextcord.Embed(colour=nextcord.Colour.red())
        embed.set_thumbnail(url=member.display_avatar)
        embed.add_field(
            name=f"**Member Left**",
            value=f"{member.mention} {member.name}#{member.discriminator}",
            inline=False,
        )
        embed.set_footer(text=f"ID: {member.id}")
        embed.timestamp = datetime.datetime.utcnow()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(os.getenv("WEBHOOK_TOKEN"), session=session)
            await webhook.send(embed=embed)

    if member.guild.id == 806949608349106197:
        embed = nextcord.Embed(colour=nextcord.Colour.red())
        embed.set_thumbnail(url=member.display_avatar)
        embed.add_field(
            name=f"**Member Left**",
            value=f"{member.mention} {member.name}#{member.discriminator}",
            inline=False,
        )
        embed.set_footer(text=f"ID: {member.id}")
        embed.timestamp = datetime.datetime.utcnow()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(os.getenv("WM_WEBHOOK_TOKEN"), session=session)
            await webhook.send(embed=embed)
    else:
        return

    # Updates the cache when a user leaves to make sure
    # everything is up to date

    invites[922523614828433419, 806949608349106197] = await member.guild.invites()


def find_invite_by_code(invite_list, code):
    for inv in invite_list:
        if inv.code == code:
            return inv


@client.event
async def on_ready():

    # versioning.

    # versioning types.

    # Turn this on/off if wanna go stable
    # version = ("main")
    # Turn this on/off if wanna go testing mode
    # version = ("testing")
    # or simply don't type anything to go undefined mode
    # version = ("")

    # Getting all the guilds our bot is in
    for guild in client.guilds:
        # Adding each guild's invites to our dict
        invites[922523614828433419, 806949608349106197] = await guild.invites()
    version = os.getenv("VERSION")

    if version == "master":
        await client.change_presence(status=nextcord.Status.online)
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(os.getenv("WEBHOOK_TOKEN"), session=session)
            await webhook.send(
                f"Hey, what's cracking now? **Robot International** initialised with version **{version}**"
            )

            webhook_WSV = Webhook.from_url(
                os.getenv("WM_WEBHOOK_TOKEN"), session=session
            )
            await webhook_WSV.send(
                f"Hey, what's cracking now? **Madeline** initialised with version **{version}**"
            )

    if version == "testing":
        await client.change_presence(
            status=nextcord.Status.idle,
            activity=nextcord.Activity(
                type=nextcord.ActivityType.playing, name=version
            ),
        )
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(os.getenv("WEBHOOK_TOKEN"), session=session)
            await webhook.send(
                f"Hey, what's cracking now? **Robot International** initialised with version **{version}**"
            )

            webhook_WSV = Webhook.from_url(
                os.getenv("WM_WEBHOOK_TOKEN"), session=session
            )
            await webhook_WSV.send(
                f"Hey, what's cracking now? **Madeline** initialised with version **{version}**"
            )

        logging.basicConfig(level=logging.INFO)
        logging.basicConfig(level=logging.WARNING)
        logging.basicConfig(level=logging.ERROR)
        logging.basicConfig(level=logging.CRITICAL)
        logging.basicConfig(level=logging.DEBUG)

    print(f"Robot International is ready for action with version {version}")


client.run(os.getenv("BOT_TOKEN"))
