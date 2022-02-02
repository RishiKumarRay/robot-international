import nextcord
from nextcord.ext import commands


class verification(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        wholesome = "<:Wholesome:825035249532403802>"
        warung_international = "<:WarungInternational:924928034388189234>"
        guild_id = payload.guild_id
        guild = self.client.get_guild(guild_id)

        # wholesomeland
        if (
            str(payload.emoji) == wholesome
            and payload.message_id == 912510518357528576
            and payload.guild_id == 806949608349106197
        ):
            dev = nextcord.utils.get(guild.roles, id=825637144731058207)
            member = payload.member
            await member.add_roles(dev)

        # warung international
        if (
            str(payload.emoji) == warung_international
            and payload.message_id == 922531092098072666
            and payload.guild_id == 922523614828433419
        ):
            dev = nextcord.utils.get(guild.roles, id=922878963817263154)
            member = payload.member
            await member.add_roles(dev)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        wholesome = "<:Wholesome:825035249532403802>"
        warung_international = "<:WarungInternational:924928034388189234>"
        guild_id = payload.guild_id
        guild = self.client.get_guild(guild_id)

        # wholesomeland
        if (
            str(payload.emoji) == wholesome
            and payload.message_id == 912510518357528576
            and payload.guild_id == 806949608349106197
        ):
            dev = guild.get_role(825637144731058207)
            member = guild.get_member(payload.user_id)
            await member.remove_roles(dev)

        # warung international
        if (
            str(payload.emoji) == warung_international
            and payload.message_id == 922531092098072666
            and payload.guild_id == 922523614828433419
        ):
            dev = nextcord.utils.get(guild.roles, id=922878963817263154)
            member = guild.get_member(payload.user_id)
            await member.remove_roles(dev)


def setup(client):
    client.add_cog(verification(client))
