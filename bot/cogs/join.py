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

warning = cluster["dagelan"]["warning"]
mute = cluster["dagelan"]["muted"]
kicks = cluster["dagelan"]["kicks"]

wm_warning = cluster["discord"]["warning"]
wm_mute = cluster["discord"]["muted"]
wm_kicks = cluster["discord"]["kicks"]


class join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 922523614828433419:
            guild = self.client.get_guild(922523614828433419)
            img = Image.open("assets/welcome/example.png")
            draw = ImageDraw.Draw(img)
            # Make sure you insert a valid font from your folder.
            font1 = ImageFont.truetype("assets/Quotable.otf", 40)
            font2 = ImageFont.truetype("assets/Quotable.otf", 25)
            #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
            async with aiohttp.ClientSession() as session:
                async with session.get(str(member.display_avatar)) as response:
                    image = await response.read()
            avatar = (
                Image.open(BytesIO(image))
                .resize((250, 250), Image.LANCZOS)
                .convert("RGB")
            )
            c = Image.open("assets/cover.png").resize((250, 250)).convert("RGBA")
            img.paste(avatar, (425, 65), c)

            draw.text(
                (300, 345),
                f"{member.name}#{member.discriminator} just joined the server",
                (255, 255, 255),
                font=font1,
            )
            draw.text(
                (495, 395), f"Member #{guild.member_count}", (255, 255, 255), font=font2
            )
            # Change Leveling/infoimg2.png if needed.
            img.save(f"assets/welcome/card.png")
            ffile = nextcord.File(f"assets/welcome/card.png")
            channel = self.client.get_channel(922527744061997106)
            await channel.send(
                f"Hey {member.mention}, Welcome to **{guild.name}** !", file=ffile
            )
            # Make sure you insert a valid font from your folder.

            # Logging new members crime record.
            stats = warning.find_one({"id": member.id})
            mutes = mute.find_one({"id": member.id})
            kicked = kicks.find_one({"id": member.id})
            if not member.bot:
                if stats is None:
                    newuser = {"id": member.id, "warncount": 0, "reason": 0, "time": 0}
                    warning.insert_one(newuser)
                if mutes is None:
                    newuser = {"id": member.id, "mutecount": 0, "reason": 0, "time": 0}
                    mute.insert_one(newuser)
                if kicked is None:
                    newuser = {"id": member.id, "kickcount": 0, "reason": 0, "time": 0}
                    kicks.insert_one(newuser)

        if member.guild.id == 806949608349106197:
            guild = self.client.get_guild(806949608349106197)
            img = Image.open("assets/welcome/example.png")
            draw = ImageDraw.Draw(img)
            # Make sure you insert a valid font from your folder.
            font1 = ImageFont.truetype("assets/Quotable.otf", 40)
            font2 = ImageFont.truetype("assets/Quotable.otf", 25)
            #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
            async with aiohttp.ClientSession() as session:
                async with session.get(str(member.display_avatar)) as response:
                    image = await response.read()
            avatar = (
                Image.open(BytesIO(image))
                .resize((250, 250), Image.LANCZOS)
                .convert("RGB")
            )
            c = Image.open("assets/cover.png").resize((250, 250)).convert("RGBA")
            img.paste(avatar, (425, 65), c)

            draw.text(
                (300, 345),
                f"{member.name}#{member.discriminator} just joined the server",
                (255, 255, 255),
                font=font1,
            )
            draw.text(
                (495, 395), f"Member #{guild.member_count}", (255, 255, 255), font=font2
            )
            # Change Leveling/infoimg2.png if needed.
            img.save(f"assets/welcome/card.png")
            ffile = nextcord.File(f"assets/welcome/card.png")
            channel = self.client.get_channel(920015757100851260)
            await channel.send(
                f"Hey {member.mention}, Welcome to **{guild.name}** !\nPlease proceed to Verification Purposes✨\nMore Info, Please visit <#834834576417357896>.",
                file=ffile,
            )
            # Make sure you insert a valid font from your folder.

            # Logging new members crime record.
            stats = wm_warning.find_one({"id": member.id})
            mutes = wm_mute.find_one({"id": member.id})
            kicked = wm_kicks.find_one({"id": member.id})
            if not member.bot:
                if stats is None:
                    newuser = {"id": member.id, "warncount": 0, "reason": 0, "time": 0}
                    wm_warning.insert_one(newuser)
                if mutes is None:
                    newuser = {"id": member.id, "mutecount": 0, "reason": 0, "time": 0}
                    wm_mute.insert_one(newuser)
                if kicked is None:
                    newuser = {"id": member.id, "kickcount": 0, "reason": 0, "time": 0}
                    wm_kicks.insert_one(newuser)


def setup(client):
    client.add_cog(join(client))
