# -*- coding: utf-8 -*-


import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, tempfile, glob, shutil, unicodedata, goslate
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="Eo59LeKBUaH3ZZVTDii4.UTQPME8r/szgvvUFPpSxXa.mIsqKqe0PAT39iPJti/YzS5xtsM5w57AgRd2zPKFgdg=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EodpPhIKKsiPkuVd7e46.bOvOGCf2RHfeZhv4yDfqvG.n5nN83+AWG41FQ1csPzKKy2baOaec+hZ8s6pKTkBd2Q=")
ki.loginResult()

ki2= LINETCR.LINE()
ki2.login(token="Eoft6jpMD5Wa4tSxfru7.Bi52EVS1f6pnSUQ8Si6kfW.vzFtSqH9JEfBGziXzonNptjBPOzPmq0MePELOYn9AHw=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EoGly4ErjyNci2b2Aai6.lW4U9ah5dzBuriFhLNTmHG.a9UcqRtvn9SXee/FY/Lncku0h0JQkzx+oAAomUBZg1g=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EolvvpoJjhtCv2aSGm58.bKxbyGM6feSgEY6806oLQa.EcNMYRBztZNdbj5f5xEy0/eTXM+LSinNQAIohKSLpNM=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EoMxFoHh1Y7Jm8Ob1T13.4xqN84T1S5cNUGFR9jI9mW.ORdX++cgS3fXLJXwB/4ItqvahJBvJ/+AVHlN/2DNJ+w=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EolAeFfggVClfau9ITG6.j9TG5+XBn+eEz8gjSQSKzG.zVcTjObfKdRu0cVfFxf6dzhcvFgP13/0vT7ItYHhNkI=")
ki6.loginResult()

ki7 = LINETCR.LINE() #Bot 7
ki7.login(token="Eo7nriEBzsTFBTHRP789.hISJl0t4r6pkGlJjGMG1wq.VYEk+9edKBQD8w7QOoOhYplvAVb7HjFFJrdCa/7Hdtk=")
ki7.loginResult()

ki8 = LINETCR.LINE() #Bot 8
ki8.login(token="EoVqUo2NplyZfu1Asncb.1YsQzRhTiLU/0wktv1FLgW.76FvjQL/n3D3rLgxbuL1uxeA/5hFnjbSiSk4wDB1FHY=")
ki8.loginResult()

ki9 = LINETCR.LINE() #Bot 9
ki9.login(token="EojzzjAbMjvLVEopA18b.PgnzRce05tAF+VfXo1F9QW.WePo4CqqEaAK6B5kOdrjcM08K/QdxBiaeUQeiazsAy0=")
ki9.loginResult()

ki10 = LINETCR.LINE() #Bot 10
ki10.login(token="Eo57AFGqLLbo4uddFbv5.4hTev1acVvrggAo7mbEKjq.OFBmL0dJ4h9SQNeEig2LC1G8jzdLEFygbY4qx6IlMpY=")
ki10.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage="""(╣••℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́••╣)
          『B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́』
  ✰ Me
  ✰ Add
  ✰ Cn "text"
  ✰ Clockname "text"
  ✰ TL:"text"
  ✰ Ban:"mid"
  ✰ Unban:"mid"
  ✰ Bl:on
  ✰ Unbl:on
  ✰ Mcheck
  ✰ Mybio:
  ✰ Mybots
  ✰ Mymid
  ✰ Mygroups
  ✰ Group id
  ✰ Message set:"text"
  ✰ Message confirm
  ✰ Msg add-"text"
  ✰ Com set:"text"
  ✰ Comment
  ✰ Comban/del/cek
  ✰ Help set:"text"
  ✰ Change
  ✰ Gn "text"
  ✰ Clink/Curl
  ✰ Kick:"mid"
  ✰ Invite:"mid"
  ✰ Creator
  ✰ Contact
  ✰ Gcancel:"jumlah"
  ✰ Gcancelall
  ✰ Ginfo
  ✰ Check
  ✰ Cctv
  ✰ Glink
  ✰ Spam on/off
  ✰ Gurl
  ✰ Clink
  ✰ Blocklist
  ✰ Banlist
  ✰ Update
  ✰ Creator
  ✰ Sc:"mid"
  ✰ Ban "@"
  ✰ Unban "@"
  ✰ Sc @
  ✰ Nuke
  ✰ Backup
  ✰ Tagall
  ✰ Bc "text"
  ✰ Say "text"
  ✰ Bom "text"
  ✰ Kick@mbl 
  ✰ Audio "text"
  ✰ Reinvite
  ✰ Clearban
  ✰ Clear 
  ✰ jointicket
  ✰ Youtube *text*
  ✰ Youtubesearch *user*
  ✰ Copy @     
  ✰ Backup @           
  ✰ Getcover @    
  ✰ Getbio @
  ✰ Getinfo @
  ✰ Gimage 
  ✰ Lirik "text"
  ✰ pict @️
  ✰ Steal @
  ✰ Micadd
  ✰ Micdel
  ✰ Checkdate
  ✰ Miclist
  ✰ Getname @
  ✰ Getinfo @
  ✰ Getcontact @
  ✰ Getvid @
  ✰ Getmid @
  ✰ Memlist
  ✰ Gid
  ✰ Steal @
  ✰ Grupname
  ✰ Setimage:
  ✰ Papimage
  ✰ Setvideo:
  ✰ Papvideo
  ✰ Myname
  ✰ Mybio
  ✰ Mypict
  ✰ Myvid
  ✰ Urlpict
  ✰ Mycover
  ✰ Urlcover
  ✰ Time
  ✰ Reboot
  ✰ Image *text*
  ✰ Lurk:on/off
  ✰ Lurkers
  ✰ Wc️
  ✰ Spam @
  ✰ Spam gift️
  ✰ Gift @
  ✰ Ig "name"
  ✰ Set
  ✰ Clear
  ✰ {Helpbots}
  ✰ {Settings}
  """
