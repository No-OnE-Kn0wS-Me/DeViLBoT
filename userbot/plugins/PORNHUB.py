"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "shitybrain":

        await event.edit(input_str)

        animation_chars = [

            "S_",

            "Sh_",

            "Shi_",

            "Shit_",
            
            "Shity_",
            
            "Shityb_",
            
            "Shitybr_", 
           
            "Shitybra_",
           
            "Shitybrai_",
            
            "Shitybrain",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "userbot":

        await event.edit(input_str)

        animation_chars = [

            "U_",

            "Us_",

            "Use_",

            "User_",
            
            "Userb_",
            
            "Userbo_",
            
            "Userbot❤",
           

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])



"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "telegram":

        await event.edit(input_str)

        animation_chars = [

            "T_",

            "TE_",

            "TEL_",

            "TELE_",
            
            "TELEG_",
            
            "TELEGR",
            
            "TELEGRA_",
            
            "TELEGRAM",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
