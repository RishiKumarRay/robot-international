import datetime
import os
import time

import aiohttp
import nextcord
from dotenv import load_dotenv
from nextcord import Webhook
from nextcord.ext import commands
from pymongo import MongoClient

load_dotenv()

edited = [
    916333093277814794,
    812170448124510220,
    906409242527924264,
    906409401135538196,
    906410156265467975,
    839444297542533140,
    892722720213725205,
    906413496852422657,
    906413616138428457,
    906413019469348955,
    906413166467108874,
    906412780796674079,
    906413793385533462,
    906413910616326184,
    906412283113119774,
    906412169313255425,
    906411908326883348,
    906411802248761354,
]

cluster = MongoClient(os.getenv("MONGODB_URL"))

levelling = cluster["discord"]["levelling"]


class logging_wsv(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.guild.id == 806949608349106197:
            message = after

            if before.content == after.content:
                return

            if message.author.bot:
                return

            if before.channel.id in edited:
                embed = nextcord.Embed(
                    description=f"**Message Edited in <#{before.channel.id}> <t:{int(time.time())}:R>** • [`🔗 Jump to Message`]({after.jump_url})",
                    colour=nextcord.Colour.dark_green(),
                )
                embed.set_author(
                    name=f"{before.author}", icon_url=before.author.display_avatar
                )
                embed.add_field(
                    name=f"Before:", value=f"{before.content}", inline=False
                )
                embed.add_field(name=f"After:", value=f"{after.content}", inline=False)
                embed.set_footer(
                    text=f"Message ID: {after.id} • User ID: {before.author.id}"
                )
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.id == 806949608349106197:
            if before.nick != after.nick:
                stats = levelling.find_one({"id": before.id})
                if stats is None:
                    return
                else:
                    if after.nick is None:
                        levelling.update_one(
                            {"id": before.id}, {"$set": {"displayname": after.name}}
                        )

                    else:
                        levelling.update_one(
                            {"id": before.id}, {"$set": {"displayname": after.nick}}
                        )
                embed = nextcord.Embed(
                    description=f"{before.mention} **Nickname Changed**",
                    colour=nextcord.Colour.blurple(),
                )
                embed.set_author(
                    name=f"{before.name}#{before.discriminator}",
                    icon_url=before.display_avatar,
                )
                embed.add_field(name=f"Before:", value=f"`{before.nick}`", inline=True)
                embed.add_field(name=f"After:", value=f"`{after.nick}`", inline=True)
                embed.set_footer(text=f"ID: {before.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

            if before.roles != after.roles:
                beforelist = before.roles
                afterlist = after.roles
                if len(before.roles) > len(after.roles):
                    for i in beforelist:
                        if i not in afterlist:
                            role = i
                    embed = nextcord.Embed(
                        description=f"{before.mention} **was removed from `{role.name}` role**",
                        colour=nextcord.Colour.red(),
                    )
                    embed.set_author(
                        name=f"{before.name}#{before.discriminator}",
                        icon_url=before.display_avatar,
                    )
                    embed.set_footer(text=f"ID: {before.id}")
                    embed.timestamp = datetime.datetime.utcnow()
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(
                            os.getenv("WM_WEBHOOK_TOKEN"), session=session
                        )
                        await webhook.send(embed=embed)
                else:
                    for i in afterlist:
                        if i not in beforelist:
                            role = i
                    embed = nextcord.Embed(
                        description=f"{after.mention} **was given the `{role.name}` role**",
                        colour=nextcord.Colour.blurple(),
                    )
                    embed.set_author(
                        name=f"{after.name}#{after.discriminator}",
                        icon_url=after.display_avatar,
                    )
                    embed.set_footer(text=f"ID: {after.id}")
                    embed.timestamp = datetime.datetime.utcnow()
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(
                            os.getenv("WM_WEBHOOK_TOKEN"), session=session
                        )
                        await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        guild = self.client.get_guild(806949608349106197)
        if guild.get_member(before.id):
            if before.avatar != after.avatar:
                stats = levelling.find_one({"id": before.id})
                if stats is None:
                    return
                else:
                    levelling.update_one(
                        {"id": before.id},
                        {"$set": {"image_url": str(after.display_avatar)}},
                    )
                embed = nextcord.Embed(
                    description=f"{before.mention} **Avatar Changed**",
                    colour=nextcord.Colour.blurple(),
                )
                embed.set_author(
                    name=f"{before.name}#{before.discriminator}",
                    icon_url=before.display_avatar,
                )
                embed.set_thumbnail(url=after.display_avatar)
                embed.add_field(
                    name=f"Before:",
                    value=f"[`click here`]({before.display_avatar})",
                    inline=True,
                )
                embed.add_field(
                    name=f"After:",
                    value=f"[`click here`]({after.display_avatar})",
                    inline=True,
                )
                embed.set_footer(text=f"ID: {before.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

            if before.name != after.name:
                stats = levelling.find_one({"id": before.id})
                if stats is None:
                    return
                else:
                    levelling.update_one(
                        {"id": before.id}, {"$set": {"username": after.name}}
                    )
                embed = nextcord.Embed(
                    description=f"{before.mention} **Username Changed**",
                    colour=nextcord.Colour.blurple(),
                )
                embed.set_author(
                    name=f"{before.name}#{before.discriminator}",
                    icon_url=after.display_avatar,
                )
                embed.set_thumbnail(url=after.display_avatar)
                embed.add_field(name=f"Before:", value=f"`{before.name}`", inline=True)
                embed.add_field(name=f"After:", value=f"`{after.name}`", inline=True)
                embed.set_footer(text=f"ID: {before.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

            if before.discriminator != after.discriminator:
                stats = levelling.find_one({"id": before.id})
                if stats is None:
                    return
                else:
                    levelling.update_one(
                        {"id": before.id}, {"$set": {"discrim": after.discriminator}}
                    )
                embed = nextcord.Embed(
                    description=f"{before.mention} **Discriminator Changed**",
                    colour=nextcord.Colour.blurple(),
                )
                embed.set_author(
                    name=f"{before.name}#{before.discriminator}",
                    icon_url=after.display_avatar,
                )
                embed.set_thumbnail(url=after.display_avatar)
                embed.add_field(
                    name=f"Before:", value=f"`#{before.discriminator}`", inline=True
                )
                embed.add_field(
                    name=f"After:", value=f"`#{after.discriminator}`", inline=True
                )
                embed.set_footer(text=f"ID: {before.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild.id == 806949608349106197:
            if message.channel.id in edited:
                if message.author.bot:
                    return
                embed = nextcord.Embed(
                    description=f"**Message sent by {message.author} deleted in <#{message.channel.id}> <t:{int(time.time())}:R>**",
                    colour=nextcord.Colour.red(),
                )
                embed.set_author(
                    name=f"{message.author}", icon_url=message.author.display_avatar
                )
                embed.add_field(
                    name=f"Message:", value=f"{message.content}", inline=False
                )
                embed.set_footer(
                    text=f"Author: {message.author.id} • Message ID: {message.id}"
                )
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.guild.id == 806949608349106197:
            embed = nextcord.Embed(
                colour=nextcord.Colour.blurple(), description="**Channel Created**"
            )
            embed.set_author(name=f"{channel.guild.name}", icon_url=channel.guild.icon)
            embed.add_field(
                name=f"Name:",
                value=f"{channel.mention} | `#{channel.name}`",
                inline=True,
            )
            embed.add_field(name=f"ID: ", value=f"{channel.id}", inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    os.getenv("WM_WEBHOOK_TOKEN"), session=session
                )
                await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if before.guild.id == 806949608349106197:
            if before.name != after.name:
                embed = nextcord.Embed(
                    description="**Channel Changed**",
                    colour=nextcord.Colour.dark_green(),
                )
                embed.set_author(name=f"{after.guild.name}", icon_url=after.guild.icon)
                embed.add_field(
                    name=f"Before:", value=f"Name: `#{before.name}`", inline=False
                )
                embed.add_field(
                    name=f"After:", value=f"Name: `#{after.name}`", inline=False
                )
                embed.set_footer(text=f"ID: {after.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        if channel.guild.id == 806949608349106197:
            embed = nextcord.Embed(
                colour=nextcord.Colour.red(), description="**Channel Deleted**"
            )
            embed.set_author(name=f"{channel.guild.name}", icon_url=channel.guild.icon)
            embed.add_field(name=f"Name: ", value=f"`#{channel.name}`", inline=True)
            embed.add_field(name=f"ID: ", value=f"{channel.id}", inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    os.getenv("WM_WEBHOOK_TOKEN"), session=session
                )
                await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_private_channel_create(self, channel):
        if channel.guild.id == 806949608349106197:
            embed = nextcord.Embed(
                colour=nextcord.Colour.blurple(),
                description="**Private Channel Created**",
            )
            embed.set_author(name=f"{channel.guild.name}", icon_url=channel.guild.icon)
            embed.add_field(
                name=f"Name:",
                value=f"{channel.mention} | `#{channel.name}`",
                inline=True,
            )
            embed.add_field(name=f"ID: ", value=f"{channel.id}", inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    os.getenv("WM_WEBHOOK_TOKEN"), session=session
                )
                await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_private_channel_update(self, before, after):
        if before.guild.id == 806949608349106197:
            if before.name != after.name:
                embed = nextcord.Embed(
                    description="**Private Channel Changed**",
                    colour=nextcord.Colour.dark_green(),
                )
                embed.set_author(name=f"{after.guild.name}", icon_url=after.guild.icon)
                embed.add_field(
                    name=f"Before:", value=f"Name: `#{before.name}`", inline=False
                )
                embed.add_field(
                    name=f"After:", value=f"Name: `#{after.name}`", inline=False
                )
                embed.set_footer(text=f"ID: {after.id}")
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_private_channel_delete(self, channel):
        if channel.guild.id == 806949608349106197:
            embed = nextcord.Embed(
                colour=nextcord.Colour.red(), description="**Private Channel Deleted**"
            )
            embed.set_author(name=f"{channel.guild.name}", icon_url=channel.guild.icon)
            embed.add_field(name=f"Name: ", value=f"`#{channel.name}`", inline=True)
            embed.add_field(name=f"ID: ", value=f"{channel.id}", inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    os.getenv("WM_WEBHOOK_TOKEN"), session=session
                )
                await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        if role.guild.id == 806949608349106197:
            embed = nextcord.Embed(
                colour=nextcord.Colour.blurple(), description="**Role Created**"
            )
            embed.set_author(name=f"{role.guild.name}", icon_url=role.guild.icon)
            embed.add_field(name=f"Name: ", value=f"{role.name}", inline=True)
            embed.add_field(name=f"Color: ", value=f"{role.color}", inline=True)
            embed.add_field(name=f"ID: ", value=f"{role.id}", inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    os.getenv("WM_WEBHOOK_TOKEN"), session=session
                )
                await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        if before.guild.id == 806949608349106197:
            if before.name == after.name and before.color == after.color:
                return

            if before.name != after.name:
                embed = nextcord.Embed(
                    description="**Role Name Changed**", colour=after.color
                )
                embed.set_author(name=f"{after.guild.name}", icon_url=after.guild.icon)
                embed.add_field(name=f"Before:", value=f"`{before.name}`", inline=True)
                embed.add_field(name=f"After:", value=f"`{after.name}`", inline=True)
                embed.add_field(name=f"ID:", value=f"{after.id}", inline=True)
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

            if before.color != after.color:
                embed = nextcord.Embed(
                    description="**Role Color Changed**", colour=after.color
                )
                embed.set_author(name=f"{after.guild.name}", icon_url=after.guild.icon)
                embed.add_field(name=f"Before:", value=f"`{before.color}`", inline=True)
                embed.add_field(name=f"After:", value=f"`{after.color}`", inline=True)
                embed.add_field(name=f"ID:", value=f"{after.id}", inline=True)
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        if role.guild.id == 806949608349106197:
            embed = nextcord.Embed(
                colour=nextcord.Colour.red(), description="**Role Deleted**"
            )
            embed.set_author(name=f"{role.guild.name}", icon_url=role.guild.icon)
            embed.add_field(name=f"Name: ", value=f"{role.name}", inline=True)
            embed.add_field(name=f"Color: ", value=f"{role.color}", inline=True)
            embed.add_field(name=f"ID: ", value=f"{role.id}", inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    os.getenv("WM_WEBHOOK_TOKEN"), session=session
                )
                await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        if before.id == 806949608349106197:
            iconmessage = "The server icon has changed."
            namemessage = "The server name has changed."
            if before.icon != after.icon:
                embed = nextcord.Embed(
                    title=f"{iconmessage}", color=nextcord.Colour.blurple()
                )
                embed.set_author(name=f"{after.name}", icon_url=after.icon_url)
                embed.set_thumbnail(url=before.icon_url)
                embed.add_field(name="Before:", value=f"**see thumbnail*", inline=True)
                embed.add_field(
                    name="After:",
                    value=f"[`Click here`]({after.icon_url})",
                    inline=True,
                )
                embed.set_image(url=after.icon_url)
                embed.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed)

            if before.name != after.name:
                embed1 = nextcord.Embed(
                    title=f"{namemessage}", color=nextcord.Colour.blurple()
                )
                embed1.set_author(name=f"{after.name}", icon_url=after.icon_url)
                embed1.add_field(name="Before:", value=f"{before.name}", inline=True)
                embed1.add_field(name="After:", value=f"{after.name}", inline=True)
                embed1.timestamp = datetime.datetime.utcnow()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        os.getenv("WM_WEBHOOK_TOKEN"), session=session
                    )
                    await webhook.send(embed=embed1)


def setup(client):
    client.add_cog(logging_wsv(client))
