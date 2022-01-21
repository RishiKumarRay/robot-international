import nextcord
from nextcord.ext import commands


class verification(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Verify yourself in this server", hidden=True)
    @commands.dm_only()
    async def verify(self, ctx):
        server = self.client.get_guild(922523614828433419)
        role = nextcord.utils.get(server.roles, id=922878963817263154)
        member = server.get_member(ctx.author.id)
        if role not in member.roles:
            await member.add_roles(role)
            embed = nextcord.Embed(
                description="<:check:839158727512293406> Anda telah terverifikasi, Enjoy your stay! ✌",
                color=0x00FF00,
            )
            await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(
                description="<:cross:839158779815657512> Anda tidak perlu mengulangi proses verifikasi!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

    @verify.error
    async def verify_error(self, ctx, error):
        if isinstance(error, commands.PrivateMessageOnly):
            embed = nextcord.Embed(
                description=f"<:cross:839158779815657512> This commands limited to DM's only!",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(verification(client))
