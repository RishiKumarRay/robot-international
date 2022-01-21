import functools
import io
import asyncio
import os
from time import time
import datetime
from typing import Coroutine

import nextcord
import requests
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ui"], description="See your/other people user info.")
    async def userinfo(self, ctx, *, member: nextcord.Member = None):

        if member is None:
            member = ctx.author

        roles = list(reversed([x.name for x in member.roles if x.name != "@everyone"]))

        if roles:
            roles = "\n".join(roles)
        else:
            roles = "None"

        embed = nextcord.Embed(color=member.color)
        embed.set_author(name=str(member))
        developer = 351147060956889088
        owner = ctx.guild.owner_id
        embed.add_field(
            name=f"Joined Discord On:",
            value=f"<t:{int(member.created_at.timestamp())}:F> (<t:{int(member.created_at.timestamp())}:R>)",
            inline=False,
        )
        embed.add_field(
            name=f"Joined Server At:",
            value=f"<t:{int(member.joined_at.timestamp())}:F> (<t:{int(member.joined_at.timestamp())}:R>)",
            inline=False,
        )
        # members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        if len(member.roles[1:]) < 1:
            embed.add_field(name=f"Roles:", value="None", inline=False)
            embed.add_field(name="User ID:", value=f"{member.id}", inline=False)
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar
            )
        elif roles is not None:
            embed.add_field(
                name="Roles:",
                value=", ".join(
                    [
                        role.mention
                        for role in list(reversed(member.roles))
                        if not role.is_default()
                    ]
                ),
                inline=False,
            )
            embed.add_field(name="User ID:", value=f"{member.id}", inline=False)
            embed.set_thumbnail(url=member.display_avatar)
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar
            )
        if member.id == owner:
            embed.add_field(name="Acknowledgements", value="Server Owner", inline=False)
        if member.id == developer:
            embed.add_field(name="Team", value="Bot Owner and Developer", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["ri"], description="See a role info.")
    async def roleinfo(self, ctx, role: nextcord.Role):
        dd = ctx.guild.roles
        if role in dd:
            embed = nextcord.Embed(title="Role Info", colour=role.color)
        fields = [
            ("Name:", str(role), True),
            ("ID:", role.id, True),
            ("Color:", role.color, True),
            ("Mentionable:", role.mentionable, True),
            ("Position:", role.position, True),
            (
                "Created at:",
                f"<t:{int(role.created_at.timestamp())}:F> (<t:{int(role.created_at.timestamp())}:R>)",
                True,
            ),
        ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)

    @commands.command(aliases=["av"], description="See your/other people avatar.")
    async def avatar(self, ctx, *, member: nextcord.Member = None):
        member = ctx.author if not member else member
        if member.display_avatar is None:
            lmao = await self.client.fetch_user(member.id)
            await ctx.send(f"{lmao.display_avatar}")
        else:
            await ctx.send(f"{member.display_avatar}")

    @commands.command(description="See your/other people banner.")
    async def banner(self, ctx, *, member: nextcord.Member = None):
        member = ctx.author if not member else member
        if member.banner is None:
            lmao = await self.client.fetch_user(member.id)
            await ctx.send(f"{lmao.banner}")
        else:
            await ctx.send(f"{member.banner}")

    @commands.command(aliases=["si"], description="See this server info.")
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        owner = str(ctx.guild.owner_id)
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon)
        boostlevel = str(ctx.guild.premium_tier)
        woah = str(ctx.guild.created_at.strftime("%d/%m/%Y"))

        embed = nextcord.Embed(color=nextcord.Colour.purple())

        embed.set_author(name=f"{name}", icon_url=icon)
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=f"<@{owner}>", inline=True)
        embed.add_field(name="Region", value=f"{ctx.guild.region}", inline=True)
        embed.add_field(
            name="Categories", value=f"{len(ctx.guild.categories)}", inline=True
        )
        embed.add_field(
            name="Text Channels", value=f"{len(ctx.guild.text_channels)}", inline=True
        )
        embed.add_field(
            name="Voice Channels", value=f"{len(ctx.guild.voice_channels)}", inline=True
        )
        embed.add_field(name="Members", value=memberCount, inline=True)
        embed.add_field(name="Roles", value=f"{len(ctx.guild.roles)}", inline=True)
        embed.add_field(name="Boost Level", value=boostlevel, inline=True)
        embed.set_footer(text=f"ID : {id} | Server Created • {woah}")
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["be"], description="as the name says, it's for emoji resizer."
    )
    async def bigemote(self, ctx, emoji):
        try:
            if emoji[0] == "<":
                name = emoji.split(":")[1]
                emoji_name = emoji.split(":")[2][:-1]
                anim = emoji.split(":")[0]
            if anim == "<a":
                url = f"https://cdn.discordapp.com/emojis/{emoji_name}.gif"
            else:
                url = f"https://cdn.discordapp.com/emojis/{emoji_name}.png"
            try:
                await ctx.send(url)
            except Exception as e:
                print(e)
                async with self.session.get(url) as resp:
                    if resp.status != 200:
                        er = "<:cross:839158779815657512> Error: Emote not found."
                        e = nextcord.Embed(description=er, color=0xFF0000)
                        await ctx.send(embed=e)
                        return
                    img = await resp.read()

                kwargs = {"parent_width": 1024, "parent_height": 1024}
                convert = False
                task = functools.partial(bigemote.generate, img, convert, **kwargs)
                task = self.client.loop.run_in_executor(None, task)
                try:
                    img = await asyncio.wait_for(task, timeout=15)
                except asyncio.TimeoutError:
                    er = "<:cross:839158779815657512> Error: Timed Out. Try again in a few seconds"
                    e = nextcord.Embed(description=er, color=0xFF0000)
                    await ctx.send(embed=e)
                    return
                await ctx.send(file=nextcord.File(img, filename=name + ".png"))

        except Exception as e:
            er = "<:cross:839158779815657512> Sorry, I couldn't send that emote."
            e = nextcord.Embed(description=er, color=0xFF0000)
            await ctx.send(embed=e)

    @staticmethod
    def generate(img, convert, **kwargs):
        img = io.BytesIO(img)
        return img

    @staticmethod
    async def timed(coro: Coroutine) -> tuple:
        """Time the execution of a coroutine."""

        start = time()
        result = await coro
        end = time()

        return (result, f"{(end - start) * 1000:.2f}ms")

    @commands.command(description="See the bots latency.")
    async def ping(self, ctx) -> None:
        """Get the bot's websocket and HTTP ping."""

        send = await self.timed(ctx.send("Testing ping..."))
        msg = send[0]
        edit = await self.timed(msg.edit(content="Testing editing..."))
        delete = await self.timed(msg.delete())

        results = nextcord.Embed(
            colour=0x0083F5,
            title="🏓 Pong!",
            description=(
                f"🌐 WebSocket latency: {self.client.latency * 1000:.2f}ms\n"
                f"▶️ Message Send: {send[1]}\n"
                f"🔄 Message Edit: {edit[1]}\n"
                f"🚫 Message Delete: {delete[1]}"
            ),
        )
        results.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar
        )
        results.timestamp = datetime.datetime.utcnow()

        await ctx.reply(embed=results)

    @commands.command(description="Search the Urban Dictionary for a word.")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def urban(self, ctx, *, searchterm):

        if searchterm is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please input a word to search for.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

        querystring = {"term": searchterm}

        headers = {
            "x-rapidapi-host": "mashape-community-urban-dictionary.p.rapidapi.com",
            "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        r = response.json()
        definition = r["list"][0]["definition"]
        author = r["list"][0]["author"]
        example = r["list"][0]["example"]
        word = r["list"][0]["word"]
        permalink = r["list"][0]["permalink"]
        up = r["list"][0]["thumbs_up"]
        down = r["list"][0]["thumbs_down"]
        embed = nextcord.Embed(
            title=f"Here's the results!",
            description=f"**[{word}]({permalink})**\nBy: {author}",
        )
        embed.add_field(name="Definition: ", value=definition, inline=False)
        embed.add_field(name="Example: ", value=example, inline=True)
        embed.set_footer(
            text=f"{down} Down/{up} Up, Powered by Urban Dictionary API 😉\nRequested by {ctx.author}",
            icon_url=ctx.author.avatar_url,
        )
        await ctx.send(embed=embed)

    def better_time(self, cd: int):
        time = f"{cd} seconds"
        if cd > 60:
            minutes = cd - (cd % 60)
            seconds = cd - minutes
            minutes = int(minutes / 60)
            time = f"{minutes} minutes {seconds} seconds"
        if minutes > 60:
            hoursglad = minutes - (minutes % 60)
            hours = int(hoursglad / 60)
            minutes = minutes - (hours * 60)
            time = f"{hours} hours {minutes} minutes"
        return time

    @urban.error  # command name error
    async def urban_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it
            # formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.display_name}**, you need to wait {self.better_time(cd)} to use that command again.",
                color=0xFF0000,
            )
            # sends the error message to the channel
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(tools(client))
