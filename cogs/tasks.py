from lib import *
from bot import *
import discord
from discord.ext import tasks


class CheckVer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Check_Loop.start()

    @tasks.loop(seconds=10.0)
    async def Check_Loop(self):
        global newVer
        message_channel = self.client.get_channel(channel_id)

        for i in urls_and_files.values():
            url, file_name, server = i[0], i[1], i[2]
            cfg = urllib.request.urlopen(url)
            for x in cfg:
                newVer = x.decode("utf-8").split()
                newVer = " ".join(newVer)

            with open(f"latest/{file_name}", "r") as f:
                latestVer = f.readline()
                f.close()
                latestVer = "".join(newVer)
                latestVer = latestVer.replace("\n", "")

            if newVer != latestVer:
                urllib.request.urlretrieve(url, file_name)
                print("There is an update")
                embed = discord.Embed(title="Update Notice",
                                      description=f"Mogu mogu! {server} patched from {latestVer[7:]} to {newVer[7:]} ",
                                      colour=discord.Colour(0xe5d1ed))

                embed.set_footer(
                    text="{}-{}-{}".format(now.year, now.month, now.day))
                await message_channel.send(embed=embed)
                move(f"{file_name}", f"latest/{file_name}")

            cfg.close()

        # # Get version from URL
        # for i in urls:
        #     file = urllib.request.urlopen(urls[i])
        #     for x in file:
        #         newVer = x.decode("utf-8")
        #
        # f = open("latest/PatchInfoServer.cfg", "r")
        # latestVer = f.read()
        #
        # if newVer != latestVer:
        #     database.query(newVer)
        #     urllib.request.urlretrieve(url['test'], filename['test'])
        #     print("There is an update")
        #     embed = discord.Embed(title="Update Notice",
        #                           description=f"Mogu mogu! Patched from {latestVer[7:]} to {newVer[7:]} ",
        #                           colour=discord.Colour(0xe5d1ed))
        #
        #     embed.set_footer(
        #         text="{}-{}-{}".format(now.year, now.month, now.day))
        #     await message_channel.send(embed=embed)
        #     f.close()
        #     move('PatchInfoServer.cfg', 'latest/PatchInfoServer.cfg')
        #
        # file.close()

    @Check_Loop.before_loop
    async def before(self):
        await self.client.wait_until_ready()


def setup(client):
    client.add_cog(CheckVer(client))
