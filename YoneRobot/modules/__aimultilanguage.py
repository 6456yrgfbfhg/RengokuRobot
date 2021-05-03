#    Copyright (C) 2020-2021 by @AmarnathCdj & @InukaAsith
#    Chatbot system written by @AmarnathCdj databse added and recoded for pyrogram by @InukaAsith
#    This programme is a part of yone (TG bot) project
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Kang with the credits
#    Special credits to @AmarnathCdj
import re

import emoji
import requests

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
from google_trans_new import google_translator
from pyrogram import filters

from YoneRobot import BOT_ID
from YoneRobot.helper_extra.aichat import add_chat, get_session, remove_chat
from YoneRobot.pyrogramee.pluginshelper import admins_only, edit_or_reply
from YoneRobot import pbot as yone

translator = google_translator()


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


yone_chats = []
en_chats = []
# AI Chat (C) 2020-2021 by @InukaAsith


@yone.on_message(filters.command("chatbot") & ~filters.edited & ~filters.bot)
@admins_only
async def hmm(_, message):
    global yone_chats
    if len(message.command) != 2:
        await message.reply_text(
            "I only recognize `/chatbot on` and /chatbot `off only`"
        )
        message.continue_propagation()
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("rengoku AI Already Activated In This Chat")
            return
        await lel.edit(
            f"rengoku AI Successfully Added For Users In The Chat {message.chat.id}"
        )

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("yone AI Was Not Activated In This Chat")
            return
        await lel.edit(
            f"rengoku AI Successfully Deactivated For Users In The Chat {message.chat.id}"
        )

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text("English AI chat Enabled!")
            return
        await message.reply_text("AI Chat Is Already Disabled.")
        message.continue_propagation()
    else:
        await message.reply_text(
            "I only recognize `/chatbot on` and /chatbot `off only`"
        )


@yone.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        message.continue_propagation()
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("yone", "Aco")
        test = test.replace("yone", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "yone")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        pro = result
        try:
            await yone.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
            lan = translator.detect(rm)
        test = rm
        if not "en" in lan and not lan == "":
            test = translator.translate(test, lang_tgt="en")

        # test = emoji.demojize(test.strip())

        # Kang with the credits bitches @InukaASiTH
        test = test.replace("yone", "Aco")
        test = test.replace("yone", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "yone")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        pro = result
        if not "en" in lan and not lan == "":
            pro = translator.translate(pro, lang_tgt=lan[0])
        try:
            await yone.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError as e:
            print(e)


@yone.on_message(filters.text & filters.private & filters.reply & ~filters.bot)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
        lan = translator.detect(rm)
    test = rm
    if not "en" in lan and not lan == "":
        test = translator.translate(test, lang_tgt="en")

    # test = emoji.demojize(test.strip())

    # Kang with the credits bitches @InukaASiTH
    test = test.replace("yone", "Aco")
    test = test.replace("yone", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {test},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "yone")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, lang_tgt=lan[0])
    try:
        await yone.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError as e:
        print(e)


@yone.on_message(
    filters.regex("rengoku|Rengoku")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
        lan = translator.detect(rm)
    test = rm
    if not "en" in lan and not lan == "":
        test = translator.translate(test, lang_tgt="en")

    # test = emoji.demojize(test.strip())

    # Kang with the credits bitches @InukaASiTH
    test = test.replace("yone", "Aco")
    test = test.replace("yone", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {test},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "yone")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, lang_tgt=lan[0])
    try:
        await yone.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError as e:
        print(e)sage.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.change_info
    )


@register(pattern="^/yeschat$")
async def _(event):
    if event.is_group:
        if not event.sender_id == OWNER_ID:
           if not await can_change_info(message=event):
              return
    else:
        return
    chat = event.chat
    is_chat = sql.is_chat(chat.id)
    k = ly.is_chat(chat.id)
    if k:
        ly.rem_chat(chat.id)
    if not is_chat:
        ses_id = 'null'
        expires = 'null'
        sql.set_ses(chat.id, ses_id, expires)
        await event.reply("AI successfully enabled for this chat!")
        return
    await event.reply("AI Bot is already enabled for this chat!")
    return ""


@register(pattern="^/nochat$")
async def _(event):
    if event.is_group:
        if not event.sender_id == OWNER_ID:
          return
    else:
        return
    chat = event.chat
    is_chat = sql.is_chat(chat.id)
    if not is_chat:
        await event.reply("AI isn't enabled here in the first place!")
        return
    sql.rem_chat(chat.id)
    await event.reply("AI Bot disabled successfully!")


@tbot.on(events.NewMessage(pattern=None))
async def _(event):
  if event.is_group:
        pass
  else:
        return
  prof = str(event.text)
  
  if not "Yone" in prof:
    if not "yone" in prof:
      reply_msg = await event.get_reply_message()
      if reply_msg.sender_id == BOT_ID:
           return
      else:
          return
  chat = event.chat
  msg = prof
  is_chat = sql.is_chat(chat.id)
  if not is_chat:
        return
  if msg.startswith("/") or msg.startswith("@"):
    return
  lan = translator.detect(msg)
  if not "en" in lan and not lan == "":
     test = translator.translate(msg, lang_tgt="en")
  else:
     test = msg
  
  url = "https://iamai.p.rapidapi.com/ask"
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
    'content-type': "application/json",
    'x-forwarded-for': "<user's ip>",
    'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
    'x-rapidapi-host': "iamai.p.rapidapi.com"
    }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  if "Thergiakis" in result:
   pro = random.choice(string)
   try:
      async with tbot.action(event.chat_id, 'typing'):
           await event.reply(pro)
   except CFError as e:
           print(e)
  elif "Ann" in result:
   pro = "Yeah, My name is Rengoku"
   try:
      async with tbot.action(event.chat_id, 'typing'):
           await event.reply(pro)
   except CFError as e:
           print(e)
  else:
    if not "en" in lan and not lan == "":
      finale = translator.translate(result, lang_tgt=lan[0])
    else:
      finale = result
    try:
      async with tbot.action(event.chat_id, 'typing'):
           await event.reply(finale)
    except CFError as e:
           await event.reply(lodu)
