import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

client = Github(os.getenv("GITHUB_TOKEN"))
gist = client.get_gist(os.getenv("GIST_ID"))
first_file = list(gist.files.values())[0]
results = first_file.raw_data["content"]

gist2 = client.get_gist(os.getenv("GIST_ID2"))
sec_file = list(gist2.files.values())[0]
results2 = sec_file.raw_data["content"]


class readme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.client.get_guild(806949608349106197)
        channel = self.client.get_channel(828959702029041664)
        msg_id = 895500785734025276  # the message's id
        msg = await channel.fetch_message(msg_id)
        embed = nextcord.Embed(
            title=f"👋 Hi there, Welcome to {guild.name} Official Discord Server.",
            description=f"{results}",
            color=0x3874FF,
        )
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/818815530647158784/888743161327943690/786714695334756402.gif"
        )
        await msg.edit(embed=embed)

        channelb = self.client.get_channel(806958144404062229)
        msg_id_b = 912510518357528576  # the message's id
        msg_b = await channelb.fetch_message(msg_id_b)
        embed = nextcord.Embed(
            title="Role Info:", description=f"{results2}", color=0x3874FF
        )
        embed.set_thumbnail(url="https://probot.media/8LBlJpkekY.png")
        embed.set_footer(
            text=f"Choose a Option to get a role!",
            icon_url="https://probot.media/luV8g6k4WT.gif",
        )
        await msg_b.edit(embed=embed)


def setup(client):
    client.add_cog(readme(client))
