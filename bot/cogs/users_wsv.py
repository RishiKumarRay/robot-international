import os
import random

import nextcord
from dotenv import load_dotenv
from millify import millify
from nextcord.ext import commands
from pymongo import MongoClient

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))

levelling = cluster["discord"]["levelling"]


class users_wsv(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == 806949608349106197:
            stats = levelling.find_one({"id": message.author.id})
            imgp = str(message.author.display_avatar)

            if not message.author.bot:

                if stats is None:

                    memek = random.randint(15, 25)
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
                    silper = stats["xp"]
                    kampung = random.randint(15, 25)
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
                            channel = self.client.get_channel(906410156265467975)
                            await channel.send(
                                f"GG {message.author.mention}, you just advanced to level {levelum}!"
                            )
                    lvlup = self.client.get_channel(906410156265467975)
                    cur_lvl = stats["level"]
                    if debus == 1:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=812176809852141569
                        )  # thug
                        if role not in message.author.roles:
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 5:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=812213398351118366
                        )  # hustler
                        reward = nextcord.utils.get(
                            message.author.guild.roles, id=910867708856389662
                        )  # perm-nickname
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=812176809852141569
                        )  # thug
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            await message.author.add_roles(reward)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {reward.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 10:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=812214255432106005
                        )  # soldier
                        reward = nextcord.utils.get(
                            message.author.guild.roles, id=910867223076302878
                        )  # perm-emoji
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=812213398351118366
                        )  # hustler
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            await message.author.add_roles(reward)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {reward.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 15:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=812215368663826442
                        )  # trigger
                        reward = nextcord.utils.get(
                            message.author.guild.roles, id=910867268123127828
                        )  # perm-image
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=812214255432106005
                        )  # soldier
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            await message.author.add_roles(reward)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {reward.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 20:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=812215661824049213
                        )  # enforcer
                        reward = nextcord.utils.get(
                            message.author.guild.roles, id=910867805321166919
                        )  # perm-stream
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=812215368663826442
                        )  # trigger
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            await message.author.add_roles(reward)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {reward.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 25:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=847144224260358214
                        )  # facilitator
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=812215661824049213
                        )  # enforcer
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 30:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=847144504535679076
                        )  # public enemy
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=847144224260358214
                        )  # facilitator
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 35:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=847144667136655410
                        )  # shot caller
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=847144504535679076
                        )  # public enemy
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 40:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=847144638430183495
                        )  # street boss
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=847144667136655410
                        )  # shot caller
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 45:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=863946146165817344
                        )  # right hand
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=847144638430183495
                        )  # street boss
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
                            message.author.guild.roles, id=910869468979269682
                        )  # active
                        reward = nextcord.utils.get(
                            message.author.guild.roles, id=812215772935749633
                        )  # top commenters
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=863946146165817344
                        )  # right hand
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {reward.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 60:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=894782251424956427
                        )  # sucka
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=910869468979269682
                        )  # active
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 70:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=894782324300976129
                        )  # poot-butt
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894782251424956427
                        )  # sucka
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
                            message.author.guild.roles, id=894782368534130708
                        )  # buster
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894782324300976129
                        )  # poot-butt
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 90:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=894782407734079521
                        )  # red-headed-stepchild
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894782368534130708
                        )  # buster
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
                            message.author.guild.roles, id=894782454924193842
                        )  # peon
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894782407734079521
                        )  # red-headed-stepchild
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 125:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=894782510947528716
                        )  # pee-wee
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894782454924193842
                        )  # peon
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 150:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=894782511345958962
                        )  # prankster
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894782510947528716
                        )  # pee-wee
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 175:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=894786710834143252
                        )  # mack
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894782511345958962
                        )  # prankster
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)
                    if debus == 200:
                        role = nextcord.utils.get(
                            message.author.guild.roles, id=894786732984250370
                        )  # pimp
                        rolea = nextcord.utils.get(
                            message.author.guild.roles, id=894786710834143252
                        )  # mack
                        if role not in message.author.roles:
                            await message.author.remove_roles(rolea)
                            await message.author.add_roles(role)
                            embed = nextcord.Embed(
                                description=f"{message.author.display_name} has unlocked {role.mention} for reaching Level {cur_lvl}",
                                color=0x00FF00,
                            )
                            await lvlup.send(embed=embed)


def setup(client):
    client.add_cog(users_wsv(client))
