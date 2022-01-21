import os

import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands
from pymongo import MongoClient

bot_channel = 906410156265467975


class custom(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        description="Shortcut to rules, for those who might need a refresher",
        hidden=True,
    )
    async def rules(self, ctx, *, member: nextcord.Member = None):
        if ctx.guild.id == 806949608349106197:

            if member is None:
                member = ctx.author

            await ctx.message.delete()
            await ctx.send(
                f"Hey {member.mention}, {ctx.message.author.display_name} thinks you should take another look at our <#828959702029041664>"
            )
        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    # put this on, if the server is not currently lockdowned.

    @commands.command(description="Get this server invite link")
    async def invite(self, ctx):
        if ctx.guild.id == 806949608349106197:
            await ctx.send(os.getenv("MAIN_INVITE"))
        elif ctx.guild.id == 922523614828433419:
            await ctx.send(os.getenv("WI_MAIN_INVITE"))
        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(description="Get our Sticker Server Invite link", hidden=True)
    async def stickerinvite(self, ctx):
        if ctx.guild.id == 806949608349106197:
            await ctx.send(os.getenv("STICKER_INVITE"))
        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @commands.command(
        description="*This command is like the wheel in GTA. You can use it every 24 hours. \nSimply type the command and the bot will give you something.",
        hidden=True,
    )
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def wheelspin(self, ctx):
        if ctx.guild.id == 806949608349106197:
            load_dotenv()

            cluster = MongoClient(os.getenv("MONGODB_URL"))

            wheelspin = cluster["discord"]["wheelspin"]

            stats = wheelspin.aggregate([{"$sample": {"size": 1}}])
            if ctx.channel.id == bot_channel:
                for x in stats:
                    pesan = x["message"]
                    await ctx.send(
                        f"{ctx.author.mention} spinned the Lucky Wheel and {pesan}"
                    )
                    # simpenan aja
                    # f"{ctx.author.mention} spinned the Lucky Wheel and hit the Fucking Jackpot and got 25,000XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
                    # f"{ctx.author.mention} spinned the Lucky Wheel and hit the Fucking Fuck Jackpot and got 35,000XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
                    # f"{ctx.author.mention} spinned the Lucky Wheel and hit the Fucking Fucker Fuck Jackpot and got 50,000XP <:FennPOG:839189820668248135> \n XP will be awarded within 3h. \n You can spin the wheel again in 3h.",
            else:
                return await ctx.send(
                    f"<:cross:839158779815657512> **{ctx.author.mention}**, that command is disabled in this channel."
                )
        else:
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands is not available in this server.",
                color=0xFF0000,
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

    @wheelspin.error  # command name error
    async def wheelspin_error(self, ctx, error):  # define error
        # tells the bot its a cool down error
        if isinstance(error, commands.CommandOnCooldown):
            # msg is the message you would like to send, the format is how it
            # formats the seconds left.
            cd = round(error.retry_after)
            if cd == 0:
                cd = 1
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> **{ctx.author.name}**, you need to wait {self.better_time(cd)} to use that command again."
            )
        # sends the error message to the channel
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(custom(client))
