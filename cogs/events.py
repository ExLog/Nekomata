import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game("mogu mogu!"))
        print("{} has logged in.".format(self.client.user))


def setup(client):
    client.add_cog(Events(client))
