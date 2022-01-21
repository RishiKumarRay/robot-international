import os
from io import BytesIO

import aiohttp
import nextcord
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from dotenv import load_dotenv
from nextcord.ext import commands
from pymongo import MongoClient

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))

levelling = cluster["dagelan"]["levelling"]
wm_levelling = cluster["discord"]["levelling"]


class levellings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["mytop"], description="Know your or someone Rank.")
    async def rank(self, ctx, *, member: nextcord.Member = None):
        if ctx.guild.id == 922523614828433419:
            if member is None:
                member = ctx.author

            stats = levelling.find_one({"id": member.id})
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    await ctx.send(embed=embed)
            else:
                xp = stats["xp"]
                exp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50 * (lvl ** 2)) + (50 * lvl)):
                        break
                    lvl += 1
                xp -= (50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1))
                boxes = int((xp / (200 * ((1 / 2) * lvl))) * 20)
                apasihmaulu = boxes * "■" + (20 - boxes) * "□"
                rankings = levelling.find().sort("xp", -1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                # Replace infoimgimg.png with your background image.
                if member.id == 351147060956889088:
                    img = Image.open("assets/template/1.png")
                else:
                    img = Image.open("assets/rank.png")
                draw = ImageDraw.Draw(img)
                # Make sure you insert a valid font from your folder.
                font = ImageFont.truetype("assets/Quotable.otf", 36)
                eggs = ImageFont.truetype("assets/Quotable.otf", 30)
                font3 = ImageFont.truetype("assets/Quotable.otf", 60)
                font4 = ImageFont.truetype("assets/Quotable.otf", 55)
                # Make sure you insert a valid font from your folder.
                font1 = ImageFont.truetype("assets/ARIALUNI.otf", 35)
                font2 = ImageFont.truetype("assets/DejaVuSerif.otf", 34)
                #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(member.display_avatar)) as response:
                        image = await response.read()
                avatar = (
                    Image.open(BytesIO(image))
                    .resize((175, 175), Image.LANCZOS)
                    .convert("RGB")
                )
                c = Image.open("assets/cover.png").resize((175, 175)).convert("RGBA")
                img.paste(avatar, (30, 55), c)
                if str(member.status) == "online":
                    d = Image.open("assets/statuses/online.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                if str(member.status) == "offline":
                    d = Image.open("assets/statuses/offline.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                if str(member.status) == "dnd":
                    d = Image.open("assets/statuses/dnd.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                if str(member.status) == "idle":
                    d = Image.open("assets/statuses/idle.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                draw.text(
                    (242, 120),
                    f"{member.name}#{member.discriminator}",
                    (255, 255, 255),
                    font=font1,
                )
                draw.text(
                    (732, 130),
                    f"{xp} / {int(200*((1/2)*lvl))} XP",
                    (255, 255, 255),
                    font=eggs,
                )
                draw.text((766, 70), f"Level", (98, 211, 245), font=font)
                draw.text((830, 50), f"{lvl}", (98, 211, 245), font=font3)
                draw.text((622, 70), f"Rank ", (255, 255, 255), font=font)
                draw.text((690, 55), f"#{rank}", (255, 255, 255), font=font4)
                draw.text((242, 165), f"{apasihmaulu}", (98, 211, 245), font=font2)
                # Change Leveling/infoimg2.png if needed.
                img.save(f"assets/card.png")
                ffile = nextcord.File(f"assets/card.png")
                await ctx.send(file=ffile)
                # Make sure you insert a valid font from your folder.

        elif ctx.guild.id == 806949608349106197:
            if member is None:
                member = ctx.author

            stats = wm_levelling.find_one({"id": member.id})
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    await ctx.send(embed=embed)
            else:
                xp = stats["xp"]
                exp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50 * (lvl ** 2)) + (50 * lvl)):
                        break
                    lvl += 1
                xp -= (50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1))
                boxes = int((xp / (200 * ((1 / 2) * lvl))) * 20)
                apasihmaulu = boxes * "■" + (20 - boxes) * "□"
                rankings = wm_levelling.find().sort("xp", -1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                # Replace infoimgimg.png with your background image.
                if member.id == 351147060956889088:
                    img = Image.open("assets/premium/matt.png")
                elif member.id == 532264079641935883:
                    img = Image.open("assets/premium/beep.png")
                elif member.id == 685969061175099460:
                    img = Image.open("assets/premium/beep.png")
                elif member.id == 678302535202635797:
                    img = Image.open("assets/premium/meh.png")
                # kyle's image, he can't change it anymore.. so, yeah.
                elif member.id == 670890892655198215:
                    img = Image.open("assets/premium/kyle.png")
                elif member.id == 494870400153550859:
                    img = Image.open("assets/premium/fib.png")
                elif member.id == 616469711995142145:
                    img = Image.open("assets/premium/neko.png")
                else:
                    img = Image.open("assets/template/1.png")
                draw = ImageDraw.Draw(img)
                # Make sure you insert a valid font from your folder.
                font = ImageFont.truetype("assets/Quotable.otf", 36)
                eggs = ImageFont.truetype("assets/Quotable.otf", 30)
                font3 = ImageFont.truetype("assets/Quotable.otf", 60)
                font4 = ImageFont.truetype("assets/Quotable.otf", 55)
                # Make sure you insert a valid font from your folder.
                font1 = ImageFont.truetype("assets/ARIALUNI.otf", 35)
                font2 = ImageFont.truetype("assets/DejaVuSerif.otf", 34)
                #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(member.display_avatar)) as response:
                        image = await response.read()
                avatar = (
                    Image.open(BytesIO(image))
                    .resize((175, 175), Image.LANCZOS)
                    .convert("RGB")
                )
                c = Image.open("assets/cover.png").resize((175, 175)).convert("RGBA")
                img.paste(avatar, (30, 55), c)
                if str(member.status) == "online":
                    d = Image.open("assets/statuses/online.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                if str(member.status) == "offline":
                    d = Image.open("assets/statuses/offline.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                if str(member.status) == "dnd":
                    d = Image.open("assets/statuses/dnd.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                if str(member.status) == "idle":
                    d = Image.open("assets/statuses/idle.png").resize((45, 45))
                    img.paste(d, (162, 180), d)

                draw.text(
                    (242, 120),
                    f"{member.name}#{member.discriminator}",
                    (255, 255, 255),
                    font=font1,
                )
                draw.text(
                    (732, 130),
                    f"{xp} / {int(200*((1/2)*lvl))} XP",
                    (255, 255, 255),
                    font=eggs,
                )
                draw.text((766, 70), f"Level", (98, 211, 245), font=font)
                draw.text((830, 50), f"{lvl}", (98, 211, 245), font=font3)
                draw.text((622, 70), f"Rank ", (255, 255, 255), font=font)
                draw.text((690, 55), f"#{rank}", (255, 255, 255), font=font4)
                draw.text((242, 165), f"{apasihmaulu}", (98, 211, 245), font=font2)
                # Change Leveling/infoimg2.png if needed.
                img.save(f"assets/card.png")
                ffile = nextcord.File(f"assets/card.png")
                await ctx.send(file=ffile)
                # Make sure you insert a valid font from your folder.
        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        aliases=["give"],
        description="Adding XP to Tagged Members.\nRequires `Kick Members` permission.",
    )
    @commands.has_permissions(kick_members=True)
    async def givexp(self, ctx, member: nextcord.Member, *, exp: int):
        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if exp is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass a valid value!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if ctx.guild.id == 922523614828433419:
            stats = levelling.find_one({"id": member.id})
            # if ctx.channel.id == botcommands_channel:
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                return await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    return await ctx.send(embed=embed)
            else:
                xp = stats["xp"] + exp
                # if ctx.channel.id == botcommands_channel
                levelling.update_one({"id": member.id}, {"$set": {"xp": xp}})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> {exp} XP has been given to **{member.display_name}**",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)
        elif ctx.guild.id == 806949608349106197:
            stats = wm_levelling.find_one({"id": member.id})
            # if ctx.channel.id == botcommands_channel:
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                return await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    return await ctx.send(embed=embed)
            else:
                xp = stats["xp"] + exp
                # if ctx.channel.id == botcommands_channel
                wm_levelling.update_one({"id": member.id}, {"$set": {"xp": xp}})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> {exp} XP has been given to **{member.display_name}**",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @givexp.error
    async def givexp_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        aliases=["reset"],
        description="Reset Tagged Members XP.\nRequires `Ban Members` permission.",
    )
    @commands.has_permissions(ban_members=True)
    async def resetxp(self, ctx, *, member: nextcord.Member):
        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if ctx.guild.id == 922523614828433419:
            stats = levelling.find_one({"id": member.id})
            # if ctx.channel.id == botcommands_channel:
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                return await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    return await ctx.send(embed=embed)
            else:
                levelling.delete_one({"id": member.id})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406>  **{member.display_name}**'s XP has been resetted.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

        elif ctx.guild.id == 806949608349106197:
            stats = wm_levelling.find_one({"id": member.id})
            # if ctx.channel.id == botcommands_channel:
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                return await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    return await ctx.send(embed=embed)
            else:
                wm_levelling.delete_one({"id": member.id})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406>  **{member.display_name}**'s XP has been resetted.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @resetxp.error
    async def resetxp_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Ban Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["top"], description="Rankings for most messages sent.")
    async def levels(self, ctx):
        if ctx.guild.id == 922523614828433419:
            await ctx.send(
                f"Here is **{ctx.guild.name}**'s leaderboard: <https://bot.gnztmpz.eu.org/leaderboard/{ctx.guild.id}>"
            )
        elif ctx.guild.id == 806949608349106197:
            await ctx.send(
                f"Here is **{ctx.guild.name}**'s leaderboard: <https://bot.gnztmpz.eu.org/leaderboard/{ctx.guild.id}>"
            )
        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        aliases=["take"],
        description="Remove some XP from Tagged Members.\nRequires `Kick Members` permission.",
    )
    @commands.has_permissions(kick_members=True)
    async def removexp(self, ctx, member, *, exp: int):

        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if exp is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass a valid value!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if ctx.guild.id == 922523614828433419:
            stats = levelling.find_one({"id": member.id})
            # if ctx.channel.id == botcommands_channel:
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                return await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    return await ctx.send(embed=embed)
            else:
                pepeq = stats["xp"] - exp
                levelling.update_one({"id": member.id}, {"$set": {"xp": pepeq}})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> {exp} XP has been taken from **{member.display_name}**.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

        elif ctx.guild.id == 806949608349106197:
            stats = wm_levelling.find_one({"id": member.id})
            # if ctx.channel.id == botcommands_channel:
            if member.bot:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> {ctx.author.mention}, bots do not have ranks!",
                    color=0xFF0000,
                )
                return await ctx.send(embed=embed)
            if stats is None:
                if not member.bot:
                    embed = nextcord.Embed(
                        description=f"<:cross:839158779815657512> **{member.display_name}** aren't ranked yet. Send some messages first, then try again.",
                        color=0xFF0000,
                    )
                    return await ctx.send(embed=embed)
            else:
                pepeq = stats["xp"] - exp
                wm_levelling.update_one({"id": member.id}, {"$set": {"xp": pepeq}})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> {exp} XP has been taken from **{member.display_name}**.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @removexp.error
    async def removexp_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(levellings(client))
