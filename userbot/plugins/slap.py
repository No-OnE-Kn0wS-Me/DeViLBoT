"""
SLAP Plugin For Userbot
usage:- .slap in reply to any message, or u gonna slap urself.

"""

import sys
from telethon import events, functions
from uniborg.util import admin_cmd
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import ALIVE_NAME

SLAP_TEMPLATES = (
    "{user1} {user2} നെ ചുറ്റിക കൊണ്ട് തലക്കടിച്ചു.",
    "{user1} തടിക്കഷണം കൊണ്ട് {user2} വിന്റെ മുഖത്തു അടിച്ചു. ",
    "{user1} {user2} നെ കാലിൽ പിടിച്ചു കറക്കി എറിഞ്ഞു ",
    "{user1} വലിയ ഒരു കല്ല് എടുത്ത് {user2} വിന്റെ തലയിലേക്ക് ഇട്ടു",
    "{user1} ഒരു വലിയ പാത്രം എടുത്ത് {user2} വിന്റെ മുഖത്ത് ആഞ്ഞടിച്ചു.",
    "{user1} {user2} വിന്റെ തലക്ക് ഇരുമ്പ് പൈപ്പ് വെച്ചടിച്ചു.",
    "{user1} ഭിത്തിയിൽ തൂക്കിയിട്ടിരുന്ന ക്ലോക്ക് എടുത്ത് {user2} വിന്റെ പ്രധാന ഭാഗത്ത് അടിച്ചു .",
    "{user1} {user2} വിനെ കുനിച്ചു നിർത്തി വലിയൊരു തടിക്കഷണം മുതുകത്തിട്ടു",
    "{user1} ഒരു ഇരുമ്പിന്റെ കസേര എടുത്ത് {user2} ന്റെ തലക്ക് അടിച്ചു..",
    "{user1} {user2} നെ മരത്തിൽ കെട്ടിയിട്ട് കാലിൽ തീ കൊടുത്തു..."
    
)

ITEMS = (
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
)

THROW = (
    "എറിഞ്ഞു",
    "വിക്ഷേപിച്ചു",
    "തട്ടി",
    "വീശിയെറിഞ്ഞു",
)

HIT = (
    "അടിച്ചു",
    "ശക്തിയായി പ്രഹരിച്ചു",
    "തല്ലി",
    "ഇടിച്ചു",
    "തൊഴിച്ചു",
)

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "GujjuBot"

@borg.on(admin_cmd(pattern="slap ?(.*)", allow_sudo=True))
async def who(event):
    if event.fwd_from:
        return
    replied_user = await get_user(event)
    caption = await slap(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.edit(caption)

    except:
        await event.edit("`Can't slap this nibba !!`")

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap strangers !!`")
            return None

    return replied_user

async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    caption = temp.format(user1=DEFAULTUSER, user2=slapped, item=item, hits=hit, throws=throw)

    return caption
