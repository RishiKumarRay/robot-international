import os
import random

import nextcord
from dotenv import load_dotenv
from millify import millify
from nextcord.ext import commands
from pymongo import MongoClient

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))

levelling = cluster["dagelan"]["levelling"]


class users_wi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == 922523614828433419:
            stats = levelling.find_one({"id": message.author.id})
            imgp = str(message.author.display_avatar)

            if not message.author.bot:

                if stats is None:

                    if message.channel.id == [
                        923044276831666177,
                        923041554917122078,
                        923640602132873226,
                        923070166521225286,
                        923986019152433242,
                        922525745207738388,
                        924658194377232414,
                        924907111866069042,
                    ]:
                        return

                    if message.content.startswith("a!"):
                        return

                    if message.content.startswith("A!"):
                        return

                    if message.content.startswith("!"):
                        return

                    if message.content.startswith(";;"):
                        return

                    if message.content.startswith("."):
                        return

                    if message.content.startswith(";"):
                        return

                    if message.content.startswith("="):
                        return

                    if message.content.startswith("pls"):
                        return

                    if message.content.startswith("Pls"):
                        return

                    if message.content.startswith("sg!"):
                        return

                    if message.content.startswith("<@668075833780469772>"):
                        return

                    if message.content.startswith("<@922557049018142740>"):
                        return

                    memek = random.randint(1, 5)
                    newuser = {
                        "id": message.author.id,
                        "xp": memek,
                        "username": message.author.name,
                        "discrim": message.author.discriminator,
                        "messagecount": 1,
                        "image_url": imgp,
                        "level": 0,
                        "formatxp": f"{millify(memek)}",
                        "formatmessage": f"{millify(1)}",
                        "displayname": message.author.display_name,
                        "xprate": 0.0,
                    }
                    levelling.insert_one(newuser)
                else:
                    if message.channel.id == [
                        923044276831666177,
                        923041554917122078,
                        923640602132873226,
                        923070166521225286,
                        923986019152433242,
                        922525745207738388,
                        924658194377232414,
                        924907111866069042,
                    ]:
                        return

                    if message.content.startswith("a!"):
                        return

                    if message.content.startswith("A!"):
                        return

                    if message.content.startswith("!"):
                        return

                    if message.content.startswith(";;"):
                        return

                    if message.content.startswith("."):
                        return

                    if message.content.startswith(";"):
                        return

                    if message.content.startswith("="):
                        return

                    if message.content.startswith("pls"):
                        return

                    if message.content.startswith("sg!"):
                        return

                    if message.content.startswith("<@668075833780469772>"):
                        return

                    if message.content.startswith("<@922557049018142740>"):
                        return

                    silper = stats["xp"]
                    kampung = random.randint(1, 5)
                    kimak = stats["xp"]
                    xp = kimak + kampung
                    kung = stats["messagecount"] + 1
                    img = str(message.author.display_avatar)
                    debus = stats["level"]
                    kungkingkang = stats["xprate"]
                    levelling.update_one(
                        {"id": message.author.id},
                        {
                            "$set": {
                                "xp": xp,
                                "messagecount": kung,
                                "formatxp": f"{millify(xp)}",
                                "formatmessage": f"{millify(kung)}",
                                "xprate": kungkingkang,
                            }
                        },
                    )
                    lvl = 0
                    while True:
                        if xp < ((50 * (lvl ** 2)) + (50 * lvl)):
                            break
                        lvl += 1
                        silper -= (50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1))
                        goled = int(200 * ((1 / 2) * lvl))
                        expee = float((silper / goled) % 100)
                        levelling.update_one(
                            {"id": message.author.id},
                            {"$set": {"level": lvl, "xprate": expee}},
                        )
                        if silper == 0:
                            levelum = stats["level"]
                            channel = self.client.get_channel(927609583608942672)
                            await channel.send(
                                f"GG {message.author.mention}, you just advanced to level {levelum}!"
                            )
                    lvlup = self.client.get_channel(927609583608942672)
                    cur_lvl = stats["level"]
                    if debus == 5:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=922558781760610326
                        )
                        if role not in message.author.roles:
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 10:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=922558836324323399
                        )
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=922558781760610326
                        )
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 20:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=922558889596166144
                        )
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=922558836324323399
                        )
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 50:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=922558950677815306
                        )
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=922558889596166144
                        )
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 80:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=922559067174608916
                        )
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=922558950677815306
                        )
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 100:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=922559490405040159
                        )
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=922559067174608916
                        )
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)


def setup(client):
    client.add_cog(users_wi(client))
