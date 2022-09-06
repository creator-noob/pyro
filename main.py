#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE



import requests
import json
import subprocess
from pyrogram import Client,filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
from pyrogram import Client, filters
import tgcrypto
from p_bar import progress_bar

from subprocess import getstatusoutput
import helper
import logging
import time
import aiohttp
import asyncio
import aiofiles
from pyrogram.types import User, Message
import sys
import re
import os
import cloudscraper

from dotenv import load_dotenv
load_dotenv()
os.makedirs("./downloads", exist_ok=True)
#API_ID = 14560088
#API_HASH = "74a2665339484da3eaaed5f4fe16da79"
#BOT_TOKEN = "5524381543:AAH-s7TDhvA_Ng2k9U5z9pvgiRPy5ChNve8"
#NAME = "BlackOuT"
#API_ID = os.getenv('API_ID')
#API_HASH = os.getenv('API_HASH')
#BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Client(
    "bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

@bot.on_message(filters.command(["start"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello im txt file downloader\nPress /pyro to download links listed in a txt file in the format **Name:link**\n\nBot made by BlackOuT")

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["link"])& ~filters.edited)
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('Send link in **Name&link** format to download')
    input9: Message = await bot.listen(editable.chat.id)
    raw = input9.text    
    name = raw.split('&')[0]
    url0 = raw.split('&')[1] or raw
    url = url0.replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    
    Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
    prog = await m.reply_text(Show)
    
    cc = f'>> **Name :** {name}'
    
    path = f"./downloads/"

    if raw_text2 =="360":
            
       cmd = f'yt-dlp -F "{url}"'
       k = await helper.run(cmd)
       out = helper.vid_info(str(k))
                # print(out)             
       if '640x360' in out:
           ytf = out['640x360']
       elif '638x360' in out:
           ytf = out['638x360']
       elif '636x360' in out:
           ytf = out['636x360']
       elif '768x432' in out:
           ytf = out['768x432']
       elif '638x358' in out:
           ytf = out['638x358']
       elif '852x316' in out:
           ytf = out['852x316']
       elif '850x480' in out:
           ytf = out['850x480']
       elif '848x480' in out:
           ytf = out['848x480']
       elif '854x480' in out:
           ytf = out['854x480']
       elif '852x480' in out:
           ytf = out['852x480']
       elif '854x470' in out:
           ytf = out['852x470']  
       elif 'unknown' in out:
           ytf = out["unknown"]
       else:
           ytf = "no"

    elif raw_text2 =="480":
                
       cmd = f'yt-dlp -F "{url}"'
       k = await helper.run(cmd)
       out = helper.vid_info(str(k))
                # print(out)               
       if '854x480' in out:
           ytf = out['854x480']
       elif '852x480' in out:
           ytf = out['852x480']                        
       elif '854x470' in out:
           ytf = out['854x470']  
       elif '768x432' in out:
           ytf = out['768x432']
       elif '848x480' in out:
           ytf = out['848x480']
       elif '850x480' in out:
           ytf =['850x480']
       elif '960x540' in out:
           ytf = out['960x540']
       elif '640x360' in out:
           ytf = out['640x360']   
       elif 'unknown' in out:
           ytf = out["unknown"]                     
       else:
           ytf = "no"

                   
    elif raw_text2 =="720":
                
          cmd = f'yt-dlp -F "{url}"'
          k = await helper.run(cmd)
          out = helper.vid_info(str(k))
                # print(out)           
          if '1280x720' in out:
              ytf = out['1280x720'] 
          elif '1280x704' in out:
              ytf = out['1280x704'] 
          elif '1280x474' in out:
              ytf = out['1280x474'] 
          elif '1920x712' in out:
              ytf = out['1920x712'] 
          elif '1920x1056' in out:
              ytf = out['1920x1056']    
          elif '854x480' in out:
              ytf = out['854x480']                        
          elif '640x360' in out:
              ytf = out['640x360']     
          elif 'unknown' in out:
              ytf = out["unknown"]              
          else:
              ytf = "no"

    if "youtu" in url:
        cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mkv "{url}"'
    elif ("/brightcove/" in url ):
        ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba"   
    elif "m3u8" or "livestream" in url:
        cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
    elif ytf == "0" or "unknown" in out:
        cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
    elif ".pdf" in url:
        cmd = "pdf"
    elif "drive" in url:
        cmd = "pdf"
    elif ytf == "no":
        cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url}"'
    else:
        cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'  
    try:
        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
        os.system(download_cmd)
        filename = f"{name}.mp4"
        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
        thumbnail = f"{filename}.jpg"
        dur = int(helper.duration(filename))
        await prog.delete (True)
        await m.reply_video(f"{name}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur)
        os.remove(f"{name}.mp4")
        os.remove(f"{filename}.jpg")
    except Exception as e:
        await m.reply_text(e)
        
         
    
# @bot.on_message(filters.command(["link"])& ~filters.edited)
# async def account_login(bot: Client, m: Message):
#     editable = await m.reply_text('Send **Name&link** to download')

#     input: Message = await bot.listen(editable.chat.id)
#     raw_file = input.text

#     name = raw_file.split('&')[0]
#     url = raw_file.split('&')[1]

@bot.on_message(filters.command(["pyro"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable = await m.reply_text("**Enter Batch Name**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    editable7= await m.reply_text("**Downloaded By : **")
    input7 = Message = await bot.listen(editable.chat.id)
    raw_te = input7.text
    
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)    

    
    try:
        for i in range(arg, len(links)):    
            url = links[i][1].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
            name = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()
            
            Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`\n\n"
            prog = await m.reply_text(Show)
            cc = f"**{count}) Title :** {name}\n\n**Quality :** {raw_text2}\n**Batch :** {raw_text0}\n**𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 :** {raw_te}\n**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝗕𝗹𝗮𝗰𝗸𝗢𝘂𝗧 (•̪●)=︻╦̵̵̿╤── **\n**𝗣𝗹𝘇 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 : https://www.youtube.com/channel/UC7udfRGdD_QoCg-OnSooGAA**"
            #cc = f'>> **Name :** {name}\n>> **Title :** {raw_text0}\n\n>> **Bot Owner:»»» 𝗕𝗹𝗮𝗰𝗸𝗢𝘂𝗧 ¯\_(ツ)_/¯**\n\n>> **Index :** {count}'
            if "youtu" in url:
                if raw_text2 in ["144", "240", "480"]:
                    ytf = f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'
                elif raw_text2 == "360":
                    ytf = "18/134"
                elif raw_text2 == "720":
                    ytf = "22/136/18"
                elif raw_text2 =="1080":
                    ytf = "137/399"
                else:
                    ytf = 18
            else:
                ytf=f"bestvideo[height<={raw_text2}]"

            if "jwplayer" in url:
                if raw_text2 in ["180", "144"]:
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['320x180 ']}/{out['256x144 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
                elif raw_text2 in ["240", "270"]:
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['480x270 ']}/{out['426x240 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
                elif raw_text2 == "360":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = out['640x360 ']
                    except Exception as e:
                        if e == 0:
                            raw_text2=="no"
                #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                elif raw_text2 == "480":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['960x540 ']}/{out['852x480 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
            # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                elif raw_text2 == "720":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['1280x720 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
            # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                elif raw_text2 == "1080":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf =f"{out['1920x1080 ']}/{['1920x1056']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
                else:
            # cmd = f'yt-dlp -F "{url}"'
            # k = await helper.run(cmd)
            #out = helper.vid_info(str(k))
            # ytf = out['640x360 ']
            #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                    raw_text2=="no"
#             except Exception as e:
#                 print(e)

            if ytf == f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]':
                 cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}" "{url}"'
    
               #elif "jwplayer" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
                    #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'    
            elif "adda247" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
                cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            elif "kdcampus" or "streamlock" in url:
                cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            elif ".pdf" in url: #and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
                cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
            elif "drive" in url:
                cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
            elif raw_text2 == "no":# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
                cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            #elif "unknown" in ytf:
                    #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}+bestaudio" "{url}"'

            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                filename = f"{name}.mp4"
                subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                reply = await m.reply_text("Uploading Video")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))
                dur = int(helper.duration(filename))
                await prog.delete (True)
                start_time = time.time()
                await m.reply_video(f"{name}.mp4",supports_streaming=True,height=720,width=1280,caption=cc,duration=dur,thumb=thumbnail, progress=progress_bar,progress_args=(reply,start_time) )
                count += 1
                os.remove(f"{name}.mp4")
                os.remove(f"{filename}.jpg")
                await reply.delete(True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(e)
                continue
    except Exception as e:
          await m.reply_text(str(e))  
    await m.reply_text("Done")  
    
    
@bot.on_message(filters.command(["top"])& ~filters.edited)
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"**Hi im Topranker dl**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0
    editable = await m.reply_text("**Enter Batch Name**")
    input8: Message = await bot.listen(editable.chat.id)
    raw_text8 = input8.text
    
    editable7= await m.reply_text("**Downloaded By : **")
    input7 = Message = await bot.listen(editable.chat.id)
    raw_te = input7.text
    
    editable = await m.reply_text(f"**Copy Paste the App Name **\n\n`anytimelearningtopranker`\n\n`anytimelearningmaster`\n\n`englishmantraonline`\n\n`Iassetu`\n\n`Exammantra`\n\n`Abhiyamlive`\n\n`vikramjeet`\n\n`sure60`\n\n`theoptimistclasses`")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
           
    count =int(raw_text)    
    try:
        for i in range(arg, len(links)):
        
            url = links[i][1]
            name = links[i][0].replace(" : ", " ").replace(" :- ", " ").replace(" :-", " ").replace(":-", " ").replace("_", " ").replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#","").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace("&", "").strip()
                # await m.reply_text(name +":"+ url)

            # Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
            # prog = await m.reply_text(Show)
            # cc = f'>> **Name :** {name}\n>> **Title :** {raw_text0}\n\n>> **Index :** {count}'
            if raw_text0 in "Iassetu":
                y = url.replace("/", "%2F")
                #rout = f"https://www.iassetu.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.iassetu.com%2Fvideo-edited%2F{y[56:-14]}%2Fmaster.m3u8"
                rout = f"https://www.iassetu.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.iassetu.com%2Fliveht{y[39:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)
            if raw_text0 in "Exammantra":
                y = url.replace("/", "%2F")
                #rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2Flive-http-origin-480-360-240%2F{y[56:-14]}%2Fmaster.m3u8"
                rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2F{y[39:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)
            if raw_text0 in "Abhiyamlive":
                y = url.replace("/", "%2F")
                #rout = f"https://live.abhayamacademy.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.abhayamacademy.com%2Flivehttporigin%2Fvideo-edited%2F{y[56:-14]}%2Fmaster.m3u8"
                rout = f"https://live.abhayamacademy.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.abhayamacademy.com%2{y[39:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)

            if raw_text0 in "vikramjeet" :
                y= url
                x =requests.get("https://www.toprankers.com/route?route=item/liveclasses&id="+y+"&response-type=2&fromapp=1&loadall=1&clientView=1&liveFromCDN=1&clientVersion=5.9")
                z=x.json()["data"]["tr1info"]["primPlaybackUrl"]
                #name=x.json()["data"]["title"]
                rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream={z}"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)
            elif raw_text0 in "sure60":
                y= url.replace("/", "%2F")
                rout = f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2Flivehttporigin%2F{y[49:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"            
            elif raw_text0 in "theoptimistclasses":
                y= url.replace("/", "%2F")
                rout=f"https://live.theoptimistclasses.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.theoptimistclasses.com%2F{y[44:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')              
                cook = "cookie.txt"
                
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{z}`"
            prog = await m.reply_text(Show)
            cc = f"**{count}) Title :** {name}\n\n**Batch :** {raw_text8}\n**𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 :** {raw_te}\n**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝗕𝗹𝗮𝗰𝗸𝗢𝘂𝗧 (•̪●)=︻╦̵̵̿╤── **\n**𝗣𝗹𝘇 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 : https://www.youtube.com/channel/UC7udfRGdD_QoCg-OnSooGAA**"

            cmd = f'yt-dlp -o "{name}.mp4" --cookies {cook} "{z}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                filename = f"{name}.mp4"
                subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                await prog.delete (True)
                reply = await m.reply_text(f"Uploading - ```{name}```")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()

                await m.reply_video(f"{name}.mp4",supports_streaming=True,height=720,width=1280,caption=cc,duration=dur,thumb=thumbnail, progress=progress_bar,progress_args=(reply,start_time) )
                count+=1
                os.remove(f"{name}.mp4")

                os.remove(f"{filename}.jpg")
                os.remove(cook)
                await reply.delete (True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - ```{url}```")
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")
bot.run()
