import asyncio
import base64
import ctypes
import datetime
import hashlib
import json
import math
import os
import random
import re
import string
import subprocess
import sys
import time
from io import BytesIO
from os import path
from random import randint
from urllib.request import urlopen

import aiohttp
import colorama
import cursor
import dateparser
import discord
import proxyscrape
import qrcode
import requests
import requests.auth
import upsidedown
import urllib3
import xurls
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont,
                 ImageOps)
from StringCalculator import SolveMathProblem
from art import *
from blockcypher import get_address_overview
from bs4 import BeautifulSoup
from colorama import Fore, Style
from discord import AsyncWebhookAdapter, Webhook
from discord.ext import commands, tasks
from discord.ext.commands import Cog, EmojiConverter, UserConverter, command
from fake_useragent import UserAgent
from google_trans_new import google_translator
from owoify.owoify import owoify
from pytube import YouTube
from readify import readify
from riotwatcher import LolWatcher
from win10toast import ToastNotifier
from zalgo_text import zalgo


def GetUUID():
    cmd = "wmic csproduct get uuid"
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n") + 2
    uuid = uuid[pos1:-15]
    return uuid


cursor.hide()
os.system("mode con: cols=80 lines=20")

start_time = time.time()
colorama.init()
cursor.hide()
ctypes.windll.kernel32.SetConsoleTitleW(f"Starting up...")
progress = 0

notifier = ToastNotifier()
http = urllib3.PoolManager()
notifier = ToastNotifier()
extractor = xurls.Strict()
extractor1 = xurls.Relaxed()
ua = UserAgent()

codeRegex = re.compile(
    "(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)"
)
text_to_regional = {
    "a": ":regional_indicator_a:",
    "b": ":regional_indicator_b:",
    "c": ":regional_indicator_c:",
    "d": ":regional_indicator_d:",
    "e": ":regional_indicator_e:",
    "f": ":regional_indicator_f:",
    "g": ":regional_indicator_g:",
    "h": ":regional_indicator_h:",
    "i": ":regional_indicator_i:",
    "j": ":regional_indicator_j:",
    "k": ":regional_indicator_k:",
    "l": ":regional_indicator_l:",
    "m": ":regional_indicator_m:",
    "n": ":regional_indicator_n:",
    "o": ":regional_indicator_o:",
    "p": ":regional_indicator_p:",
    "q": ":regional_indicator_q:",
    "r": ":regional_indicator_r:",
    "s": ":regional_indicator_s:",
    "t": ":regional_indicator_t:",
    "u": ":regional_indicator_u:",
    "v": ":regional_indicator_v:",
    "w": ":regional_indicator_w:",
    "x": ":regional_indicator_x:",
    "y": ":regional_indicator_y:",
    "z": ":regional_indicator_z:",
    "1": ":one:",
    "2": ":two:",
    "3": ":three:",
    "4": ":four:",
    "5": ":five:",
    "6": ":six:",
    "7": ":seven:",
    "8": ":eight:",
    "9": ":nine:",
    "0": ":zero:",
    "!": ":exclamation:",
    "?": ":question:",
}
ipgeolocationioapikey = "bc036c32b784424ba03d6b74d28492de"
rgapi = "RGAPI-0bb36dba-aad6-4d3e-b59b-b15b5ab33eb1"
lol_watcher = LolWatcher(rgapi)
footer_url = "https://cdn.discordapp.com/emojis/882727520183660574.png?v=1"
desyncer_version = "2.3"
documents = os.path.expanduser(r"~\Documents").replace(os.sep, "/") + "/Desyncer"
alias_file = f"{documents}/files/aliases.json"

second_message = []
first_message = []
imitating = []
muted = []
rainbow = {}
last_message = []
typing = []
owoToggle = False

tags_dict = {}
langs = {
    "ab": "Abkhaz",
    "aa": "Afar",
    "af": "Afrikaans",
    "ak": "Akan",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "an": "Aragonese",
    "hy": "Armenian",
    "as": "Assamese",
    "av": "Avaric",
    "ae": "Avestan",
    "ay": "Aymara",
    "az": "Azerbaijani",
    "bm": "Bambara",
    "ba": "Bashkir",
    "eu": "Basque",
    "be": "Belarusian",
    "bn": "Bengali",
    "bh": "Bihari",
    "bi": "Bislama",
    "bs": "Bosnian",
    "br": "Breton",
    "bg": "Bulgarian",
    "my": "Burmese",
    "ch": "Chamorro",
    "ce": "Chechen",
    "zh": "Chinese",
    "cv": "Chuvash",
    "kw": "Cornish",
    "co": "Corsican",
    "cr": "Cree",
    "hr": "Croatian",
    "cs": "Czech",
    "da": "Danish",
    "dv": "Maldivian",
    "nl": "Dutch",
    "dz": "Dzongkha",
    "en": "English",
    "eo": "Esperanto",
    "et": "Estonian",
    "ee": "Ewe",
    "fo": "Faroese",
    "fj": "Fijian",
    "fi": "Finnish",
    "fr": "French",
    "ff": "Fula",
    "gl": "Galician",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek",
    "gn": "Guaraní",
    "gu": "Gujarati",
    "ht": "Haitian",
    "ha": "Hausa",
    "he": "Hebrew",
    "hz": "Herero",
    "hi": "Hindi",
    "ho": "HiriMotu",
    "hu": "Hungarian",
    "ia": "Interlingua",
    "id": "Indonesian",
    "ie": "Interlingue",
    "ga": "Irish",
    "ig": "Igbo",
    "ik": "Inupiaq",
    "io": "Ido",
    "is": "Icelandic",
    "it": "Italian",
    "iu": "Inuktitut",
    "ja": "Japanese",
    "jv": "Javanese",
    "kl": "Kalaallisut",
    "kn": "Kannada",
    "kr": "Kanuri",
    "ks": "Kashmiri",
    "kk": "Kazakh",
    "km": "Khmer",
    "rw": "Kinyarwanda",
    "kv": "Komi",
    "kg": "Kongo",
    "ko": "Korean",
    "ku": "Kurdish",
    "la": "Latin",
    "lb": "Luxembourgish",
    "lg": "Luganda",
    "li": "Limburgish",
    "ln": "Lingala",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lu": "Luba-Katanga",
    "lv": "Latvian",
    "gv": "Manx",
    "mk": "Macedonian",
    "mg": "Malagasy",
    "ms": "Malay",
    "ml": "Malayalam",
    "mt": "Maltese",
    "mi": "Māori",
    "mh": "Marshallese",
    "mn": "Mongolian",
    "na": "Nauru",
    "nb": "Norwegian",
    "nd": "North Ndebele",
    "ne": "Nepali",
    "ng": "Ndonga",
    "no": "Norwegian",
    "ii": "Nuosu",
    "nr": "South Ndebele",
    "oc": "Occitan",
    "om": "Oromo",
    "or": "Oriya",
    "os": "Ossetian",
    "pa": "Panjabi",
    "pi": "Pāli",
    "fa": "Persian",
    "pl": "Polish",
    "ps": "Pashto",
    "pt": "Portuguese",
    "qu": "Quechua",
    "rm": "Romansh",
    "rn": "Kirundi",
    "ro": "Romanian",
    "ru": "Russian",
    "sc": "Sardinian",
    "sd": "Sindhi",
    "sm": "Samoan",
    "sg": "Sango",
    "sr": "Serbian",
    "gd": "Scottish",
    "sn": "Shona",
    "si": "Sinhala",
    "sk": "Slovak",
    "sl": "Slovene",
    "so": "Somali",
    "st": "Sotho",
    "es": "Spanish",
    "su": "Sundanese",
    "sw": "Swahili",
    "ss": "Swati",
    "sv": "Swedish",
    "ta": "Tamil",
    "te": "Telugu",
    "tg": "Tajik",
    "th": "Thai",
    "ti": "Tigrinya",
    "bo": "Tibetan",
    "tk": "Turkmen",
    "tl": "Tagalog",
    "tn": "Tswana",
    "to": "Tonga",
    "tr": "Turkish",
    "ts": "Tsonga",
    "tt": "Tatar",
    "tw": "Twi",
    "ty": "Tahitian",
    "ug": "Uighur",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "ve": "Venda",
    "vi": "Vietnamese",
    "vo": "Volapük",
    "wa": "Walloon",
    "cy": "Welsh",
    "wo": "Wolof",
    "fy": "Frisian",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "za": "Zhuang",
    "zu": "Zulu",
}
langs1 = {value: key for key, value in langs.items()}

languages = {
    "da": "Danish, Denmark",
    "de": "German, Germany",
    "en-GB": "English, United Kingdom",
    "en-US": "English, United States",
    "es-ES": "Spanish, Spain",
    "fr": "French, France",
    "hr": "Croatian, Croatia",
    "lt": "Lithuanian, Lithuania",
    "hu": "Hungarian, Hungary",
    "nl": "Dutch, Netherlands",
    "no": "Norwegian, Norway",
    "pl": "Polish, Poland",
    "pt-BR": "Portuguese, Brazilian, Brazil",
    "ro": "Romanian, Romania",
    "fi": "Finnish, Finland",
    "sv-SE": "Swedish, Sweden",
    "vi": "Vietnamese, Vietnam",
    "tr": "Turkish, Turkey",
    "cs": "Czech, Czechia, Czech Republic",
    "el": "Greek, Greece",
    "bg": "Bulgarian, Bulgaria",
    "ru": "Russian, Russia",
    "uk": "Ukranian, Ukraine",
    "th": "Thai, Thailand",
    "zh-CN": "Chinese, China",
    "ja": "Japanese",
    "zh-TW": "Chinese, Taiwan",
    "ko": "Korean, Korea",
}

cc_digits = {"american express": "3", "visa": "4", "mastercard": "5"}

emoji_dict = {
    "a": ["🇦", "🅰", "🍙", "🔼", "4⃣"],
    "b": ["🇧", "🅱", "8⃣"],
    "c": ["🇨", "©", "🗜"],
    "d": ["🇩", "↩"],
    "e": ["🇪", "3⃣", "📧", "💶"],
    "f": ["🇫", "🎏"],
    "g": ["🇬", "🗜", "6⃣", "9⃣", "⛽"],
    "h": ["🇭", "♓"],
    "i": ["🇮", "ℹ", "🚹", "1⃣"],
    "j": ["🇯", "🗾"],
    "k": ["🇰", "🎋"],
    "l": ["🇱", "1⃣", "🇮", "👢", "💷"],
    "m": ["🇲", "Ⓜ", "📉"],
    "n": ["🇳", "♑", "🎵"],
    "o": ["🇴", "🅾", "0⃣", "⭕", "🔘", "⏺", "⚪", "⚫", "🔵", "🔴", "💫"],
    "p": ["🇵", "🅿"],
    "q": ["🇶", "♌"],
    "r": ["🇷", "®"],
    "s": ["🇸", "💲", "5⃣", "⚡", "💰", "💵"],
    "t": ["🇹", "✝", "➕", "🎚", "🌴", "7⃣"],
    "u": ["🇺", "⛎", "🐉"],
    "v": ["🇻", "♈", "☑"],
    "w": ["🇼", "〰", "📈"],
    "x": ["🇽", "❎", "✖", "❌", "⚒"],
    "y": ["🇾", "✌", "💴"],
    "z": ["🇿", "2⃣"],
    "0": ["0⃣", "🅾", "0⃣", "⭕", "🔘", "⏺", "⚪", "⚫", "🔵", "🔴", "💫"],
    "1": ["1⃣", "🇮"],
    "2": ["2⃣", "🇿"],
    "3": ["3⃣"],
    "4": ["4⃣"],
    "5": ["5⃣", "🇸", "💲", "⚡"],
    "6": ["6⃣"],
    "7": ["7⃣"],
    "8": ["8⃣", "🎱", "🇧", "🅱"],
    "9": ["9⃣"],
    "?": ["❓"],
    "!": ["❗", "❕", "⚠", "❣"],
}

responses = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most Likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes",
    "Yes - Definitely",
    "You may rely on it.",
]

    
os.system("mode con: cols=80 lines=20")


def printer(msg):
    print(Fore.RED + msg + Fore.RESET)


def unixtodate(unix):
    if isinstance(unix, int):
        pass
    else:
        unix = int(unix)
    return datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d - %I:%M %p")


def welcome_message():
    os.system("mode con: cols=80 lines=20")
    ctypes.windll.kernel32.SetConsoleTitleW(
        f"Desyncer v{desyncer_version} | User: {username} | Logged in as {client.user.name}#{client.user.discriminator} "
    )
    os.system("cls")
    print(f"{Fore.BLUE}{Style.BRIGHT}")
    print(
        """
               ___                               
              / _ \___ ___ __ _____  _______ ____
             / // / -_|_-</ // / _ \/ __/ -_) __/
            /____/\__/___/\_, /_//_/\__/\__/_/   
                         /___/ 

    """
    )
    print(
        """────────────────────────────────────────────────────────────────────────────────\n\n"""
    )
    print(
        f'{Fore.BLUE}            Username: {Fore.CYAN}{client.user.name}        {Fore.BLUE}Servers: {Fore.CYAN}{len(client.guilds)}\n{Fore.BLUE}            Discriminator: {Fore.CYAN}#{client.user.discriminator}        {Fore.BLUE}Friends: {Fore.CYAN}{len(client.user.friends)}\n{Fore.BLUE}            ID: {Fore.CYAN}{client.user.id}      {Fore.BLUE}Blocked: {Fore.CYAN}{len(client.user.blocked)}\n\n')

    notifier.show_toast(
        "Welcome to Desyncer",
        f"Welcome {username},\nVersion: {desyncer_version}\nStatus: Connected",
        duration=15,
        icon_path=f"{documents}/assets/images/desyncer.ico",
    )


def replace_letters(react_me):
    for char in "abcdefghijklmnopqrstuvwxyz0123456789!?":
        char_count = react_me.count(char)
        if char_count > 1:
            if len(emoji_dict[char]) >= char_count:
                i = 0
                while i < char_count:
                    if emoji_dict[char][i] not in react_me:
                        react_me = react_me.replace(char, emoji_dict[char][i], 1)
                    else:
                        char_count += 1
                    i += 1
        else:
            if char_count == 1:
                react_me = react_me.replace(char, emoji_dict[char][0])
    return react_me


async def arg_parser(ctx, argument, returnurl=False):
    try:
        urls = extractor.findall(argument)
        if urls:
            asset = urls[0]
            response = requests.get(urls[0])
            data = BytesIO(response.content)
            img = Image.open(data)
            if returnurl:
                return asset
            else:
                return img
        if ctx.message.attachments:
            asset = ctx.message.attachments[0]
            data = BytesIO(await asset.read())
            img = Image.open(data)
            if returnurl:
                return str(asset.url)
            else:
                return img
        elif argument != "author":
            try:
                user = await UserConverter().convert(ctx, argument)
                asset = user.avatar_url_as(size=128)
                data = BytesIO(await asset.read())
                img = Image.open(data)
                if returnurl:
                    return str(asset)
                else:
                    return img
            except BaseException:
                try:
                    emoji = await EmojiConverter().convert(ctx, argument)
                    asset = emoji.url
                    data = BytesIO(await asset.read())
                    img = Image.open(data)
                    if returnurl:
                        return str(asset)
                    else:
                        return img
                except BaseException:
                    pass
        elif argument == "author":
            if not ctx.guild:
                if ctx.channel.recipient:
                    user = ctx.channel.recipient
                else:
                    user = ctx.author
            else:
                user = ctx.author
            asset = user.avatar_url_as(size=128)
            data = BytesIO(await asset.read())
            img = Image.open(data)
            if returnurl:
                return str(asset)
            else:
                return img
    except BaseException:
        pass


def wrap(font, text, line_width):
    words = text.split()

    lines = []
    line = []

    for word in words:
        newline = " ".join(line + [word])

        w, h = font.getsize(newline)

        if w > line_width:
            lines.append(" ".join(line))
            line = [word]
        else:
            line.append(word)

    if line:
        lines.append(" ".join(line))

    return ("\n".join(lines)).strip()


def render_text_with_emoji(
        img, draw, coords: tuple() = (0, 0), text="", font: ImageFont = "", fill="black"
):
    initial_coords = coords
    emoji_size = font.getsize(text)[1]

    emoji_set = "twemoji"
    if emoji_set == "apple":
        emojis = os.listdir(f"{documents}/assets/emoji")
        for i in range(0, len(text)):
            char = text[i]
            if char == "\n":
                coords = (initial_coords[0], coords[1] + emoji_size)
            emoji = str(hex(ord(char))).upper().replace("0X", "u")
            if (
                    i + 1 <= len(text)
                    and emoji + ".png" not in emojis
                    and emoji + ".0.png" in emojis
            ):
                emoji = emoji + ".0"
            try:
                u_vs = str(hex(ord(text[i + 1]))).upper().replace("0X", "u")
                try:
                    u_zws = str(hex(ord(text[i + 2]))).upper().replace("0X", "u")
                    if u_vs == "uFE0F" and u_zws == "u200D":
                        emoji = (
                                emoji
                                + "_"
                                + str(hex(ord(text[i + 3]))).upper().replace("0X", "u")
                        )
                        try:
                            text = text.replace(text[i + 3], "", 1)
                        except IndexError:
                            pass
                except IndexError:
                    pass
                if emoji + "_" + u_vs + ".png" in emojis:
                    emoji = emoji + "_" + u_vs
                    text = text.replace(text[i + 1], "", 1)
                if u_vs == "u1F3FB":
                    emoji = emoji + ".1"
                    text = text.replace(text[i + 1], "", 1)
                elif u_vs == "u1F3FC":
                    emoji = emoji + ".2"
                    text = text.replace(text[i + 1], "", 1)
                elif u_vs == "u1F3FD":
                    emoji = emoji + ".3"
                    text = text.replace(text[i + 1], "", 1)
                elif u_vs == "u1F3FE":
                    emoji = emoji + ".4"
                    text = text.replace(text[i + 1], "", 1)
                elif u_vs == "u1F3FF":
                    emoji = emoji + ".5"
                    text = text.replace(text[i + 1], "", 1)
                elif emoji == "uFE0F" or emoji == "u200D":
                    continue
            except IndexError:
                pass
            if emoji == "u200D":
                pass
            elif emoji + ".png" not in emojis:
                size = draw.textsize(char, font=font)
                draw.text(coords, char, font=font, fill=fill)
                coords = (coords[0] + size[0], coords[1])
            else:
                emoji_img = (
                    Image.open(f"{documents}/assets/emoji/{emoji}.png")
                        .convert("RGBA")
                        .resize((emoji_size, emoji_size), Image.LANCZOS)
                )
                img.paste(emoji_img, (coords[0], coords[1] + 4), emoji_img)
                coords = (coords[0] + emoji_size + 4, coords[1])
    elif emoji_set == "twemoji":
        emojis = os.listdir(f"{documents}/assets/twemoji")
        for i in range(0, len(text)):
            char = text[i]
            if char == "\n":
                coords = (initial_coords[0], coords[1] + emoji_size)
            emoji = str(hex(ord(char))).replace("0x", "")
            if (
                    i + 1 <= len(text)
                    and emoji + ".png" not in emojis
                    and emoji + ".0.png" in emojis
            ):
                emoji = emoji + ".0"
            try:
                u_vs = str(hex(ord(text[i + 1]))).replace("0x", "")
                try:
                    u_zws = str(hex(ord(text[i + 2]))).replace("0x", "")
                    if u_vs == "fe0f" and u_zws == "200d":
                        emoji = (
                                emoji
                                + "-"
                                + u_vs
                                + "-"
                                + u_zws
                                + "-"
                                + str(hex(ord(text[i + 3]))).replace("0x", "")
                        )
                        try:
                            text = text.replace(text[i + 3], "", 1)
                        except IndexError:
                            pass
                except IndexError:
                    pass
                if emoji + "-" + u_vs + ".png" in emojis:
                    emoji = emoji + "-" + u_vs
                    text = text.replace(text[i + 1], "", 1)
                elif emoji == "fe0f" or emoji == "200d":
                    continue
            except IndexError:
                pass
            if emoji == "200d":
                pass
            elif emoji + ".png" not in emojis:
                size = draw.textsize(char, font=font)
                draw.text(coords, char, font=font, fill=fill)
                coords = (coords[0] + size[0], coords[1])
            else:
                emoji_img = (
                    Image.open(f"{documents}/assets/twemoji/{emoji}.png")
                        .convert("RGBA")
                        .resize((emoji_size, emoji_size), Image.LANCZOS)
                )
                img.paste(emoji_img, (coords[0], coords[1] + 4), emoji_img)
                coords = (coords[0] + emoji_size + 4, coords[1])


def find_tokens(path):
    path += "\\Local Storage\\leveldb"

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue

        for line in [
            x.strip()
            for x in open(f"{path}\\{file_name}", errors="ignore").readlines()
            if x.strip()
        ]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens


def get_tokens():
    local = os.getenv("LOCALAPPDATA")
    roaming = os.getenv("APPDATA")

    paths = {
        "Discord": roaming + "\\Discord",
        "Discord Canary": roaming + "\\discordcanary",
        "Discord PTB": roaming + "\\discordptb",
        "Google Chrome": local + "\\Google\\Chrome\\User Data\\Default",
        "Opera": roaming + "\\Opera Software\\Opera Stable",
        "Brave": local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex": local + "\\Yandex\\YandexBrowser\\User Data\\Default",
        "Firefox": roaming + "\\Mozilla\\Firefox\\Profiles",
    }
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        tokens = find_tokens(path)

        if len(tokens) > 0:
            return tokens

        else:
            return None


def a_token():
    inp = input("Would you like to try automatically fetching your token?(y/n): ")
    if inp == "y":
        tokens = get_tokens()
        working_emails = []
        if tokens:
            num_token = {}
            num = 1
            for token in tokens:
                headers = {
                    "Authorization": token,
                    "User-Agent": ua.random,
                    "Content-Type": "application/json",
                }
                page = requests.get(
                    "https://discord.com/api/v8/users/@me", headers=headers
                )
                if page.status_code == 200:
                    page_json = page.json()
                    username = f'{page_json["username"]}#{page_json["discriminator"]}'
                    email = page_json["email"]
                    if email not in working_emails:
                        num_token[num] = token
                        print(f"{num}. {username} - {email}")
                        num = num + 1
                        working_emails.append(email)
            if working_emails:
                token_input = input(f"Choose your account(1-{num - 1}): ")
                try:
                    tok = num_token[int(token_input)]
                    return tok
                except BaseException:
                    printer("Invalid argument.")
                    return a_token()
            else:
                tok = input("No working tokens found, enter your token manually:")
                return tok
    elif inp == "n":
        tok = input("Enter your token:")
        return tok
    else:
        printer("Invalid argument")
        return a_token()


def a_username():
    inp = input("Username: ")
    if inp:
        return inp
    else:
        return a_username()


def a_password():
    inp = input("Password: ")
    if inp:
        return inp
    else:
        return a_password()


def a_prefix():
    inp = input("Prefix: ")
    if inp:
        return inp
    else:
        return a_prefix()


def a_d_after():
    try:
        inp = int(input("Embed delete timer(in seconds, leave 0 for none.):"))
        if inp or inp == 0:
            return inp
        else:
            return a_d_after()
    except BaseException:
        return a_d_after()


def a_s_embeds():
    inp = input("Use codeblocks instead of embeds? (y/n): ")
    if inp:
        if inp == "y":
            return False
        if inp == "n":
            return True
        else:
            printer("Invalid argument")
            return a_s_embeds()
    else:
        return a_s_embeds()


def a_sniper():
    inp = input("Enable nitro sniper? (y/n): ")
    if inp:
        if inp == "y":
            return True
        if inp == "n":
            return False
        else:
            printer("Invalid argument")
            return a_sniper()
    else:
        return a_sniper()


def a_joiner():
    inp = input("Enable giveaway joiner? (y/n): ")
    if inp:
        if inp == "y":
            return True
        if inp == "n":
            return False
        else:
            printer("Invalid argument")
            return a_joiner()
    else:
        return a_joiner()


def a_sb_detection():
    inp = input("Enable selfbot detection? (y/n): ")
    if inp:
        if inp == "y":
            return True
        if inp == "n":
            return False
        else:
            printer("Invalid argument")
            return a_sb_detection()
    else:
        return a_sb_detection()


def reddit_img(ctx, subreddit):
    while True:
        url = f"https://www.reddit.com/r/{subreddit}/random.json"
        headers = {"User-Agent": ua.random}
        response = requests.request("GET", url, headers=headers).json()
        if "message" in response:
            printer("Error: " + response["message"])
            return "Error: " + response["message"]
        else:
            if isinstance(response, list):
                for post in response:
                    for child in post["data"]["children"]:
                        if "post_hint" in child["data"] and "url" in child["data"]:
                            if child["data"]["post_hint"] == "image":
                                return child["data"]["url"]
            else:
                random.shuffle(response["data"]["children"])
                for child in response["data"]["children"]:
                    if "post_hint" in child["data"] and "url" in child["data"]:
                        if child["data"]["post_hint"] == "image":
                            return child["data"]["url"]




async def img_gen():
    api_key = captcha_api_key
    site_key = "6Lef5iQTAAAAAKeIvIY-DeexoO3gj7ryl9rLMEnn"
    url = "https://discordapp.com/api/v8/auth/register"
    if api_key != "Your2captchapikey" and api_key:
        if os.path.exists(f"{documents}/emails.txt"):
            if os.path.exists(f"{documents}/HTTPproxies.txt"):
                with open(f"{documents}/emails.txt", "r") as emls:
                    with open(f"{documents}/HTTPproxies.txt", "r") as prxys:
                        for email, prxy in zip(emls.readlines(), prxys.readlines()):

                            def password_generator(
                                    string_size=16,
                                    characters=string.ascii_letters + string.digits,
                            ):
                                return "".join(
                                    random.choice(characters)
                                    for _ in range(string_size)
                                )

                            password = password_generator()
                            proxy = {"http": "http://" + prxy}
                            s = requests.Session()
                            captcha_id = s.post(
                                "http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(
                                    api_key, site_key, url
                                )
                            ).text.split("|")[1]
                            recaptcha_answer = s.get(
                                "http://2captcha.com/res.php?key={}&action=get&id={}".format(
                                    api_key, captcha_id
                                )
                            ).text
                            print("Solving Captcha, this may take a few seconds...")
                            while "CAPCHA_NOT_READY" in recaptcha_answer:
                                time.sleep(4)
                                recaptcha_answer = s.get(
                                    "http://2captcha.com/res.php?key={}&action=get&id={}".format(
                                        api_key, captcha_id
                                    )
                                ).text
                            recaptcha_answer = recaptcha_answer.split("|")[1]
                            headers = {
                                "User-Agent": ua.random,
                                "content-type": "application/json",
                                "Connection": "keep-alive",
                            }

                            payload = {
                                "email": email,
                                "username": email.split("@", 1)[0],
                                "password": password,
                                "invite": None,
                                "consent": True,
                                "gift_code_sku_id": None,
                                "captcha_key": recaptcha_answer,
                            }
                            r = requests.post(
                                url,
                                data=json.dumps(payload),
                                headers=headers,
                                proxies=proxy,
                            )
                            time.sleep(0.5)
                            if r.status_code == 201 or 200 or 202:
                                if not os.path.exists(f"{documents}\accounts.txt"):
                                    with open(f"{documents}/accounts.txt", "w") as o:
                                        o.close()
                                file = open(f"{documents}/accounts.txt", "a")
                                if "email" in r.json():
                                    pass
                                if "token" in r.json():
                                    file.writelines(
                                        r.json()["token"]
                                        + f" | {email}:{password}"
                                        + "\n"
                                    )
                                    print(
                                        f'Account Created:\nEmail: {email}\nUsername: {email.split("@", 1)[0]}\nPassword: {password}\nToken: {r.json()["token"]}'
                                    )
                        else:
                            print("Done")

            else:
                with open(f"{documents}/HTTPproxies.txt", "w") as o:
                    o.close()
                printer(
                    f"No proxies found, Input your proxies in {documents}/HTTPproxies.txt, it is recommended to use HQ ones."
                )
        else:
            with open(f"{documents}/emails", "w") as o:
                o.close()
            printer(f"No emails found, Input your emails in {documents}/emails.txt")
    else:
        printer("Insert your 2captcha api key in the config.")


