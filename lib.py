# Import necessary packages
import logging
import datetime
import os
import urllib.request
from os import getenv
from shutil import move

import discord
from discord.ext import commands, tasks

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

now = datetime.datetime.now()
urls_and_files = {
    "test": ["http://127.0.0.1/Patch/PatchInfoServer.cfg", "PatchInfoServer.cfg", "Test"],
    "sea": ["http://patchsea.dragonnest.com/Game/DragonNest/Patch/PatchInfoServer.cfg", "PatchInfoServer_SEA.cfg", "SEA"],
    "us": ["http://patchus.dragonnest.com/Game/DragonNest/patch/PatchInfoServer.cfg", "PatchInfoServer_US.cfg", "US"],
    "kr": ["http://res.dn.pupugame.com/Patch/PatchInfoServer.cfg", "PatchInfoServer_KR.cfg", "Korea"],
    "jp": ["http://patchjp.dragonnest.com/Game/Patch/PatchInfoServer.cfg", "PatchInfoServer_JP.cfg", "Japan"]
}
