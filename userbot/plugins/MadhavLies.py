"""
Pulls Up A Random Lie of Madhav Seth's Realmeme Series...
Syntax: .madhav
    orginal author : @TechyNewbie"""
from telethon import events
import asyncio
import os
import sys
import random



@borg.on(events.NewMessage(pattern=r"\.madhav", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    x=(random.randrange(1,11)) 
    if (x==1):
      await event.edit("**“We Will Release A Flash Tool in Q2 2019” - Madhav Seth**")
    if (x==2):
      await event.edit("**“No ADs in UI” - Madhav Seth**")
    if (x==3):
      await event.edit("**“If realme makes its Own OS, then all our devices will be running on it” - Madhav Seth**")
    if (x==4):
      await event.edit("**“We will try to add as many Clone Apps as possible” - Madhav Seth**")
    if (x==5):
      await event.edit("**“We are the most Customer Centered brand” - Madhav Seth**")
    if (x==6):
      await event.edit("**“We sell phones, not ADs” - Madhav Seth**")
    if (x==7):
      await event.edit("**“We will never place ADs in OS” - Madhav Seth**")
    if (x==8):
      await event.edit("**“realme is the only brand which provides regular updates” - Madhav Seth**")
    if (x==9):
      await event.edit("**“We will add Internal Audio Recording in all devices by November (2019)” - Madhav Seth**")
    if (x==10):
      await event.edit("**“We work on feedback taken from users” - Madhav Seth**")
    if (x==11):
      await event.edit("**“Redmi's 48MP Camera (RN7pro) is just a number game” - Madhav Seth\n\n“We are launching the world's first 64MP Camera Phone”**")