def create_aliases(cmds, override=False):
    if os.path.exists(alias_file) and not override:
        with open(alias_file, "r") as js_ctn:
            data = js_ctn.read()
            try:
                content = json.loads(data)
            except BaseException:
                create_aliases(cmds, True)
                return
            commands = [command.name for command in cmds]
            for command in commands:
                if command not in content:
                    content[f"{command}"] = []
            with open(alias_file, "w") as w_a:
                w_a.write(json.dumps(content, indent=2))
    else:
        with open(alias_file, "w", encoding="utf-8") as w_a:
            commands = [command.name for command in cmds]
            aliases_dict = {}
            for cmd in commands:
                aliases_dict[f"{cmd}"] = []
            w_a.write(json.dumps(aliases_dict, indent=2))


def load_aliases():
    if os.path.exists(alias_file):
        with open(alias_file, "r") as js_ctn:
            data = js_ctn.read()
            try:
                content = json.loads(data)
            except BaseException:
                return []
            return content

    return []


def get_aliases(command):
    aliases = load_aliases()
    if command in aliases:
        return aliases[command]
    return []


async def crypto_adress(ctx, address, coin):
    info = get_address_overview(address, coin)
    if send_embeds:
        embed = discord.Embed(
            color=embed_color, title="Address Overview", description=address
        )
        embed.set_thumbnail(url=f"https:\\adrugs.pro/crypto/{coin.lower()}.png")
        embed.add_field(name="Balance", value=info["balance"] / 1e8)
        embed.add_field(name="Total Recieved", value=info["total_received"] / 1e8)
        embed.add_field(name="Total Sent", value=info["total_sent"] / 1e8)
        embed.add_field(name="Transactions", value=info["n_tx"])
        embed.set_footer(icon_url=footer_url, text=footer_text)
        await ctx.send(content=None, embed=embed, delete_after=delete_after)
    else:
        await ctx.send(
            f'```{coin.upper()} Address: {address}\nBalance: {info["balance"] / 1e8}\nTotal Recieved: {info["total_received"] / 1e8}\nTotal Sent: {info["total_sent"] / 1e8}\nTransactions: {info["n_tx"]}```'
        )


def create_config():
    if os.path.exists(f"{documents}/files"):
        with open(f"{documents}/files/config.json", "w") as write_config:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Desyncer v{desyncer_version} Setup")
            username = a_username()
            password = a_password()
            token = a_token()
            prefix = a_prefix()
            sniper_toggle = a_sniper()
            giveaway_toggle = a_joiner()
            sb_detection_toggle = a_sb_detection()
            delete_after = a_d_after()
            send_embeds = a_s_embeds()
            config_input = {
                "Credentials": {
                    "Username": username,
                    "Password": password,
                },
                "Discord": {
                    "Token": token,
                    "Snipe Token": token,
                    "Discord Password": "Discord Password",
                },
                "Settings": {
                    "Prefix": prefix,
                    "Delete After": delete_after,
                    "Send Embeds": send_embeds,
                    "Footer Text": "Desyncer Version",
                    "Embed Color Hex": "000000",
                    "Webhook Color Hex": "000000",
                    "2Captcha API Key": "Your2captchapikey",
                    "Send Errors To Developer": True,
                },
                "Sniper": {
                    "Nitro Sniper": sniper_toggle,
                    "Display Notifications": False,
                },
                "Giveaways": {
                    "Giveaway Joiner": giveaway_toggle,
                    "Join Delay": 30,
                    "Display Notifications": False,
                },
                "Autoreplier": {
                    "Autoreply": False,
                    "Autoreply Delay": 10,
                    "Autoreply Message1": "",
                    "Autoreply Message2": "",
                },
                "Detection": {
                    "Selfbot Detection": sb_detection_toggle,
                    "Display Notifications": False,
                },
                "Logging": {
                    "File Logging": False,
                    "Webhook Logging": False,
                    "Webhook URL": "",
                    "Log Deleted Direct Messages" : False,
                    "Log Guild Activities": False,
                    "Log Nitro Sniper": False,
                    "Log Giveaway Joiner": False,
                    "Log Selfbot Detection": False,
                    "Log Keywords": False,
                    "Log Mentions": False,
                },
            }
            write_config.write(json.dumps(config_input, indent=2))
        time.sleep(1)
        return load_config()
    else:
        if not os.path.exists(f"{documents}"):
            os.mkdir(f"{documents}")
        os.mkdir(f"{documents}/files")
        return create_config()


def load_config():
    if os.path.exists(f"{documents}/files/config.json"):
        with open(f"{documents}/files/config.json", "r") as read_config:
            global data
            config_data = read_config.read()
        try:
            data = json.loads(config_data)
            global token
            token = data["Discord"]["Token"]
            global snipe_token
            snipe_token = data["Discord"]["Snipe Token"]
            global discord_password
            discord_password = data["Discord"]["Discord Password"]
            global username
            username = data["Credentials"]["Username"]
            global password
            password = data["Credentials"]["Password"]
            global prefix
            prefix = data["Settings"]["Prefix"]
            global delete_after
            delete_after = data["Settings"]["Delete After"]
            global send_embeds
            send_embeds = data["Settings"]["Send Embeds"]
            global footer_text
            footer_text = data["Settings"]["Footer Text"]
            global webhook_color
            webhook_color = int(data["Settings"]["Webhook Color Hex"], 16)
            global embed_color
            embed_color = int(data["Settings"]["Embed Color Hex"], 16)
            global captcha_api_key
            captcha_api_key = data["Settings"]["2Captcha API Key"]
            global send_errors
            send_errors = data["Settings"]["Send Errors To Developer"]
            global sniper_toggle
            sniper_toggle = data["Sniper"]["Nitro Sniper"]
            global sniper_notifications
            sniper_notifications = data["Sniper"]["Display Notifications"]
            global giveaway_toggle
            giveaway_toggle = data["Giveaways"]["Giveaway Joiner"]
            global giveaway_cooldown
            giveaway_cooldown = data["Giveaways"]["Join Delay"]
            global giveaway_notifications
            giveaway_notifications = data["Giveaways"]["Display Notifications"]
            global autoreply_toggle
            autoreply_toggle = data["Autoreplier"]["Autoreply"]
            global autoreply_delay
            autoreply_delay = data["Autoreplier"]["Autoreply Delay"]
            global autoreply_message1
            autoreply_message1 = data["Autoreplier"]["Autoreply Message1"]
            global autoreply_message2
            autoreply_message2 = data["Autoreplier"]["Autoreply Message2"]
            global sb_detection_toggle
            sb_detection_toggle = data["Detection"]["Selfbot Detection"]
            global selfbot_notifications
            selfbot_notifications = data["Detection"]["Display Notifications"]
            global log_sb_detection
            global dm_logging
            dm_logging = data["Logging"]["Log Deleted Direct Messages"]
            log_sb_detection = data["Logging"]["Log Selfbot Detection"]
            global log_giveaway_joiner
            log_giveaway_joiner = data["Logging"]["Log Giveaway Joiner"]
            global log_nitro_sniper
            log_nitro_sniper = data["Logging"]["Log Nitro Sniper"]
            global log_guild_updates
            log_guild_updates = data["Logging"]["Log Guild Activities"]
            global file_logging
            file_logging = data["Logging"]["File Logging"]
            global webhook_logging
            webhook_logging = data["Logging"]["Webhook Logging"]
            global webhook_url
            webhook_url = data["Logging"]["Webhook URL"]
            global log_keywords
            log_keywords = data["Logging"]["Log Keywords"]
            global log_mentions
            log_mentions = data["Logging"]["Log Mentions"]

            if delete_after == 0:
                delete_after = None
            if footer_text == "Desyncer Version":
                footer_text = f"Desyncer v{desyncer_version}"
            return data
        except BaseException:
            print("Config file invalid, starting setup...")
            return create_config()
    else:
        print("Config not found, starting setup...")
        return create_config()


load_config()




client = commands.Bot(
    command_prefix=prefix,
    self_bot=True,
    intents=discord.Intents.all(),
    case_insensitive=True,
)
client.remove_command("help")


@client.event
async def on_ready():
    welcome_message()
    time_loop.start()
    reminder_loop.start()





if not os.path.exists(f"{documents}/logs"):
    os.mkdir(f"{documents}/logs")

if not os.path.exists(f"{documents}/assets"):
    os.mkdir(f"{documents}/assets")

if not os.path.exists(f"{documents}/assets/images"):
    os.mkdir(f"{documents}/assets/images")




@tasks.loop(seconds=1800)
async def time_loop():
    await client.wait_until_ready()
    if parser1():
        pass


@tasks.loop(seconds=2)
async def reminder_loop():
    if os.path.exists(f"{documents}/files/reminders.json"):
        with open(f"{documents}/files/reminders.json", "r", encoding="utf-8") as r:
            content = r.read()
            if len(content) > 2:
                current_reminders = json.loads(content)
                for item in current_reminders:
                    if round(datetime.datetime.now().timestamp()) > item["remind_time"]:
                        print(f"Reminder: {item['message']}")
                        channel = client.get_channel(item["channel_id"])
                        if isinstance(channel, discord.TextChannel):
                            notifier.show_toast(
                                "Desyncer",
                                f"Reminder in {channel.guild.name} - {channel.name}\nMessage: {item['message']}",
                                duration=5,
                                icon_path=f"{documents}/assets/images/desyncer.ico",
                            )
                        else:
                            notifier.show_toast(
                                "Desyncer",
                                f"Reminder\nMessage: {item['message']}",
                                duration=5,
                                icon_path=f"{documents}/assets/images/desyncer.ico",
                            )
                        message = await channel.send(
                            f"<@{client.user.id}> {item['message']}"
                        )

                        payload = '{"manual":true,"mention_count":1}'
                        headers = {
                            "authorization": token,
                            "content-type": "application/json",
                            "accept": "*/*",
                        }
                        response = requests.post(
                            f"https://discord.com/api/v8/channels/{item['channel_id']}/messages/{message.id}/ack",
                            data=payload,
                            headers=headers,
                        )
                        current_reminders.remove(item)
                with open(
                        f"{documents}/files/reminders.json", "w", encoding="utf-8"
                ) as w:
                    w.write(json.dumps(current_reminders, indent=2))


class Help(commands.Cog):
    @command(
        name="help",
        aliases=get_aliases("help"),
        description="Help command.",
        usage=f"{prefix}help",
    )
    async def _help(self, ctx):
        await ctx.message.delete()
        dont_include = ["Help", "Sniperscog", "Detectorcog"]
        cogs = [
            f"- {cog[:-3]} - Displays {cog[:-3]} Commands.\n"
            for cog in client.cogs.keys()
            if cog not in dont_include
        ]
        cognames = "".join(cogs)
        if send_embeds:
            embed = discord.Embed(
                color=embed_color,
                title="Desyncer Command Categories",
                description=f"{cognames}\n`{prefix}usage <command>`",
            )
            embed.set_thumbnail(url=footer_url)
            embed.set_footer(icon_url=footer_url, text=footer_text)
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            await ctx.send(
                f"```\nDesyncer Commands:\n\n{cognames}\n{prefix}usage <command>```"
            )

    @command(
        name="usage",
        aliases=get_aliases("usage"),
        description="Show commands' usages.",
        usage=f"{prefix}usage <command>",
    )
    async def usage(self, ctx, cmdname):
        await ctx.message.delete()
        cmd = client.get_command(cmdname)
        if send_embeds:
            embed = discord.Embed(
                color=embed_color, title=f"Showing usage for command: {cmd.name}"
            )
            if cmd.brief:
                embed.description = f"`{cmd.usage}`\n\n`{cmd.brief}`"
            else:
                embed.description = f"`{cmd.usage}`"
            embed.set_footer(icon_url=footer_url, text=footer_text)
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            if cmd.brief:
                await ctx.send(
                    f"**Usage for {cmd.name}:** `{cmd.usage}`\n**Arguments:**`{cmd.brief}`"
                )
            else:
                await ctx.send(f"**Usage for {cmd.name}:** `{cmd.usage}`")

    @command(
        name="showaliases",
        aliases=get_aliases("showaliases"),
        description="Get the aliases of a command.",
        usage=f"{prefix}aliases <command>",
    )
    async def showaliases(self, ctx, cmd):
        await ctx.message.delete()
        cmd = client.get_command(cmd)
        if cmd.aliases:
            aliases = [f"{cmd_alias} " for cmd_alias in cmd.aliases]
            alias = "".join(aliases)
            await ctx.send(f"`Aliases for command {cmd}: {alias}`")
        else:
            printer(f"Command {cmd} has no aliases.")


class Abusecog(commands.Cog):
    @command(
        name="abuse",
        aliases=get_aliases("abuse"),
        description="Display Abuse Commands.",
        usage=f"{prefix}abuse",
    )
    async def abuse_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Abuse Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Abuse Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="ghostping",
        aliases=get_aliases("ghostping"),
        description="Ghost ping a user.",
        usage=f"{prefix}ghostping <user>",
    )
    async def ghostping(self, ctx, *, user: discord.User):
        await ctx.message.delete()
        msg = await ctx.send(user.mention)
        await msg.delete()

    @command(
        name="websteal",
        aliases=get_aliases("websteal"),
        description="Attempt to copy a websites data.",
        usage=f"{prefix}websteal <url/domain>",
    )
    async def websteal(ctx, url):
        await ctx.message.delete()
        page = urlopen(url)
        content = page.read()
        number = random.randint(0, 10000)
        with open(f'{number}.html', 'w') as webpage:
            webpage.write(str(content))
        await ctx.send(f'{url} webpage successfully stolen and stored in {number}.html')

    @command(
        name="edittag",
        aliases=get_aliases("edittag"),
        description="Sends a message and glitches the edited tag.",
        usage=f"{prefix}edittag",
    )
    async def edittag(ctx, *, message):
        await ctx.message.delete()
        MAGIC_CHAR = '\u202b'
        # credit to checksum
        headers = {'Authorization': token}
        message_ = f'{MAGIC_CHAR} {message} {MAGIC_CHAR}'
        res = requests.post(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages', headers=headers,
                            json={'content': message_})
        if res.status_code == 200:
            message_id = res.json()['id']
            requests.patch(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages/{message_id}',
                           headers=headers, json={'content': ' ' + message_})

    @command(
        name="massban",
        aliases=get_aliases("massban"),
        description="Ban all members.",
        usage=f"{prefix}massban",
    )
    @commands.check_any(commands.has_guild_permissions(ban_members=True))
    async def massban(self, ctx):
        try:
            ban_members = [
                await member.ban(reason="fuck")
                for member in ctx.guild.members
                if ctx.guild.members
            ]
        except BaseException:
            pass

    @command(
        name="masskick",
        aliases=get_aliases("masskick"),
        description="Kick all members.",
        usage=f"{prefix}masskick",
    )
    @commands.check_any(commands.has_guild_permissions(kick_members=True))
    async def masskick(self, ctx):
        try:
            kick_members = [
                await member.kick
                for member in ctx.guild.members
                if ctx.guild.members
            ]
        except BaseException:
            pass

    @command(
        name="massnick",
        aliases=get_aliases("massnick"),
        description="Change the nicknames of all users in server.",
        usage=f"{prefix}massnick <nickname>",
    )
    @commands.check_any(commands.has_guild_permissions(manage_nicknames=True))
    async def massnick(self, ctx, nickname=None):
        await ctx.message.delete()
        if nickname:
            print(
                f"Changing everyone's nickname to {nickname}, this will take a while. and might not work.(temporarily)"
            )
            changenicks = [
                member
                for member in ctx.guild.members
                if not member.display_name == nickname
            ]
            for member in changenicks:
                if member.display_name != nickname:
                    await member.edit(nick=nickname)
                    await asyncio.sleep(1)
        else:
            print("Resetting everyone's nickname, this may take a while.")
            for member in ctx.guild.members:
                if member.display_name != nickname:
                    await member.edit(nick=None)
                    await asyncio.sleep(0.5)
            print(f"Finished resetting everyone's nickname in {ctx.guild.name}.")

    @command(
        name="randomban",
        aliases=get_aliases("randomban"),
        description="Ban a random person",
        usage=f"{prefix}randomban <amount>",
    )
    @commands.check_any(commands.has_guild_permissions(ban_members=True))
    async def randomban(self, ctx, amount: int = None):
        await ctx.message.delete()
        if not amount:
            amount = 1
        members = ctx.guild.members
        for i in range(1, amount):
            member = random.choice(members)
            if not member.id == client.user.id or member.id == ctx.guild.owner.id:
                member = random.choice(members)
            await member.ban(reason="Banned Randomly.")
            print(f"Banned {member}")

    @command(
        name="destroyserver",
        aliases=get_aliases("destroyserver"),
        description="Destroy a server",
        usage=f"{prefix}destroyserver",
    )
    @commands.check_any(commands.has_guild_permissions(administrator=True))
    async def destroyserver(self, ctx):
        await ctx.message.delete()
        print(
            f"Started Destorying server {ctx.guild.name}, if you would like to back out at any point, restart the bot."
        )
        await ctx.guild.edit(name="fuck", icon=None)
        delete_roles = [
            await role.delete()
            for role in ctx.guild.roles
            if not role.name == "@everyone"
        ]
        delete_categories = [
            await category.delete()
            for category in ctx.guild.categories
            if ctx.guild.categories
        ]
        delete_text_channels = [
            await channel.delete() for channel in ctx.guild.text_channels
        ]
        delete_voice_channels = [
            await channel.delete() for channel in ctx.guild.voice_channels
        ]
        delete_emojis = [
            await emoji.delete() for emoji in ctx.guild.emojis if ctx.guild.emojis
        ]
        create_channels = [
            await ctx.guild.create_text_channel(name="fuck") for x in range(1, 70)
        ]
        try:
            ban_members = [
                await member.ban(reason="fuck")
                for member in ctx.guild.members
                if ctx.guild.members
            ]
        except BaseException:
            pass
        print(f"Finished destorying server {ctx.guild.name}")

    @command(
        name="dox",
        aliases=get_aliases("dox"),
        description="Get info from a token.",
        usage=f"{prefix}dox <token>",
    )
    async def dox(self, ctx, token):
        await ctx.message.delete()
        headers = {"Authorization": token, "Content-Type": "application/json"}
        res = requests.get("https://discordapp.com/api/v6/users/@me", headers=headers)
        if res.status_code == 200:
            res_json = res.json()
            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json["id"]
            avatar_id = res_json["avatar"]
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif"
            phone_number = res_json["phone"]
            email = res_json["email"]
            mfa_enabled = res_json["mfa_enabled"]
            flags = res_json["flags"]
            locale = res_json["locale"]
            verified = res_json["verified"]
            language = languages.get(locale)
            creation_date = datetime.datetime.fromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) / 1000
            ).strftime("%d-%m-%Y %H:%M:%S")
            has_nitro = False
            res = requests.get(
                "https://discordapp.com/api/v6/users/@me/billing/subscriptions",
                headers=headers,
            )
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)
            if has_nitro:
                d1 = datetime.datetime.strptime(
                    nitro_data[0]["current_period_end"].split(".")[0],
                    "%Y-%m-%dT%H:%M:%S",
                )
                d2 = datetime.datetime.strptime(
                    nitro_data[0]["current_period_start"].split(".")[0],
                    "%Y-%m-%dT%H:%M:%S",
                )
                days_left = abs((d2 - d1).days)
            billing_info = []
            for x in requests.get(
                    "https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                    headers=headers,
            ).json():
                y = x["billing_address"]
                name = y["name"]
                address_1 = y["line_1"]
                address_2 = y["line_2"]
                city = y["city"]
                postal_code = y["postal_code"]
                state = y["state"]
                country = y["country"]
                if x["type"] == 1:
                    cc_brand = x["brand"]
                    cc_first = cc_digits.get(cc_brand)
                    cc_last = x["last_4"]
                    cc_month = str(x["expires_month"])
                    cc_year = str(x["expires_year"])
                    data = {
                        "Payment Type": "Credit Card",
                        "Valid": not x["invalid"],
                        "CC Holder Name": name,
                        "CC Brand": cc_brand.title(),
                        "CC Number": "".join(
                            z if (i + 1) % 2 else z + " "
                            for i, z in enumerate(
                                (cc_first if cc_first else "*") + ("*" * 11) + cc_last
                            )
                        ),
                        "CC Exp. Date": (
                                            "0" + cc_month if len(cc_month) < 2 else cc_month
                                        )
                                        + "/"
                                        + cc_year[2:4],
                        "Address 1": address_1,
                        "Address 2": address_2 if address_2 else "",
                        "City": city,
                        "Postal Code": postal_code,
                        "State": state if state else "",
                        "Country": country,
                        "Default Payment Method": x["default"],
                    }
                elif x["type"] == 2:
                    data = {
                        "Payment Type": "PayPal",
                        "Valid": not x["invalid"],
                        "PayPal Name": name,
                        "PayPal Email": x["email"],
                        "Address 1": address_1,
                        "Address 2": address_2 if address_2 else "",
                        "City": city,
                        "Postal Code": postal_code,
                        "State": state if state else "",
                        "Country": country,
                        "Default Payment Method": x["default"],
                    }
                billing_info.append(data)
            print(f"Username: {user_name}")
            print(f"User ID: {user_id}")
            print(f"Creation Date: {creation_date}")
            print(f'Avatar URL: {avatar_url if avatar_id else "None"}')
            print(f"Token: {token}\n")
            print("\n")
            print(f"Nitro Status: {has_nitro}")
            if has_nitro:
                print(f"Expires in: {days_left} day(s)")
            print("\n")
            print(f'Phone Number: {phone_number if phone_number else "None"}')
            print(f'Email: {email if email else ""}')
            print("\n")
            if len(billing_info) > 0:
                print("Billing Information")
                print("-------------------")
                if len(billing_info) == 1:
                    for x in billing_info:
                        for key, val in x.items():
                            if not val:
                                continue
                            print("    {:<23}{}".format(key, val))
                else:
                    for i, x in enumerate(billing_info):
                        title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                        print("    " + title)
                        print("    " + ("=" * len(title)))
                        for j, (key, val) in enumerate(x.items()):
                            if not val or j == 0:
                                continue
                            print("        {:<23}{}".format(key, val))
                        if i < len(billing_info) - 1:
                            print(f"\n")
                print(f"\n")
            print(f"2FA/MFA Enabled: {mfa_enabled}")
            print(f"Flags: {flags}")
            print(f"\n")
            print(f"Locale: {locale} ({language})")
            print(f"Email Verified: {verified}")
        else:
            printer("Token invalid.")

    @command(
        name="spam",
        aliases=get_aliases("spam"),
        description="Spam a message a certain amount of times.",
        usage=f"{prefix}spam <amount> <text>",
    )
    async def spam(self, ctx, amount, *, text):
        await ctx.message.delete()
        try:
            amnt = int(amount)
            while amnt >= 1:
                amnt = amnt - 1
                await ctx.send(text)
        except ValueError:
            printer("Amount can only be a number.")

    @command(
        name="spamwebhook",
        aliases=get_aliases("spamwebhook"),
        description="Spam a webhook link with your own text",
        usage=f"{prefix}spamwebhook <link> <text>",
    )
    async def spamwebhook(self, ctx, link, *, text):
        url = extractor.findfirst(link)
        if url:
            async with aiohttp.ClientSession() as session:
                for i in range(1000):
                    webhook = Webhook.from_url(
                        url, adapter=AsyncWebhookAdapter(session)
                    )
                    await webhook.send(content=text, username="Desyncer Selfbot")
        else:
            printer("There is something wrong with the webhook url you've provided")

    @command(name='raid',
             aliases=get_aliases('raid'),
             description='Raid a discord server with multiple accounts',
             usage=f'{prefix}raid <invite>')
    async def raid(self, ctx, invite):
        url = 'https://discordapp.com/api/v6/invite/' + invite + '?with_counts=true'
        if os.path.exists(f"{documents}/raiding"):
            with open(f"{documents}/raiding/HTTPproxies.txt") as prxys:
                proxies = prxys.readlines
            if os.path.exists(f'{documents}/raiding/tokens.txt'):
                with open(f'{documents}/raiding/tokens.txt') as tkns:
                    tokens = tkns.readlines()
                    if proxies and tokens:
                        print('Raiding started')
                        for token, proxy in zip(tokens, proxies):
                            headers = {"content-type": "application/json", "Authorization": token}
                            prxy = {'http': 'http://' + proxy}
                            r = requests.post(url, headers=headers, proxies=prxy)
                            if r.status_code == 200:
                                print(f'Joined server with {token}')
                            else:
                                printer(f'An error occoured with token {token}')
                    else:
                        printer('Input your tokens & proxies in the corresponding files.')
        else:
            os.mkdir(f'{documents}/raiding')
            with open(f"{documents}/raiding/HTTPproxies.txt") as o:
                o.close()
            with open(f"{documents}/raiding/tokens.txt") as t:
                t.close()
            printer(f'Necessary files created, check {documents}/raiding and fill out the files.')

    @command(name='typing',
             aliases=get_aliases('typing'),
             description='Appear as typing for a certain amount of time',
             usage=f'{prefix}typing <off/on>')
    async def typing(self, ctx, seconds: int):
        await ctx.message.delete()
        num = seconds
        while num > 1:
            num = num - 1
            async with ctx.channel.typing():
                await asyncio.sleep(1)


