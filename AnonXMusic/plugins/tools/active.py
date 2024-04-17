from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["vc", "activevoice"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("Getting Active Voice Chats List...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"No Active Voice Chats On {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» List Of Currently Active Voice Chats :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["vcv", "activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» Getting Active Video Chats List...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"No Active Video Chats On {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>List Of Currently Active Video Chats :</b>\n\n{text}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.command("aktif", [".", "^", "-", "!", "/"]) & SUDOERS)
async def activecilik(_, message: Message):
    ms = len(await get_active_chats())
    vd = len(await get_active_video_chats())
    await app.send_message(message.chat.id, 
    f"💽 Active Chats:\n\n๏» Music: {ms}\n๏» Video:{vd}")