helpself="""╔{C༘֮֮O༘֮֮M༘֮֮M༘֮֮A༘֮֮N༘֮֮D༘֮֮ ֮A༘֮֮L༘֮֮L༘֮֮ ֮B༘֮֮O༘֮֮T༘֮֮S༘֮֮}╗
  ✰ Fuck1/10 "@"
  ✰ Kick1/10 "@"
  ✰ All mid
  ✰ B:out "leave all group"
  ✰ B1-10 mid
  ✰ B1-10name "text"
  ✰ B1-10
  ✰ B1-10 gift
  ✰ B1-10 in
  ✰ B1-10 bye
  ✰ Allgift
  ✰ Spam gift️
  ✰ All:
  ✰ Allbio:
  ✰ Masuk
  ✰ Keluar
  ✰ Cancel/Bcancel
  """
helpset="""(╣ S༘̏̏Ȅ༘̏T༘̏̏T༘̏̏Ȉ༘̏N༘̏̏G༘̏̏ ̏B༘̏̏Ȍ༘̏T༘̏̏S༘̏̏.╣)
  ✰ Ban:on/Unbl:on
  ✰ Contact:on/off
  ✰ Add:on/off
  ✰ Join:on/off
  ✰ Leave:on/off
  ✰ Share:on/off
  ✰ Com:on/off
  ✰ Clock:on/off
  ✰ Respon:on/off
  ✰ Notag:on/off
  ✰ Mimic on/off
  ✰ Auto read:0n/off
  ✰ Like:on/off
  ✰ Runtime
    (╣S̰֮֮Ḛ֮֮T̰֮֮T̰֮֮Ḭ֮֮N̰֮֮G̰֮֮ ֮G̰֮֮R̰֮֮O̰֮֮Ṵ֮֮P̰֮֮S̰֮֮╣)
  ★ Pro:on/off
  ★ Prolink:on/off
  ★ Proinvite:on/off
  ★ Procancel:on/off
     『B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́』
(╚••℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́••╝)
"""
helo="====I AM SELFBOT TEAM BLACK OF GAMER"

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid]
admsa = "mid"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""❂••••••••AUTO ADD BY•••••••❂
                  https://line.me/R/ti/p/%40iya4481p