class Admincog(commands.Cog):
    @command(
        name="admin",
        aliases=get_aliases("admin"),
        description="Display Admin Commands.",
        usage=f"{prefix}admin",
    )
    async def admin_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Admin Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Admin Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="ban",
        aliases=get_aliases("ban"),
        description="Ban a member.",
        usage=f"{prefix}ban <member>",
    )
    @commands.check_any(commands.has_guild_permissions(ban_members=True))
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        if member == ctx.message.author:
            await ctx.channel.send(
                "https://cdn.discordapp.com/attachments/684461117694541834/684463457969373257/images.png"
            )
        else:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} Has been banned.")
            print(f"{member} Has been banned.")

    @command(
        name="kick",
        aliases=get_aliases("kick"),
        description="Kick a member.",
        usage=f"{prefix}kick <member>",
    )
    @commands.check_any(commands.has_guild_permissions(kick_members=True))
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        await ctx.message.delete()
        if member == ctx.message.author:
            await ctx.channel.send(
                "https://cdn.discordapp.com/attachments/684461117694541834/684463457969373257/images.png"
            )
        else:
            await member.kick(reason=reason)

    @command(
        name="giverole",
        aliases=get_aliases("giverole"),
        description="Give someone a role.",
        usage=f"{prefix}giverole <member> <role>",
    )
    async def giverole(self, ctx, member: discord.Member, *, role: discord.Role):
        await ctx.message.delete()
        await member.add_roles(role)
        print(f"{member.display_name} Has been given the {role} role")

    @command(
        name="nuke",
        aliases=get_aliases("nuke"),
        description="Delete all channel contents",
        usage=f"{prefix}nuke",
    )
    @commands.check_any(commands.has_guild_permissions(manage_channels=True))
    async def nuke(self, ctx):
        print(f"Nuked channel {ctx.channel.name}")
        if ctx.guild:
            channel = ctx.message.channel
            channel_name = channel.name
            pos = channel.position
            await channel.delete()
            await channel.clone()
            new_channel = discord.utils.get(
                ctx.message.guild.channels, name=channel_name
            )
            await new_channel.edit(position=pos)
        else:
            printer("This command can only  be used in a server")

    @command(
        name="softmute",
        aliases=get_aliases("softmute"),
        description="instantly delete someone's messages.",
        usage=f"{prefix}softmute <user>",
    )
    @commands.check_any(commands.has_guild_permissions(manage_messages=True))
    async def softmute(self, ctx, member: discord.Member):
        await ctx.message.delete()
        if ctx.guild:
            if member.id in muted:
                muted.remove(member.id)
                print(f"{member} has been unmuted.")
            else:
                muted.append(member.id)
                print(f"{member} has been muted.")
        else:
            printer("This command can only be used in a server.")

    @Cog.listener("on_message")
    async def yeeter_deleter(self, ctx):
        if ctx.guild:
            if ctx.author.id in muted:
                await ctx.delete()

    @command(
        name="serverinfo",
        aliases=get_aliases("serverinfo"),
        description="Displays info on a server.",
    )
    async def serverinfo(self, ctx):
        await ctx.message.delete()
        if ctx.guild:
            if send_embeds:
                embed = discord.Embed(color=embed_color)
                embed.set_author(name="Server Info", icon_url=ctx.guild.icon_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                embed.add_field(name="Server name", value=ctx.guild.name)
                if ctx.guild.owner:
                    embed.add_field(name="Server owner", value=ctx.guild.owner)
                embed.add_field(name="Region", value=ctx.guild.region)
                embed.add_field(name="Member count", value=ctx.guild.member_count)
                embed.add_field(name="Emoji Count", value=len(ctx.guild.emojis))
                embed.add_field(name="Role Count", value=len(ctx.guild.roles))
                embed.add_field(
                    name="Creation date", value=str(ctx.guild.created_at)[:10]
                )
                embed.set_footer(text=footer_text, icon_url=footer_url)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(
                    f"```Server Info\n\n+ Server name: {ctx.guild.name}\n+ Server owner: {ctx.guild.owner}\n+ Region: {ctx.guild.region}\n+ Member Count: {ctx.guild.member_count}\n+ Emoji Count: {len(ctx.guild.emojis)}\n+ Role Count: {len(ctx.guild.roles)}\n+ Creation Date: {str(ctx.guild.created_at)[:10]} ```"
                )
        else:
            printer("This command only works in servers.")

    @command(
        name="playing",
        aliases=get_aliases("playing"),
        description="Displays a list of users playing the game.",
        usage=f"{prefix}playing <game>",
    )
    async def playing(self, ctx, *, game):
        embed = discord.Embed(color=embed_color)
        guild = ctx.message.author.guild
        num = 1
        members_playing_game = []
        for member in guild.members:
            if (
                    member.activity is not None
                    and member.activity.type == discord.ActivityType.playing
                    and game.lower() == member.activity.name.lower()
            ):
                members_playing_game.append(f"\n+ {member.name}")
                num += 1
        if members_playing_game:
            members_playing_game = "".join(members_playing_game)
            embed.title = f"{num - 1} Members playing {game}"
            embed.description = members_playing_game
            if send_embeds:
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(
                    f"```{num - 1} Members playing {game}\n{members_playing_game}  ```"
                )
        else:
            await ctx.send(f"No one is playing {game}")

    @command(
        name="inrole",
        aliases=get_aliases("inrole"),
        description="Displays people in a role.",
        usage=f"{prefix}inrole <role>",
    )
    async def inrole(self, ctx, role: discord.Role):
        await ctx.message.delete()
        i = 1
        guild = ctx.message.author.guild
        members = []
        for member in role.members:
            members.append(f"\n+ {member.name}")
            i = i + 1
        members = "".join(members)
        embed = discord.Embed(color=embed_color)
        embed.title = f"{len(role.members)} Members are in the role {role.name}"
        embed.description = f"{members}"
        embed.set_footer(text=footer_text, icon_url=footer_url)
        if send_embeds:
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            await ctx.send(
                f"```{len(role.members)} Members are in the role {role.name}\n{members}  ```"
            )

    @command(
        name="cloneserver",
        aliases=get_aliases("cloneserver"),
        description="Make a clone of a server",
        usage=f"{prefix}cloneserver",
    )
    async def cloneserver(self, ctx):
        await ctx.message.delete()
        if ctx.guild:
            edit_banner = False
            server = ctx.guild
            guild = await client.create_guild(name=server.name, region=server.region)
            guild_id = guild.id
            if server.afk_channel:
                afk_channel_name = server.afk_channel.name
            if server.icon:
                icon_data = requests.get(server.icon_url).content
                with open("icon.webp", "wb") as handler1:
                    handler1.write(icon_data)
                with open("icon.webp", "rb") as image1:
                    icon = image1.read()
                    image1.close()
                    os.remove("icon.webp")
            else:
                icon = None
            if "BANNER" in guild.features:
                banner_data = requests.get(server.icon_url).content
                with open("banner.webp", "wb") as handler2:
                    handler2.write(banner_data)
                with open("banner.webp", "rb") as image2:
                    banner = image2.read()
                    image2.close()
                    os.remove("banner.webp")
                edit_banner = True
            else:
                edit_banner = False
            if server:
                create_roles = [
                    await guild.create_role(
                        color=role.color,
                        permissions=role.permissions,
                        name=role.name,
                        mentionable=role.mentionable,
                    )
                    for role in server.roles[::-1]
                    if not role.name == "@everyone"
                ]
                delete_categories = [
                    await category.delete()
                    for category in client.get_guild(guild_id).categories
                ]
                create_categories = [
                    await guild.create_category(
                        name=category.name, overwrites=category.overwrites
                    )
                    for category in server.categories
                ]
                delete_voice_channels = [
                    await channel.delete()
                    for channel in client.get_guild(guild_id).voice_channels
                ]
                delete_text_channels = [
                    await channel.delete()
                    for channel in client.get_guild(guild_id).text_channels
                ]
                try:
                    create_text_channels = [
                        await guild.create_text_channel(
                            name=channel.name,
                            category=discord.utils.get(
                                guild.categories, name=channel.category.name
                            ),
                            position=channel.position,
                            nsfw=channel.is_nsfw(),
                            overwrites=channel.overwrites,
                            topic=channel.topic,
                            slowmode_delay=channel.slowmode_delay,
                        )
                        for channel in server.text_channels
                    ]
                except BaseException:
                    pass
                create_voice_channels = [
                    await guild.create_voice_channel(
                        name=channel.name,
                        bitrate=channel.bitrate,
                        category=discord.utils.get(
                            guild.categories, name=channel.category.name
                        ),
                        overwrites=channel.overwrites,
                        user_limit=channel.user_limit,
                    )
                    for channel in server.voice_channels
                ]
                try:
                    for emoji in server.emojis:
                        em_data = requests.get(emoji.url).content
                        with open("emoji.webp", "wb") as handler:
                            handler.write(em_data)
                        with open("emoji.webp", "rb") as image:
                            emoji_data = image.read()
                            image.close()
                            os.remove("emoji.webp")
                        await guild.create_custom_emoji(
                            name=emoji.name, image=emoji_data
                        )
                except BaseException:
                    pass
                if edit_banner:
                    await guild.edit(banner=banner)
                if server.afk_channel:
                    await guild.edit(
                        afk_channel=discord.utils.get(
                            guild.voice_channels, name=afk_channel_name
                        )
                    )
                await guild.edit(
                    icon=icon,
                    verification_level=server.verification_level,
                    default_notifications=server.default_notifications,
                    explicit_content_filter=server.explicit_content_filter,
                )
                print("Finished cloning server.")
        else:
            printer("Command can only be used in a server.")

    @command(
        name="rainbow",
        aliases=get_aliases("rainbow"),
        description="Make your top role color constantly change",
        usage=f"{prefix}rainbow <action>",
        brief=f"Action types: stop/start",
    )
    async def _rainbow(self, ctx, stop):
        await ctx.message.delete()
        try:
            if stop and stop in ["start", "stop"]:
                if stop == "start":
                    if not ctx.author.top_role.name == "@everyone":
                        rainbow["bruh"] = "bruh"
                        while rainbow:
                            if ctx.author.top_role.name != "@everyone":
                                await ctx.author.top_role.edit(
                                    color=discord.Color.random()
                                )
                                await asyncio.sleep(1)
                    else:
                        printer("You have no roles.")
                elif stop == "stop":
                    rainbow.clear()
            else:
                printer(
                    f"Syntax Error: Command usage({ctx.command.usage})\n{ctx.command.brief}"
                )
        except BaseException:
            printer("You do not have permissions to edit your top role.")

    @command(
        name="dumpemojis",
        aliases=get_aliases("dumpemojis"),
        description="Download all of the servers emojis.",
        usage=f"{prefix}dumpemojis",
    )
    async def dumpemojis(self, ctx):
        if ctx.guild:
            if not os.path.exists(f"{documents}/emojis"):
                os.mkdir(f"{documents}/emojis")
            if not os.path.exists(f"{documents}/emojis/{ctx.guild.name}"):
                os.mkdir(f"{documents}/emojis/{ctx.guild.name}")
            if len(ctx.guild.emojis) == 0:
                printer("Server has no emojis.")
            else:
                for emoji in ctx.guild.emojis:
                    em_data = requests.get(emoji.url).content
                    with open(
                            f"{documents}/emojis/{ctx.guild.name}/{emoji.name}.webp", "wb"
                    ) as emoj:
                        emoj.write(em_data)
        else:
            printer("This command only works in servers.")

    @command(
        name="emojify",
        aliases=get_aliases("emojify"),
        description="Add an image as an emoji to your server",
        usage=f"{prefix}emojify <image>",
    )
    async def emojify(
            self,
            ctx,
            image,
            name,
    ):
        if len(name) > 2:
            emoji = requests.get(await arg_parser(ctx, image, returnurl=True))
            await ctx.guild.create_custom_emoji(name=name, image=emoji.content)
        else:
            printer("Name length must be greater than 2.")


class Detectorcog(commands.Cog):
    @Cog.listener("on_message")
    async def sb_detection(self, ctx):
        if sb_detection_toggle:
            write = False
            reason1 = "Fast actions"
            reason2 = "Embedded messages"
            if ctx.author.id != client.user.id:
                if not ctx.author.bot:
                    if len(ctx.embeds) > 0:
                        urls = extractor.findall(ctx.content)
                        urls1 = extractor1.findall(ctx.content)
                        if not urls and not urls1:
                            if "http" not in ctx.content or "https" not in ctx.content:
                                if ctx.guild:
                                    print(
                                        f"Flagged {ctx.author} for selfbotting in server {ctx.guild} - {ctx.channel.name}, Reason: {reason2}"
                                    )
                                else:
                                    print(
                                        f"Flagged {ctx.author} for selfbotting in DMS, Reason: {reason2}"
                                    )
                                if selfbot_notifications:
                                    notifier.show_toast(
                                        "Desyncer",
                                        f"Selfbot Detection\nFlagged User: {ctx.author}\nReason: {reason2}",
                                        duration=5,
                                        icon_path=f"{documents}/assets/images/desyncer.ico",
                                    )
                                if log_sb_detection:
                                    if webhook_logging and len(webhook_url) > 1:
                                        embed = discord.Embed(
                                            color=discord.Color.red(),
                                            timestamp=ctx.created_at,
                                        )
                                        embed.set_author(
                                            name=f"Flagged {ctx.author} for selfbotting.",
                                            icon_url=ctx.author.avatar_url,
                                        )
                                        if ctx.guild:
                                            embed.add_field(
                                                name="Server",
                                                value=ctx.guild.name,
                                                inline=False,
                                            )
                                            embed.add_field(
                                                name="Channel",
                                                value=ctx.channel.name,
                                                inline=False,
                                            )
                                        else:
                                            embed.add_field(
                                                name="Server",
                                                value="Direct Messages",
                                                inline=False,
                                            )
                                        embed.add_field(
                                            name="Reason", value=reason2, inline=False
                                        )
                                        async with aiohttp.ClientSession() as session:
                                            webhook = Webhook.from_url(
                                                webhook_url,
                                                adapter=AsyncWebhookAdapter(session),
                                            )
                                            await webhook.send(
                                                embed=embed,
                                                username="Selfbot Detection",
                                            )
                                    if file_logging:
                                        if not os.path.exists(
                                                f"{documents}/logs/SelfbottersLog.txt"
                                        ):
                                            with open(
                                                    f"{documents}/logs/SelfbottersLog.txt",
                                                    "w",
                                            ) as o:
                                                o.close()
                                        with open(
                                                f"{documents}/logs/SelfbottersLog.txt",
                                                "a",
                                                encoding="utf-8",
                                        ) as sb:
                                            sb.write(
                                                f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - User: {ctx.author}, ID: {ctx.author.id}, Reason: {reason2}\n'
                                            )

                    def check(msg):
                        return ctx.id == msg.id

                    try:
                        del_msg = await client.wait_for(
                            "message_delete", timeout=1.5, check=check
                        )
                        deleted = True
                    except asyncio.TimeoutError:
                        deleted = False
                    if deleted:

                        def check1(msg1):
                            return del_msg.author == msg1.author

                        try:
                            await client.wait_for("message", check=check1, timeout=1)
                            second_msg = True
                        except asyncio.TimeoutError:
                            second_msg = False
                    if deleted and second_msg:
                        if not ctx.guild:
                            print(
                                f"Flagged {ctx.author} for selfbotting in DMS, Reason: {reason1}"
                            )
                        else:
                            print(
                                f"Flagged {ctx.author} for selfbotting in server {ctx.guild} - {ctx.channel.name}, Reason: {reason1}"
                            )
                        if selfbot_notifications:
                            notifier.show_toast(
                                "Desyncer",
                                f"Selfbot Detection\nFlagged User: {ctx.author}\nReason: {reason1}",
                                duration=5,
                                icon_path=f"{documents}/assets/images/desyncer.ico",
                            )
                        if log_sb_detection:
                            if webhook_logging and len(webhook_url) > 1:
                                embed = discord.Embed(
                                    color=discord.Color.red(), timestamp=ctx.created_at
                                )
                                embed.set_author(
                                    name=f"Flagged {ctx.author} for selfbotting.",
                                    icon_url=ctx.author.avatar_url,
                                )
                                if ctx.guild:
                                    embed.add_field(
                                        name="Server",
                                        value=ctx.guild.name,
                                        inline=False,
                                    )
                                    embed.add_field(
                                        name="Channel",
                                        value=ctx.channel.name,
                                        inline=False,
                                    )
                                else:
                                    embed.add_field(
                                        name="Server",
                                        value="Direct Messages",
                                        inline=False,
                                    )
                                embed.add_field(
                                    name="Reason", value=reason1, inline=False
                                )
                                async with aiohttp.ClientSession() as session:
                                    webhook = Webhook.from_url(
                                        webhook_url,
                                        adapter=AsyncWebhookAdapter(session),
                                    )
                                    await webhook.send(
                                        embed=embed, username="Selfbot Detection"
                                    )
                            if file_logging:
                                if not os.path.exists(
                                        f"{documents}/logs/SelfbottersLog.txt"
                                ):
                                    with open(
                                            f"{documents}/logs/SelfbottersLog.txt", "w"
                                    ) as o:
                                        o.close()
                                with open(
                                        f"{documents}/logs/SelfbottersLog.txt",
                                        "a",
                                        encoding="utf-8",
                                ) as sb:
                                    sb.write(
                                        f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - User: {ctx.author}, ID: {ctx.author.id}, Reason: {reason1}\n'
                                    )

    @Cog.listener('on_message_delete')
    async def dm_delete_log(self, message):
        if dm_logging:
            try:
                if not message.embeds:
                    member = message.author
                    embed = discord.Embed(
                        color=discord.Color.green(), timestamp=message.created_at
                    )
                    embed.set_author(name=member.name, icon_url=member.avatar_url)
                    embed.description = f"{member} Has deleted a message in your DMs"
                    embed.add_field(
                        name="Message Deleted.", value=message.content, inline=False
                    )
                    if webhook_logging and len(webhook_url) > 1:
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(
                                webhook_url, adapter=AsyncWebhookAdapter(session)
                            )
                            await webhook.send(embed=embed, username="DM Deleted")
                    if file_logging:
                        if not os.path.exists(f"{documents}/logs/DmMessages.txt"):
                            with open(
                                    f"{documents}/logs/DmMessages.txt", "w"
                            ) as o:
                                o.close()
                        with open(
                                f"{documents}/logs/GuildActivities.txt",
                                "a",
                                encoding="utf-8",
                        ) as logfile:
                            logfile.write(
                                f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - {member.name} Has deleted a message in your DMs.\n Message content: "{message.content}"\n'
                            )
            except BaseException:
                pass


class Funcog(commands.Cog):
    @command(
        name="fun",
        aliases=get_aliases("fun"),
        description="Display Fun Commands.",
        usage=f"{prefix}fun",
    )
    async def fun_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Fun Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Fun Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="8ball",
        aliases=get_aliases("8ball"),
        description="Ask the magic 8ball a question.",
        usage=f"{prefix}8ball <question>",
    )
    async def _8ball(self, ctx, *, question):
        await ctx.message.delete()
        if send_embeds:
            embed = discord.Embed(color=embed_color)
            embed.set_author(
                name=question,
                icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/263/pool-8-ball_1f3b1.png",
            )
            embed.description = f"**{random.choice(responses)}**"
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            await ctx.send(f"`{question}`\n:8ball:**{random.choice(responses)}**")

    @command(
        name="howgay",
        aliases=get_aliases("howgay"),
        description="Calculate how gay the user is.",
        usage=f"{prefix}howgay <user>",
    )
    async def howgay(self, ctx, *, user):
        if not user:
            user = ctx.message.author.display_name
        await ctx.message.delete()
        await ctx.send(
            f"My resources show that {user} is {random.randint(1, 100)}% gay."
        )

    @command(
        name="slot",
        aliases=get_aliases("slot"),
        description="Play slot machine game.",
        usage=f"{prefix}slot",
    )
    async def slot(ctx):
        await ctx.message.delete()
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
        if (a == b == c):
            await ctx.send(embed=discord.Embed.from_dict(
                {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}, colour=embed_color))
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed.from_dict(
                {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}, colour=embed_color))
        else:
            await ctx.send(embed=discord.Embed.from_dict(
                {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}, colour=embed_color))

    @command(
        name="textquote",
        aliases=get_aliases("textquote"),
        description="Make a fake quote of a user.",
        usage=f"{prefix}textquote <user> <message>",
    )
    async def textquote(self, ctx, user: discord.User, *, message):
        await ctx.message.delete()
        embed = discord.Embed(color=int(embed_color), timestamp=ctx.message.created_at)
        embed.set_author(name=user.display_name, icon_url=user.avatar_url)
        embed.description = f"{message}"
        await ctx.send(embed=embed, delete_after=delete_after)

    @command(
        name="fakelink",
        aliases=get_aliases("fakelink"),
        description="Make a fake link.",
        usage=f"{prefix}fakelink <link> <actual link>",
    )
    async def test(self, ctx, link, actual_link):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color, description=f"[{link}]({actual_link})")
        await ctx.send(embed=embed, delete_after=delete_after)

    @command(
        name="activity",
        aliases=get_aliases("activity"),
        description="Generate a random activity.",
        usage=f"{prefix}activity",
    )
    async def activity(self, ctx):
        await ctx.message.delete()
        activity = requests.get("https://www.boredapi.com/api/activity").json()
        if send_embeds:
            embed = discord.Embed(
                color=embed_color, title="Activity", description=activity["activity"]
            )
            embed.add_field(
                name="Accessibility",
                value=f"{round((1 - activity['accessibility']) * 10)}/10",
            )
            embed.add_field(name="Type", value=activity["type"].capitalize())
            if activity["link"]:
                embed.add_field(name="Link", value=f"[Click Here]({activity['link']})")
            embed.set_footer(icon_url=footer_url, text=footer_text)
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            content = f"\nActivity\n{activity['activity']}\nAccessibility: {activity['accessibility'] * 10}/10\nType: {activity['type'].capitalize()}"
            if activity["link"]:
                content += f"Link: {activity['link']}"

            await ctx.send(f"```{content}```")

    @command(
        name="calculate",
        aliases=get_aliases("calculate"),
        description="Make mathematical calculations.",
        usage=f"{prefix}calculate <equation>",
    )
    async def calculate(self, ctx, *, equation):
        await ctx.message.delete()
        equation = equation.replace(' ', '')
        result = SolveMathProblem(equation)
        if result.is_integer():
            result = round(result)
        await ctx.send(result)
        print(f'{equation} = {result}')

    @command(
        name="sqrt",
        aliases=get_aliases("sqrt"),
        description="Get the square root of a number.",
        usage=f"{prefix}sqrt <number>",
    )
    async def sqrt(self, ctx, num: int):
        await ctx.message.delete()
        try:
            await ctx.send(math.sqrt(num))
        except BaseException:
            printer(f"Syntax Error: Command usage({ctx.command.usage})")

    @command(
        name="unread",
        aliases=get_aliases("unread"),
        description="Set the amount of unreads for the current channel.",
        usage=f"{prefix}unread <amount>",
    )
    async def unread(self, ctx, amount: int = 1):
        await ctx.message.delete()
        payload = {"manual": True, "mention_count": amount}
        headers = {
            "authorization": token,
            "content-type": "application/json",
            "accept": "*/*",
        }
        last_message = await ctx.channel.history(limit=1).flatten()
        response = requests.post(
            f"https://discord.com/api/v8/channels/{ctx.channel.id}/messages/{last_message[0].id}/ack",
            data=json.dumps(payload),
            headers=headers,
        )

    @command(
        name="imitate",
        aliases=get_aliases("imitate"),
        description="Repeat after everything a user says.",
        usage=f"{prefix}imitate <user>",
    )
    async def imitate(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        if user:
            if user in imitating:
                imitating.remove(user)
                print(f"Finished imitating {user}")
            else:
                imitating.append(user)
                print(f"Started imitating {user}")
        else:
            if imitating:
                print("Cleared imitating list.")
                imitating.clear()
            else:
                printer("Missing user argument.")

    @Cog.listener("on_message")
    async def _imitating(self, ctx):
        if ctx.author in imitating:
            await ctx.channel.send(ctx.content)

    @command(
        "poll",
        aliases=get_aliases("poll"),
        description="Make a poll for members to vote.",
        usage=f"{prefix}poll <question>|<option1>|<option2>|<etc>",
    )
    async def poll(self, ctx, *, pollcontent):
        await ctx.message.delete()
        if pollcontent:
            emojis = [
                "1️⃣",
                "2️⃣",
                "3️⃣",
                "4️⃣",
                "5️⃣",
                "6️⃣",
                "7️⃣",
                "8️⃣",
                "9️⃣",
                "🔟",
            ]
            emoji_num = 0
            num = 1
            options = []
            poll = pollcontent.split("|")
            poll_question = poll.pop(0)
            poll_options = poll
            if len(poll_options) <= 10:
                if not len(poll_options) < 2:
                    if send_embeds:
                        for option1 in poll_options:
                            options.append(f"{emojis[emoji_num]} - {option1}\n")
                            emoji_num += 1
                    else:
                        for option1 in poll_options:
                            options.append(f"{num}. {option1}\n")
                            num += 1
                    options_text = "".join(options)
                    emoji_num1 = 0
                    embed = discord.Embed(color=embed_color)
                    embed.title = f"{poll_question}"
                    embed.description = f"{options_text}"
                    embed.set_footer(text=footer_text, icon_url=footer_url)
                    if send_embeds:
                        msg = await ctx.send(embed=embed, delete_after=delete_after)
                    else:
                        msg = await ctx.send(
                            f"**__{poll_question}__**\n\n```{options_text}```"
                        )
                    for _ in poll_options:
                        await msg.add_reaction(emojis[emoji_num1])
                        emoji_num1 += 1
                    print(f"Sent a poll asking {poll_question}")
                else:
                    printer("Input more than one option.")
            else:
                printer("Maximum amount of options is 10.")
        else:
            printer(f"Syntax Error: Command usage({ctx.command.usage}")

    @command(
        name="react",
        aliases=get_aliases("react"),
        description="Reacts to the previous message with text.",
        usage=f"{prefix}react <text>",
    )
    async def react(self, ctx, *, text):
        await ctx.message.delete()
        last_message = await ctx.channel.history(limit=1).flatten()
        reactions = replace_letters(text.lower())
        for emoji in reactions:
            try:
                await last_message[0].add_reaction(emoji)
            except BaseException:
                pass

    @command(
        name="meme",
        aliases=get_aliases("meme"),
        description="Send a random meme.",
        usage=f"{prefix}meme",
    )
    async def meme(self, ctx):
        subreddits = ["memes", "dankmemes"]
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit=random.choice(subreddits)))

    @command(
        name="minesweeper",
        aliases=get_aliases("minesweeper"),
        description="Play minesweeper on discord.",
        usage=f"{prefix}minesweeper",
    )
    async def minesweeper(self, ctx, bomb=None):
        await ctx.message.delete()
        columns = 9
        rows = 9
        if not bomb:
            bombs = 15
        grid = [[0 for num in range(columns)] for num in range(rows)]
        loop_count = 0
        while loop_count < bombs:
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)
            if grid[y][x] == 0:
                grid[y][x] = "B"
                loop_count = loop_count + 1
            if grid[y][x] == "B":
                pass
        pos_x = 0
        pos_y = 0
        while pos_x * pos_y < columns * rows and pos_y < rows:
            adj_sum = 0
            for (adj_y, adj_x) in [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),
            ]:
                try:
                    if (
                            grid[adj_y + pos_y][adj_x + pos_x] == "B"
                            and adj_y + pos_y > -1
                            and adj_x + pos_x > -1
                    ):
                        adj_sum = adj_sum + 1
                except Exception as error:
                    pass
            if grid[pos_y][pos_x] != "B":
                grid[pos_y][pos_x] = adj_sum
            if pos_x == columns - 1:
                pos_x = 0
                pos_y = pos_y + 1
            else:
                pos_x = pos_x + 1
        string_builder = []
        for the_rows in grid:
            string_builder.append("".join(map(str, the_rows)))
        string_builder = "\n".join(string_builder)
        string_builder = string_builder.replace("0", "||:blue_square:||")
        string_builder = string_builder.replace("1", "||:one:||")
        string_builder = string_builder.replace("2", "||:two:||")
        string_builder = string_builder.replace("3", "||:three:||")
        string_builder = string_builder.replace("4", "||:four:||")
        string_builder = string_builder.replace("5", "||:five:||")
        string_builder = string_builder.replace("6", "||:six:||")
        string_builder = string_builder.replace("7", "||:seven:||")
        string_builder = string_builder.replace("8", "||:eight:||")
        final = string_builder.replace("B", "||:boom:||")
        await ctx.send(content=f"\U0000FEFF\n{final}")


