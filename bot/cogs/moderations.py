import datetime
import json
import os
import time
from datetime import timedelta
from typing import Optional

import nextcord
import requests
from dotenv import load_dotenv
from nextcord.ext import commands
from pymongo import MongoClient

load_dotenv()

cluster = MongoClient(os.getenv("MONGODB_URL"))
warning = cluster["dagelan"]["warning"]
mute = cluster["dagelan"]["muted"]
kicks = cluster["dagelan"]["kicks"]

wi_warning = cluster["discord"]["warning"]
wi_mute = cluster["discord"]["muted"]
wi_kicks = cluster["discord"]["kicks"]


class moderations(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        description="Ban Somebody out from this server.\nRequires `Ban Members` permission."
    )
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason="No reason provided"):
        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        if member == ctx.message.author:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't kick yourself.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        if member.top_role >= ctx.author.top_role:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't use this commands on members above your role!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        embed = nextcord.Embed(
            description=f"<:check:839158727512293406> Successfully banned {member.mention} for: {reason}",
            color=0x00FF00,
        )
        await ctx.send(embed=embed)
        try:
            await member.send(
                f"You have been banned from **{ctx.guild}** for the following reason: {reason}"
            )
        except BaseException:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Failed to send DM to {member.mention}. They probably had their DM's closed.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)
        user = await self.client.fetch_user(member)
        await ctx.guild.ban(user, reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Ban Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        description="Unban Somebody out from this server.\nRequires `Ban Members` permission."
    )
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):

        if id is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by passing their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        embed = nextcord.Embed(
            description=f"<:check:839158727512293406> Successfully unbanned {user.mention}",
            color=0x00FF00,
        )
        await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Ban Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        description="Kick Somebody out from this server.\nRequires `Kick Members` permission."
    )
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason="No reason provided"):
        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        if member == ctx.message.author:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't kick yourself.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        if member.top_role >= ctx.author.top_role:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't use this commands on members above your role!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if ctx.guild.id == 922523614828433419:
            kicked = kicks.find_one({"id": ctx.member.id})
            if kicked is None:
                newuser = {"id": member.id, "kickcount": 1, "reason": reason}
                kicks.insert_one(newuser)
            else:
                kickcounts = kicks["kickcount"] + 1
                kicks.update_one(
                    {"id": member.id},
                    {"$set": {"kickcount": kickcounts, "reason": reason}},
                )

        elif ctx.guild.id == 806949608349106197:
            kicked = wi_kicks.find_one({"id": ctx.member.id})
            if kicked is None:
                newuser = {"id": member.id, "kickcount": 1, "reason": reason}
                wi_kicks.insert_one(newuser)
            else:
                kickcounts = kicks["kickcount"] + 1
                wi_kicks.update_one(
                    {"id": member.id},
                    {"$set": {"kickcount": kickcounts, "reason": reason}},
                )

        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        embed = nextcord.Embed(
            description=f"<:check:839158727512293406> Successfully Kicked {member.mention} for: {reason}",
            color=0x00FF00,
        )
        await ctx.send(embed=embed)
        try:
            await member.send(
                f"You have been Kicked from **{ctx.guild}** for the following reason: {reason}"
            )
        except BaseException:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Failed to send DM to {member.mention}. They probably had their DM's closed.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        embed = nextcord.Embed(
            description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
            color=0xFF0000,
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["clear", "purge"],
        description="Cleaning the chats.\nRequires `Manage Messages` permission.",
    )
    @commands.has_permissions(manage_messages=True)
    async def prune(self, ctx, amount: int):

        if amount is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass the amount to prune correctly!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        await ctx.channel.purge(limit=amount + 1)

    @prune.error
    async def prune_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Manage Messages` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        aliases=["slow"],
        description="Slow down the chats.\nRequires `Manage Messages` permission.",
    )
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        if seconds == 0:
            embed = nextcord.Embed(
                description=f"<:check:839158727512293406> Slowmode has been disabled for this channel.",
                color=0x00FF00,
            )
            await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(
                description=f"<:check:839158727512293406> Slowmode has been enabled for {seconds} second(s) in this channel.",
                color=0x00FF00,
            )
            await ctx.send(embed=embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        embed = nextcord.Embed(
            description=f"<:cross:839158779815657512> You must have the `Manage Messages` permission to use this command!",
            color=0xFF0000,
        )
        await ctx.send(embed=embed)

    @commands.command(
        description="Mute/Unmute Somebody on this server.\nRequires `Timeout Members` permission."
    )
    @commands.has_permissions(moderate_members=True)
    async def mute(
        self,
        ctx,
        member: nextcord.Member = None,
        time: Optional[int] = 0,
        *,
        reason: Optional[str] = "No Description Provided",
    ):
        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        if member == ctx.message.author:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't mute yourself.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        if member.top_role >= ctx.author.top_role:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't use this commands on members above your role!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)
        year = datetime.datetime.utcnow()
        month = year + timedelta(minutes=time)
        tiemout = str(month)
        token = os.getenv("BOT_TOKEN")
        payload = {
            "communication_disabled_until": f"{tiemout}",
        }
        headers = {
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json",
            "X-Audit-Log-Reason": f"{reason}",
        }

        r = requests.patch(
            f"https://discord.com/api/v9/guilds/{member.guild.id}/members/{member.id}",
            data=json.dumps(payload),
            headers=headers,
        )
        if time == 0:
            embed = nextcord.Embed(colour=nextcord.Colour.blurple())
            embed.set_author(
                name=f"{member.name}#{member.discriminator} has been unmuted",
                icon_url=member.display_avatar,
            )
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            if ctx.guild.id == 922523614828433419:
                stats = mute.find_one({"id": member.id})
                if stats is None:
                    mute.insert_one(
                        {
                            "id": member.id,
                            "mutecount": 1,
                            "reason": reason,
                            "time": int(time.time()),
                        }
                    )
                else:
                    mutecount = stats["mutecount"] + 1
                    mute.update_one(
                        {"id": member.id},
                        {
                            "$set": {
                                "mutecount": mutecount,
                                "reason": reason,
                                "time": int(time.time()),
                            }
                        },
                    )
            elif ctx.guild.id == 806949608349106197:
                stats = wi_mute.find_one({"id": member.id})
                if stats is None:
                    wi_mute.insert_one(
                        {
                            "id": member.id,
                            "mutecount": 1,
                            "reason": reason,
                            "time": int(time.time()),
                        }
                    )
                else:
                    mutecount = stats["mutecount"] + 1
                    wi_mute.update_one(
                        {"id": member.id},
                        {
                            "$set": {
                                "mutecount": mutecount,
                                "reason": reason,
                                "time": int(time.time()),
                            }
                        },
                    )
            else:
                embed = nextcord.Embed(
                    description=f"<:cross:839158779815657512> This commands is not available in this server.",
                    color=0xFF0000,
                )
                return await ctx.send(embed=embed)

            embed = nextcord.Embed(
                description=f"**Reason:** {reason}", colour=nextcord.Colour.blurple()
            )
            embed.set_author(
                name=f"{member.name}#{member.discriminator} has been muted",
                icon_url=member.display_avatar,
            )
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
            await member.send(
                f"You have been muted on **{ctx.guild}** for the following reason: {reason}"
            )

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Timeout Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == 922523614828433419:
            stats = warning.find_one({"id": message.author.id})
            mutes = mute.find_one({"id": message.author.id})
            kicked = kicks.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {
                        "id": message.author.id,
                        "warncount": 0,
                        "reason": 0,
                        "time": 0,
                    }
                    warning.insert_one(newuser)
                if mutes is None:
                    newuser = {
                        "id": message.author.id,
                        "mutecount": 0,
                        "reason": 0,
                        "time": 0,
                    }
                    mute.insert_one(newuser)
                if kicked is None:
                    newuser = {
                        "id": message.author.id,
                        "kickcount": 0,
                        "reason": 0,
                        "time": 0,
                    }
                    kicks.insert_one(newuser)

        if message.guild.id == 806949608349106197:
            stats = wi_warning.find_one({"id": message.author.id})
            mutes = wi_mute.find_one({"id": message.author.id})
            kicked = wi_kicks.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {
                        "id": message.author.id,
                        "warncount": 0,
                        "reason": 0,
                        "time": 0,
                    }
                    wi_warning.insert_one(newuser)
                if mutes is None:
                    newuser = {
                        "id": message.author.id,
                        "mutecount": 0,
                        "reason": 0,
                        "time": 0,
                    }
                    wi_mute.insert_one(newuser)
                if kicked is None:
                    newuser = {
                        "id": message.author.id,
                        "kickcount": 0,
                        "reason": 0,
                        "time": 0,
                    }
                    wi_kicks.insert_one(newuser)

    @commands.command(
        description="Warn a User in this server.\nRequires `Kick Members` permission."
    )
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: nextcord.Member = None, *, reason: str = None):

        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if member.top_role >= ctx.author.top_role:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't use this commands on members above your role!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if member is member.bot:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> {ctx.author.mention}, You can't warn bots.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if member is ctx.author:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.mention}**, you can't warn yourself!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if reason is None:
            reason = "No Reason Provided."

        if ctx.guild.id == 922523614828433419:
            stats = warning.find_one({"id": member.id})
            if stats is None:
                warning.insert_one(
                    {
                        "id": member.id,
                        "warncount": 1,
                        "reason": reason,
                        "time": int(time.time()),
                    }
                )
                await member.send(
                    f"You have been warned on **{ctx.guild}** for the following reason: {reason}"
                )
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> **{member.mention}** has been warned for the following reason: {reason}.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)
            else:
                warncount = stats["warncount"] + 1
                warning.update_one(
                    {"id": member.id},
                    {
                        "$set": {
                            "warncount": warncount,
                            "reason": reason,
                            "time": int(time.time()),
                        }
                    },
                )
                await member.send(
                    f"You have been warned on **{ctx.guild}** for the following reason: {reason}"
                )
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> **{member.mention}** has been warned for the following reason: {reason}.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

        elif ctx.guild.id == 806949608349106197:
            stats = wi_warning.find_one({"id": member.id})
            if stats is None:
                wi_warning.insert_one(
                    {
                        "id": member.id,
                        "warncount": 1,
                        "reason": reason,
                        "time": int(time.time()),
                    }
                )
                await member.send(
                    f"You have been warned on **{ctx.guild}** for the following reason: {reason}"
                )
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> **{member.mention}** has been warned for the following reason: {reason}.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)
            else:
                warncount = stats["warncount"] + 1
                wi_warning.update_one(
                    {"id": member.id},
                    {
                        "$set": {
                            "warncount": warncount,
                            "reason": reason,
                            "time": int(time.time()),
                        }
                    },
                )
                await member.send(
                    f"You have been warned on **{ctx.guild}** for the following reason: {reason}"
                )
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406> **{member.mention}** has been warned for the following reason: {reason}.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

        else:
            await member.send(
                f"You have been warned on **{ctx.guild}** for the following reason: {reason}"
            )
            embed = nextcord.Embed(
                description=f"<:check:839158727512293406> **{member.mention}** has been warned for the following reason: {reason}.",
                color=0x00FF00,
            )
            await ctx.send(embed=embed)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        description="Reset User Warnings.\nRequires `Kick Members` permission."
    )
    @commands.has_permissions(kick_members=True)
    async def resetwarn(self, ctx, *, member: nextcord.Member = None):

        if member is None:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> Please pass in a valid user by mentioning them or using their ID.",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if member.top_role >= ctx.author.top_role:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You can't use this commands on members above your role!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if member is member.bot:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> {ctx.author.mention}, Bot doesn't have warnings!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        if member is ctx.author:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.mention}**, you can't reset your own warnings!",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)

        else:
            if ctx.guild.id == 922523614828433419:
                warning.delete_one({"id": member.id})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406>  **{member.mention}**'s warnings has been resetted.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

            if ctx.guild.id == 806949608349106197:
                wi_warning.delete_one({"id": member.id})
                embed = nextcord.Embed(
                    description=f"<:check:839158727512293406>  **{member.mention}**'s warnings has been resetted.",
                    color=0x00FF00,
                )
                await ctx.send(embed=embed)

    @resetwarn.error
    async def resetwarn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        description="Receive a DM from me with the list of your warnings on this server."
    )
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def warnings(self, ctx):
        if ctx.guild.id == 922523614828433419:
            stats = warning.find_one({"id": ctx.author.id})
            mutes = mute.find_one({"id": ctx.author.id})
            kicked = kicks.find_one({"id": ctx.author.id})
            if stats is None:
                newuser = {"id": ctx.member.id, "warncount": 0, "reason": 0, "time": 0}
                warning.insert_one(newuser)
            elif mutes is None:
                newuser = {"id": ctx.member.id, "mutecount": 0, "reason": 0, "time": 0}
                mute.insert_one(newuser)
            elif kicked is None:
                newuser = {"id": ctx.member.id, "kickcount": 0, "reason": 0, "time": 0}
                kicks.insert_one(newuser)
            hitungkick = kicked["kickcount"]
            waktukick = kicked["time"]
            alasankick = kicked["reason"]
            hitungmute = mutes["mutecount"]
            waktumute = mutes["time"]
            alasanmute = mutes["reason"]
            hitungwarn = stats["warncount"]
            alasanwarn = stats["reason"]
            waktuwarn = stats["time"]
            embed = nextcord.Embed(
                title="{}'s Warnings".format(ctx.author.display_name), colour=0xF1EE19
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            embed.set_thumbnail(url=ctx.author.display_avatar)
            embed.add_field(
                name=":pushpin: **Kicks**",
                value=f"> **Kick Count**: {hitungkick} Kick(s)\n> **Date**: <t:{waktukick}:f>\n> **Latest Reason**: {alasankick}",
                inline=False,
            )
            embed.add_field(
                name=":pushpin: **Mutes**",
                value=f"> **Mute Count**: {hitungmute} Mute(s)\n> **Date**: <t:{waktumute}:f>\n> **Latest Reason**: {alasanmute}",
                inline=False,
            )
            embed.add_field(
                name=":pushpin: **Warnings**",
                value=f"> **Warn Count**: {hitungwarn} Warn(s)\n> **Date**: <t:{waktuwarn}:f>\n> **Latest Reason**: {alasanwarn}",
                inline=False,
            )
            await ctx.author.send(embed=embed)

        if ctx.guild.id == 806949608349106197:
            stats = wi_warning.find_one({"id": ctx.author.id})
            mutes = wi_mute.find_one({"id": ctx.author.id})
            kicked = wi_kicks.find_one({"id": ctx.author.id})
            if stats is None:
                newuser = {"id": ctx.member.id, "warncount": 0, "reason": 0, "time": 0}
                wi_warning.insert_one(newuser)
            elif mutes is None:
                newuser = {"id": ctx.member.id, "mutecount": 0, "reason": 0, "time": 0}
                wi_mute.insert_one(newuser)
            elif kicked is None:
                newuser = {"id": ctx.member.id, "kickcount": 0, "reason": 0, "time": 0}
                wi_kicks.insert_one(newuser)
            hitungkick = kicked["kickcount"]
            waktukick = kicked["time"]
            alasankick = kicked["reason"]
            hitungmute = mutes["mutecount"]
            waktumute = mutes["time"]
            alasanmute = mutes["reason"]
            hitungwarn = stats["warncount"]
            alasanwarn = stats["reason"]
            waktuwarn = stats["time"]
            embed = nextcord.Embed(
                title="{}'s Warnings".format(ctx.author.display_name), colour=0xF1EE19
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            embed.set_thumbnail(url=ctx.author.display_avatar)
            embed.add_field(
                name=":pushpin: **Kicks**",
                value=f"> **Kick Count**: {hitungkick} Kick(s)\n> **Date**: <t:{waktukick}:f>\n> **Latest Reason**: {alasankick}",
                inline=False,
            )
            embed.add_field(
                name=":pushpin: **Mutes**",
                value=f"> **Mute Count**: {hitungmute} Mute(s)\n> **Date**: <t:{waktumute}:f>\n> **Latest Reason**: {alasanmute}",
                inline=False,
            )
            embed.add_field(
                name=":pushpin: **Warnings**",
                value=f"> **Warn Count**: {hitungwarn} Warn(s)\n> **Date**: <t:{waktuwarn}:f>\n> **Latest Reason**: {alasanwarn}",
                inline=False,
            )
            await ctx.author.send(embed=embed)

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

    @warnings.error  # command name error
    async def warnings_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it
            # formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            # msg is the message you would like to send, the format is how it
            # formats the seconds left.
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.display_name}**, you need to wait {self.better_time(cd)} to use that command again.",
                color=0xFF0000,
            )
            # sends the error message to the channel
            await ctx.send(embed=embed)

    @commands.command(description="Imagine being so funny LMAO", hidden=True)
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dadjoke(self, ctx):

        url = "https://dad-jokes.p.rapidapi.com/random/joke"
        headers = {
            "x-rapidapi-host": "dad-jokes.p.rapidapi.com",
            "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
        }

        response = requests.request("GET", url, headers=headers)
        r = response.json()
        author = r["body"][0]["setup"]
        definition = r["body"][0]["punchline"]
        await ctx.send(f"{author}\n{definition}")

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

    @dadjoke.error  # command name error
    async def dadjoke_error(self, ctx, error):  # define error
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
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
                color=0xFF0000,
            )
        await ctx.send(embed=embed)
        # sends the error message to the channel

    @commands.command(description="Toggle a commands on/off", hidden=True)
    @commands.has_permissions(administrator=True)
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)
        if command == None:
            await ctx.send("That command does not exist!")
        elif ctx.command == command:
            await ctx.send("you can't toggle that command")
        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"Command `{command.name}` has been {ternary}")

    @toggle.error
    async def toggle_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Administrator` permission to use this command!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.DisabledCommand):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.display_name}**, That command is disabled!",
                color=0xFF0000,
            )
            # sends the error message to the channel
            return await ctx.send(embed=embed)

    @dadjoke.error  # command name error
    async def dadjoke_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
                color=0xFF0000,
            )
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> You must have the `Kick Members` permission to use this command!",
                color=0xFF0000,
            )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(moderations(client))
