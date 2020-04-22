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

SLAP_TEMPLATES = [
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} in the face with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} launches a {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} gave a friendly push to help {user2} learn to swim in lava."
]

ITEMS = [
    "ഇസ്തിരി പ്പെട്ടി",
    "കടുക്",
    "ചട്ടുകം",
    "ചീഞ്ഞ മുട്ട",
    "ചീഞ്ഞ തക്കാളി",
    "ഉണ്ണിയപ്പം",
    "കുടുക്ക",
    "ചട്ടി",
    "ഇഷ്ടിക",
    "പഴംപൊരി",
    "പൊറോട്ട",
    "ചുറ്റിക",
    "ബോംബ്",
    "കല്ല്",
    "പഴയ ടിവി",
    "ബുക്ക്‌",
    "കേടായ ലാപ്ടോപ്",
    "ചത്ത എലി",
    "കരി മൂർഖൻ",
    "കോയി🐥",
    "കാക്ക",
    "ഉറുമ്പ്",
    "ചാണകം",
    "ചെളി",
    "മണ്ണ്",
    "beehive",
    "piece of rotten meat",
    "മീൻ",
    "കുറെ കല്ലുകൾ",
]

THROW = [
    "എറിഞ്ഞു",
    "വലിച്ചെറിഞ്ഞു",
    "തള്ളിയിട്ടു",
    "ഉന്തി",
]

HIT = [
    "അടിച്ചു",
    "പൊട്ടിച്ചു",
    "കൊടുത്തു",
    "ഇടിച്ചു",
    "ചവിട്ടി",
]

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