class Imagecog(commands.Cog):
    @command(
        name="image",
        aliases=get_aliases("image"),
        description="Display Image Commands.",
        usage=f"{prefix}image",
    )
    async def image_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Image Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Image Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="cat",
        aliases=get_aliases("cat"),
        description="Send a random cat image",
        usage=f"{prefix}cat",
    )
    async def cat(self, ctx):
        await ctx.message.delete()
        url = "https://api.thecatapi.com/v1/images/search"
        image = requests.get(url).json()
        cat = image[0]["url"]
        await ctx.send(cat)

    @command(
        name="dog",
        aliases=get_aliases("dog"),
        description="Send a random dog image",
        usage=f"{prefix}dog",
    )
    async def dog(self, ctx):
        await ctx.message.delete()
        url = "https://dog.ceo/api/breeds/image/random"
        image = requests.get(url).json()
        dog = image["message"]
        await ctx.send(dog)

    @command(
        name="invert",
        aliases=get_aliases("invert"),
        description="Invert an image or avatar.",
        usage=f"{prefix}george <user/attachment>",
    )
    async def invert(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = ImageOps.invert(pfp.convert("RGB"))
        img.save(f"{documents}/assets/images/invert.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/invert.png"))
        os.remove(f"{documents}/assets/images/invert.png")

    @command(
        name="flip",
        aliases=get_aliases("flip"),
        description="Vertically flip image or avatar.",
        usage=f"{prefix}flip <user/attachment>",
    )
    async def flip(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = ImageOps.flip(pfp)
        img.save(f"{documents}/assets/images/flip.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/flip.png"))
        os.remove(f"{documents}/assets/images/flip.png")

    @command(
        name="mirror",
        aliases=get_aliases("mirror"),
        description="Horizontally mirror image or avatar.",
        usage=f"{prefix}mirror <user/attachment>",
    )
    async def mirror(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = ImageOps.mirror(pfp)
        img.save(f"{documents}/assets/images/mirror.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/mirror.png"))
        os.remove(f"{documents}/assets/images/mirror.png")

    @command(
        name="equalize",
        aliases=get_aliases("equalize"),
        description="Equalize image or avatar.",
        usage=f"{prefix}equalize <user/attachment>",
    )
    async def equalize(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = ImageOps.equalize(pfp.convert("RGB"))
        img.save(f"{documents}/assets/images/equalize.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/equalize.png"))
        os.remove(f"{documents}/assets/images/equalize.png")

    @command(
        name="blur",
        aliases=get_aliases("blur"),
        description="Blur an image or avatar.",
        usage=f"{prefix}blur <user/attachment>",
    )
    async def blur(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = pfp.filter(ImageFilter.BLUR)
        img.save(f"{documents}/assets/images/blur.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/blur.png"))
        os.remove(f"{documents}/assets/images/blur.png")

    @command(
        name="edges",
        aliases=get_aliases("edges"),
        description="Find edges of an image or avatar.",
        usage=f"{prefix}edges <user/attachment>",
    )
    async def edges(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = pfp.convert("RGB").filter(ImageFilter.FIND_EDGES)
        img.save(f"{documents}/assets/images/edges.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/edges.png"))
        os.remove(f"{documents}/assets/images/edges.png")

    @command(
        name="george",
        aliases=get_aliases("george"),
        description="Send an avatar as george floyd.",
        usage=f"{prefix}george <user/attachment>",
    )
    async def george(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = Image.open(f"{documents}/assets/images/george.png")
        pfp = pfp.resize((125, 125))
        img.paste(pfp, (43, 11))
        img.save(f"{documents}/assets/images/george1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/george1.png"))
        os.remove(f"{documents}/assets/images/george1.png")

    @command(
        name="delete",
        aliases=get_aliases("delete"),
        description="Delete a user.",
        usage=f"{prefix}delete <user/attachment>",
    )
    async def delete(self, ctx, image="author"):
        img = Image.open(f"{documents}/assets/images/delete.png")
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        pfp = pfp.resize((195, 195))
        img.paste(pfp, (118, 134))
        img.save(f"{documents}/assets/images/delete1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/delete1.png"))
        os.remove(f"{documents}/assets/images/delete1.png")

    @command(
        name="trash",
        aliases=get_aliases("trash"),
        description="Show people what they are.",
        usage=f"{prefix}trash <user/attachment>",
    )
    async def trash(self, ctx, image="author"):
        img = Image.open(f"{documents}/assets/images/trash.png")
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        pfp = pfp.resize((480, 480))
        pfp = pfp.convert(mode="RGB")
        pfp = pfp.filter(ImageFilter.BoxBlur(10))
        img.paste(pfp, (480, 0))
        img.save(f"{documents}/assets/images/trash1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/trash1.png"))
        os.remove(f"{documents}/assets/images/trash1.png")

    @command(
        name="disability",
        aliases=get_aliases("disability"),
        description="Display what a disability looks like.",
        usage=f"{prefix}disability <user/attachment>",
    )
    async def disability(self, ctx, image="author"):
        img = Image.open(f"{documents}/assets/images/disability.png")
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        pfp = pfp.resize((175, 175))
        img.paste(pfp, (450, 325))
        img.save(f"{documents}/assets/images/disability1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/disability1.png"))
        os.remove(f"{documents}/assets/images/disability1.png")

    @command(
        name="quote",
        aliases=get_aliases("quote"),
        description="Quote a user saying anything.",
        usage=f"{prefix}quote <user> <text>",
    )
    async def quote(self, ctx, user: discord.User, *, text):
        await ctx.message.delete()
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        avatar = Image.open(data)
        avatar = avatar.resize((128, 128))
        base = Image.new("RGBA", (1500, 300))
        font_med = ImageFont.truetype(f"{documents}/assets/fonts/medium.woff", size=60)
        font_time = ImageFont.truetype(f"{documents}/assets/fonts/medium.woff", size=40)
        font_sb = ImageFont.truetype(f"{documents}/assets/fonts/semibold.woff", size=55)
        poly = Image.new("RGBA", avatar.size)
        pdraw = ImageDraw.Draw(poly)
        pdraw.ellipse([(0, 0), *avatar.size], fill=(255, 255, 255, 255))
        if poly.mode == "RGBA":
            r, g, b, a = poly.split()
            rgb_image = Image.merge("RGB", (r, g, b))
            inverted = ImageOps.invert(rgb_image)
            r, g, b = inverted.split()
            iv = Image.merge("RGBA", (r, g, b, a))
        else:
            iv = ImageOps.invert(poly)
        base.paste(avatar, (15, 75), mask=iv)
        words = Image.new("RGBA", base.size)
        canvas = ImageDraw.Draw(words)
        render_text_with_emoji(
            base, canvas, (230, 70), user.name, font=font_med, fill="White"
        )
        render_text_with_emoji(
            base, canvas, (230, 150), text, font=font_sb, fill=(160, 160, 160)
        )
        timestamp_left = 230 + canvas.textsize(user.name, font=font_med)[0] + 20
        render_text_with_emoji(
            base,
            canvas,
            (timestamp_left, 90),
            "Today at {}".format(datetime.datetime.utcnow().strftime("%H:%M")),
            font=font_time,
            fill=(125, 125, 125),
        )
        final = Image.alpha_composite(base, words)
        downscaled = final.resize((500, 100), Image.ANTIALIAS)
        downscaled = downscaled.convert("RGBA")
        downscaled.save(f"{documents}/assets/images/quote1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/quote1.png"))
        os.remove(f"{documents}/assets/images/quote1.png")

    @command(
        name="sickban",
        aliases=get_aliases("sickban"),
        description="Ban this nerd.",
        usage=f"{prefix}sickban <user/attachment>",
    )
    async def sickban(self, ctx, image="author"):
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        img = Image.open(f"{documents}/assets/images/sickban.png")
        pfp = pfp.resize((400, 400))
        img.paste(pfp, (70, 344))
        img.save(f"{documents}/assets/images/sickban1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/sickban1.png"))
        os.remove(f"{documents}/assets/images/sickban1.png")

    @command(
        name="ugly",
        aliases=get_aliases("ugly"),
        description="Damn this guy ugly.",
        usage=f"{prefix}ugly <user/attachment>",
    )
    async def ugly(self, ctx, image="author"):
        img = Image.open(f"{documents}/assets/images/ugly.png")
        pfp = await arg_parser(ctx, image)
        await ctx.message.delete()
        pfp = pfp.resize((176, 176))
        img.paste(pfp, (120, 55))
        img.save(f"{documents}/assets/images/ugly1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/ugly1.png"))
        os.remove(f"{documents}/assets/images/ugly1.png")

    @command(
        name="youtube",
        aliases=get_aliases("youtube"),
        description="Send a fake youtube comment",
        usage=f"{prefix}youtube <user> <text>",
    )
    async def youtube(self, ctx, user: discord.User, *, text):
        await ctx.message.delete()
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        avatar = Image.open(data).resize((52, 52)).convert("RGBA")
        name = user.name
        base = Image.open(f"{documents}/assets/images/youtube.png").convert("RGBA")
        font = ImageFont.truetype(
            f"{documents}/assets/fonts/robotomedium.ttf",
            size=17,
        )
        font2 = ImageFont.truetype(
            f"{documents}/assets/fonts/robotoregular.ttf",
            size=17,
        )
        font3 = ImageFont.truetype(
            f"{documents}/assets/fonts/robotoregular.ttf",
            size=19,
        )
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new("L", bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)
        base.paste(avatar, (17, 33), avatar)
        canv = ImageDraw.Draw(base)
        op = wrap(font, name, 1150)
        size = canv.textsize(name, font=font)
        comment = wrap(font3, text, 550)
        num = randint(1, 59)
        plural = "" if num == 1 else "s"
        time = f"{num} minute{plural} ago"
        render_text_with_emoji(base, canv, (92, 34), op, font=font, fill="Black")
        render_text_with_emoji(
            base, canv, (100 + size[0], 34), time, font=font2, fill="Grey"
        )
        render_text_with_emoji(base, canv, (92, 59), comment, font=font3, fill="Black")
        base = base.convert("RGBA")
        base.save(f"{documents}/assets/images/youtube1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/youtube1.png"))
        os.remove(f"{documents}/assets/images/youtube1.png")

    @command(
        name="magik",
        aliases=get_aliases("magik"),
        description="Distort an image.",
        usage=f"{prefix}magik <image> <intensity>",
    )
    async def magik(self, ctx, image="author", intensity=1):
        image = await arg_parser(ctx, image, returnurl=True)
        url = f"https://nekobot.xyz/api/imagegen?type=magik&image={image.replace('.webp', '.png')}&intensity={intensity}"
        magik = requests.get(url).json()["message"]
        r = requests.get(magik, allow_redirects=True)
        open("magik1.png", "wb").write(r.content)
        await ctx.send(file=discord.File("magik1.png"))
        await ctx.message.delete()
        os.remove("magik1.png")

    @command(
        name="deepfry",
        aliases=get_aliases("deepfry"),
        description="Deepfry an image.",
        usage=f"{prefix}deepfry <user/attachment>",
    )
    async def deepfry(self, ctx, image="author"):
        avatar = await arg_parser(ctx, image)
        await ctx.message.delete()

        def modify_all_pixels(im, noise_gen):
            width, height = im.size
            pxls = im.load()
            for x in range(width):
                for y in range(height):
                    pxls[x, y] = noise_gen(x, y, *pxls[x, y])

        def add_noise(image, strength=100):
            def pixel_noise(x, y, r, g, b):
                noise = int(random.randint(0, strength) - strength / 2)
                return (
                    max(0, min(r + noise, 255)),
                    max(0, min(g + noise, 255)),
                    max(0, min(b + noise, 255)),
                )

            modify_all_pixels(image, pixel_noise)
            return image

        noise = avatar.convert("RGB")
        noise = add_noise(noise, 25)
        noise = ImageEnhance.Contrast(noise).enhance(20)
        noise = ImageEnhance.Sharpness(noise).enhance(20)
        noise = ImageEnhance.Color(noise).enhance(15)
        noise.save(f"{documents}/assets/images/deepfry1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/deepfry1.png"))
        os.remove(f"{documents}/assets/images/deepfry1.png")

    @command(
        name="qr",
        aliases=get_aliases("qrcode"),
        description="Generate a qr code with custom data.",
        usage=f"{prefix}qr <data>",
    )
    async def qr(self, ctx, *, data):
        await ctx.message.delete()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=0,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="transparent")
        img.save(f"{documents}/assets/images/qr.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/qr.png"))
        os.remove(f"{documents}/assets/images/qr.png")

    @command(
        name="tweet",
        aliases=get_aliases("tweet"),
        description="Make a fake tweet.",
        usage=f"{prefix}tweet <user> <text>",
    )
    async def tweet(self, ctx, user: discord.User, *, text):
        base = Image.open(f"{documents}/assets/images/trump.png")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        avatar = Image.open(data).resize((98, 98)).convert("RGBA")
        await ctx.message.delete()
        name = user.name
        font = ImageFont.truetype(
            f"{documents}/assets/fonts/segoeuireg.ttf",
            size=50,
        )
        font2 = ImageFont.truetype(
            f"{documents}/assets/fonts/robotomedium.ttf", size=40
        )
        font3 = ImageFont.truetype(
            f"{documents}/assets/fonts/robotoregular.ttf", size=29
        )
        font4 = ImageFont.truetype(
            f"{documents}/assets/fonts/robotoregular.ttf", size=35
        )
        circle = Image.new("L", (20, 20), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, 20, 20), fill=255)
        alpha = Image.new("L", avatar.size, 255)
        w, h = avatar.size
        alpha.paste(circle.crop((0, 0, 10, 10)), (0, 0))
        alpha.paste(circle.crop((0, 10, 10, 10 * 2)), (0, h - 10))
        alpha.paste(circle.crop((10, 0, 10 * 2, 10)), (w - 10, 0))
        alpha.paste(circle.crop((10, 10, 10 * 2, 10 * 2)), (w - 10, h - 10))
        avatar.putalpha(alpha)
        base.paste(avatar, (42, 38), avatar)
        canv = ImageDraw.Draw(base)
        text2 = wrap(font2, name, 1150)
        tag_raw = name
        text3 = wrap(font3, f"@{tag_raw}", 1150)
        now = datetime.datetime.now()
        time = f"{now:%H:%M} {now:%p} - {now:%d} {now:%b} {now:%Y}"
        retweets = "{:,}".format(randint(0, 99999))
        likes = "{:,}".format(randint(0, 99999))
        text4 = wrap(font3, time, 1150)
        text5 = wrap(font4, retweets, 1150)
        text6 = wrap(font4, likes, 1150)
        total_size = (45, 160)
        for i in text.split(" "):
            i += " "
            if i.startswith(("@", "#")):
                if total_size[0] > 1000:
                    total_size = (45, total_size[1] + 65)
                render_text_with_emoji(
                    base, canv, total_size, i, font=font, fill="#1b95e0"
                )
                y = canv.textsize(i, font=font)
                total_size = (total_size[0] + y[0], total_size[1])
            else:
                if total_size[0] > 1000:
                    total_size = (45, total_size[1] + 65)
                render_text_with_emoji(
                    base, canv, total_size, i, font=font, fill="Black"
                )
                y = canv.textsize(i, font=font)
                total_size = (total_size[0] + y[0], total_size[1])
        render_text_with_emoji(base, canv, (160, 45), text2, font=font2, fill="Black")
        render_text_with_emoji(base, canv, (160, 95), text3, font=font3, fill="Grey")
        render_text_with_emoji(base, canv, (40, 570), text4, font=font3, fill="Grey")
        render_text_with_emoji(base, canv, (40, 486), text5, font=font4, fill="#2C5F63")
        render_text_with_emoji(
            base, canv, (205, 486), text6, font=font4, fill="#2C5F63"
        )
        base.save(f"{documents}/assets/images/trump1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/trump1.png"))
        os.remove(f"{documents}/assets/images/trump1.png")

    @command(
        name="facts",
        aliases=get_aliases("facts"),
        description="Straight facts.",
        usage=f"{prefix}facts <text>",
    )
    async def facts(self, ctx, *, text):
        if text:
            base = Image.open(f"{documents}/assets/images/facts.png")
            text_layer = Image.new("RGBA", base.size)
            font = ImageFont.truetype(f"{documents}/assets/fonts/verdana.ttf", size=25)
            canv = ImageDraw.Draw(text_layer)
            text = wrap(font, text, 400)
            await ctx.message.delete()
            render_text_with_emoji(
                text_layer, canv, (90, 600), text, font=font, fill="Black"
            )
            text_layer = text_layer.rotate(-13, resample=Image.BICUBIC)
            base.paste(text_layer, (0, 0), text_layer)
            base.save(f"{documents}/assets/images/facts1.png")
            await ctx.send(file=discord.File(f"{documents}/assets/images/facts1.png"))
            os.remove(f"{documents}/assets/images/facts1.png")

    @command(
        name="affect",
        aliases=get_aliases("affect"),
        description="This surely has no affect.",
        usage=f"{prefix}affect <user/attachment>",
    )
    async def affect(self, ctx, image="author"):
        avatar = await arg_parser(ctx, image)
        avatar = avatar.resize((200, 157)).convert("RGBA")
        await ctx.message.delete()
        base = Image.open(f"{documents}/assets/images/affect.png").convert("RGBA")
        base.paste(avatar, (180, 383, 380, 540), avatar)
        base = base.convert("RGB")
        base.save(f"{documents}/assets/images/affect1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/affect1.png"))
        os.remove(f"{documents}/assets/images/affect1.png")

    @command(
        name="fedora",
        aliases=get_aliases("fedora"),
        description="Tips fedora.",
        usage=f"{prefix}fedora <user/attachment>",
    )
    async def fedora(self, ctx, image="author"):
        avatar = await arg_parser(ctx, image)
        avatar = avatar.resize((275, 275)).convert("RGBA")
        await ctx.message.delete()
        base = Image.open(f"{documents}/assets/images/fedora.png").convert("RGBA")
        final_image = Image.new("RGBA", base.size)
        final_image.paste(avatar, (112, 101), avatar)
        final_image.paste(base, (0, 0), base)
        final_image.save(f"{documents}/assets/images/fedora1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/fedora1.png"))
        os.remove(f"{documents}/assets/images/fedora1.png")

    @command(
        name="hitler",
        aliases=get_aliases("hitler"),
        description="This man is worse than hitler.",
        usage=f"{prefix}hitler <user/attachment>",
    )
    async def hitler(self, ctx, image="author"):
        avatar = await arg_parser(ctx, image)
        avatar = avatar.convert("RGBA").resize((140, 140))
        await ctx.message.delete()
        base = Image.open(f"{documents}/assets/images/hitler.png")
        base.paste(avatar, (46, 43), avatar)
        base = base.convert("RGB")
        base.save(f"{documents}/assets/images/hitler1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/hitler1.png"))
        os.remove(f"{documents}/assets/images/hitler1.png")

    @command(
        name="gay",
        aliases=get_aliases("gay"),
        description="This dude kinda gay.",
        usage=f"{prefix}gay <user/attachment>",
    )
    async def gay(self, ctx, image="author"):
        avatar = await arg_parser(ctx, image)
        avatar = avatar.convert("RGBA")
        await ctx.message.delete()
        img2 = (
            Image.open(f"{documents}/assets/images/gay.png")
                .convert("RGBA")
                .resize(avatar.size)
        )
        img2.putalpha(128)
        avatar.paste(img2, (0, 0), img2)
        avatar = avatar.convert("RGB")
        avatar.save(f"{documents}/assets/images/gay1.png")
        await ctx.send(file=discord.File(f"{documents}/assets/images/gay1.png"))
        os.remove(f"{documents}/assets/images/gay1.png")


class Infocog(commands.Cog):
    @command(
        name="info",
        aliases=get_aliases("info"),
        description="Display Info Commands.",
        usage=f"{prefix}info",
    )
    async def info_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Info Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Info Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="uptime",
        aliases=get_aliases("uptime"),
        description="Displays the bots uptime duration.",
        usage=f"{prefix}uptime",
    )
    async def uptime(self, ctx):
        await ctx.message.delete()
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=embed_color)
        embed.add_field(name="Uptime:", value=text)
        embed.set_footer(text=footer_text, icon_url=footer_url)
        if send_embeds:
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            await ctx.send("Current uptime: " + text)

    @command(
        name="ping",
        aliases=get_aliases("ping"),
        description="Displays the bots delay.",
        usage=f"{prefix}ping",
    )
    async def ping(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color)
        embed.description = f"**Ping:** `{round(client.latency * 1000)}\n`"
        embed.set_footer(text=footer_text, icon_url=footer_url)
        await ctx.send(embed=embed, delete_after=delete_after)

    @command(
        name="botinfo",
        aliases=get_aliases("botinfo"),
        description="Displays information on Desyncer.",
        usage=f"{prefix}botinfo",
    )
    async def botinfo(self, ctx):
        await ctx.message.delete()
        if send_embeds:
            embed = discord.Embed(color=embed_color)
            embed.title = "Desyncer Bot Info\n\n"
            embed.set_thumbnail(url=footer_url)
            embed.add_field(name="Developer", value="`Systematic`", inline=False)
            embed.add_field(name="Language", value="`Python`", inline=False)
            embed.add_field(name="Version", value=f"`{desyncer_version}`", inline=False)
            embed.description = f"[**Website**](https://systematic.wtf)\n\n[**Discord**](https://discord.gg/TByqPXND4u)\n\n"
            embed.set_footer(text=footer_text, icon_url=footer_url)
            embed.add_field(
                name="Commands",
                value=f"`{len([command for command in client.commands])}`",
            )
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            await ctx.send(
                f"```Desyncer Bot Info\n\n+ Website: https://systematic.wtf\n+ Discord: https://discord.gg/TByqPXND4u\n+ Developer: Systematic\n+ Language: Python\n+ Commands: {len([command for command in client.commands])}\n+ Version: {desyncer_version}```"
            )

    @command(
        name="clear",
        aliases=get_aliases("clear"),
        description="Reset the console",
        usage=f"{prefix}clear",
    )
    async def clear(self, ctx):
        await ctx.message.delete()
        welcome_message()


class NSFWcog(commands.Cog):
    @command(
        name="nsfw",
        aliases=get_aliases("nsfw"),
        description="Display NSFW Commands.",
        usage=f"{prefix}nsfw",
    )
    async def nsfw_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"NSFW Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```NSFW Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="rule34",
        aliases=get_aliases("rule34"),
        description="Search for images on rule34.",
        usage=f"{prefix}rule34 <tags>",
    )
    async def rule35(self, ctx, *, search):
        await ctx.message.delete()

        url = "https://r34-json-api.herokuapp.com/posts"
        querystring = {"tags": search.replace(' ', '_').replace(', ', '+').replace(',', '+')}
        response = requests.get(url, params=querystring).json()
        if len(response) == 0:
            print(f"No Rule34 results for '{search}'.")
        else:
            url = random.choice(response)["file_url"][46:]
            filename = f"{documents}/assets/{url.split('/')[-1]}"
            r = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(r.content)
            await ctx.send(file=discord.File(filename))
            os.remove(filename)

    @command(
        name="butt",
        aliases=get_aliases("butt"),
        description="Send a random butt image.",
        usage=f"{prefix}butt",
    )
    async def butt(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="butts"))

    @command(
        name="boobs",
        aliases=get_aliases("boobs"),
        description="Send a random boob image.",
        usage=f"{prefix}boobs",
    )
    async def boobs(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="boobs"))

    @command(
        name="pussy",
        aliases=get_aliases("pussy"),
        description="Send a random pussy image.",
        usage=f"{prefix}pussy",
    )
    async def pussy(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="pussy"))

    @command(
        name="anal",
        aliases=get_aliases("anal"),
        description="Send a random anal image.",
        usage=f"{prefix}anal",
    )
    async def anal(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="anal"))

    @command(
        name="hentai",
        aliases=get_aliases("hentai"),
        description="Send a random hentai image.",
        usage=f"{prefix}hentai",
    )
    async def hentai(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="hentai"))

    @command(
        name="feet",
        aliases=get_aliases("feet"),
        description="Send a random foot image.",
        usage=f"{prefix}feet",
    )
    async def feet(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="feet"))

    @command(
        name="dick",
        aliases=get_aliases("dick"),
        description="Send a random dickpic.",
        usage=f"{prefix}dick",
    )
    async def dick(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="penis"))

    @command(
        name="yiff",
        aliases=get_aliases("yiff"),
        description="Send a random yiff image.",
        usage=f"{prefix}yiff",
    )
    async def yiff(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="yiff"))

    @command(
        name="milf",
        aliases=get_aliases("milf"),
        description="Send a random milf image.",
        usage=f"{prefix}milf",
    )
    async def milf(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="milf"))

    @command(
        name="futa",
        aliases=get_aliases("futa"),
        description="Send a random futa image.",
        usage=f"{prefix}futa",
    )
    async def futa(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="futanari"))

    @command(
        name="trap",
        aliases=get_aliases("trap"),
        description="Send a random trap image.",
        usage=f"{prefix}trap",
    )
    async def trap(self, ctx):
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit="traps"))

    @command(
        name="ahegao",
        aliases=get_aliases("ahegao"),
        description="Send a random ahegao image.",
        usage=f"{prefix}ahegao",
    )
    async def ahegao(self, ctx):
        subreddits = ["ahegao", "RealAhegao"]
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit=random.choice(subreddits)))

    @command(
        name="cosplay",
        aliases=get_aliases("cosplay"),
        description="Send a random cosplay image.",
        usage=f"{prefix}cosplay",
    )
    async def cosplay(self, ctx):
        subreddits = ["nsfwcosplay", "cosplaygirls", "NSFWCostumes", "CosplayLewd"]
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit=random.choice(subreddits)))

    @command(
        name="tentacles",
        aliases=get_aliases("tentacles"),
        description="Send a random tentacle porn image.",
        usage=f"{prefix}tentacles",
    )
    async def tentacles(self, ctx):
        subreddits = ["Tentai", "consentacles", "Allthewaythrough"]
        await ctx.message.delete()
        await ctx.send(reddit_img(ctx=ctx, subreddit=random.choice(subreddits)))

    @command(
        name="source",
        aliases=get_aliases("source"),
        description="Gets the source of image.",
        usage=f"{prefix}source <url>",
    )
    async def source(self, ctx, *, url):
        await ctx.message.delete()
        sauce_nao = "http://saucenao.com/search.php?db=999&url="
        request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
        }
        try:
            req = requests.get(sauce_nao + url, headers=request_headers).text
        except BaseException:
            printer("You are being rate limited.")
        codeblock = "Source Information\n"
        soup = BeautifulSoup(req, "html.parser")
        pretty_soup = soup.prettify()
        em = discord.Embed(color=embed_color, title="Source Lookup")
        try:
            em.set_thumbnail(url=url)
        except BaseException:
            pass
        match = re.findall(
            r'(?s)linkify" href="(.*?)"', str(soup.find("div", id="middle"))
        )
        title = re.findall(
            r'(?s)<div class="resulttitle">(.*?)</td',
            str(soup.find("div", id="middle")),
        )
        similarity_percent = re.findall(
            r'(?s)<div class="resultsimilarityinfo">(.*?)<',
            str(soup.find("div", id="middle")),
        )
        ti = ""
        if title and float(similarity_percent[0][:-1]) > 50.0:
            title = (
                title[0]
                    .strip()
                    .replace("<br/>", "\n")
                    .replace("<strong>", "")
                    .replace("</strong>", "")
                    .replace('<div class="resultcontentcolumn">', "")
                    .replace('<span class="subtext">', "\n")
                    .replace("<small>", "")
                    .replace("</span>", " ")
                    .replace("</small>", "")
                    .replace("</tr>", "")
                    .replace("</td>", "")
                    .replace("</table>", "")
                    .replace("</div>", "")
                    .split("\n")
            )
            ti = "\n".join([i.strip() for i in title if i.strip() != ""])
            if "</a>" not in ti:
                if send_embeds:
                    em.add_field(name="Source", value=ti)
                else:
                    codeblock += f"Source:\n{ti}\n"
            try:
                pretty_soup = pretty_soup.split('id="result-hidden-notification"', 1)[0]
            except BaseException:
                pass
            episode = re.findall(
                r'(?s)<span class="subtext">\n EP(.*?)<div', pretty_soup
            )
            ep = ""
            if episode:
                episode = (
                    episode[0]
                        .strip()
                        .replace("<br/>", "")
                        .replace("<strong>", "**")
                        .replace("</strong>", "**")
                        .replace('<span class="subtext">', "")
                        .replace("</span>", "")
                        .replace("</tr>", "")
                        .replace("</td>", "")
                        .replace("</table>", "")
                        .replace("</div>", "")
                        .split("\n")
                )
                ep = " ".join([j.strip() for j in episode if j.strip() != ""])
                ep = ep.replace("Est Time:", "\nEst Time:")
                em.add_field(name="More Info", value="**Episode** " + ep, inline=False)
            est_time = re.findall(r"(?s)Est Time:(.*?)<div", pretty_soup)
            if est_time and "Est Time:" not in ep:
                est_time = (
                    est_time[0]
                        .strip()
                        .replace("<br/>", "")
                        .replace("<strong>", "")
                        .replace("</strong>", "")
                        .replace('<span class="subtext">', "")
                        .replace("</span>", "")
                        .replace("</tr>", "")
                        .replace("</td>", "")
                        .replace("</table>", "")
                        .replace("</div>", "")
                        .split("\n")
                )
                est = " ".join([j.strip() for j in est_time if j.strip() != ""])
                est = est.replace("Est Time:", "\nEst Time:")
                em.add_field(
                    name="More Info", value="**Est Time:** " + est, inline=False
                )
        sources = ""
        count = 0
        source_sites = {
            "www.pixiv.net": "pixiv",
            "danbooru": "danbooru",
            "seiga.nicovideo": "nico nico seiga",
            "yande.re": "yande.re",
            "openings.moe": "openings.moe",
            "fakku.net": "fakku",
            "gelbooru": "gelbooru",
            "deviantart": "deviantart",
            "bcy.net": "bcy.net",
            "konachan.com": "konachan",
            "anime-pictures.net": "anime-pictures.net",
            "drawr.net": "drawr",
        }
        for i in match:
            if not i.__contains__("saucenao.com"):
                if float(similarity_percent[count][:-1]) > 50.0:
                    link_to_site = "{} - {}, ".format(i, similarity_percent[count])
                    for site in source_sites:
                        if site in i:
                            if send_embeds:
                                link_to_site = "[{}]({}) - {}, ".format(
                                    source_sites[site], i, similarity_percent[count]
                                )
                            else:
                                link_to_site = f"{similarity_percent[count]} - {i}\n"
                            break
                    sources += link_to_site
                    count += 1
            if count == 4:
                break
        if send_embeds:
            sources = sources.rstrip(", ")
        material = re.search(
            r"(?s)Material:(.*?)</div", str(soup.find("div", id="middle"))
        )
        if material and ("Materials:" not in ti and "Material:" not in ti):
            material_list = (
                material.group(1)
                    .strip()
                    .replace("<br/>", "\n")
                    .replace("<strong>", "")
                    .replace("</strong>", "")
                    .split("\n")
            )
            mat = ", ".join([i.strip() for i in material_list if i.strip() != ""])
            if send_embeds:
                em.add_field(name="Material", value=mat)
            else:
                codeblock += f"Material: {mat}\n"
        characters = re.search(
            r"(?s)Characters:(.*?)</div", str(soup.find("div", id="middle"))
        )
        if characters and ("Characters:" not in ti and "Character:" not in ti):
            characters_list = (
                characters.group(1)
                    .strip()
                    .replace("<br/>", "\n")
                    .replace("<strong>", "")
                    .replace("</strong>", "")
                    .split("\n")
            )
            chars = ", ".join([i.strip() for i in characters_list if i.strip() != ""])
            if send_embeds:
                em.add_field(name="Character", value=chars)
            else:
                codeblock += f"Characters: {chars}\n"
        creator = re.search(
            r"(?s)Creator:(.*?)</div", str(soup.find("div", id="middle"))
        )
        if creator and ("Creators:" not in ti and "Creator:" not in ti):
            creator_list = (
                creator.group(1)
                    .strip()
                    .replace("<br/>", "\n")
                    .replace("<strong>", "")
                    .replace("</strong>", "")
                    .split("\n")
            )
            creat = ", ".join([i.strip() for i in creator_list if i.strip() != ""])
            if send_embeds:
                em.add_field(name="Creator", value=creat)
            else:
                codeblock += f"Creator: {creat}\n"
        if sources != "" and sources:
            if send_embeds:
                em.add_field(
                    name="Source sites - percent similarity",
                    value=sources,
                    inline=False,
                )
            else:
                codeblock += f"\n{sources}"
        if (
                not sources
                and not creator
                and not characters
                and not material
                and not title
                or float(similarity_percent[0][:-1]) < 50.0
        ):
            if send_embeds:
                em = discord.Embed(color=embed_color, title="No results found")
            else:
                codeblock = "No results found"
        if send_embeds:
            em.set_footer(icon_url=footer_url, text=footer_text)
            await ctx.send(content=None, embed=em)
        else:
            await ctx.send(f"```{codeblock}```")