『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』""",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "commentOn":False,
    "likeOn":True,
    "alwayRead":False,
    "detectMention":False,    
    "kickMention":False,
    "steal":False,
    'pap':{},
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 


contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read)
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def updateProfilePicture(self, path):
        file=open(path, 'rb')
        files = {
            'file': file
        }
        params = {
            'name': 'media',
            'type': 'image',
            'oid': self.profile.mid,
            'ver': '1.0',
        }
        data={
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True

def sendVideo(self, to_, path):
        M = Message(to=to_, text=None, contentType = 2)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'video',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        #print r
        if r.status_code != 201:
            raise Exception('Upload video failure.')
        return True

def sendVideoWithURL(self, to_, url):
        path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download video failure.')

        try:
            self.sendVideo(to_, path)
        except Exception as e:
            raise (e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True


        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def fullwidth(text):
    '''converts a regular string to Unicode Fullwidth
    Preconditions: text, a string'''
    translator = ''
    translator = translator.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~' , '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［］＾＿‘｛｜｝～')
    return text.translate(translator)

def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e
            
def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki7.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki7.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki8.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki8.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki9.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki9.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki10.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki10.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki11.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki11.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki12.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki12.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki13.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki13.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki14.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki14.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki15.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki15.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ���Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki16.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki16.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            ki17.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki17.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            #cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"AutoLike by : ZETSU 々•┅─────")
            ki18.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki18.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"❂•••••••AUTO LIKE BY•••••••❂\n           https://line.me/R/ti/p/%40iya4481p\n『⊰์◉⊱ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    

groupParam = ""

def SiriGetOut(targ):
    ki.kickoutFromGroup(groupParam,[targ])
    ki2.kickoutFromGroup(groupParam,[targ])
    ki10.kickoutFromGroup(groupParam,[targ])

def bot(op):
    global groupParam
    try:
        if op.type == 25:
            msg = op.message
            if msg.text.lower() == ".removesiri":
                gs = cl.getGroup(msg.to)
                sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"])]
                if sirilist != []:
                    groupParam = msg.to
                    try:
                        p = Pool(40)
                        p.map(SiriGetOut,sirilist)
                        p.close()
                    except:
                        p.close()

    except Exception as error:
        if error == SystemExit:
            exit()
        print error
                        
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)

                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ue5f60d1f688be23082e4932dd6b1ea5d":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1001)
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki3.like(url[25:58], url[66:], likeType=1001)
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki5.like(url[25:58], url[66:], likeType=1001)
                ki6.like(url[25:58], url[66:], likeType=1001)
                ki7.like(url[25:58], url[66:], likeType=1001)
                ki8.like(url[25:58], url[66:], likeType=1001)
                ki9.like(url[25:58], url[66:], likeType=1001)
                ki10.like(url[25:58], url[66:], likeType=1001)
#                ki11.like(url[25:58], url[66:], likeType=1001)
 #               ki12.like(url[25:58], url[66:], likeType=1001)
  #              ki13.like(url[25:58], url[66:], likeType=1001)
   #             ki14.like(url[25:58], url[66:], likeType=1001)
    #            ki15.like(url[25:58], url[66:], likeType=1001)
     #           ki16.like(url[25:58], url[66:], likeType=1001)
      #          ki17.like(url[25:58], url[66:], likeType=1001)
       #         ki18.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ki2.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "🤠" + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag🤔?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja🙄","-_-","Acil lagi off😴", cName + " ada apa ?","yang tag gw jones 😒 " + cName, "Jangan Suka Tag gua 😒" + cName, "Kamu siapa 🤔" + cName + "?", "Ada Perlu apa 😒" + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Dont tag my self .!"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  ki.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             cl.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 cl.findAndAddContactsByMid(target)
                                 cl.inviteIntoGroup(msg.to,[target])
                                 cl.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      cl.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#--------------------------------- Remove Chat ------------------------------
            elif "Removechat" in msg.text.lower():
#                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        #ki.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#----------------------------------------------------------------------------
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif msg.text.lower() == 'helpbots':
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,helpself)
                else:
                    cl.sendText(msg.to,helpself)
            elif msg.text.lower() == 'settings':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpset)
                else:
                    cl.sendText(msg.to,helpset)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "Mybots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                cl.sendMessage(msg)
  #              msg.contentType = 13
   #             msg.contentMetadata = {'mid': ki11mid}
    #            cl.sendMessage(msg)
     #           msg.contentType = 13
      #          msg.contentMetadata = {'mid': ki12mid}
       #         cl.sendMessage(msg)
        #        msg.contentType = 13
         #       msg.contentMetadata = {'mid': ki13mid}
          #      cl.sendMessage(msg)
           #     msg.contentType = 13
            #    msg.contentMetadata = {'mid': ki14mid}
             #   cl.sendMessage(msg)
              #  msg.contentType = 13
               # msg.contentMetadata = {'mid': ki15mid}
#                cl.sendMessage(msg)
 #               msg.contentType = 13
  #              msg.contentMetadata = {'mid': ki16mid}
   #             cl.sendMessage(msg)
    #            msg.contentType = 13
     #           msg.contentMetadata = {'mid': ki17mid}
      #          cl.sendMessage(msg)
       #         msg.contentType = 13
        #        msg.contentMetadata = {'mid': ki18mid}
         #       cl.sendMessage(msg)
            elif "B1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "B2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "B3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "B4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "B5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "B6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "B7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif "B8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
            elif "B9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
            elif "B10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
            elif "B11" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki11mid}
                ki11.sendMessage(msg)
            elif "B12" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki12mid}
                ki12.sendMessage(msg)
            elif "B13" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki13mid}
                ki13.sendMessage(msg)
            elif "B14" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki14mid}
                ki14.sendMessage(msg)
            elif "B15" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki15mid}
                ki15.sendMessage(msg)
            elif "B16" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki16mid}
                ki16.sendMessage(msg)
            elif "B17" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki17mid}
                ki17.sendMessage(msg)
            elif "B18" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki18mid}
                ki18.sendMessage(msg)
            elif "Creator" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u84734a2bb2201d465e6015f90dc462f0'}
                cl.sendMessage(msg)
            elif msg.text in ["Allgift","B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Allgift","B2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Allgift","B3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Allgift","B4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)
            elif msg.text in ["Allgift","B5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki5.sendMessage(msg)
            elif msg.text in ["Allgift","B6 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ki6.sendMessage(msg)
            elif msg.text in ["Allgift","B7 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki7.sendMessage(msg)
            elif msg.text in ["Allgift","B8 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '13'}
                msg.text = None
                ki8.sendMessage(msg)
            elif msg.text in ["Allgift","B9 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '11'}
                msg.text = None
                ki9.sendMessage(msg)
            elif msg.text in ["Allgift","B10 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki10.sendMessage(msg)
            elif msg.text in ["Allgift","B11 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ki11.sendMessage(msg)
            elif msg.text in ["Allgift","B12 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki12.sendMessage(msg)
            elif msg.text in ["Allgift","B13 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '9'}
                msg.text = None
                ki13.sendMessage(msg)
            elif msg.text in ["Allgift","B14 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '1'}
                msg.text = None
                ki14.sendMessage(msg)
            elif msg.text in ["Allgift","B15 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki15.sendMessage(msg)
            elif msg.text in ["Allgift","B16 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki16.sendMessage(msg)
            elif msg.text in ["Allgift","B17 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki17.sendMessage(msg)
            elif msg.text in ["Allgift","B18 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki18.sendMessage(msg)
            elif msg.text in ["Spam gift"]:
				#if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					ki2.sendMessage(msg)
					ki3.sendMessage(msg)
					ki4.sendMessage(msg)
					ki5.sendMessage(msg)
					ki6.sendMessage(msg)
					ki7.sendMessage(msg)
					ki8.sendMessage(msg)
					ki9.sendMessage(msg)
					ki10.sendMessage(msg)
#					ki11.sendMessage(msg)
#					ki12.sendMessage(msg)
#					ki13.sendMessage(msg)
#					ki14.sendMessage(msg)
#					ki15.sendMessage(msg)
#					ki16.sendMessage(msg)
#					ki17.sendMessage(msg)
#					ki18.sendMessage(msg)
#-------------------------Audio------------------------------------------#
            elif "Contact @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Contact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                        pass
#-----------------------------------------------
            elif "Gid" == msg.text:
                kk.sendText(msg.to,msg.to)

#------------------------------------------------------------------------#
            elif msg.text in ["B Cancel","Cancel dong","Bcancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
#-------------------------
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Clink"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close 👈")
                    else:
                        cl.sendText(msg.to,"URL close 👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ")
            elif msg.text.lower() == 'ginfo':        
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md ="✥GROUP NAME✥\n" + group.name + "\n\n✥GROUP ID✥\n✿" + group.id +"✿" "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\n✥TOTAL MEMBER✥\n" + str(len(group.members)) + " Orang" + "\n✥PENDINGAN✥\n" + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "B1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "B2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "B3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "B4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "B5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "B6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "B7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "B8 mid" == msg.text:
                ki8.sendText(msg.to,ki8mid)
            elif "B9 mid" == msg.text:
                ki9.sendText(msg.to,ki9mid)
            elif "B10 mid" == msg.text:
                ki10.sendText(msg.to,ki10mid)
            elif "B11 mid" == msg.text:
                ki11.sendText(msg.to,ki11mid)
            elif "B12 mid" == msg.text:
                ki12.sendText(msg.to,ki12mid)
            elif "B13 mid" == msg.text:
                ki13.sendText(msg.to,ki13mid)
            elif "B14 mid" == msg.text:
                ki14.sendText(msg.to,ki14mid)
            elif "B15 mid" == msg.text:
                ki15.sendText(msg.to,ki15mid)
            elif "B16 mid" == msg.text:
                ki16.sendText(msg.to,ki16mid)
            elif "B17 mid" == msg.text:
                ki17.sendText(msg.to,ki17mid)
            elif "B18 mid" == msg.text:
                ki18.sendText(msg.to,ki18mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
     #           ki11.sendText(msg.to,ki11mid)
      #          ki12.sendText(msg.to,ki12mid)
       #         ki13.sendText(msg.to,ki13mid)
        #        ki14.sendText(msg.to,ki14mid)
         #       ki15.sendText(msg.to,ki15mid)
          #      ki16.sendText(msg.to,ki16mid)
           #     ki17.sendText(msg.to,ki17mid)
            #    ki18.sendText(msg.to,ki18mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "👈")
#------------------------------------------------------------------------------------------#
            elif "Cn " in msg.text:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B2name " in msg.text:
                string = msg.text.replace("B2name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B3name " in msg.text:
                string = msg.text.replace("B3name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B4name " in msg.text:
                string = msg.text.replace("B4name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
#--------------------------------------------------------
            elif "B5name " in msg.text:
                string = msg.text.replace("B5name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀇔 􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B6name " in msg.text:
                string = msg.text.replace("B6name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names��" + string + "👈")
#---------------------------------------------------------
            elif "B7name " in msg.text:
                string = msg.text.replace("B7name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B8name " in msg.text:
                string = msg.text.replace("B8name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B9name " in msg.text:
                string = msg.text.replace("B9name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B10name " in msg.text:
                string = msg.text.replace("B10name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")

#--------------------------------------------------------
            elif "Sc:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact:on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open ✔")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact:off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ✖")
                    else:
                        cl.sendText(msg.to,"It is already off ✖")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off already")
                    else:
                        cl.sendText(msg.to,"already Close ✔")
            elif msg.text in ["Pro:on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Enable􀜁✔􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ✔")
            elif msg.text in ['Prolink:on']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect Enable􀜁􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Proinvite:on']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ¨")
            elif msg.text in ['Procancel:on']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'join:on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="✖User Blocked List✖\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text.lower() == 'join:off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off✔")
                    else:
                        cl.sendText(msg.to,"Auto Join set off✔")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close✔")
                    else:
                        cl.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Pro:off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Disable ✔")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Prolink:off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Disable ✖")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close✖")
                    else:
                        cl.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Proinvite:off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection Disable ✖")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close✖")
                    else:
                        cl.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Procancel:off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Disable ✖")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close✖")
                    else:
                        cl.sendText(msg.to,"It is already open ✔")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak✖\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan✖")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak✖Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis✔")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar✖")
                    else:
                        cl.sendText(msg.to,"Weird value✖")
            elif msg.text in ["Leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔✔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Is already open􀇔􏿿✔")
            elif msg.text in ["Leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off􀜁􀇔􏿿✖")
                    else:
                        cl.sendText(msg.to,"Sudah off􀜁􀇔􏿿✖")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Is already close􀇔􏿿✔")
            elif msg.text in ["Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ✖")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on ✔")
                    else:
                        cl.sendText(msg.to,"on ✔")
            elif msg.text in ["Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done􀇔􏿿✔")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿✔")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off ✖")
                    else:
                        cl.sendText(msg.to,"Off ✖")
            elif msg.text.lower() == 'set':
                md = "{==℘ґ∂ηк в❍тs==}\n     |==S E T T I N G==|\n\n"
                if wait["likeOn"] == True: md+="【Like:ON⚫\n"
                else: md+="【Like:OFF⚪\n"
                if wait["detectMention"] == True: md+="【Respon:ON⚫\n"
                else: md +="【Respon:OFF⚪\n"
                if wait["alwayRead"] == True: md+="【Auto read:ON⚫\n"
                else: md+="【Auto read:OFF⚪\n"
                if wait["kickMention"] == True: md+="【Notag:ON⚫\n"
                else:md+="【Notag:OFF⚪\n"
                if wait["contact"] == True: md+="【Contact:ON⚫\n"
                else: md+="【Contact:OFF⚪\n"
                if wait["autoJoin"] == True: md+="【Join:ON⚫\n"
                else: md +="【Join:OFF⚪\n"
                if wait["autoCancel"]["on"] == True:md+="【Cancel:" + str(wait["autoCancel"]["members"]) + "⚫\n"
                else: md+= "【Cancel:OFF⚪\n"
                if wait["leaveRoom"] == True: md+="【Leave:ON⚫\n"
                else: md+="【Leave:OFF⚪\n"
                if wait["timeline"] == True: md+="【Share:ON⚫\n"
                else:md+="【Share:OFF⚪\n"
                if wait["autoAdd"] == True: md+="【Add:ON⚫\n"
                else:md+="【Add:OFF⚪\n"
                if wait["commentOn"] == True: md+="【Com:ON⚫\n"
                else:md+="【Com:OFF⚪\n________________\n✠❩“““PROTECTION”””❨✠\n________________\n"
                if wait["protect"] == True: md+="【Pro:ON⚫\n"
                else:md+="【Pro:OFF⚪\n"
                if wait["linkprotect"] == True: md+="【Prolink:ON⚫\n"
                else:md+="【Prolink:OFF⚪\n"
                if wait["inviteprotect"] == True: md+="【Proinvite:ON⚫\n"
                else:md+="【Proinvite:OFF⚪\n"
                if wait["cancelprotect"] == True: md+"【Procancel:ON⚫\n"
                else:md+="【Procancel:OFF⚪\n"
                cl.sendText(msg.to,md + "\n\n✙   O W N E R   ✙\n{====℘ґ∂ηк в❍тѕ====}")
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': admsa}
#                cl.sendMessage(msg)
            elif "Gowner" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")
            elif cms(msg.text,["Add"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u5818cb4404411c2e2e6e6937d172cca8'}
                cl.sendText(msg.to,"❂•••••••••✧••••••••••❂")
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'udfaf52176415b46cb445ae2757ec85f3'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"❂••••••••✰•✰••••••••❂")
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = "❂•••••••••L I S T  I D  G R O U P••••••••••❂\n "
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text.lower() == 'all:out':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
       #         gid = ki11.getGroupIdsJoined()
      #          gid = ki12.getGroupIdsJoined()
     #           gid = ki13.getGroupIdsJoined()
    #            gid = ki14.getGroupIdsJoined()
   #             gid = ki15.getGroupIdsJoined()
  #              gid = ki16.getGroupIdsJoined()
 #               gid = ki17.getGroupIdsJoined()
#                gid = ki18.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                    ki10.leaveGroup(i)
       #             ki11.leaveGroup(i)
      #              ki12.leaveGroup(i)
     #               ki13.leaveGroup(i)
    #                ki14.leaveGroup(i)
   #                 ki15.leaveGroup(i)
  #                  ki16.leaveGroup(i)
 #                   ki17.leaveGroup(i)
#                    ki18.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kitsune Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Gcancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Add:on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On✔")
                    else:
                        cl.sendText(msg.to,"Already On✔")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On✔")
                    else:
                        cl.sendText(msg.to,"Already On✔")
            elif msg.text in ["Add:off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off✖")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan✖")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off✖")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off✖")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"✨We changed the message✨")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"✨We changed the Help✨")
            elif "Msg add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"✨Kami mengubah pesan✨")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message confirm"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis✔")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia✔")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Com set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah✔")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah✔\n\n" + c)
            elif msg.text in ["Comment:on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di✔")
                    else:
                        cl.sendText(msg.to,"To open✔")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✔")
                    else:
                        cl.sendText(msg.to,"✔")
            elif msg.text in ["Com:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off ✖")
                    else:
                        cl.sendText(msg.to,"It is already turned off ✖")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off✖")
                    else:
                        cl.sendText(msg.to,"To turn off✖")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"✨Auto komentar saat ini telah ditetapkan sebagai berikut✨\n\n" + str(wait["comment"]))
            elif msg.text in ["Glink","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“👈")

            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#                else:
#                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Comban"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist…”✚")
            elif msg.text in ["Comban del"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist…”✚")
            elif msg.text in ["Comban cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist✖")
                else:
                    cl.sendText(msg.to,"The following is a blacklist✔")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
                        
#            elif msg.text in ["Simisimi on","Simisimi:on"]:
 #               settings["simiSimi"][msg.to] = True
  #              cl.sendText(msg.to,"BOT API SIMISIMI TURN ON")
   #             ki.sendText(msg.to,"already turn active")
                
    #        elif msg.text in ["Simisimi off","Simisimi:off"]:
     #           settings["simiSimi"][msg.to] = False
      #          cl.sendText(msg.to,"BOT API SIMISIMI TURN OFF")
       #         ki.sendText(msg.to,"already non active")
                
            elif msg.text in ["Read on","Read:on"]:
                if wait['alwayRead'] == True:
                    if wait["alwayRead"] == "JP": 
                        cl.sendText(msg.to,"Auto Sider ON")
                else:
                    wait["alwayRead"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                        
            elif msg.text in ["Read off","Read:off"]:
                if wait['alwayRead'] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Sider OFF")
                else:
                    wait['alwayRead'] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already OFF auto read")
                
            elif msg.text in ["Autorespon on","Autorespon:on","Respon on","Respon:on"]:
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon ON")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                        
            elif msg.text in ["Autorespon off","Autorespon:off","Respon off","Respon:off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon OFF")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already OFF")
                        
            elif msg.text in ["Notag:on"]:
                if wait["kickMention"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"☠️DANGER TAG KICK ON☠️")
                else:
                    wait["kickMention"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already ON")
            elif msg.text in ["Notag:off"]:
                if wait["kickMention"] == False:
                   if wait["lang"] == "JP":
                        ki.sendText(msg.to,"SELF PROTECT TAG OFF ✔")
                else:
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already turn OF")
            elif msg.text.lower() == 'Clock:on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam on✔")
            elif msg.text.lower() == 'Clock:off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off✖")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to," Dimatikan ✔")
            elif "Clockname " in msg.text:
                n = msg.text.replace("Jam say ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah✔\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui✔")
                else:
                    cl.sendText(msg.to,"✨Silahkan Aktifkan Nama✨")

            elif "Fuck1 " in msg.text:
                       nk0 = msg.text.replace("Fuck1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck2 " in msg.text:
                       nk0 = msg.text.replace("Fuck2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki2.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki2.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck3 " in msg.text:
                       nk0 = msg.text.replace("Fuck3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki3.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck4 " in msg.text:
                       nk0 = msg.text.replace("Fuck4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki4.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki4.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck5 " in msg.text:
                       nk0 = msg.text.replace("Fuck5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki5.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki5.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck6 " in msg.text:
                       nk0 = msg.text.replace("Fuck6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki6.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki6.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck7 " in msg.text:
                       nk0 = msg.text.replace("Fuck7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki7.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki7.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck8 " in msg.text:
                       nk0 = msg.text.replace("Fuck8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki8.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki8.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck9 " in msg.text:
                       nk0 = msg.text.replace("Fuck9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki9.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki9.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Fuck10 " in msg.text:
                       nk0 = msg.text.replace("Fuck10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki10.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki10.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Kick1 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif ("Kick2 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("Kick3 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif ("Kick4 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"Error")
            elif ("Kick5 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif ("Kick6 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki6.kickoutFromGroup(msg.to,[target])
                       except:
                           ki6.sendText(msg.to,"Error")
            elif ("Kick7 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki7.kickoutFromGroup(msg.to,[target])
                       except:
                           ki7.sendText(msg.to,"Error")
            elif ("Kick8 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki8.kickoutFromGroup(msg.to,[target])
                       except:
                           ki8.sendText(msg.to,"Error")
            elif ("Kick9 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki9.kickoutFromGroup(msg.to,[target])
                       except:
                           ki9.sendText(msg.to,"Error")
            elif ("Kick10 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki10.kickoutFromGroup(msg.to,[target])
                       except:
                           ki10.sendText(msg.to,"Error")
            elif ("Sc " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)

            elif "Bro " in msg.text:
                       nk0 = msg.text.replace("Bro ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass


            elif ("Ban " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass

            elif msg.text in ["Mygroups"]:
                 gid = cl.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "[⛓️] %s \n" % (cl.getGroup(i).name + " | 🗜️Members : " + str(len (cl.getGroup(i).members)))
                 cl.sendText(msg.to, "☆「Group List」☆\n"+ h +"🗜️Total Group : " +str(len(gid)))

#----------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")
 #=======================================================
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-th" in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
                
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO ENGLISH----\n" + "" + result + "\n------SUKSES-----")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM EN----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
#________________________________________________________________________
            elif 'ig ' in msg.text.lower():
              #if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
#==============================================================================#

                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot has been active "+waktu(eltime)
                cl.sendText(msg.to,van) 
                
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif msg.text in ["Myname"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["pap"])
#=========================
#-----------------------------------------------------------
            elif msg.text == "Check":
                    cl.sendText(msg.to, "Check Yang nyimak")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text == "Cctv":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to,"======Tercyduck====== %s\n=====[CCTV SAAT INI]======\n%s\nReading point creation date n time:\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                         cl.sendText(msg.to,"An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-------------------------------------------------
	    elif "Spam @" in msg.text:
#	      if msg.from_ in admin:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
		       cl.sendText(msg.to,"Wating in progres...")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
	  	       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Succes")
                       print " Spammed !"
#--------------------------------------------------------------------------
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 10000:
                        for x in range(jmlh):
                            ki.sendText(msg.to, text)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 10000:
                        ki.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Gid" in msg.text:
                saya = msg.text.replace('Gid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═════════List FriendMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    
#-----------------------------------------------
            elif "lurk:on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk:off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")           
#-----------------------------------------------

#-----------------------------------------------------------
            elif msg.text.lower() == 'respon':
#                cl.sendText(msg.to,"clear all blacklist")
                ki.sendText(msg.to,"HADIR😂")
                ki2.sendText(msg.to,"HADIR😂")
                ki3.sendText(msg.to,"HADIR😂")
                ki4.sendText(msg.to,"HADIR😂")
                ki5.sendText(msg.to,"HADIR😂")
                ki6.sendText(msg.to,"HADIR😂")
                ki7.sendText(msg.to,"HADIR😂")
                ki8.sendText(msg.to,"HADIR😂")
                ki9.sendText(msg.to,"HADIR😂")
                ki10.sendText(msg.to,"KUMPLIT OM 😎")
                
#-----------------------------------------------------------speed
            elif msg.text in ["Bl:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbl:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
 #---------Fungsi Banlist With Tag--------#
            elif msg.text in ["Banlist","ip banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    ki.sendText(msg.to,"Blacklisted user")
                    mc = " 🛡️====||B L A C K L I S T||====🛡️\n"
                    for mi_d in wait["blacklist"]:
                        mc += "🗜️" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
                    print "[Command]Banlist executed"
            elif msg.text in ["Clearban"]:
                if msg.toType == 2:
                   wait["blacklist"] = {}
                   cl.sendText(msg.to,"clear all blacklist")
                   ki.sendText(msg.to,"done ✔")
                   ki2.sendText(msg.to,"done ✔")
                   ki3.sendText(msg.to,"done ✔")
                   ki4.sendText(msg.to,"done ✔")
                   ki5.sendText(msg.to,"done ✔")
                   ki6.sendText(msg.to,"done ✔")
                   ki7.sendText(msg.to,"done ✔")
                   ki8.sendText(msg.to,"done ✔")
                   ki9.sendText(msg.to,"done ✔")
                   ki10.sendText(msg.to,"done ✔")
      #             ki11.sendText(msg.to,"done ✔")
       #            ki12.sendText(msg.to,"done ✔")
        #           ki13.sendText(msg.to,"done ✔")
         #          ki14.sendText(msg.to,"done ✔")
          #         ki15.sendText(msg.to,"done ✔")
           #        ki16.sendText(msg.to,"done ✔")
            #       ki17.sendText(msg.to,"done ✔")
             #      ki18.sendText(msg.to,"done ✔")
                   ki.sendText(msg.to,"blacklist done all removed 👮")
            elif msg.text.lower() == 'kick@mbl':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            ki8.kickoutFromGroup(msg.to,[jj])
                            ki9.kickoutFromGroup(msg.to,[jj])
                            ki10.kickoutFromGroup(msg.to,[jj])
      #                      ki11.kickoutFromGroup(msg.to,[jj])
       #                     ki12.kickoutFromGroup(msg.to,[jj])
        #                    ki13.kickoutFromGroup(msg.to,[jj])
         #                   ki14.kickoutFromGroup(msg.to,[jj])
          #                  ki15.kickoutFromGroup(msg.to,[jj])
           #                 ki16.kickoutFromGroup(msg.to,[jj])
            #                ki17.kickoutFromGroup(msg.to,[jj])
             #               ki18.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#-----------------------------------------------
            elif "Translate" in msg.text:
                cl.sendText(msg.to, "★[TRANSLATE]★\nTr-id ☆to indonesia☆\nTr-en ☆to english☆\nTr-jp ☆to japan☆\nTr-th ☆to thailand☆\nTr-ar ☆to arab☆\nTr-ko ☆to korea☆\n_______________")

#---------------------------------------------------
#            elif "ATM" in msg.text:
#				cl.sendText(msg.to, "==BANK MANDIRI==\nno req:\n1270007723859\natas nama:\nSRI ROHANA")
#---------------------------------------------------
            elif "Pict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Pict @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#---------------------------------------------------
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
#---------------------------------------------------
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#-----------------------------------------------------------------------
            elif "Youtube " in msg.text:
                try:
                    textToSearch = (msg.text).replace("Youtube ", "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
#------------------------------------------------
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n~Header\n" + str(cu))
                except:
                    cl.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\n" + str(cu))
            
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
            elif "Gimage" in msg.text:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
					cl.sendImageWithURL(msg.to,path)
            
            elif "Getprofile @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getprofile @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-----------------------------------------------------------------#
            elif "Copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "Stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - succes"
            
            elif "Bcopy @" in msg.text:
                if msg.toType == 2:
#                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.CloneContactProfile(target)
                                    ki2.CloneContactProfile(target)
                                    ki3.CloneContactProfile(target)
                                    ki4.CloneContactProfile(target)
                                    ki5.CloneContactProfile(target)
                                    ki6.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#------------------------------------------------------------
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                random.choice(KAC).sendText(msg.to,"send contact 😉")
#------------------------------------------------------------
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
#-----------------------------------------------
            elif "Steal " in msg.text:
                #if msg.from_ in admin:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
#-----------------------------------------------
#----------------------------------------------
            elif "Steal @" in msg.text:
        #        if msg.from_ in admin:
                    if msg.toType == 2:
                        steal = msg.text.replace("Steal @","")
                        stealname = steal.rstrip(" ")
                        group = cl.getGroup(msg.to)
                        targets = []
                        if steal == "":
                            cl.sendText(msg.to,"Invalid user")
                        else:
                            for i in group.members:
                                if stealname == i.displayName:
                                    targets.append(i.mid)
                            if targets == []:
                                cl.sendText(msg.to,"User tidak ditemukan")
                            else:
                                for target in targets:
                                    try:
                                        contact = cl.getContact(target)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        try:
                                            cover = cl.channel.getCover(contact)
                                        except:
                                            cover = ""
                                        try:
                                            cl.sendText(msg.to,"Gambar Foto Profilenya")
                                            cl.sendImageWithURL(msg.to,image)
                                            if cover == "":
                                                cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                                            else:
                                                cl.sendText(msg.to,"Gambar Covernya")
                                                cl.sendImageWithURL(msg.to,cover)
                                        except Exception as error:
                                            cl.sendText(msg.to,(error))
                                            break
                                    except:
                                        cl.sendText(msg.to,"Error!")
                                        break
                    else:
                        cl.sendText(msg.to,"Tidak bisa dilakukan di luar wilayah")
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)
                        ki.sendMessage(msg,g)
                        ki2.sendMessage(msg,g)
                        ki3.sendMessage(msg,g)
                        ki4.sendMessage(msg,g)
                        ki5.sendMessage(msg,g)
                        ki6.sendMessage(msg,g)
                        ki7.sendMessage(msg,g)
                        ki8.sendMessage(msg,g)
                        ki9.sendMessage(msg,g)
            elif 'ig ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'audio ' in msg.text.lower():
           #   if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('audio ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))

            elif msg.text.lower() == 'reboot':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
	    elif 'record' in msg.text:
                 psn = msg.text.replace("record ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Mp3 " in msg.text:
                say = msg.text.replace("Mp3 ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#==================================================
            elif 'lirik ' in msg.text.lower():
#              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))

#---------------------- = NUKE = ------------------
            elif 'Nuke' in msg.text:
                if msg.toType == 2:
                    print "Nuke ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
      #              gs = ki11.getGroup(msg.to)
       #             gs = ki12.getGroup(msg.to)
        #            gs = ki13.getGroup(msg.to)
         #           gs = ki14.getGroup(msg.to)
          #          gs = ki15.getGroup(msg.to)
           #         gs = ki16.getGroup(msg.to)
            #        gs = ki17.getGroup(msg.to)
             #       gs = ki18.getGroup(msg.to)
              #      start = time.time()
               #     ki.sendText(msg.to, "Nuke Speed")
                #    elapsed_time = time.time() - start
                 #   ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                  #  ki3.sendText(msg.to, "Nuke Start")
                   # ki4.sendText(msg.to, "Nuke Proses")
                    #ki5.sendText(msg.to,"􀜁􀇔􏿿 Sikaatt all..􀜁􀇔􏿿")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
#                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
#                                    ki3.sendText(msg,to,"Nuke Finish")
#                                    ki2.sendText(msg,to,"
#-------------------------------------------------------------
            elif msg.text in ["Tag","Tagall","Mencret"]:
	            #if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
#-------------------FUNGSI TAGALL---------------#
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#-----------------------------------------------
            elif "join: " in msg.text.lower():
		rplace=msg.text.lower().replace("join: ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))

#-----------------------------------------------
            elif msg.text.lower() == '.':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
            #            ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
             #           time.sleep(0.01)
              #          ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
               #         time.sleep(0.01)
                #        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                 #       time.sleep(0.01)
                  #      ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                   #     time.sleep(0.01)
                    #    ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                     #   time.sleep(0.01)
                      #  ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                      #  time.sleep(0.01)
                      #  ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                      #  time.sleep(0.01)
                      #  ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                      #  time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)

#-----------------------------------------------
            elif msg.text.lower() == 'reinvite':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"waitting...")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
      #                  ki11.leaveGroup(msg.to)
       #                 ki12.leaveGroup(msg.to)
        #                ki13.leaveGroup(msg.to)
         #               ki14.leaveGroup(msg.to)
          #              ki15.leaveGroup(msg.to)
           #             ki16.leaveGroup(msg.to)
            #            ki17.leaveGroup(msg.to)
             #           ki18.leaveGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
      #                  ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
       #                 ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
        #                ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
         #               ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
          #              ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
           #             ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
            #            ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
             #           ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() == 'prank come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
#                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
 #                       ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
  #                      ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
   #                     ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
    #                    ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
     #                   ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
      #                  ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
       #                 ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
        #                ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
         #               ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
          #              ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
           #             ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
            #            ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
             #           ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "B1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "B2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "B3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "B4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "B5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "B6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "B7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "B8 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "B9 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "B10 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
#------------------------------------------------------------------

            elif msg.text.lower() == ',':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
#                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
      #                  ki11.leaveGroup(msg.to)
       #                 ki12.leaveGroup(msg.to)
        #                ki13.leaveGroup(msg.to)
         #               ki14.leaveGroup(msg.to)
          #              ki15.leaveGroup(msg.to)
           #             ki16.leaveGroup(msg.to)
            #            ki17.leaveGroup(msg.to)
             #           ki18.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B10 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
#				ki11.sendText(msg.to,(bctxt))
#				ki12.sendText(msg.to,(bctxt))
#				ki13.sendText(msg.to,(bctxt))
#				ki14.sendText(msg.to,(bctxt))
#				ki15.sendText(msg.to,(bctxt))
#				ki16.sendText(msg.to,(bctxt))
#				ki17.sendText(msg.to,(bctxt))
#				ki18.sendText(msg.to,(bctxt))
            elif "Bom " in msg.text:
				bctxt = msg.text.replace("Bom ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
#                cl.sendText(msg.to, "Bom chat selesai mbut.😂")
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki7.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki8.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki9.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki10.sendText(msg.to,"Ping 􀜁􀇔􏿿")

#-----------------------------------------------
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)




                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True



                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki2.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)


                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)


                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)


                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)


                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)


                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)


                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in kimid:
                    if op.param2 in ki7mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in kimid:
                    if op.param2 in ki9mid:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)

                        ki10.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki10mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki11mid:
                    if op.param2 in ki10mid:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)

                        ki10.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki12mid:
                    if op.param2 in ki11mid:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                    else:
                        G = ki11.getGroup(op.param1)

                        ki10.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki13mid:
                    if op.param2 in ki12mid:
                        G = ki12.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)
                    else:
                        G = ki12.getGroup(op.param1)

                        ki12.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki14mid:
                    if op.param2 in ki13mid:
                        G = ki13.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                    else:
                        G = ki13.getGroup(op.param1)

                        ki13.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki15mid:
                    if op.param2 in ki14mid:
                        G = ki14.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                    else:
                        G = ki14.getGroup(op.param1)

                        ki14.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki16mid:
                    if op.param2 in ki15mid:
                        G = ki15.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
                    else:
                        G = ki15.getGroup(op.param1)

                        ki15.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki17mid:
                    if op.param2 in ki16mid:
                        G = ki16.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki16.updateGroup(G)
                        Ticket = ki16.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)
                    else:
                        G = ki16.getGroup(op.param1)

                        ki16.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki16.updateGroup(G)
                        Ticket = ki16.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki17.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in mid:
                    if op.param2 in ki18mid:
                        G = ki18.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki18.updateGroup(G)
                        Ticket = ki18.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                    else:
                        G = ki18.getGroup(op.param1)

                        ki18.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki18.updateGroup(G)
                        Ticket = ki18.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki18mid:
                    if op.param2 in ki17mid:
                        G = ki17.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki17.updateGroup(G)
                        Ticket = ki17.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki17.updateGroup(G)
                    else:
                        G = ki17.getGroup(op.param1)

                        ki17.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki17.updateGroup(G)
                        Ticket = ki17.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True


                elif op.param3 in ki18mid:
                    if op.param2 in ki14mid:
                        G = ki14.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                    else:
                        G = ki14.getGroup(op.param1)

                        ki14.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki5.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open Kick finish-----#
#------invite Kick start------#
        if op.type == 13:
            if wait["inviteprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------invite Kick finish-----#
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                cl.sendText

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            


        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(0.30)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki7.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki8.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki9.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki10.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki11.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki12.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki13.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki14.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki15.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki16.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki17.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki18.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autolike)
thread1.daemon = True
thread1.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

