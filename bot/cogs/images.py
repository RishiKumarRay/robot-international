import aiohttp
import nextcord
from nextcord.ext import commands
import nekos


class images(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="**KATS!** :3", aliases=["cat", "cats"])
    async def meow(self, ctx):
        await ctx.send(nekos.cat())

    @commands.command(description="Provide you with Neko Pics :3")
    async def neko(self, ctx):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://neko-love.xyz/api/v1/neko")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        await ctx.send(dogjson["url"])  # Send the embed

    @commands.command(description="Hug somebody :3")
    async def hug(self, ctx, *, member: nextcord.Member = None):
        if member == ctx.author:
            return await ctx.send(
                ":neutral_face: W.. wait, You can't hug yourself.. \n How ruud you are :pensive:"
            )

        if member is None:
            return await ctx.send(
                ":neutral_face: W.. wait, You can't hug yourself.. \n How ruud you are :pensive:"
            )

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://some-random-api.ml/animu/hug")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = nextcord.Embed(
            title=f"**{ctx.author.display_name}** hugging **{member.display_name}** <a:rooLove:839188637773594674>",
            color=nextcord.Color.purple(),
        )  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson["link"])
        embed.set_footer(text=f"Powered by some-random-api.ml API😉")
        await ctx.send(embed=embed)  # Send the embed

    @commands.command(description="Kiss somebody :3")
    async def kiss(self, ctx, *, member: nextcord.Member = None):
        if member == ctx.author:
            return await ctx.send(
                ":neutral_face: W.. wait, You can't kiss yourself.. \n How ruud you are :pensive:"
            )

        if member is None:
            return await ctx.send(
                ":neutral_face: W.. wait, You can't kiss yourself.. \n How ruud you are :pensive:"
            )

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://neko-love.xyz/api/v1/kiss")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = nextcord.Embed(
            title=f"**{ctx.author.display_name}** kissing **{member.display_name}** :kissing_heart:",
            color=nextcord.Color.purple(),
        )  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson["url"])
        embed.set_footer(text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed

    @commands.command(description="Pat somebody :D")
    async def pat(self, ctx, *, member: nextcord.Member = None):
        if member == ctx.author:
            return await ctx.send(
                ":neutral_face: W.. wait, You can't pat yourself.. \n How ruud you are :pensive:"
            )

        if member is None:
            return await ctx.send(
                ":neutral_face: W.. wait, You can't pat yourself.. \n How ruud you are :pensive:"
            )

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://some-random-api.ml/animu/pat")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = nextcord.Embed(
            title=f"<:uwu:839161075986726982> **{ctx.author.display_name}** patting **{member.display_name}**",
            color=nextcord.Color.purple(),
        )  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson["link"])
        embed.set_footer(text=f"Powered by some-random-api.ml API😉")
        await ctx.send(embed=embed)  # Send the embed

    @commands.command(description="Punch somebody >:(")
    async def punch(self, ctx, *, member: nextcord.Member = None):
        if member == ctx.author:
            return await ctx.send(":neutral_face: W.. wait, You can't punch yourself.")

        if member is None:
            return await ctx.send(":neutral_face: W.. wait, You can't punch yourself.")

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://neko-love.xyz/api/v1/punch")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = nextcord.Embed(
            title=f"**{ctx.author.display_name}** punching **{member.display_name}**",
            color=nextcord.Color.purple(),
        )  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson["url"])
        embed.set_footer(text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed

    @commands.command(description="Slap somebody >:(")
    async def slap(self, ctx, *, member: nextcord.Member = None):
        if member == ctx.author:
            return await ctx.send(":neutral_face: W.. wait, You can't slap yourself.")

        if member is None:
            return await ctx.send(":neutral_face: W.. wait, You can't slap yourself.")

        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://neko-love.xyz/api/v1/slap")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = nextcord.Embed(
            title=f"**{ctx.author.display_name}** slapping **{member.display_name}** <a:Slap:839192442199867422>",
            color=nextcord.Color.purple(),
        )  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson["url"])
        embed.set_footer(text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed

    @commands.command(description="😏")
    async def smug(self, ctx):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://neko-love.xyz/api/v1/smug")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = nextcord.Embed(
            title=f"**{ctx.author.display_name}**, Here's some Smug pics for you! ;)",
            color=nextcord.Color.purple(),
        )  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson["url"])
        embed.set_footer(text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed

    @commands.command(description="Express your sadness to everyone 😭😭")
    async def sad(self, ctx):
        async with aiohttp.ClientSession() as session:
            # Make a request
            request = await session.get("https://neko-love.xyz/api/v1/cry")
            dogjson = await request.json()  # Convert it to a JSON dictionary
        embed = nextcord.Embed(
            title=f"**{ctx.author.display_name}** is sad <:sadge:841528068651876413>",
            color=nextcord.Color.purple(),
        )  # Create embed
        # Set the embed image to the value of the 'link' key
        embed.set_image(url=dogjson["url"])
        embed.set_footer(text=f"Powered by neko-love.xyz API😉")
        await ctx.send(embed=embed)  # Send the embed


def setup(client):
    client.add_cog(images(client))