class Sniperscog(commands.Cog):
    @Cog.listener("on_message")
    async def sniper(self, ctx):
        if sniper_toggle:
            codeRegex = re.compile(
                "(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)"
            )
            start_time = time.time()
            if codeRegex.search(ctx.content):
                code = codeRegex.search(ctx.content).group(2)
                if len(code) < 16:
                    try:
                        print(
                            f"Detected a fake nitro code from {ctx.author} in {ctx.guild.name} {ctx.channel.name}"
                        )
                    except BaseException:
                        print(f"Detected a fake nitro code from {ctx.author}")
                else:
                    res = http.request(
                        "POST",
                        url="https://discordapp.com/api/v6/entitlements/gift-codes/"
                            + code
                            + "/redeem",
                        headers={
                            "authorization": snipe_token,
                            "user-agent": "Mozilla/5.0",
                        },
                    )
                    delay = time.time() - start_time
                    result = json.loads(res.data.decode("utf-8"))
                    try:
                        print(
                            f"Sniper - Sniping Code: {code} from {ctx.author} in {ctx.guild.name} - {ctx.channel.name}"
                        )
                    except BaseException:
                        print(f"Sniper - Sniping Code: {code} from {ctx.author}")
                    col = discord.Color.blue()
                    msg = ""
                    if "This gift has been redeemed already" in str(result["message"]):
                        print(f"Sniper - Code has been already redeemed")
                        msg = "Code has been already redeemed"
                        col = discord.Color.red()
                    elif "nitro" in str(result["message"]):
                        print(f"Sniper - Congratulations, Nitro Redeemed!.")
                        msg = "Congratulations, Nitro Redeemed!."
                        col = discord.Color.green()
                    elif "Unknown Gift Code" in str(result["message"]):
                        print("Sniper - Invalid code")
                        msg = "Invalid code"
                        col = discord.Color.red()
                    print("Sniper - Delay:" + " %.3fs" % delay)
                    if ctx.guild:
                        server_channel = f"{ctx.guild.name} - {ctx.channel.name}"
                    else:
                        server_channel = "DMs"
                    if sniper_notifications:
                        if msg == "Congratulations, Nitro Redeemed!.":
                            notifier.show_toast(
                                "Desyncer",
                                f"Nitro Sniper\nSniped Code {code}\n{msg}\nDelay: "
                                + "%.3fs" % delay,
                                duration=5,
                                icon_path=f"{documents}/assets/images/desyncer.ico",
                            )
                    if log_nitro_sniper:
                        embed = discord.Embed(color=col, timestamp=ctx.created_at)
                        embed.set_author(
                            name=msg,
                            icon_url="https://static.wikia.nocookie.net/discord/images/e/ea/Nitro.png/revision/latest/scale-to-width-down/150?cb=20210105222501",
                        )
                        embed.add_field(name="Code", value=code, inline=False)
                        if ctx.guild:
                            embed.add_field(
                                name="Server", value=ctx.guild.name, inline=False
                            )
                            embed.add_field(
                                name="Channel", value=ctx.channel.name, inline=False
                            )
                        embed.add_field(
                            name="Sender", value=ctx.author.name, inline=False
                        )
                        embed.add_field(
                            name="Delay", value=" %.3fs" % delay, inline=False
                        )
                        if webhook_logging and len(webhook_url) > 1:
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(
                                    webhook_url, adapter=AsyncWebhookAdapter(session)
                                )
                                await webhook.send(embed=embed, username="Nitro Sniper")
                        if file_logging:
                            if not os.path.exists(
                                    f"{documents}/logs/NitrosniperLog.txt"
                            ):
                                with open(
                                        f"{documents}/logs/NitrosniperLog.txt", "w"
                                ) as o:
                                    o.close()
                            with open(
                                    f"{documents}/logs/NitrosniperLog.txt",
                                    "a",
                                    encoding="utf-8",
                            ) as logfile:
                                logfile.write(
                                    f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Nitro Sniper - Sniping Code: {code} from {ctx.author} in {server_channel}, Result: {msg}\n '
                                )

    @Cog.listener("on_message")
    async def giveaway_joiner(self, ctx):
        if giveaway_toggle:
            if ctx.guild:
                if ctx.author.bot:
                    if 'ban' not in str(ctx.content).lower() or 'bot' not in str(
                            ctx.content).lower() or 'kick' not in str(ctx.content).lower():
                        if "**giveaway**" in str(ctx.content).lower() or (
                                "react with" in str(ctx.content).lower()
                                and "giveaway" in str(ctx.content).lower()
                        ):
                            col = discord.Color.blue()
                            msg = ""
                            try:
                                await asyncio.sleep(giveaway_cooldown)
                                await ctx.add_reaction("🎉")
                                print(
                                    f"Giveaway Joiner - Entered giveaway in {ctx.guild.name} - {ctx.channel.name}"
                                )
                                msg = f"Entered giveaway in {ctx.guild.name} - {ctx.channel.name}"
                                col = discord.Color.green()
                            except BaseException:
                                print(
                                    f"Giveaway Joiner - Failed to enter giveaway in {ctx.guild.name} - {ctx.channel.name}"
                                )
                                msg = f"Failed to enter giveaway in {ctx.guild.name} - {ctx.channel.name}"
                                col = discord.Color.red()
                            if giveaway_notifications:
                                notifier.show_toast(
                                    "Desyncer",
                                    f"Giveaway Joiner\n{msg}\n",
                                    duration=5,
                                    icon_path=f"{documents}/assets/images/desyncer.ico",
                                )
                            if log_giveaway_joiner:
                                embed = discord.Embed(color=col, timestamp=ctx.created_at)
                                embed.set_author(
                                    name=msg,
                                    icon_url="https://www.pinclipart.com/picdir/big/107-1079672_bing-christmas-clip-art-ndash-discord-tada-emoji.png",
                                )
                                embed.add_field(
                                    name="Server", value=ctx.guild.name, inline=False
                                )
                                embed.add_field(
                                    name="Channel", value=ctx.channel.name, inline=False
                                )
                                if webhook_logging and len(webhook_url) > 1:
                                    async with aiohttp.ClientSession() as session:
                                        webhook = Webhook.from_url(
                                            webhook_url,
                                            adapter=AsyncWebhookAdapter(session),
                                        )
                                        await webhook.send(
                                            embed=embed, username="Giveaway Joiner"
                                        )
                                if file_logging:
                                    if not os.path.exists(
                                            f"{documents}/logs/GiveawayjoinerLog.txt"
                                    ):
                                        with open(
                                                f"{documents}/logs/GiveawayjoinerLog.txt", "w"
                                        ) as o:
                                            o.close()
                                    with open(
                                            f"{documents}/logs/GiveawayjoinerLog.txt",
                                            "a",
                                            encoding="utf-8",
                                    ) as logfile:
                                        logfile.write(
                                            f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Giveaway Joiner - {msg}\n'
                                        )
                        elif "<@" + str(client.user.id) + ">" in ctx.content and (
                                "giveaway" in str(ctx.content).lower()
                                or "won" in ctx.content
                                or "winner" in str(ctx.content).lower()
                        ):
                            try:
                                won = re.search(
                                    r"You won the \*\*(.*)\*\*", ctx.content
                                ).group(1)
                            except BaseException:
                                won = "Unkown"
                            print(
                                f"Giveaway Joiner - Congratulations, You won the giveaway for {won} in {ctx.guild.name} - {ctx.channel.name}"
                            )
                            if giveaway_notifications:
                                notifier.show_toast(
                                    "Desyncer",
                                    f"Giveaway Joiner\nYou won a giveaway!\nWinnings: {won}",
                                    duration=5,
                                    icon_path=f"{documents}/assets/images/desyncer.ico",
                                )
                            if log_giveaway_joiner:
                                embed = discord.Embed(
                                    color=discord.Color.green, timestamp=ctx.created_at
                                )
                                embed.set_author(
                                    name=f"Congratulations!, You won a giveaway in {ctx.guild.name}",
                                    icon_url="https://www.pinclipart.com/picdir/big/107-1079672_bing-christmas-clip-art-ndash-discord-tada-emoji.png",
                                )
                                embed.add_field(name="Winnings", value=won, inline=False)
                                embed.description = "\n\nDM them to claim your winnings!"
                                if webhook_logging and len(webhook_url) > 1:
                                    async with aiohttp.ClientSession() as session:
                                        webhook = Webhook.from_url(
                                            webhook_url,
                                            adapter=AsyncWebhookAdapter(session),
                                        )
                                        await webhook.send(
                                            embed=embed, username="Giveaway Joiner"
                                        )
                                if file_logging:
                                    if not os.path.exists(
                                            f"{documents}/logs/GiveawayjoinerLog.txt"
                                    ):
                                        with open(
                                                f"{documents}/logs/GiveawayjoinerLog.txt", "w"
                                        ) as o:
                                            o.close()
                                    with open(
                                            f"{documents}/logs/GiveawayjoinerLog.txt",
                                            "a",
                                            encoding="utf-8",
                                    ) as logfile:
                                        logfile.write(
                                            f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Giveaway Joiner - Giveaway won in {ctx.guild.name} channel {ctx.channel.name}\n'
                                        )


