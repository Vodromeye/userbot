# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import asyncio
import os
import time

from pyUltroid import *
from pyUltroid.functions.admins import *
from pyUltroid.functions.helper import *
from pyUltroid.functions.info import *
from pyUltroid.functions.misc import *
from pyUltroid.functions.tools import *
from pyUltroid.functions.ytdl import *
from pyUltroid.misc._assistant import callback, in_pattern, owner
from pyUltroid.misc._decorators import ultroid_cmd
from pyUltroid.misc._wrappers import eod, eor
from pyUltroid.version import __version__, ultroid_version
from telethon import Button, events
from telethon.tl import functions, types

from strings import get_string

start_time = time.time()
Redis = udB.get
OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id
LOG_CHANNEL = int(udB.get("LOG_CHANNEL"))

List = []
Dict = {}
N = 0

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001327032795,  # UltroidSupport
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]