class Textcog(commands.Cog):
    owoToggle = False

    @command(
        name="text",
        aliases=get_aliases("text"),
        description="Display Text Commands.",
        usage=f"{prefix}text",
    )
    async def text_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Text Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Text Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="replace",
        aliases=get_aliases("replace"),
        description="Auto-replace text with a chosen value.",
        usage=f"{prefix}replace <action> <word1>,<word2>",
        brief="Action types: add/remove/clear",
    )
    async def replace(self, ctx, action, *, msg):
        await ctx.message.delete()
        try:
            if "," in ctx.message.content:
                msg = msg.split(",")
                msg[0] = msg[0].replace("add ", "")
            if action == "add":
                if not path.exists(f"{documents}/files/replacements.json"):
                    with open(
                            f"{documents}/files/replacements.json", "w"
                    ) as replacements_write:
                        replace1 = {}
                        replace1["values"] = {msg[0]: msg[1]}
                        write_to_json = json.dumps(replace1)
                        replacements_write.write(write_to_json)
                else:
                    with open(
                            f"{documents}/files/replacements.json", "r"
                    ) as replacements_read:
                        replacements_r = replacements_read.read()
                        if len(replacements_r) > 1:
                            replacements = json.loads(replacements_r)
                            with open(
                                    f"{documents}/files/replacements.json", "w"
                            ) as replacements_w:
                                replacements["values"][msg[0]] = msg[1]
                                replacementsjson = json.dumps(replacements)
                                replacements_w.write(replacementsjson)
                        else:
                            with open(
                                    f"{documents}/files/replacements.json", "w"
                            ) as replacements_write:
                                replace1 = {}
                                replace1["values"] = {msg[0]: msg[1]}
                                write_to_json = json.dumps(replace1)
                                replacements_write.write(write_to_json)
                print(f"The word {msg[0]} will now be replaced by {msg[1]}")
            elif action == "remove":
                with open(
                        f"{documents}/files/replacements.json", "r"
                ) as replacements_read:
                    replacements_r = replacements_read.read()
                    replacements = json.loads(replacements_r)
                    replacements["values"].pop(msg)
                    replacementsjson = json.dumps(replacements)
                    with open(
                            f"{documents}/files/replacements.json", "w"
                    ) as replacements_w:
                        replacements_w.write(replacementsjson)
                        print(f"The word {msg[0]} will no longer replaced by {msg[1]}")
            elif action == "clear":
                with open(
                        f"{documents}/files/replacements.json", "w"
                ) as clear_replacements:
                    print("Cleared all replacements.")
            else:
                printer(
                    f"Syntax Error: Command usage({ctx.command.usage})\n{ctx.command.brief}"
                )
        except BaseException:
            printer(
                f"Syntax Error: Command usage({ctx.command.usage})\n{ctx.command.brief}"
            )

    @Cog.listener("on_message")
    async def replacing(self, ctx):
        if ctx.author == client.user:
            if not ctx.content.startswith(
                    f"{prefix}replace"
            ) and not ctx.content.startswith(f"{prefix}logkeyword"):
                if path.exists(f"{documents}/files/replacements.json"):
                    with open(
                            f"{documents}/files/replacements.json", "r"
                    ) as replacements_read:
                        replacements_r = replacements_read.read()
                        if replacements_r:
                            replacementsr = json.loads(replacements_r)
                            replacements = replacementsr["values"]
                            for key in replacements.keys():
                                value = replacements[key]
                                if key in ctx.content:
                                    msg = ctx.content.replace(key, value)
                                    await ctx.edit(content=msg)

    @command(
        name="fact",
        aliases=get_aliases("fact"),
        description="Sends a random fact.",
        usage=f"{prefix}fact",
    )
    async def fact(self, ctx):
        await ctx.message.delete()
        api = requests.get(
            "https://uselessfacts.jsph.pl/random.json?language=en"
        ).json()
        await ctx.send(api["text"])

    @command(
        name="insult",
        aliases=get_aliases("insult"),
        description="Send a random insult.",
        usage=f"{prefix}insult",
    )
    async def insult(self, ctx, user):
        await ctx.message.delete()
        insults = requests.get(
            "https://evilinsult.com/generate_insult.php?lang=en&type=json"
        ).json()
        await ctx.send(insults["insult"])

    @command(
        name="embed",
        aliases=get_aliases("embed"),
        description="Embed your text.",
        usage=f"{prefix}embed <text>",
    )
    async def embed(self, ctx, *, msg):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color)
        embed.title = msg
        await ctx.send(embed=embed, delete_after=delete_after)

    @command(
        name="webhook",
        aliases=get_aliases("webhook"),
        description="Send a custom webhook message.",
        usage=f"{prefix}webhook <name>|<message>",
    )
    async def webhook(self, ctx, *, name_message):
        if "|" in name_message:
            message_name = name_message.split("|")
            message = message_name[1]
            name = message_name[0]
            embed = discord.Embed(color=webhook_color)
            embed.description = message
            await ctx.message.delete()
            author_pfp = ctx.message.author.avatar_url_as(static_format="webp")
            img_data = requests.get(author_pfp).content
            web = await ctx.channel.create_webhook(name=name, avatar=img_data)
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(
                    web.url, adapter=AsyncWebhookAdapter(session)
                )
                await webhook.send(embed=embed, username=name)
        else:
            printer(f"Syntax Error: Command usage({ctx.command.usage})")

    @command(
        name="nitro",
        aliases=get_aliases("nitro"),
        description="Generate random nitro codes.",
        usage=f"{prefix}nitro <amount>",
    )
    async def nitro(self, ctx, amount=1):
        await ctx.message.delete()
        if amount > 0:
            print(f"Generating {amount} nitro codes.")

            def nitro_generator(
                    string_size=16, characters=string.ascii_letters + string.digits
            ):
                return "".join(random.choice(characters) for _ in range(string_size))

            for code in range(amount):
                await ctx.send(f"discord.gift/{nitro_generator()}")
        else:
            printer("Input an amount greater than 0.")

    @command(
        name="owofy",
        aliases=get_aliases("owofy"),
        description="Owofy your text",
        usage=f"{prefix}owofy",
    )
    async def owofy(self, ctx):
        global owoToggle
        await ctx.message.delete()
        if owoToggle:
            owoToggle = False
            print("owofyer deactivated.")
        else:
            print("owofyer activated.")
            owoToggle = True

    @Cog.listener("on_message")
    async def owofier(self, ctx):
        global owoToggle
        if (
                not ctx.content.startswith(prefix)
                and owoToggle
                and client.user.id == ctx.author.id
        ):
            custom_emojis = re.findall(r"<:\w*:\d*>", ctx.content)
            custom_emojis = [
                int(e.split(":")[1].replace(">", "")) for e in custom_emojis
            ]
            custom_emojis = [
                discord.utils.get(client.emojis, id=e) for e in custom_emojis
            ]
            if not custom_emojis:
                msg = owoify(ctx.content, "uwu")
                if not msg == ctx.content:
                    await ctx.edit(content=msg)

    @command(
        name="translate",
        aliases=get_aliases("translate"),
        description="Translate your text to another language",
        usage=f"{prefix}translate <language> <text>",
    )
    async def translate(self, ctx, language, *, text):
        await ctx.message.delete()
        try:
            if len(language) == 2:
                lang = language
            else:
                try:
                    lang = langs1[f"{language.title()}"]
                except BaseException:
                    lang = "lol"
            if lang in langs:
                translator = google_translator()
                txt = translator.translate(text, lang_tgt=lang)
                await ctx.send(txt)

            else:
                printer("invalid language")
        except BaseException:
            printer("Invalid language.")

    @command(
        name="big",
        aliases=get_aliases("big"),
        description="Replace letters with regional letters.",
        usage=f"{prefix}big <message>",
    )
    async def big(self, ctx, *, text):
        await ctx.message.delete()
        text1 = text.lower()
        text_list = [char for char in text1]
        regional = []
        appending = [
            regional.append(text_to_regional[char])
            if char in text_to_regional
            else regional.append(char)
            for char in text_list
        ]
        str = "".join(regional)
        await ctx.send(str)
        print(f"Bigified {text}")

    @command(
        name="clap",
        aliases=get_aliases("clap"),
        description="Place a clap emoji between words.",
        usage=f"{prefix}clap <message>",
    )
    async def clap(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text.replace(" ", " :clap: "))

    @command(
        name="cap",
        aliases=get_aliases("cap"),
        description="Place a cap emoji between words.",
        usage=f"{prefix}cap <message>",
    )
    async def cap(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text.replace(" ", " :billed_cap: "))

    @command(
        name="imp",
        aliases=get_aliases("imp"),
        description="Place an imp emoji between words.",
        usage=f"{prefix}imp <message>",
    )
    async def imp(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text.replace(" ", " :smiling_imp: "))

    @command(
        name="upsidedown",
        aliases=get_aliases("upsidedown"),
        description="Flip text upsidedown.",
        usage=f"{prefix}upsidedown <message>",
    )
    async def upsidedown(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(upsidedown.transform(text))

    @command(
        name="zalgo",
        aliases=get_aliases("zalgo"),
        description="Create zalgo text.",
        usage=f"{prefix}zalgo <message>",
    )
    async def zalgo(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(zalgo.zalgo().zalgofy(text))

    @command(
        name="upper",
        aliases=get_aliases("upper"),
        description="Make the text all uppercase.",
        usage=f"{prefix}upper <message>",
    )
    async def upper(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text.upper())

    @command(
        name="lower",
        aliases=get_aliases("lower"),
        description="Make the text all lowercase.",
        usage=f"{prefix}lower <message>",
    )
    async def lower(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text.lower())

    @command(
        name="alternating",
        aliases=get_aliases("alternating"),
        description="Make the text all alternating case.",
        usage=f"{prefix}alternating <message>",
    )
    async def alternating(self, ctx, *, text):
        await ctx.message.delete()
        res = [
            ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(text)
        ]
        await ctx.send("".join(res))

    @command(
        name="kanye",
        aliases=get_aliases("kanye"),
        description="Send a quote of kanye west.",
        usage=f"{prefix}kanyequote",
    )
    async def kanye(self, ctx):
        await ctx.message.delete()
        await ctx.send(requests.get("https://api.kanye.rest/?format=text").text)

    @command(
        name="affirmation",
        aliases=get_aliases("affirmation"),
        description="Send an affirmation.",
        usage=f"{prefix}affirmation",
    )
    async def affirmation(self, ctx):
        await ctx.message.delete()
        await ctx.send(
            requests.get("https://www.affirmations.dev/").json()["affirmation"]
        )

    @command(
        name="joke",
        aliases=get_aliases("joke"),
        description="Send a joke.",
        usage=f"{prefix}joke",
    )
    async def joke(self, ctx):
        await ctx.message.delete()
        await ctx.send(
            requests.get(
                "https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=political&type=single"
            ).json()["joke"]
        )

    @command(
        name="twopartjoke",
        aliases=get_aliases("twopartjoke"),
        description="Send a two part joke.",
        usage=f"{prefix}twopartjoke",
    )
    async def twopartjoke(self, ctx):
        joke = requests.get(
            "https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=political&type=twopart"
        ).json()
        await ctx.message.delete()
        await ctx.send(joke["setup"])
        await asyncio.sleep(3)
        await ctx.send(joke["delivery"])

    @command(
        name="dadjoke",
        aliases=get_aliases("dadjoke"),
        description="Send a Dad joke.",
        usage=f"{prefix}dadjoke",
    )
    async def dadjoke(self, ctx):
        await ctx.message.delete()
        await ctx.send(
            requests.get("https://icanhazdadjoke.com/slack").json()["attachments"][0][
                "text"
            ]
        )

    @command(
        name="ascii",
        aliases=get_aliases("ascii"),
        description="Turn your text into ascii art.",
        usage=f"{prefix}ascii <text>",
    )
    async def _ascii(self, ctx, *, text):
        await ctx.message.delete()
        art = text2art(text)
        await ctx.send(f"```{art}```")

    @command(
        name="empty",
        aliases=get_aliases("empty"),
        description="Send and empty message.",
        usage=f"{prefix}empty",
    )
    async def empty(self, ctx):
        await ctx.message.delete()
        await ctx.send("​")

    @command(
        name="clearscreen",
        aliases=get_aliases("clearscreen"),
        description="Clear the screen.",
        usage=f"{prefix}clearscreen",
    )
    async def clearscreen(self, ctx):
        await ctx.message.delete()
        await ctx.send(
            "​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n"
        )

    @command(
        name="tags",
        description="Create your own custom commands.",
        usage=f"{prefix}tags <add/remove> <tag> <text>",
    )
    async def tags(self, ctx, action, tag, *, value):
        await ctx.message.delete()
        if tag.lower() in [command.name for command in client.commands]:
            print("There is already an existing command with that name.")
        else:
            if not os.path.exists(f"{documents}/files/tags.json"):
                with open(f"{documents}/files/tags.json", "w") as _:
                    pass
            with open(f"{documents}/files/tags.json", "r") as tags_r:
                data = tags_r.read()
                content = {}
                if data:
                    content = json.loads(data)
                if action == "add":
                    if tag in content:
                        printer("This tag already exists.")
                    else:
                        with open(f"{documents}/files/tags.json", "w") as tags_w:
                            content[f"{tag}"] = value
                            tags_w.write(json.dumps(content, indent=2))
                            print(f"Tag {tag} added.")
                elif action == "remove":
                    if tag in content:
                        with open(f"{documents}/files/tags.json", "w") as tags_w:
                            del content[tag]
                            tags_w.write(json.dumps(content, indent=2))
                            print(f"Tag {tag} removed.")
                    else:
                        printer("Tag does not exist.")
                else:
                    printer("Invalid action.")

    @command(
        name="last",
        aliases=get_aliases("last"),
        description="Resend your last message.",
        usage=f"{prefix}last",
    )
    async def last(self, ctx):
        await ctx.message.delete()
        if last_message:
            await ctx.send(last_message)
        else:
            printer("No message found.")

    @command(
        "countdown",
        aliases=get_aliases("countdown"),
        description="Count down from an x amount of seconds.",
        usage=f"{prefix}countdown <seconds>",
    )
    async def countdown(self, ctx, seconds: int):
        await ctx.message.delete()
        print(f"Initated countdown started at {seconds}")
        sec = seconds
        msg = await ctx.send(sec)
        while sec >= 1:
            sec -= 1
            await msg.edit(content=sec)
            await asyncio.sleep(1)
        else:
            print(f"Finished counting down from {seconds}")

    @Cog.listener("on_message")
    async def lastmsg(self, ctx):
        if ctx.author.id == client.user.id:
            if not ctx.content.startswith(f"{prefix}last"):
                last_message = ctx.content

    @Cog.listener("on_message")
    async def tags_watcher(self, ctx):
        if ctx.author.id == client.user.id:
            if os.path.exists(f"{documents}/files/tags.json"):
                with open(f"{documents}/files/tags.json", "r") as tags_r:
                    content = {}
                    data = tags_r.read()
                    if data:
                        content = json.loads(data)
                    for tag in content.keys():
                        msg = ctx.content.split(" ")
                        if msg[0] == (f"{prefix}{tag}"):
                            await ctx.delete()
                            await ctx.channel.send(content.get(tag))
                            break

    @command(
        name="script",
        aliases=get_aliases("script"),
        description="Send a script.",
        usage=f"{prefix}script <seconds> <filename>",
    )
    async def script(self, ctx, delay, *, filename):
        await ctx.message.delete()
        try:
            delay = int(delay)
            if os.path.exists(f"{documents}/scripts/{filename}.txt"):
                with open(
                        f"{documents}/scripts/{filename}.txt", "r", encoding="utf-8"
                ) as f:
                    scr = f.readlines()
                    if scr[0]:
                        script = [l for l in (line.strip() for line in scr) if l]
                        for l in script:
                            await ctx.send(l)
                            await asyncio.sleep(delay)
                    else:
                        printer("File is empty.")
            else:
                printer(f"No file found called {filename}")
        except ValueError:
            printer("Delay must be a number.")

    @command(
        name="mock",
        aliases=get_aliases("mock"),
        description="Mock something a person said.",
        usage=f"{prefix}mock <text>",
    )
    async def mock(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send("".join(random.choice((str.upper, str.lower))(c) for c in text))


class Toolscog(commands.Cog):
    @command(
        name="tools",
        aliases=get_aliases("tools"),
        description="Display Tools Commands.",
        usage=f"{prefix}tools",
    )
    async def tools_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Tools Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Tools Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="lmgtfy",
        aliases=get_aliases("lmgtfy"),
        description="Sends an lmgtfy link with a query.",
        usage=f"{prefix}lmgtfy <query>",
    )
    async def lmgtfy(self, ctx, *, query):
        if send_embeds:
            embed = discord.Embed(color=embed_color)
            embed.set_footer(text=footer_text, icon_url=footer_url)
            embed.title = "Google results for:"
            embed.description = (
                f'[**{query}**](http://letmegooglethat.com/?q={query.replace(" ", "")})'
            )
            await ctx.message.delete()
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            await ctx.send(f'http://letmegooglethat.com/?q={query.replace(" ", "")}')

    @command(
        name="friend",
        aliases=get_aliases("friend"),
        description="Sends a friend request to the mentioned user.",
        usage=f"{prefix}friend <member>",
    )
    async def friend(ctx, member: discord.Member = None):
        await ctx.message.delete()
        if not member:
            pass
        else:
            await member.send_friend_request()

    @command(
        name="unfriend",
        aliases=get_aliases("unfriend"),
        description="Remove the mentioned user as a friend.",
        usage=f"{prefix}unfriend <member>",
    )
    async def unfriend(ctx, member: discord.Member = None):
        await ctx.message.delete()
        if not member:
            pass
        else:
            await member.remove_friend()

    @command(
        name="theme",
        aliases=get_aliases("theme"),
        description="Change your discord theme.",
        usage=f"{prefix}theme <light/dark>",
    )
    async def theme(self, ctx, theme):
        if theme in ["light", "dark"]:
            url = "https://discord.com/api/v8/users/@me/settings"
            payload = '{"theme":"' + theme + '"}'
            headers = {
                "authority": "discord.com",
                "authorization": token,
                "content-type": "application/json",
            }
            requests.request("PATCH", url, data=payload, headers=headers)
        else:
            printer("Invalid theme.")

    @command(
        name="allchannels",
        aliases=get_aliases("allchannels"),
        description="Show all channels even when not visible for you.",
        usage=f"{prefix}allchannels",
    )
    async def allchannels(self, ctx):
        await ctx.message.delete()
        await ctx.send('\n'.join([channel.mention for channel in ctx.guild.channels]))

    @command(
        name="hypesquad",
        aliases=get_aliases("hypesquad"),
        description="Change your hypesquad house.",
        usage=f"{prefix}hypesquad <bravery/balance/brilliance>",
    )
    async def hypesquad(self, ctx, house):
        if house in ["bravery", "balance", "brilliance"]:
            url = "https://discord.com/api/v8/hypesquad/online"
            house_id = 1

            if house.lower() == "balance":
                house_id = 2
            elif house.lower == "bravery":
                house_id = 3
            payload = '{"house_id":' + str(house_id) + "}"
            headers = {"authorization": token, "content-type": "application/json"}
            requests.request("POST", url, data=payload, headers=headers)
        else:
            printer("Invalid house.")

    @command(
        name="attack",
        aliases=get_aliases("attack"),
        description="Send attack to IP.",
        usage=f"{prefix}attack <ip/port/seconds/method>",
    )
    async def attack(ctx, host, port, secs, *, method):
        requests.get(
            "https://yariya.dev/api2.php?key=Vypxr&host=" + host + "&port=" + port + "&time=" + secs + "&method=" + method)
        sent = discord.Embed(title="NIGGA GOT GANGBANGED", color=0x0088ff)
        sent.add_field(name="IP:", value=f"▸ {host}", inline=False)
        sent.add_field(name="Port:", value=f"▸ {port}", inline=False)
        sent.add_field(name="Seconds:", value=f"▸ {secs}", inline=False)
        sent.add_field(name="Method:", value=f"▸ {method}", inline=False)
        sent.set_image(url="https://media1.tenor.com/images/63bed665d9e519352209228c0ba68083/tenor.gif?itemid=15640615")
        await ctx.send(embed=sent)

    @command(
        name="covid",
        aliases=get_aliases("covid"),
        description="Displays covid statistics for a country",
        usage=f"{prefix}covid <country>",
    )
    async def covid(self, ctx, *, location):
        await ctx.message.delete()
        countries = [
            c["country"]
            for c in requests.get(
                "https://coronavirus-19-api.herokuapp.com/countries/"
            ).json()
        ]
        if location == "uk" or location == "Uk" or location == "UK":
            location = "UK"
        elif (
                location == "us"
                or location == "usa"
                or location == "Us"
                or location == "Usa"
                or location == "USA"
        ):
            location = "USA"
        else:
            location = location.title()
        if location in countries:
            country_code = requests.get(
                f"https://restcountries.eu/rest/v2/name/{location}"
            ).json()[0]["alpha2Code"]
            country_status = requests.get(
                f"https://coronavirus-19-api.herokuapp.com/countries/{location}"
            ).json()
            embed = discord.Embed(color=embed_color)
            if location == "UK":
                thumbnail = f"https://www.countryflags.io/gb/flat/64.png"
            elif location == "USA":
                thumbnail = f"https://www.countryflags.io/us/flat/64.png"
            else:
                thumbnail = f"https://www.countryflags.io/{country_code}/flat/64.png"
            embed.set_thumbnail(url=thumbnail)
            embed.title = f'Covid-19 Statistics For {country_status["country"]}.'
            embed.add_field(
                name="Confirmed Cases", value=country_status["cases"], inline=False
            )
            embed.add_field(
                name="Active Cases", value=country_status["active"], inline=False
            )
            embed.add_field(
                name="Cases Today", value=country_status["todayCases"], inline=False
            )
            embed.add_field(
                name="Total Deaths", value=country_status["deaths"], inline=False
            )
            embed.add_field(
                name="Deaths Today", value=country_status["todayDeaths"], inline=False
            )
            embed.add_field(
                name="Total Recovered", value=country_status["recovered"], inline=False
            )
            embed.add_field(
                name="Critical", value=country_status["critical"], inline=False
            )
            embed.add_field(name="Total Tests", value=country_status["totalTests"])
            embed.set_footer(text=footer_text, icon_url=footer_url)
            if send_embeds:
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(
                    f'```Covid-19 Statistics For {country_status["country"]}\n\n+ Confirmed Cases: {country_status["cases"]}\n+ Active Cases: {country_status["active"]}\n+ Cases Today {country_status["todayCases"]}\n+ Deaths: {country_status["deaths"]}\n+ Deaths Today: {country_status["todayDeaths"]}\n+ Recovered: {country_status["recovered"]}\n+ Ctritical: {country_status["critical"]}\n+ Total Tests: {country_status["totalTests"]}```'
                )
            print(f'Covid stats for {country_status["country"]} have been sent. ')
        else:
            printer("Incorrect location")

    @command(
        name="coins",
        aliases=get_aliases("coins"),
        description="List coins available with the coin command.",
        usage=f"{prefix}coins",
    )
    async def coins(self, ctx):
        await ctx.message.delete()
        url = "https://api.coincap.io/v2/assets"
        response = requests.get(url).json()

        content = [""]
        for coin in response["data"]:
            if len(content[-1]) > 1900:
                content.append("")
            content[
                -1
            ] += f"{coin['symbol']} - {coin['name']} - {round(float(coin['priceUsd']), 3)} USD\n"

        for chunk in content:
            await ctx.send(chunk)

    @command(
        name="channelinfo",
        aliases=get_aliases("channelinfo"),
        description="Get information about a channel.",
        usage=f"{prefix}channelinfo",
    )
    async def channelinfo(ctx, channel: discord.TextChannel = None):
        await ctx.message.delete()
        if not channel:
            channel = ctx.channel
            embed = discord.Embed(title='**Channel Info**', color=0xFFFAFA,
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.add_field(name='**Is NSFW?**', value=channel.is_nsfw(), inline=False)
            embed.add_field(name='**Is News Channel?**', value=channel.is_news(), inline=False)
            embed.add_field(name='**Channel ID**', value=channel.id, inline=False)
            embed.add_field(name='**Created At**', value=channel.created_at, inline=False)
            embed.add_field(name='**Category ID**', value=channel.category_id, inline=False)
            embed.add_field(name='**Members**', value=len(channel.members), inline=False)
            embed.add_field(name='**Last Message ID**', value=channel.last_message_id, inline=False)
            embed.add_field(name='**Mention**', value=channel.mention, inline=False)
            embed.add_field(name='**Topic**', value=channel.topic, inline=False)
            embed.add_field(name='**Position**', value=channel.position, inline=False)
            embed.add_field(name='**Slowmode Delay**', value=channel.slowmode_delay, inline=False)
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            embed = discord.Embed(title='**Channel Info**', color=0xFFFAFA,
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.add_field(name='**Is NSFW?**', value=channel.is_nsfw(), inline=False)
            embed.add_field(name='**Is News Channel?**', value=channel.is_news(), inline=False)
            embed.add_field(name='**Channel ID**', value=channel.id, inline=False)
            embed.add_field(name='**Created At**', value=channel.created_at, inline=False)
            embed.add_field(name='**Category ID**', value=channel.category_id, inline=False)
            embed.add_field(name='**Members**', value=len(channel.members), inline=False)
            embed.add_field(name='**Last Message ID**', value=channel.last_message_id, inline=False)
            embed.add_field(name='**Mention**', value=channel.mention, inline=False)
            embed.add_field(name='**Topic**', value=channel.topic, inline=False)
            embed.add_field(name='**Position**', value=channel.position, inline=False)
            embed.add_field(name='**Slowmode Delay**', value=channel.slowmode_delay, inline=False)
            await ctx.send(embed=embed, delete_after=delete_after)

    @command(
        name="coin",
        aliases=get_aliases("coin"),
        description="Get information about a cryptocoin.",
        usage=f"{prefix}coin <coin name>",
    )
    async def coin(self, ctx, *, coin):
        await ctx.message.delete()
        url = "https://api.coincap.io/v2/assets?search=" + coin
        response = requests.get(url).json()

        if len(response["data"]) == 0:
            printer("Unknown coin provided")
        else:
            url = "https://api.coincap.io/v2/assets/" + response["data"][0]["id"]
            response = requests.get(url).json()
            if send_embeds:
                embed = discord.Embed(color=embed_color, title=response["data"]["name"])
                try:
                    embed.set_thumbnail(
                        url=f"https://icons.bitbot.tools/api/{response['data']['symbol'].lower()}/128x128"
                    )
                except BaseException:
                    pass
                if response["data"]["explorer"] is not None:
                    embed.description = f"[Explorer]({response['data']['explorer']})"
                embed.add_field(
                    name="Supply",
                    value=readify(round(float(response["data"]["supply"])), 1),
                )
                if response["data"]["maxSupply"] is not None:
                    embed.add_field(
                        name="Max Supply",
                        value=readify(round(float(response["data"]["maxSupply"])), 1),
                    )
                if response["data"]["marketCapUsd"] is not None:
                    embed.add_field(
                        name="Market Cap",
                        value=f"{readify(round(float(response['data']['marketCapUsd'])), 1)} USD",
                    )
                if response["data"]["volumeUsd24Hr"] is not None:
                    embed.add_field(
                        name="24h Volume",
                        value=f"{readify(round(float(response['data']['volumeUsd24Hr'])), 1)} USD",
                    )
                embed.add_field(
                    name="24h Change",
                    value=f"{round(float(response['data']['changePercent24Hr']), 2)}%",
                )
                embed.add_field(
                    name="Price",
                    value=f"{round(float(response['data']['priceUsd']), 3)} USD",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                content = f"```\n{response['data']['name']}\n"
                if response["data"]["explorer"] is not None:
                    content += f"Explorer: {response['data']['explorer']}\n"
                content += (
                    f"Supply: {readify(round(float(response['data']['supply'])), 1)}\n"
                )
                if response["data"]["maxSupply"] is not None:
                    content += f"Max Supply: {readify(round(float(response['data']['maxSupply'])), 1)}\n"
                if response["data"]["marketCapUsd"] is not None:
                    content += f"Market Cap: {readify(round(float(response['data']['marketCapUsd'])), 1)} USD\n"
                if response["data"]["volumeUsd24Hr"] is not None:
                    content += f"24h Volume: {readify(round(float(response['data']['volumeUsd24Hr'])), 1)} USD\n"
                content += f"24h Change: {round(float(response['data']['changePercent24Hr']), 2)}%\n"
                content += f"Price: {round(float(response['data']['priceUsd']), 2)} USD"

                await ctx.send(f"{content}```")

    @command(
        name="geo",
        aliases=get_aliases("geo"),
        description="Get geographical data for an ip address.",
        usage=f"{prefix}geo <ip>",
    )
    async def geo(self, ctx, ip):
        await ctx.message.delete()
        try:
            response = requests.get(
                f"https://api.ipgeolocation.io/ipgeo?apiKey={ipgeolocationioapikey}&ip={ip}"
            )
            ip_data = response.json()
            timestamp = ip_data["time_zone"]["current_time"][:-12]
            embed = discord.Embed(color=embed_color)
            embed.title = name = f"Results For - {ip}"
            embed.set_thumbnail(url=ip_data["country_flag"])
            embed.add_field(
                name="Country Name", value=ip_data["country_name"], inline=False
            )
            embed.add_field(
                name="Country Code", value=ip_data["country_code2"], inline=True
            )
            embed.add_field(
                name="Continent", value=ip_data["continent_name"], inline=True
            )
            embed.add_field(
                name="Continent Code", value=ip_data["continent_code"], inline=True
            )
            embed.add_field(
                name="Country Capital", value=ip_data["country_capital"], inline=True
            )
            embed.add_field(name="City", value=ip_data["city"], inline=True)
            if ip_data["state_prov"]:
                embed.add_field(
                    name="State Providance", value=ip_data["state_prov"], inline=True
                )
            embed.add_field(
                name="Long/Lat",
                value=f'{ip_data["longitude"]}\n{ip_data["latitude"]}',
                inline=True,
            )
            if ip_data["zipcode"]:
                embed.add_field(name="Zip Code", value=ip_data["zipcode"], inline=True)
            embed.add_field(name="ISP", value=ip_data["isp"], inline=True)
            embed.add_field(
                name="Currency",
                value=f'{ip_data["currency"]["name"]}\n{ip_data["currency"]["code"]}\n{ip_data["currency"]["symbol"]}',
                inline=True,
            )
            embed.add_field(
                name="Timezone", value=ip_data["time_zone"]["name"], inline=True
            )
            embed.add_field(name="Time", value=timestamp.replace("-", "/"), inline=True)
            embed.set_footer(text=footer_text, icon_url=footer_url)
            print(f"Fetching Geo-Location data for {ip}")
            if send_embeds:
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                if ip_data["state_prov"] and ip_data["zipcode"]:
                    await ctx.send(
                        f'```Results for - {ip}\n\n+ Country Name: {ip_data["country_name"]}\n+ Country Code: {ip_data["country_code2"]}\n+ Continent: {ip_data["continent_name"]}\n+ Continent Code: {ip_data["continent_code"]}\n+ Country Capital: {ip_data["country_capital"]}\n+ City: {ip_data["city"]}\n+ State Providance: {ip_data["state_prov"]}\n+ Long/Lat: {ip_data["longitude"]}/{ip_data["latitude"]}\n+ Zip Code: {ip_data["zipcode"]}\n+ ISP: {ip_data["isp"]}\n+ Currency: {ip_data["currency"]["name"]}/{ip_data["currency"]["code"]}/{ip_data["currency"]["symbol"]}\n+ Timezone: {ip_data["time_zone"]["name"]}\n+ Time: {timestamp.replace("-", "/").replace(" ", " - ")}```'
                    )
                elif ip_data["state_prov"] and not ip_data["zipcode"]:
                    await ctx.send(
                        f'```Results for - {ip}\n\n+ Country Name: {ip_data["country_name"]}\n+ Country Code: {ip_data["country_code2"]}\n+ Continent: {ip_data["continent_name"]}\n+ Continent Code: {ip_data["continent_code"]}\n+ Country Capital: {ip_data["country_capital"]}\n+ City: {ip_data["city"]}\n+ State Providance: {ip_data["state_prov"]}\n+ Long/Lat: {ip_data["longitude"]}/{ip_data["latitude"]}\n+ ISP: {ip_data["isp"]}\n+ Currency: {ip_data["currency"]["name"]}/{ip_data["currency"]["code"]}/{ip_data["currency"]["symbol"]}\n+ Timezone: {ip_data["time_zone"]["name"]}\n+ Time: {timestamp.replace("-", "/").replace(" ", " - ")}```'
                    )
                elif not ip_data["state_prov"] and ip_data["zipcode"]:
                    await ctx.send(
                        f'```Results for - {ip}\n\n+ Country Name: {ip_data["country_name"]}\n+ Country Code: {ip_data["country_code2"]}\n+ Continent: {ip_data["continent_name"]}\n+ Continent Code: {ip_data["continent_code"]}\n+ Country Capital: {ip_data["country_capital"]}\n+ City: {ip_data["city"]}\n+ Long/Lat: {ip_data["longitude"]}/{ip_data["latitude"]}\n+ Zip Code: {ip_data["zipcode"]}\n+ ISP: {ip_data["isp"]}\n+ Currency: {ip_data["currency"]["name"]}/{ip_data["currency"]["code"]}/{ip_data["currency"]["symbol"]}\n+ Timezone: {ip_data["time_zone"]["name"]}\n+ Time: {timestamp.replace("-", "/").replace(" ", " - ")}```'
                    )
                elif not ip_data["state_prov"] and not ip_data["zipcode"]:
                    await ctx.send(
                        f'```Results for - {ip}\n\n+ Country Name: {ip_data["country_name"]}\n+ Country Code: {ip_data["country_code2"]}\n+ Continent: {ip_data["continent_name"]}\n+ Continent Code: {ip_data["continent_code"]}\n+ Country Capital: {ip_data["country_capital"]}\n+ City: {ip_data["city"]}\n+ Long/Lat: {ip_data["longitude"]}/{ip_data["latitude"]}\n+ ISP: {ip_data["isp"]}\n+ Currency: {ip_data["currency"]["name"]}/{ip_data["currency"]["code"]}/{ip_data["currency"]["symbol"]}\n+ Timezone: {ip_data["time_zone"]["name"]}\n+ Time: {timestamp.replace("-", "/").replace(" ", " - ")}```'
                    )
        except BaseException:
            printer("Invalid IP Address")

    if autoreply_toggle and autoreply_message1:

        @Cog.listener("on_message")
        async def autoreply(self, ctx):
            if not ctx.guild and client.user != ctx.author:
                if ctx.author.name not in first_message:
                    asyncio.sleep(autoreply_delay)
                    await ctx.channel.send(autoreply_message1)
                    first_message.append(ctx.author.name)
                    print(f'Auto-replied to {ctx.author.name} "{autoreply_message1}".')
                elif ctx.author.name not in second_message:
                    asyncio.sleep(autoreply_delay)
                    await ctx.channel.send(autoreply_message2)
                    second_message.append(ctx.author.name)
                    print(f'Auto-replied to {ctx.author.name} "{autoreply_message2}".')

    @command(
        name="globalnick",
        aliases=get_aliases("globalnick"),
        description="Replace your nickname in all servers.",
        usage=f"{prefix}globalnick <nickname>",
    )
    async def globalnick(self, ctx, *, nick):
        await ctx.message.delete()
        newname = nick
        errors = []
        for s in client.guilds:
            member = s.get_member(client.user.id)
            print(f"Successfully changed nickname in {s.name}")
            try:
                await member.edit(nick=newname)
            except BaseException:
                errors.append(s.name)
                pass
        if errors:
            print(
                "**Failed changing nickname on the following servers:**\n\n"
                + "\n".join(errors)
            )
        else:
            print("Successfully changed nick on all servers")

    @command(
        name="purge",
        aliases=get_aliases("purge"),
        description="Purge an amount of messages sent by you",
        usage=f"{prefix}purge <amount>",
    )
    async def purge(self, ctx, amount: int = 0):
        await ctx.message.delete()
        try:
            if amount and amount > 0:
                print(f"Purging {amount} messages sent by you.")
                messages = await ctx.channel.history(limit=amount).flatten()
                delete = [
                    message
                    for message in messages
                    if message.author.id == client.user.id
                ]
                for message in delete:
                    if not message == ctx.message:
                        await message.delete()
            else:
                printer("Enter an amount greater than 0.")
        except BaseException:
            pass

    @command(
        name="pingip",
        aliases=get_aliases("pingip"),
        description="Ping an ip address",
        usage=f"{prefix}pingip <ip> <amount of times>",
    )
    async def pingip(self, ctx, ip, amount=1):
        ping = os.system(f"ping -n {amount} {ip}")
        if ping == 1:
            await ctx.send(f"```{ip} is Unavailable```")
        elif ping == 0:
            await ctx.send(f"```{ip} is Available```")

    @command(
        name="exportfriendlist",
        aliases=get_aliases("exportfriendlist"),
        description="Export your whole friendlist to a file.",
        usage=f"{prefix}exportfriendlist",
    )
    async def exportfriendlist(self, ctx):
        await ctx.message.delete()
        with open(
                f"{documents}/files/friendlist.txt", "w", encoding="utf-8"
        ) as write_friends:
            friends = [f"{friend} - {friend.id}\n" for friend in client.user.friends]
            if friends:
                friends_str = "".join(friends)
                write_friends.write(friends_str)
                print("Friend list exported to file.")
            else:
                printer("You dont have any friends. :(")

    @command(
        name="exportblocklist",
        aliases=get_aliases("exportblocklist"),
        description="Export your whole blocklist to a file.",
        usage=f"{prefix}exportblocklist",
    )
    async def exportblocklist(self, ctx):
        await ctx.message.delete()
        with open(
                f"{documents}/files/blocklist.txt", "w", encoding="utf-8"
        ) as write_friends:
            blocked = [f"{blocked} - {blocked.id}\n" for blocked in client.user.blocked]
            if blocked:
                blocked_str = "".join(blocked)
                write_friends.write(blocked_str)
                print("Block list exported to file.")
            else:
                printer("You dont have anyone blocked.")

    @command(
        name="markasread",
        aliases=get_aliases("markasread"),
        description="Mark all server messages as read",
        usage=f"{prefix}markasread",
    )
    async def markasread(self, ctx):
        await ctx.message.delete()
        try:
            for guild in client.guilds:
                await guild.ack()
                await asyncio.sleep(3)
            print("Finished marking all servers as read.")
        except BaseException:
            printer("You're being rate limited.")

    @command(
        name="proxy",
        aliases=get_aliases("proxy"),
        description="Gets random proxies",
        usage=f"{prefix}proxy <http/https/socks4/socks5> <count>",
    )
    async def proxy(self, ctx, proxy_type="http", count: int = 1):
        await ctx.message.delete()
        if proxy_type.lower() in ["http", "https", "socks4", "socks5"]:
            try:
                collector = proxyscrape.get_collector(proxy_type)
            except BaseException:
                collector = proxyscrape.create_collector(proxy_type, proxy_type)
            proxies = collector.get_proxies()
            proxies = proxies[: min(len(proxies), count)]
            chunks = [""]
            for proxy in proxies:
                if len(chunks[-1]) > 1900:
                    chunks.append("")
                chunks[-1] += f"{proxy.host}:{proxy.port}\n"
            for chunk in chunks:
                await ctx.channel.send(chunk)
        else:
            printer("Invalid proxy type")

    async def whoiscomment(self):
        pass
        # @command(name='whois',
        #         aliases=get_aliases('whois'),
        #         description='Get info on a domain',
        #         usage=f'{prefix}whois <domain>')
        # async def _whois(self, ctx, *, domain=None):
        #    if domain:
        #        try:
        #            print(f'Fetching whois data for {domain}')
        #            await ctx.message.edit(content=f'Loading whois data for {domain}...')
        #            w = whois.whois(f'{domain}')
        #            if isinstance(w['domain_name'], list):
        #                if send_embeds:
        #                    domain_names = [
        #                        f'{domain}\n' for domain in w['domain_name']]
        #                else:
        #                    domain_names = [
        #                        f'\n  {domain}' for domain in w['domain_name']]
        #                domain_names = ''.join(domain_names)
        #            else:
        #                domain_names = w['domain_name']
        #            if isinstance(w['name_servers'], list):
        #                if send_embeds:
        #                    name_servers = [
        #                        f'{name}\n' for name in w['name_servers']]
        #                else:
        #                    name_servers = [
        #                        f'\n  {name}' for name in w['name_servers']]
        #                name_servers = ''.join(name_servers)
        #            else:
        #                name_servers = w['name_servers']
        #            if isinstance(w['updated_date'], list):
        #                if send_embeds:
        #                    updated_date = [
        #                        f'{date}\n' for date in w['updated_date'] if date != '0001-01-01 00:00:00']
        #                else:
        #                    updated_date = [
        #                        f'\n  {date}' for date in w['updated_date'] if date != '0001-01-01 00:00:00']
        #                updated_date = ''.join(updated_date)
        #            else:
        #                updated_date = w['updated_date']
        #            if isinstance(w['emails'], list):
        #                if send_embeds:
        #                    emails = [f'{email}\n' for email in w['emails']]
        #                else:
        #                    emails = [f'\n  {email}' for email in w['emails']]
        #                emails = ''.join(emails)
        #            else:
        #                emails = w['emails']
        #            if isinstance(w['status'], list):
        #                if send_embeds:
        #                    status = [f'{status}\n' for status in w['status']]
        #                else:
        #                    status = [f'\n  {status}' for status in w['status']]
        #                status = ''.join(status)
        #            else:
        #                status = w['status']
        #            if isinstance(w['expiration_date'], list):
        #                if send_embeds:
        #                    expiration_date = [
        #                        f'{date}\n' for date in w['expiration_date']]
        #                else:
        #                    expiration_date = [
        #                        f'\n  {date}' for date in w['expiration_date']]
        #                expiration_date = ''.join(expiration_date)
        #            else:
        #                expiration_date = w['expiration_date']
        #            if isinstance(w['creation_date'], list):
        #                if send_embeds:
        #                    creation_date = [
        #                        f'{date}\n' for date in w['creation_date']]
        #                else:
        #                    creation_date = [
        #                        f'\n  {date}' for date in w['creation_date']]
        #                creation_date = ''.join(creation_date)
        #            else:
        #                creation_date = w['creation_date']
        #            embed = discord.Embed(color=embed_color)
        #            embed.title = name = f'Results For - {domain}'
        #            embed.add_field(
        #                name='Domain Name',
        #                value=domain_names,
        #                inline=False)
        #            embed.add_field(
        #                name='Registrar',
        #                value=w['registrar'],
        #                inline=False)
        #            embed.add_field(
        #                name='Whois Server',
        #                value=w['whois_server'],
        #                inline=False)
        #            embed.add_field(
        #                name='Name Servers',
        #                value=name_servers,
        #                inline=False)
        #            embed.add_field(name='Status', value=status, inline=False)
        #            embed.add_field(name='Emails', value=emails, inline=False)
        #            embed.add_field(name='DNSSEC', value=w['dnssec'], inline=False)
        #            embed.add_field(
        #                name='Updated date',
        #                value=updated_date,
        #                inline=True)
        #            embed.add_field(
        #                name='Creation Date',
        #                value=creation_date,
        #                inline=True)
        #            embed.add_field(
        #                name='Expiration Date',
        #                value=expiration_date,
        #                inline=True)
        #            embed.add_field(name='Name', value=w['name'], inline=True)
        #            embed.add_field(name='Org', value=w['org'], inline=True)
        #            embed.add_field(
        #                name='Country',
        #                value=w['country'],
        #                inline=True)
        #            embed.add_field(name='State', value=w['state'], inline=True)
        #            embed.add_field(name='City', value=w['city'], inline=True)
        #            embed.add_field(
        #                name='Address',
        #                value=w['address'],
        #                inline=True)
        #            embed.add_field(
        #                name='Zipcode',
        #                value=w['zipcode'],
        #                inline=True)
        #            embed.set_footer(
        #                text=footer_text,
        #                icon_url=footer_url)
        #            if send_embeds:
        #                await ctx.message.delete()
        #                await ctx.send(embed=embed, delete_after=delete_after)
        #            else:
        #                await ctx.message.delete()
        #                await ctx.send(f'```Results for = {domain}\n\n+ Domain Name: {domain_names}\n+ Registrar: {w["registrar"]}\n+ Whois Server: {w["whois_server"]}\n+ Name Servers: {name_servers}\n+ Status: {status}\n+ Emails: {emails}\n+ DNSSEC: {w["dnssec"]}\n+ Updated Date: {updated_date}\n+ Creation Date: {creation_date}\n+ Expiration Date: {expiration_date}\n+ Name: {w["name"]}\n+ Org: {w["org"]}\n+ Country: {w["country"]}\n+ State: {w["state"]}\n+ City: {w["city"]}\n+ Zipcode: {w["zipcode"]}```')
        #        except BaseException:
        #            printer('Invalid domain.')
        #    else:
        #        printer('Please Input an IP Address')

    @command(
        name="shorturl",
        aliases=get_aliases("shortenurl"),
        description="Shorten your url",
        usage=f"{prefix}shorturl <url>",
    )
    async def shortenurl(self, ctx, url):
        await ctx.message.delete()
        urls = extractor.findall(ctx.message.content)
        urls1 = extractor1.findall(ctx.message.content)
        if urls or urls1:
            surl = requests.post(f"https://tinyurl.com/api-create.php?url={url}").text
            if surl == "Error":
                surl = requests.post(
                    f"https://tinyurl.com/api-create.php?url=https://{url}"
                ).text
        else:
            printer("Invalid URL")
        if surl and not surl == "error":
            await ctx.send(surl)
            print(f"URL {url} Shortened to: {surl}")

    @command(
        name="unshortenurl",
        aliases=get_aliases("unshortenurl"),
        description="Unshorten your url",
        usage=f"{prefix}unshorturl <url>",
    )
    async def unshortenurl(self, ctx, url):
        await ctx.message.delete()
        try:
            usurl = requests.get(f"https://unshorten.me/s/{url}")
        except BaseException:
            printer("invalid URL")
        await ctx.send(usurl.text)
        print(f"URL {url} Unshortened to: {usurl.text}")

    @command(
        name="base64",
        aliases=get_aliases("base64"),
        description="Base64 encoding and decoding",
        usage=f"{prefix}base64 <encode/decode> <data>",
    )
    async def base64(self, ctx, action, *, data):
        await ctx.message.delete()
        if action.lower() == "encode":
            await ctx.send(base64.b64encode(data.encode("ascii")).decode("ascii"))
        elif action.lower() == "decode":
            await ctx.send(base64.b64decode(data).decode("ascii"))
        else:
            printer("Invalid action")

    @command(
        name="btcaddress",
        aliases=get_aliases("btcaddress"),
        description="Get information about a BTC address.",
        usage=f"{prefix}btcaddress <address>",
    )
    async def btcaddress(self, ctx, *, address):
        await ctx.message.delete()
        await crypto_adress(ctx, address, "btc")

    @command(
        name="ethaddress",
        aliases=get_aliases("ethaddress"),
        description="Get information about a ETH address.",
        usage=f"{prefix}ethaddress <address>",
    )
    async def ethaddress(self, ctx, *, address):
        await ctx.message.delete()
        await crypto_adress(ctx, address, "eth")

    @command(
        name="ltcaddress",
        aliases=get_aliases("ltcaddress"),
        description="Get information about a LTC address.",
        usage=f"{prefix}ltcaddress <address>",
    )
    async def ltcaddress(self, ctx, *, address):
        await ctx.message.delete()
        await crypto_adress(ctx, address, "ltc")

    @command(
        name="dogeaddress",
        aliases=get_aliases("dogeaddress"),
        description="Get information about a Dogecoin address.",
        usage=f"{prefix}dogeaddress <address>",
    )
    async def dogeaddress(self, ctx, *, address):
        await ctx.message.delete()
        await crypto_adress(ctx, address, "doge")

    @command(
        name="dashaddress",
        aliases=get_aliases("dashaddress"),
        description="Get information about a Dash address.",
        usage=f"{prefix}dashaddress <address>",
    )
    async def dashaddress(self, ctx, *, address):
        await ctx.message.delete()
        await crypto_adress(ctx, address, "dash")

    @command(
        name="genpassword",
        aliases=get_aliases("genpassword"),
        description="Generate a secure password.",
        usage=f"{prefix}genpassword",
    )
    async def genpassword(self, ctx):
        await ctx.message.delete()

        def password_generator(
                string_size=16, characters=string.ascii_letters + string.digits
        ):
            return "".join(random.choice(characters) for _ in range(string_size))

        password = password_generator()
        await ctx.send(password)
        if not os.path.exists(f"{documents}/files/passwords.txt"):
            with open(f"{documents}/files/passwords.txt", "a") as _:
                pass
        with open(f"{documents}/files/passwords.txt", "a") as a:
            a.write(password + "\n")
        print("Password generated and saved to file.")

    @command(
        name="gentoken",
        aliases=get_aliases("gentoken"),
        description="Generate discord accounts.",
        usage=f"{prefix}gentoken",
    )
    async def gentoken(self, ctx):
        await ctx.message.delete()
        load_config()
        print("Generating discord accounts...")
        await img_gen()

    @command(
        name="remindme",
        aliases=get_aliases("remindme"),
        description="Set a reminder",
        usage=f"{prefix}remindme <duration> <message>",
    )
    async def remindme(self, ctx, duration, *, message):
        await ctx.message.delete()
        try:
            current_unix = round(datetime.datetime.now().timestamp())
            reminder_unix = round(dateparser.parse(f"in {duration}").timestamp())
            channel_id = ctx.channel.id

            if not os.path.exists(f"{documents}/files/reminders.json"):
                with open(
                        f"{documents}/files/reminders.json", "w", encoding="utf-8"
                ) as o:
                    o.close()
            with open(f"{documents}/files/reminders.json", "r", encoding="utf-8") as r:
                content = r.read()
                if content:
                    current_reminders = json.loads(content)
                else:
                    current_reminders = []
                current_reminders.append(
                    {
                        "message": message,
                        "remind_time": reminder_unix,
                        "current_time": current_unix,
                        "channel_id": channel_id,
                    }
                )
            with open(f"{documents}/files/reminders.json", "w", encoding="utf-8") as w:
                w.write(json.dumps(current_reminders, indent=2))
        except ValueError:
            printer("Number argument must be an integer.")

    @command(
        name="yt2mp4",
        aliases=get_aliases("yt2mp4"),
        description="Get an mp4 file from a youtube url",
        usage=f"{prefix}yt2mp4 <url>",
    )
    async def yt2mp4(self, ctx, *, link):
        await ctx.message.delete()
        if not os.path.exists(f"{documents}/videos"):
            os.mkdir(f"{documents}/videos")
        yt = YouTube(link)
        y = yt.streams.first().download(output_path=f"{documents}/videos")
        print("Finished video download.")


class Usercog(commands.Cog):
    @command(
        name="user",
        aliases=get_aliases("user"),
        description="Display User Commands.",
        usage=f"{prefix}user",
    )
    async def user_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"User Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```User Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="stealavatar",
        aliases=get_aliases("stealavatar"),
        description="Set a users avatar as your own.",
        usage=f"{prefix}stealavatar <user>",
    )
    async def stealavatar(self, ctx, *, username: discord.User):
        if not discord_password == "Discord Password" and discord_password:
            await ctx.message.delete()
            users_pfp = username.avatar_url_as(static_format="webp")
            image = requests.get(str(users_pfp))
            try:
                await client.user.edit(password=discord_password, avatar=image.content)
                print(f"Replaced avatar with the avatar of {username}")
            except BaseException:
                printer("You're changing avatars too quickly")
        else:
            printer(
                "Your discord password is required for this command, input it in the config."
            )

    @command(
        name="dump",
        aliases=get_aliases("dump"),
        description="Dump your DMs with the user to a txt.",
        usage=f"{prefix}dump",
    )
    async def dump(self, ctx):
        await ctx.message.delete()
        if not ctx.guild:
            print(
                f"Dumping chat with {ctx.channel.recipient.name}, this might take a while."
            )
            with open(
                    f"Chat with {ctx.channel.recipient.name}.txt", "w", encoding="utf-8"
            ) as chat_file:
                messages = await ctx.channel.history(limit=None).flatten()
                _ = [
                    chat_file.write(f"{x.author.name}: {x.content}\n") for x in messages
                ]
                print(f"Finished dumping chat with {ctx.channel.recipient.name}.")
        else:
            printer("This command can only be used in DMS.")

    @command(
        name="userinfo",
        aliases=get_aliases("userinfo"),
        description="Display the users info.",
        usage=f"{prefix}userinfo <user>",
    )
    async def userinfo(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        owner = False
        if not user:
            user = ctx.author
        if not user.id == client.user.id:
            user_profile = await user.profile()
        if ctx.guild:
            if user.id == ctx.guild.owner.id:
                owner = True
        embed = discord.Embed(color=embed_color)
        embed.set_author(name=f"User Info - {user}", icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=footer_text, icon_url=footer_url)
        embed.add_field(
            name=" Username",
            value=user.display_name,
        )
        embed.add_field(
            name="User ID",
            value=user.id,
        )
        embed.add_field(
            name="Created at",
            value=str(user.created_at)[:10],
        )
        if ctx.guild:
            member = ctx.guild.get_member(user_id=user.id)
            embed.add_field(
                name="Is Owner",
                value=owner,
            )
            embed.add_field(
                name="Joined at",
                value=str(member.joined_at)[:10],
            )
            embed.add_field(
                name=f"Role Count",
                value=len(member.roles),
            )
            embed.add_field(
                name="Top role",
                value=member.top_role.mention,
            )
            embed.add_field(
                name="Activity ",
                value=member.activity,
            )
        if not user.id == client.user.id:
            if user.relationship:
                relationship = (
                    str(user.relationship.type)
                        .replace("RelationshipType.", "")
                        .replace("-", " ")
                )
            else:
                relationship = "None"
            embed.add_field(
                name="Relationship",
                value=relationship,
            )
            if await user.mutual_friends():
                mutfrnds = []
                for frnd in await user.mutual_friends():
                    if send_embeds:
                        mutfrnds.append(f"{frnd.name}#{frnd.discriminator}\n")
                    else:
                        mutfrnds.append(f"\n  {frnd.name}#{frnd.discriminator}")
                mutfrnds = "".join(mutfrnds)
            else:
                mutfrnds = "None"
            embed.add_field(
                name="Mutual Friends",
                value=mutfrnds,
            )
            if user_profile.mutual_guilds:
                mutglds = []
                for gld in user_profile.mutual_guilds:
                    if send_embeds:
                        mutglds.append(f"{gld.name}\n")
                    else:
                        mutglds.append(f"\n  {gld.name}")
                mutglds = "".join(mutglds)
            else:
                mutglds = "None"
            embed.add_field(
                name="Mutual Servers",
                value=mutglds,
            )
            if user_profile.connected_accounts:
                con_accs = []
                for acc in user_profile.connected_accounts:
                    if send_embeds:
                        con_accs.append(f'{acc["type"]}: {acc["name"]}\n')
                    else:
                        con_accs.append(f'\n  {acc["type"]}: {acc["name"]}')
                con_accs = "".join(con_accs)
            else:
                con_accs = "None"
            embed.add_field(
                name="Connected Accounts",
                value=con_accs,
            )
        if send_embeds:
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            default_message = f"Userinfo - {user.name}\n\n+ Username: {user.display_name}\n+ User ID: {user.id}\n+ Created At: {str(user.created_at)[:10]}\n"
            if ctx.guild:
                membinfo = f"+ Joined At: {str(member.joined_at)[:10]}\n+ Is Owner {owner}\n+ Role Count: {len(member.roles)}\n+ Top Role: {member.top_role.name}\n+ Activity: {member.activity}\n"
            if not user.id == client.user.id:
                not_me_info = f"+ Relationship: {relationship}\n+ Mututal Friends: {mutfrnds}\n+ Mutual Servers: {mutglds}\n+ Connected Accounts: {con_accs}"
            if ctx.guild and user.id == client.user.id:
                await ctx.send(f"```{default_message}{membinfo}```")
            elif ctx.guild and not user.id == client.user.id:
                await ctx.send(f"```{default_message}{membinfo}{not_me_info}```")
            elif not ctx.guild and user.id == client.user.id:
                await ctx.send(f"```{default_message}```")
            elif not ctx.guild and not user.id == client.user.id:
                await ctx.send(f"```{default_message}{not_me_info}```")
        print(f"Fetching info for user {user.name}#{user.discriminator}")

    @command(
        name="status",
        description="Edit your user status.",
        usage=f"{prefix}status <activity> <text>",
        brief=" Activity types: watching/playing/listening/reset",
    )
    async def _status(self, ctx, activitytype, *, msg):
        await ctx.message.delete()
        if activitytype == "watching" and msg:
            await client.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching, name=f"{msg}"
                )
            )
            print(f"Status changed to {activitytype} {msg}")
        elif activitytype == "playing" and msg:
            await client.change_presence(activity=discord.Game(f"{msg}"))
            print(f"Status changed to {activitytype} {msg}")
        elif activitytype == "listening" and msg:
            await client.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.listening, name=f"{msg}"
                )
            )
            print(f"Status changed to {activitytype} {msg}")
        elif activitytype == "reset" or activitytype == "clear":
            await client.change_presence(status=discord.Status.online, activity=None)
        else:
            printer(f"Syntax Error: Command usage({ctx.command.usage})")

    @command(
        name="streaming",
        aliases=get_aliases("streaming"),
        description="Have your status show a stream.",
        usage=f"{prefix}streaming <url> <name>",
    )
    async def streaming(self, ctx, url, *, name):
        await ctx.message.delete()
        try:
            if url.startswith("https"):
                await client.change_presence(
                    activity=discord.Streaming(name=name, url=url)
                )
            else:
                printer(f"Syntax Error: Command usage({ctx.command.usage})")
        except BaseException:
            printer(f"Syntax Error: Command usage({ctx.command.usage})")

    @command(
        name="stopstatus",
        aliases=get_aliases("stopstatus"),
        description="Have your status removed.",
        usage=f"{prefix}stopstatus",
    )
    async def stopstatus(ctx):
        await ctx.message.delete()
        await client.change_presence(activity=None, status=discord.Status.dnd)

    @command(
        name="setavatar",
        aliases=get_aliases("setavatar"),
        description="Replace your avatar with an attachment.",
        usage=f"{prefix}setavatar <attachment>",
    )
    async def setavatar(self, ctx, image):
        image = requests.get(await arg_parser(ctx, image, returnurl=True))
        if not discord_password == "Discord Password" and discord_password:
            try:
                await client.user.edit(password=discord_password, avatar=image.content)
                print("Avatar changed")
                await ctx.message.delete()
            except BaseException:
                printer("You're changing avatars too quickly")
                await ctx.message.delete()
        else:
            printer(
                "Your discord password is required for this command, input it in the config."
            )
            await ctx.message.delete()

    @command(
        name="nick",
        aliases=get_aliases("nick"),
        description="Change a users nickname.",
        usage=f"{prefix}nick <member> <nickname>",
    )
    @commands.check_any(commands.has_guild_permissions(manage_nicknames=True))
    async def nick(self, ctx, member: discord.Member, *, nickname):
        await ctx.message.delete()
        await member.edit(nick=nickname)
        print(f"{member.name}'s nickname has been changed to {nickname}")

    @command(
        name="avatar",
        aliases=get_aliases("avatar"),
        description="Display a users avatar.",
        usage=f"{prefix}avatar <user>",
    )
    async def avatar(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        if not user:
            user = ctx.author
        await ctx.send(user.avatar_url)


class Loggingcog(commands.Cog):
    @command(
        name="logging",
        aliases=get_aliases("logging"),
        description="Display Logging Commands.",
        usage=f"{prefix}logging",
    )
    async def logging_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Logging Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Logging Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="setlogs",
        aliases=get_aliases("setlogs"),
        description="Set this channel as your log channel",
        usage=f"{prefix}setlogs",
    )
    async def setlogs(self, ctx):
        await ctx.message.delete()
        img_data = requests.get(footer_url).content
        with open(f"{documents}/files/config.json", "r") as read_config:
            web = await ctx.channel.create_webhook(
                name="Desyncer Logs Webhook", avatar=img_data
            )
            config_data = read_config.read()
            data = json.loads(config_data)
            data["Logging"]["Webhook Logging"] = True
            data["Logging"]["Webhook URL"] = web.url
            with open(f"{documents}/files/config.json", "w") as write_config:
                write_config.write(json.dumps(data, indent=2))

    @command(
        name="logkeyword",
        aliases=get_aliases("logkeyword"),
        description="Automatically log chosen keywords to file",
        usage=f"{prefix}logkeyword <keyword>",
    )
    async def logkeyword(self, ctx, keyword):
        await ctx.message.delete()
        if not os.path.exists(f"{documents}/files/keywords.txt"):
            with open(f"{documents}/files/keywords.txt", "a", encoding="utf-8") as o:
                o.close()
        with open(
                f"{documents}/files/keywords.txt", "a", encoding="utf-8"
        ) as write_keywords:
            write_keywords.write(f"{keyword}\n")
            print(f"The keyword {keyword} will now be logged.")

    @Cog.listener("on_message")
    async def keyword_logger(self, ctx):
        if log_keywords:
            keywords = []
            if not ctx.author.id == client.user.id:
                if os.path.exists(f"{documents}/files/keywords.txt"):
                    with open(
                            f"{documents}/files/keywords.txt", "r", encoding="utf-8"
                    ) as read_keywords:
                        server_channel = ""
                        keywords = [
                            f" {keyword}".rstrip()
                            for keyword in read_keywords.readlines()
                            if keyword.rstrip().lower() in ctx.content.lower()
                        ]
                        keywords1 = "".join(keywords)
                        if keywords:
                            if not os.path.exists(f"{documents}/logs/KeywordsLog.txt"):
                                with open(
                                        f"{documents}/logs/KeywordsLog.txt", "w"
                                ) as o:
                                    o.close()
                            with open(
                                    f"{documents}/logs/KeywordsLog.txt",
                                    "a",
                                    encoding="utf-8",
                            ) as write_keywords:
                                if ctx.guild:
                                    server_channel = (
                                        f"Server {ctx.guild.name} - {ctx.channel.name}"
                                    )
                                else:
                                    server_channel = "DMs"
                                print(
                                    f"Message sent by {ctx.author} in {server_channel} | contains the keywords:{keywords1} | message content: {ctx.content}"
                                )
                                if file_logging:
                                    write_keywords.write(
                                        f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Message sent by {ctx.author} in {server_channel} | contains the keywords:{keywords1}, | message content: {ctx.content}\n'
                                    )
                                if webhook_logging and len(webhook_url) > 1:
                                    embed = discord.Embed(
                                        color=discord.Color.blue(),
                                        timestamp=ctx.created_at,
                                    )
                                    embed.set_author(
                                        name=ctx.author.name,
                                        icon_url=ctx.author.avatar_url,
                                    )
                                    embed.description = f"Message containing keywords sent by {ctx.author.name}"
                                    embed.add_field(
                                        name="Keywords", value=keywords1, inline=False
                                    )
                                    if ctx.guild:
                                        embed.add_field(
                                            name="Server",
                                            value=ctx.guild.name,
                                            inline=False,
                                        )
                                        embed.add_field(
                                            name="Channel",
                                            value=ctx.channel.name,
                                            inline=False,
                                        )
                                    embed.add_field(
                                        name="Message", value=ctx.content, inline=False
                                    )
                                    async with aiohttp.ClientSession() as session:
                                        webhook = Webhook.from_url(
                                            webhook_url,
                                            adapter=AsyncWebhookAdapter(session),
                                        )
                                        await webhook.send(
                                            embed=embed, username="Keyword Logger"
                                        )

    @Cog.listener("on_message")
    async def mention_logger(self, ctx):
        if log_mentions:
            m_client_mention = client.user.mention
            d_client_mention = client.user.mention[:2] + "!" + client.user.mention[2:]
            if d_client_mention in ctx.content or m_client_mention in ctx.content:
                if ctx.guild:
                    server_channel = f"Server {ctx.guild.name} - {ctx.channel.name}"
                else:
                    server_channel = "DMs"
                if d_client_mention in ctx.content:
                    content = ctx.content.replace(
                        f"{d_client_mention}", f"@{client.user.name}"
                    )
                if m_client_mention in ctx.content:
                    content = ctx.content.replace(
                        f"{m_client_mention}", f"@{client.user.name}"
                    )
                print(
                    f"You've been mentioned by {ctx.author} in {server_channel}, Message content: {content}"
                )
                if file_logging:
                    if not os.path.exists(f"{documents}/logs/Mentions.txt"):
                        with open(f"{documents}/logs/Mentions.txt", "w") as o:
                            o.close()
                        with open(
                                f"{documents}/logs/Mentions.txt", "a"
                        ) as write_mentions_log:
                            write_mentions_log.write(
                                f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - {ctx.author} Has mentioned you in {server_channel}, Message content: {content}\n'
                            )
                if webhook_logging and len(webhook_url) > 1:
                    embed = discord.Embed(
                        color=discord.Color.blue(), timestamp=ctx.created_at
                    )
                    embed.set_author(
                        name=ctx.author.name, icon_url=ctx.author.avatar_url
                    )
                    embed.description = f"**You've been mentioned by:** {ctx.author}"
                    if ctx.guild:
                        embed.add_field(
                            name="Server", value=ctx.guild.name, inline=False
                        )
                        embed.add_field(
                            name="Channel", value=ctx.channel.name, inline=False
                        )
                    embed.add_field(name="Message", value=content, inline=False)
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(
                            webhook_url, adapter=AsyncWebhookAdapter(session)
                        )
                        await webhook.send(embed=embed, username="Mention Logger")

    @Cog.listener("on_message_delete")
    async def on_message_delete(self, message):
        if log_guild_updates:
            try:
                if not message.embeds:
                    member = message.author
                    embed = discord.Embed(
                        color=discord.Color.red(), timestamp=message.created_at
                    )
                    embed.set_author(name=member.name, icon_url=member.avatar_url)
                    embed.description = f"**message sent by **`{member.name}` **deleted in:**\n\n**Guild: **`{message.guild.name}`\n\n**Channel: **`{message.channel.name}`"
                    embed.add_field(
                        name="Message Deleted.", value=message.content, inline=False
                    )
                    if webhook_logging and len(webhook_url) > 1:
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(
                                webhook_url, adapter=AsyncWebhookAdapter(session)
                            )
                            await webhook.send(embed=embed, username="Message Deleted")
                    if file_logging:
                        if not os.path.exists(f"{documents}/logs/GuildActivities.txt"):
                            with open(
                                    f"{documents}/logs/GuildActivities.txt", "w"
                            ) as o:
                                o.close()
                        with open(
                                f"{documents}/logs/GuildActivities.txt",
                                "a",
                                encoding="utf-8",
                        ) as logfile:
                            logfile.write(
                                f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Message Sent by {member.name} in server {message.guild.name} - {message.channel.name} was deleted.\n Message content: "{message.content}"\n'
                            )
            except BaseException:
                pass

    @Cog.listener("on_message_edit")
    async def on_message_edit(self, before, after):
        if log_guild_updates:
            try:
                if not before.embeds:
                    member = after.author
                    embed = discord.Embed(
                        color=discord.Color.blue(), timestamp=after.created_at
                    )
                    if before.content != after.content:
                        jump_to_message = f"https://discordapp.com/channels/{after.guild.id}/{after.channel.id}/{after.id}"
                        embed.set_author(name=member.name, icon_url=member.avatar_url)
                        embed.description = f"**Message sent by **`{after.author.name}`** edited in server **`{after.guild.name}` **channel **`{after.channel.name}`\n[Jump to Message]({jump_to_message})"
                        embed.add_field(
                            name="Previous Message", value=before.content, inline=False
                        )
                        embed.add_field(
                            name="New Message", value=after.content, inline=False
                        )
                        if webhook_logging and len(webhook_url) > 1:
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(
                                    webhook_url, adapter=AsyncWebhookAdapter(session)
                                )
                                await webhook.send(
                                    embed=embed, username="Message Edited"
                                )
                        if file_logging:
                            if not os.path.exists(
                                    f"{documents}/logs/GuildActivities.txt"
                            ):
                                with open(
                                        f"{documents}/logs/GuildActivities.txt", "w"
                                ) as o:
                                    o.close()
                            with open(
                                    f"{documents}/logs/GuildActivities.txt",
                                    "a",
                                    encoding="utf-8",
                            ) as logfile:
                                logfile.write(
                                    f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Message sent by {member.name} in server {after.guild.name} - {after.channel.name} was edited.\nPrevious Message: "{before.content}"\nNew Message: "{after.content}"\n'
                                )
            except BaseException:
                pass

    @Cog.listener("on_member_ban")
    async def on_member_ban(self, guild, user):
        if log_guild_updates:
            embed = discord.Embed(
                color=discord.Color.red(), timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(name=user, icon_url=user.avatar_url)
            embed.description = f"User banned in {guild.name}"
            embed.add_field(name="Username", value=user, inline=False)
            embed.add_field(name="ID", value=f"`{user.id}`", inline=False)
            if webhook_logging and len(webhook_url) > 1:
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        webhook_url, adapter=AsyncWebhookAdapter(session)
                    )
                    await webhook.send(embed=embed, username="Member Banned")
            if file_logging:
                if not os.path.exists(f"{documents}/logs/GuildActivities.txt"):
                    with open(f"{documents}/logs/GuildActivities.txt", "w") as o:
                        o.close()
                with open(
                        f"{documents}/logs/GuildActivities.txt", "a", encoding="utf-8"
                ) as logfile:
                    logfile.write(
                        f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Member {user} was banned in server {guild.name}.\n'
                    )

    @Cog.listener("on_member_unban")
    async def on_member_unban(self, guild, user):
        if log_guild_updates:
            embed = discord.Embed(
                color=discord.Color.blue(), timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(
                name=f"Member unbanned in {guild.name}", icon_url=user.avatar_url
            )
            embed.add_field(name="Username", value=user, inline=False)
            embed.add_field(name="ID", value=f"`{user.id}`", inline=False)
            if webhook_logging and len(webhook_url) > 1:
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        webhook_url, adapter=AsyncWebhookAdapter(session)
                    )
                    await webhook.send(embed=embed, username="Member Unbanned")
            if file_logging:
                if not os.path.exists(f"{documents}/logs/GuildActivities.txt"):
                    with open(f"{documents}/logs/GuildActivities.txt", "w") as o:
                        o.close()
                with open(
                        f"{documents}/logs/GuildActivities.txt", "a", encoding="utf-8"
                ) as logfile:
                    logfile.write(
                        f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Member {user} was unbanned in server {guild.name}.\n'
                    )

    @Cog.listener("on_bulk_message_delete")
    async def on_bulk_message_delete(self, messages):
        if log_guild_updates:
            embed = discord.Embed(
                color=discord.Color.red(), timestamp=datetime.datetime.utcnow()
            )
            if messages[0].guild.icon_url:
                embed.set_author(
                    name=f"{messages[0].guild.name}",
                    icon_url=messages[0].guild.icon_url,
                )
            else:
                embed.set_author(name=f"{messages[0].guild.name}")
            embed.description = f"{len(messages)} Messages Purged In server {messages[0].guild.name} channel {messages[0].channel.name}"
            if webhook_logging and len(webhook_url) > 1:
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(
                        webhook_url, adapter=AsyncWebhookAdapter(session)
                    )
                    await webhook.send(embed=embed, username="Messages Purged")
            if file_logging:
                if not os.path.exists(f"{documents}/logs/GuildActivities.txt"):
                    with open(f"{documents}/logs/GuildActivities.txt", "w") as o:
                        o.close()
                with open(
                        f"{documents}/logs/GuildActivities.txt", "a", encoding="utf-8"
                ) as logfile:
                    logfile.write(
                        f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - {len(messages)} Purged in server {messages[0].guild.name} - {messages[0].channel.name}.\n'
                    )

    @Cog.listener("on_guild_update")
    async def on_guild_update(self, before, after):
        if log_guild_updates:
            try:
                embed = discord.Embed(
                    color=discord.Color.blue(), timestamp=datetime.datetime.utcnow()
                )
                if before.name != after.name:
                    embed.set_author(
                        name=f"Server {before.name} has been renamed",
                        icon_url=after.icon_url,
                    )
                    embed.add_field(name="Old Name", value=before.name, inline=False)
                    embed.add_field(name="New Name", value=after.name, inline=False)
                    if webhook_logging and len(webhook_url) > 1:
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(
                                webhook_url, adapter=AsyncWebhookAdapter(session)
                            )
                            await webhook.send(embed=embed, username="Server Renamed")
                    if file_logging:
                        if not os.path.exists(f"{documents}/logs/GuildActivities.txt"):
                            with open(
                                    f"{documents}/logs/GuildActivities.txt", "w"
                            ) as o:
                                o.close()
                        with open(
                                f"{documents}/logs/GuildActivities.txt",
                                "a",
                                encoding="utf-8",
                        ) as logfile:
                            logfile.write(
                                f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Server {before.name} has been renamed to {after.name}.\n'
                            )
                elif before.icon_url != after.icon_url:
                    if log_guild_updates:
                        embed.set_author(
                            name=f"Server {after.name} has changed it's icon",
                            icon_url=after.icon_url,
                        )
                        embed.set_thumbnail(url=after.icon_url)
                        if before.icon:
                            embed.description = f"[**old Icon**]({str(before.icon_url)})\n\n[**New Icon**]({str(after.icon_url)})"
                        else:
                            embed.description = f"[**New Icon**]({str(after.icon_url)})"
                        if webhook_logging and len(webhook_url) > 1:
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(
                                    webhook_url, adapter=AsyncWebhookAdapter(session)
                                )
                                await webhook.send(
                                    embed=embed, username="Server Icon Changed"
                                )
                        if file_logging:
                            if not os.path.exists(
                                    f"{documents}/logs/GuildActivities.txt"
                            ):
                                with open(
                                        f"{documents}/logs/GuildActivities.txt", "w"
                                ) as o:
                                    o.close()
                            with open(
                                    f"{documents}/logs/GuildActivities.txt",
                                    "a",
                                    encoding="utf-8",
                            ) as logfile:
                                logfile.write(
                                    f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Server {after.name} has changed its icon to {after.icon.url}.\n'
                                )
                    elif before.region != after.region:
                        if after.icon:
                            embed.set_author(
                                name=f"Server {after.name} has changed it's region",
                                icon_url=after.icon_url,
                            )
                            embed.set_thumbnail(url=after.icon_url)
                        else:
                            embed.set_author(
                                name=f"Server {after.name} has changed it's region"
                            )
                        embed.add_field(
                            name="Previous Region", value=before.region, inline=False
                        )
                        embed.add_field(
                            name="Current Region", value=after.region, inline=False
                        )
                        if webhook_logging and len(webhook_url) > 1:
                            async with aiohttp.ClientSession() as session:
                                webhook = Webhook.from_url(
                                    webhook_url, adapter=AsyncWebhookAdapter(session)
                                )
                                await webhook.send(
                                    embed=embed, username="Server Region Changed"
                                )
                        if file_logging:
                            if not os.path.exists(
                                    f"{documents}/logs/GuildActivities.txt"
                            ):
                                with open(
                                        f"{documents}/logs/GuildActivities.txt", "w"
                                ) as o:
                                    o.close()
                            with open(
                                    f"{documents}/logs/GuildActivities.txt",
                                    "a",
                                    encoding="utf-8",
                            ) as logfile:
                                logfile.write(
                                    f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - Server {after.name} has changed its region from {before.region} to {after.region}.\n'
                                )
            except BaseException:
                pass


class Configcog(commands.Cog):
    @command(
        name="config",
        aliases=get_aliases("config"),
        description="Display Config Commands.",
        usage=f"{prefix}config",
    )
    async def config_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"**{command.name}** - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Config Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Config Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="reload",
        aliases=get_aliases("reload"),
        description="Load your most recent config changes.",
        usage=f"{prefix}reload",
    )
    async def reload(self, ctx):
        load_config()
        print('Reloaded.')

    @command(name='restart',
             aliases=get_aliases('restart'),
             description='Fully restart the bot.',
             usage=f'{prefix}restart')
    async def restart(self, ctx):
        if os.path.exists(documents + '/desyncer.exe'):
            print('Restarting, please wait..')
            await client.logout()
            os.system(documents + '/desyncer.exe')
        else:
            printer('Executable not found, cant restart.')

    @command(
        name="aliases",
        aliases=get_aliases("aliases"),
        description="Add your own aliases to a command",
        usage=f"{prefix}aliases <add/remove> <command> <alias>",
    )
    async def aliases(self, ctx, action, commandname, alias):
        await ctx.message.delete()
        cmd = client.get_command(commandname)
        if cmd:
            if action == "add":
                if not os.path.exists(alias_file):
                    with open(alias_file, "w", encoding="utf-8") as o:
                        o.close()
                with open(alias_file, "r") as js_ctn:
                    data = js_ctn.read()
                    if len(data) > 2:
                        content = json.loads(data)
                    else:
                        content = {}
                    if cmd.name in content:
                        if alias in content[cmd.name]:
                            printer("Alias already exists.")
                            return
                    else:
                        content[cmd.name] = []
                    content[cmd.name].append(alias)
                    print(f"Added alias {alias} to command {cmd.name}.")
                    with open(alias_file, "w") as w_aliases:
                        w_aliases.write(json.dumps(content, indent=2))
            elif action == "remove":
                if not os.path.exists(alias_file):
                    with open(alias_file, "w", encoding="utf-8") as o:
                        o.close()
                with open(alias_file, "r") as js_ctn:
                    data = js_ctn.read()
                    if len(data) > 2:
                        content = json.loads(data)
                    else:
                        content = {}
                    content = json.loads(data)
                    if cmd.name in content:
                        if alias in content[cmd.name]:
                            content[cmd.name].remove(alias)
                            print(f"Removed alias {alias} from command {cmd.name}.")
                        else:
                            printer("Alias doesnt exist.")
                    else:
                        printer("Alias doesnt exist.")
                    with open(alias_file, "w") as w_aliases:
                        w_aliases.write(json.dumps(content, indent=2))
            else:
                printer("Invalid action.")
        else:
            printer("Invalid command name.")
        load_config()
        load_aliases()
        print(get_aliases(cmd.name))

    @command(
        name="sendembeds",
        aliases=get_aliases("sendembeds"),
        description="Set sending embeds to false/true.",
        usage=f"{prefix}sendembeds <false/true>",
    )
    async def sendembeds(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Settings"]["Send Embeds"] = True
                print("Sending embeds enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Settings"]["Send Embeds"] = False
                print("Sending embeds disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                print("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="deletetimer",
        aliases=get_aliases("deletetimer"),
        description="Change how long your embeds will be deleted after",
        usage=f"{prefix}deletetimer <seconds>",
    )
    async def deletetimer(self, ctx, value):
        await ctx.message.delete()
        try:
            value = int(value)
            with open(f"{documents}/files/config.json", "r") as r_c:
                data = r_c.read()
                content = json.loads(data)
                with open(f"{documents}/files/config.json", "w") as r_c:
                    content["Settings"]["Delete After"] = value
                    r_c.write(json.dumps(content, indent=2))
                    print("Changed deletion timer.")
            load_config()
        except BaseException:
            printer("Value must be a number.")

    @command(
        name="footertext",
        aliases=get_aliases("footertext"),
        description="Edit the footer text.",
        usage=f"{prefix}footertext <text>",
    )
    async def footertext(self, ctx, value):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
            with open(f"{documents}/files/config.json", "w") as r_c:
                content["Settings"]["Footer Text"] = value
                r_c.write(json.dumps(content, indent=2))
                print("Changed Footer text.")
        load_config()

    @command(
        name="embedhex",
        aliases=get_aliases("embedhex"),
        description="Edit the embed color hex.",
        usage=f"{prefix}embedhex <hex>",
    )
    async def embedhex(self, ctx, value):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
            with open(f"{documents}/files/config.json", "w") as r_c:
                content["Settings"]["Embed Color Hex"] = value
                r_c.write(json.dumps(content, indent=2))
                print("Changed embed color hex.")
        load_config()

    @command(
        name="webhookhex",
        aliases=get_aliases("webhookhex"),
        description="Edit the webhook color hex.",
        usage=f"{prefix}webhookhex <hex>",
    )
    async def webhookhex(self, ctx, value):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
            with open(f"{documents}/files/config.json", "w") as r_c:
                content["Settings"]["Webhook Color Hex"] = value
                r_c.write(json.dumps(content, indent=2))
                print("Changed webhook color hex.")
        load_config()

    @command(
        name="nitrosniper",
        aliases=get_aliases("nitrosniper"),
        description="Set nitro sniper to false/true.",
        usage=f"{prefix}nitrosniper <false/true>",
    )
    async def nitrosniper(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Sniper"]["Nitro Sniper"] = True
                print("Nitro sniper enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Sniper"]["Nitro Sniper"] = False
                print("Nitro sniper disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="snipernotifs",
        aliases=get_aliases("snipernotifs"),
        description="Set nitro sniper notifications to false/true.",
        usage=f"{prefix}snipernotifs <false/true>",
    )
    async def snipernotifs(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Sniper"]["Display Notifications"] = True
                print("Sniper notifications enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Sniper"]["Display Notifications"] = False
                print("Sniper notifications disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="giveawayjoiner",
        aliases=get_aliases("giveawayjoiner"),
        description="Set giveaway joiner to false/true.",
        usage=f"{prefix}giveawayjoiner <false/true>",
    )
    async def giveawayjoiner(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Giveaways"]["Giveaway Joiner"] = True
                print("Giveaway joiner enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Giveaways"]["Giveaway Joiner"] = False
                print("Giveaway joiner disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="joindelay",
        aliases=get_aliases("joindelay"),
        description="Edit the giveaway joiner delay.",
        usage=f"{prefix}joindelay <seconds>",
    )
    async def joindelay(self, ctx, value):
        await ctx.message.delete()
        try:
            value = int(value)
            with open(f"{documents}/files/config.json", "r") as r_c:
                data = r_c.read()
                content = json.loads(data)
                with open(f"{documents}/files/config.json", "w") as r_c:
                    content["Giveaways"]["Join Delay"] = value
                    r_c.write(json.dumps(content, indent=2))
                    print("Changed giveaway joiner delay")
            load_config()
        except BaseException:
            printer("Value must be a number.")

    @command(
        name="joinernotifs",
        aliases=get_aliases("joinernotifs"),
        description="Set giveaway joiner notifications to false/true.",
        usage=f"{prefix}joinernotifs <false/true>",
    )
    async def joinernotifs(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Giveaways"]["Display Notifications"] = True
                print("Giveaway joiner notifications enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Giveaways"]["Display Notifications"] = False
                print("Giveaway joiner notifications disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="autoreplier",
        aliases=get_aliases("autoreplier"),
        description="Set selfbot detection to false/true.",
        usage=f"{prefix}autoreplier <false/true>",
    )
    async def autoreplier(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Autoreplier"]["Autoreply"] = True
                print("Autoreplier enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Autoreplier"]["Autoreply"] = False
                print("Autoreplier disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="autoreplierdelay",
        aliases=get_aliases("autoreplierdelay"),
        description="Edit the autoreplier delay.",
        usage=f"{prefix}autoreplierdelay <seconds>",
    )
    async def autoreplierdelay(self, ctx, value):
        await ctx.message.delete()
        try:
            value = int(value)
            with open(f"{documents}/files/config.json", "r") as r_c:
                data = r_c.read()
                content = json.loads(data)
                with open(f"{documents}/files/config.json", "w") as r_c:
                    content["Autoreplier"]["Autoreply Delay"] = value
                    r_c.write(json.dumps(content, indent=2))
                    print("Changed autoreply delay")
            load_config()
        except BaseException:
            printer("Value must be a number.")

    @command(
        name="autorepliermessage1",
        aliases=get_aliases("autorepliermessage1"),
        description="Edit the first autoreplier message.",
        usage=f"{prefix}autorepliermessage1 <text>",
    )
    async def autorepliermessage1(self, ctx, value):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
            with open(f"{documents}/files/config.json", "w") as r_c:
                content["Autoreplier"]["Autoreply Message1"] = value
                r_c.write(json.dumps(content, indent=2))
                print("Changed first autoreply message")

        load_config()

    @command(
        name="autorepliermessage2",
        aliases=get_aliases("autorepliermessage2"),
        description="Edit the second autoreplier message.",
        usage=f"{prefix}autorepliermessage2 <text>",
    )
    async def autorepliermessage2(self, ctx, value):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        if value:
            with open(f"{documents}/files/config.json", "w") as r_c:
                content["Autoreplier"]["Autoreply Message2"] = value
                r_c.write(json.dumps(content, indent=2))
                print("Changed second autoreply message")
        load_config()

    @command(
        name="sbdetection",
        aliases=get_aliases("sbdetection"),
        description="Set selfbot detection to false/true.",
        usage=f"{prefix}sbdetection <false/true>",
    )
    async def sbdetection(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Detection"]["Selfbot Detection"] = True
                print("Selfbot detection enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Detection"]["Selfbot Detection"] = False
                print("Selfbot detection disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="sbdetectionnotifs",
        aliases=get_aliases("sbdetectionnotifs"),
        description="Set selfbot detection notifications to false/true.",
        usage=f"{prefix}sbdetectionnotifs <false/true>",
    )
    async def sbdetectionnotifs(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Detection"]["Display Notifications"] = True
                print("Selfbot detection notifications enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Detection"]["Display Notifications"] = False
                print("Selfbot detection notifications disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="filelogging",
        aliases=get_aliases("filelogging"),
        description="Set file logging to false/true.",
        usage=f"{prefix}filelogging <false/true>",
    )
    async def filelogging(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["File Logging"] = True
                print("File logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["File Logging"] = False
                print("File logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="webhooklogging",
        aliases=get_aliases("webhooklogging"),
        description="Set webhook logging to false/true.",
        usage=f"{prefix}webhooklogging <false/true>",
    )
    async def webhooklogging(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["Webhook Logging"] = True
                print("Webhook logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["Webhook Logging"] = False
                print("Webhook logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="logguildactivities",
        aliases=get_aliases("logguildactivities"),
        description="Set guild activities logging to false/true.",
        usage=f"{prefix}logguildactivities <false/true>",
    )
    async def logguildactivities(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["Log Guild Activities"] = True
                print("Guild activities logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["Log Guild Activities"] = False
                print("Guild activities logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="lognitrosniper",
        aliases=get_aliases("lognitrosniper"),
        description="Set nitro sniper logging to false/true.",
        usage=f"{prefix}lognitrosniper <false/true>",
    )
    async def lognitrosniper(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["Log Nitro Sniper"] = True
                print("Nitro sniper logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["Log Nitro Sniper"] = False
                print("Nitro sniper logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="loggiveawayjoiner",
        aliases=get_aliases("loggiveawayjoiner"),
        description="Set giveaway joiner logging to false/true.",
        usage=f"{prefix}loggiveawayjoiner <false/true>",
    )
    async def loggiveawayjoiner(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["Log Giveaway Joiner"] = True
                print("Giveaway joiner logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["Log Giveaway Joiner"] = False
                print("Giveaway joiner logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="logsbdetection",
        aliases=get_aliases("logsbdetection"),
        description="Set selfbot detection logging to false/true.",
        usage=f"{prefix}logsbdetection <false/true>",
    )
    async def logsbdetection(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["Log Selfbot Detection"] = True
                print("Selfbot detection logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["Log Selfbot Detection"] = False
                print("Selfbot detection logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="logkeywords",
        aliases=get_aliases("logkeywords"),
        description="Set keyword logging to false/true.",
        usage=f"{prefix}logkeywords <false/true>",
    )
    async def logkeywords(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["Log Keywords"] = True
                print("Keywords logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["Log Keywords"] = False
                print("Keywords logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()

    @command(
        name="logmentions",
        aliases=get_aliases("logmentions"),
        description="Set mention logging to false/true.",
        usage=f"{prefix}logmentions <false/true>",
    )
    async def logmentions(self, ctx, toggle):
        await ctx.message.delete()
        with open(f"{documents}/files/config.json", "r") as r_c:
            data = r_c.read()
            content = json.loads(data)
        with open(f"{documents}/files/config.json", "w") as w_c:
            if toggle.lower() == "true":
                content["Logging"]["Log Mentions"] = True
                print("Mention logging enabled.")
                w_c.write(json.dumps(content, indent=2))
            elif toggle.lower() == "false":
                content["Logging"]["Log Mentions"] = False
                print("Mention logging disabled.")
                w_c.write(json.dumps(content, indent=2))
            else:
                printer("Toggle invalid. use true/false")
                w_c.write(json.dumps(content, indent=2))
        load_config()


class Gamecog(commands.Cog):
    @command(
        name="game",
        aliases=get_aliases("game"),
        description="Display Game Commands.",
        usage=f"{prefix}game",
    )
    async def tools_cmd(self, ctx, page=1):
        try:
            page = int(page)
            await ctx.message.delete()
            cm = [
                f"{command.name} - {command.description}\n"
                for command in ctx.cog.walk_commands()
                if command != ctx.command
            ]
            cm = [cm[x: x + 10] for x in range(0, len(cm), 10)]
            cmds = "".join(cm[page - 1])
            if not cmds:
                printer("Page does not exist.")
            if send_embeds:
                embed = discord.Embed(
                    color=embed_color,
                    title=f"Game Commands",
                    description=f"{cmds}\n**({page}/{len(cm)})**",
                )
                embed.set_footer(icon_url=footer_url, text=footer_text)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(f"```Game Commands\n\n{cmds}\n({page}/{len(cm)})```")
        except IndexError:
            printer("Page does not exist.")
        except ValueError:
            printer("Argument must be a number.")

    @command(
        name="league",
        aliases=get_aliases("league"),
        description="Show league of legends player stats.",
        usage=f"{prefix}league <region> <summoner>",
    )
    async def league(self, ctx, region, *, summoner):
        platforms = {
            "br": "br1",
            "eune": "eun1",
            "euw": "euw1",
            "jp": "jp1",
            "kr": "kr",
            "lan": "la1",
            "las": "la2",
            "na": "na1",
            "oce": "oc1",
            "tr": "tr1",
            "ru": "ru",
        }
        if region not in platforms:
            printer("Invalid region.")
            return
        await ctx.message.delete()
        reg = platforms[region]
        try:
            summ = lol_watcher.summoner.by_name(reg, summoner)
            rs = lol_watcher.league.by_summoner(reg, summ["id"])[0]
        except:
            printer("Invalid Summoner")
            return
        tier = rs["tier"]
        lp = rs["leaguePoints"]
        wins = rs["wins"]
        losses = rs["losses"]
        rank = rs["rank"]
        icon = f'http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/{summ["profileIconId"]}.png'
        embed = discord.Embed(color=embed_color)
        embed.title = f'Displaying ranked stats for - {summ["name"]}.'
        winrate = f"{round(wins / (wins + losses) * 100)}%"
        icon = f'http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/{summ["profileIconId"]}.png'
        embed = discord.Embed(color=embed_color)
        embed.title = f'Displaying ranked stats for - {summ["name"]}.'
        if rs:
            if send_embeds:
                embed.add_field(name="Tier", value=tier, inline=False)
                embed.add_field(name="Rank", value=rank)
                embed.add_field(name="LP", value=lp, inline=False)
                embed.add_field(
                    name="Wins/Losses", value=f"{wins}/{losses}", inline=False
                )
                embed.add_field(name="Winrate", value=winrate, inline=False)
                embed.set_thumbnail(url=icon)
                embed.description = (
                    f"[op.gg](https://{region}.op.gg/summoner/userName={summoner})"
                )
                embed.set_footer(text=footer_text, icon_url=footer_url)
                await ctx.send(embed=embed, delete_after=delete_after)
            else:
                await ctx.send(
                    f'```Displaying ranked stats for {summ["name"]}\n\n+ Tier: {tier}\n+ Rank: {rank}\n+ LP: {lp}\n+ Wins/Losses: {wins}/{losses}\n+ Winrate: {winrate}```'
                )
        else:
            await ctx.send(f"No ranked data found for {summoner}")

    @command(
        name="mcplayer",
        aliases=get_aliases("mcplayer"),
        description="Get info about a minecraft player",
        usage=f"{prefix}mcplayer <username>",
    )
    async def mcplayer(self, ctx, *, username):
        await ctx.message.delete()
        userid = requests.get(
            f"https://api.mojang.com/users/profiles/minecraft/{username}"
        ).json()["id"]
        name_history = requests.get(
            f"https://api.mojang.com/user/profiles/{userid}/names"
        ).json()
        names = []
        num = 1
        for name in name_history:
            if num <= 1:
                names.append(f'\nOriginal - {name["name"]}')
            else:
                names.append(
                    f'\n{unixtodate(str(name["changedToAt"])[:10])[:10]} - {name["name"]}'
                )
            num = num + 1
        if send_embeds:
            embed = discord.Embed(
                color=embed_color, title=f"Minecraft User - {username}"
            )
            embed.add_field(name="UUID", value=userid, inline=False)
            embed.add_field(name="Name History", value=f"".join(names), inline=False)
            embed.set_footer(text=footer_text, icon_url=footer_url)
            embed.set_thumbnail(url="https://www.freeiconspng.com/img/16689")
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            await ctx.send(
                f'```Minecraft User - {username}\n\nName History:{"".join(names)}```'
            )

    @command(
        name="mcserverlookup",
        aliases=get_aliases("mcserverlookup"),
        description="Get information on a minecraft server",
        usage=f"{prefix}mcserverlookup <ip/domain>",
    )
    async def mcserverlookup(self, ctx, domain):
        await ctx.message.delete()
        page = requests.get(f"https://api.mcsrvstat.us/2/{domain}").json()
        try:
            ip_port = (
                    str(page["ip"])
                    + ":"
                    + str(page["port"]).replace("[", "").replace("[", "")
            )
            players = page["players"]
            version = page["version"]
            online = page["online"]
            protocol = page["protocol"]
            hostname = page["hostname"]
            if send_embeds:
                players = f"  Online: {players['online']}\n  Max: {players['max']}"
            else:
                players = f"  Online: {players['online']}\n  Max: {players['max']}"
        except BaseException:
            printer("Server Offline.")
            return
        if send_embeds:
            embed = discord.Embed(
                color=embed_color, title=f"Minecraft Server - {domain}"
            )
            embed.add_field(name="IP", value=ip_port, inline=False)
            embed.add_field(name="Online", value=online, inline=False)
            embed.add_field(name="Players", value=players, inline=False)
            embed.add_field(name="Version", value=version, inline=False)
            if "mods" in page:
                embed.add_field(name="Modded", value="true", inline=False)
            if "plugins" in page:
                embed.add_field(name="Plugins", value="true", inline=False)
            embed.add_field(name="Protocol", value=protocol, inline=False)
            embed.add_field(name="Host Name", value=hostname, inline=False)
            embed.set_thumbnail(url="https://mcsrvstat.us/img/minecraft.png")
            embed.set_footer(text=footer_text, icon_url=footer_url)
            await ctx.send(embed=embed, delete_after=delete_after)
        else:
            if "plugins" in page and "mods" in page:
                await ctx.send(
                    f"```Minecraft Server - {domain}\n+ IP: {ip_port}\n+ Online: {online}\n+ Players:\n{players}\n+ Version: {version}\n+ Modded: true\n+ Plugins: true\n+ Protocol: {protocol}\n+ Host Name: {hostname}```"
                )
            elif "mods" in page:
                await ctx.send(
                    f"```Minecraft Server - {domain}\n+ IP: {ip_port}\n+ Online: {online}\n+ Players:\n{players}\n+ Version: {version}\n+ Modded: true\n+ Protocol: {protocol}\n+ Host Name: {hostname}```"
                )
            elif "plugins" in page:
                await ctx.send(
                    f"```Minecraft Server - {domain}\n+ IP: {ip_port}\n+ Online: {online}\n+ Players:\n{players}\n+ Version: {version}\n+ Plugins: true\n+ Protocol: {protocol}\n+ Host Name: {hostname}```"
                )
            else:
                await ctx.send(
                    f"```Minecraft Server - {domain}\n+ IP: {ip_port}\n+ Online: {online}\n+ Players:\n{players}\n+ Version: {version}\n+ Protocol: {protocol}\n+ Host Name: {hostname}```"
                )

    @command(
        name="mcseedlookup",
        aliases=get_aliases("mcseedlookup"),
        description="Lookup a minecraft seed.",
        usage=f"{prefix}mcseedlookup <seed>",
    )
    async def mcseedlookup(self, ctx, seed):
        await ctx.message.delete()
        page = f"https://www.chunkbase.com/apps/biome-finder#{seed}"
        await ctx.send(page)


# @client.event
# async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandInvokeError):
#        error = error.original
#        printer(str(error))
#    elif isinstance(error, commands.CommandNotFound):
#        pass
#    elif isinstance(error, commands.CheckAnyFailure):
#        printer("Insufficient permissions.")
#    elif isinstance(error, commands.MemberNotFound):
#        printer("Member not found.")
#    elif isinstance(error, commands.RoleNotFound):
#        printer("Role not found")
#    elif isinstance(error, commands.UserNotFound):
#        printer("User not found")
#    elif isinstance(error, commands.BadArgument):
#        printer("Bad argument.")
#    elif isinstance(error, commands.MissingRequiredArgument):
#        printer(str(error))
#    elif isinstance(error, commands.EmojiNotFound):
#        pass
#    elif isinstance(error, discord.errors.NotFound):
#        pass
#    else:
#        try:
#            raise error
#        except Exception as e:
#            exc_type, exc_obj, exc_tb = sys.exc_info()
#            printer(
#                f"Error: {error}\nIf you believe you should not be receiving this error please contact the developer"
#            )
#            if send_errors:
#                embed = discord.Embed(color=discord.Color.red())
#                embed.set_author(name="New Error", icon_url=footer_url)
#                embed.add_field(name="Caused by user", value=client.user, inline=False)
#                embed.add_field(name="Command", value=ctx.command.name, inline=False)
#                embed.add_field(name="Error", value=error, inline=False)
#                embed.set_footer(text=f"Desyncer v{desyncer_version}", icon_url=footer_url)
#                embed.set_thumbnail(url=footer_url)
#                async with aiohttp.ClientSession() as session:
#                    webhook = Webhook.from_url(
#                        "https://discord.com/api/webhooks/808010467414638622/P6MnG4yzkhzb2CHUuckpdANdtnq3NxB9Ev9hdLllQ1oY7DRmN1i3GVMdkXW4vOLfjGaj",
#                        adapter=AsyncWebhookAdapter(session),
#                    )
#                    await webhook.send(embed=embed, username="Desyncer")
#
#
#
# @client.event
# async def on_error(event, *args, **kwargs):
#    pass


client.add_cog(Help())
client.add_cog(Admincog())
client.add_cog(Detectorcog())
client.add_cog(Loggingcog())
client.add_cog(NSFWcog())
client.add_cog(Abusecog())
client.add_cog(Sniperscog())
client.add_cog(Configcog())
client.add_cog(Imagecog())
client.add_cog(Gamecog())
client.add_cog(Toolscog())
client.add_cog(Usercog())
client.add_cog(Textcog())
client.add_cog(Infocog())
client.add_cog(Funcog())
try:
    client.run(token, bot=False)
except discord.errors.LoginFailure:
    printer("Your discord token is invalid.")
    time.sleep(5)
    sys.exit(1)
except:
    printer('There has been an error logging in to your discord account.')

people = []





