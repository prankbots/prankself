# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib
#from bs4 import BeautifulSoup
#import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia

cl = LINETCR.LINE()
cl.login(token="EmLXl2qfMBtttFcmvpua.apGNZMzba418M2CeQxD9/G.MxgDoVhW2Za7RZ8k0vOzBrIqrTgmBEIK8fpypHVDj4k=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="Em5WmSSb1EnnuDgnKeU6.pXN+7RvYi/ufIldOHYCunG.zlkmHzW/4l0cF5eXrh+QIZVWgc6V28DbWYr2IZjV8Jw=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EmDWIGjYCuofPMxF29cb.QGfPOYoWMry0tHUk7ByfsW.Myr4DRzu9JYmkOAKzjQ7o+4//k6RZov1qXg2Qzc+g9w=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EmTfzU14RQ2Xn28r8G20.wr8xgcuZEfwwnOv8gP+n0a.yMo3gzHdBfO844j41I/DTvUjJuxVREh1WcNaIhep5gU=")
kc.loginResult()

kd = LINETCR.LINE()
kd.login(token="EmhQC6haTCouZKQXQo4f.UTvwOPYi0sJi3oXTG6tPRW.doOaLVexPbu2jxTEzXbvD+R3GTEzNsKNIzzogcOc16I=")
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token="Em24yJCFtOCj3TeoNfM5.6BDfmN53HxXiA9R9UVF9fq.ImYJz96qjTKAcOLZxlcezzwzqawyeu6nG+rA8uJ2T9s=")
ke.loginResult()

kf = LINETCR.LINE()
kf.login(token="EmrXbTZ1rg6vNIicb2ub.5lF7KrBwbqurrYqk5Y36MW.2RQfzJ14nCuBNedj7ilPr9GzHH3j4TtS5FcCfk6PRhE=")
kf.loginResult()

kg = LINETCR.LINE()
kg.login(token="EmHlDLVK6Q9oiPEM3SU2.h5edYb4WKUebl+MD5E8YeG.zVZOFt+c1fMK2gfTOwwDFisaTloi+KPMPWiyHHd4RGU=")
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token="EmczQgw6tM3GSb0OaFqc.PLwpKkxpN1vUmOxTOmbVla.1EvN9s3UdXdgkQwifkX6h4relbyE4IUEJgaT+cgC8Ko=")
kh.loginResult()

kj = LINETCR.LINE()
kj.login(token="EmFheViE6bJieDOGnnqf.7dmJj7Pl3NYc9mQ0bmv9lW.pIGYFbTXE/1lUj+p86MWBBtIyWDbacFu78VQxHY+T2o=")
kj.loginResult()

kl = LINETCR.LINE()
kl.login(token="EmPjYsvzXyHidKQvuUNf.V7DEhRk+zfq16AuaIHOk+W.pD3DSBWKnwuJReq78Fefn4Ys4QcI3YhYEGKlkLbq6OA=")
kl.loginResult()

km = LINETCR.LINE()
km.login(token="Em74tzXHsIM42LE0rhH8.H/2+dXDF6mXvxwjFFKFrsa.Z2JMGYOrrIfcV0woXziwkzmgdBDdfKqdg/z5inDvH5I=")
km.loginResult()

kn = LINETCR.LINE()
kn.login(token="EmHmcfpTKmJFpYoC4Htf.X84wLwnCQjJbsPF0Ghq1dW.bprZcr45aNGe2nOaW8Z47Yw9EzrOnJC70zq3goVysgM=")
kn.loginResult()

ko = LINETCR.LINE()
ko.login(token="EmlryaX0p2Hh6AgRaGb3.mOSG1MHBcjvyM0tjBkZHeW.JVQQpJKxEaoqRMzFITNmnhWc9L54RJIAkh7MR1beHlw=")
ko.loginResult()

kp = LINETCR.LINE()
kp.login(token="EmwNmLdW0M6YTBYB78Ba./LRkqg9QVBS5pCvYrPQxwG.elVqaYnzQ2olBroYs1VtbdumPdBoKCWx0a8OjXsSJic=")
kp.loginResult()

kq = LINETCR.LINE()
kq.login(token="EmbhD4BxvTwdkVFsFhb5.T6aQj64lnmQ+piddBWaZzq.5pVyPq9iNl7ncTZlynv/kOL2Q484vhTH3akP8SDC8hM=")
kq.loginResult()

kr = LINETCR.LINE()
kr.login(token="EmyFapSP77PCgqPUkSA1.5KGDSM93GAyvTG52mPLbCq.JFsBEXRcBMy+rqsYLz/98rrJ7LQ91Rxuqe5mTM8euCE=")
kr.loginResult()

ks = LINETCR.LINE()
ks.login(token="Em5CpuXREc9uw9FsZTD8.0SD7v1JpFHS4lNELlxT2wa.cFVfqAc6EJYdGB4hiqy8Q9Z+Cc7p8GANGKUVZZvLlv4=")
ks.loginResult()

kt = LINETCR.LINE()
kt.login(token="Em7pVfHsFYfPDlNRMIy6.3tHrCXSlxxV7l5g65M4UvG.tBw/Rs8JYi6wTO4AS1H6RTbc9WQR6m2jV+bHJ4h6uZc=")
kt.loginResult()
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage =""" ====[Self Bots PHET HECK BOT]====

              ༺•㏒ ᴳᵘ ᵀᵃʳ ᴾʰᵉᵗ ㏒•༻

❂͜͡☆➣ Me
❂͜͡☆➣ Id
❂͜͡☆➣ Mid
❂͜͡☆➣ Gift
❂͜͡☆➣ Mid @
❂͜͡☆➣ Cn: Display Name
❂͜͡☆➣ Cc: Clock Name
❂͜͡☆➣ Mc:
❂͜͡☆➣ Tl: text
❂͜͡☆➣ Auto join: on/off
❂͜͡☆➣ Auto add: on/off
❂͜͡☆➣ Auto leave: on/off
❂͜͡☆➣ Clock: on/off
❂͜͡☆➣ Share on
❂͜͡☆➣ Add message: text
❂͜͡☆➣ Message:
❂͜͡☆➣ Add comment: text
❂͜͡☆➣ Comment: 
❂͜͡☆➣ Cbroadcast text
❂͜͡☆➣ Gbroadcast text
❂͜͡☆➣ Reject

       ༺•㏒ Instruction Room ㏒•༻

❂͜͡☆➣ Creator
❂͜͡☆➣ Gn: text
❂͜͡☆➣ Invite: mid
❂͜͡☆➣ Invite:on Send contact
❂͜͡☆➣ Mybot
❂͜͡☆➣ Allgift 
❂͜͡☆➣ All mid
❂͜͡☆➣ Cancel
❂͜͡☆➣ Link on/off
❂͜͡☆➣ ginfo
❂͜͡☆➣ Gurl
❂͜͡☆➣ Glist
❂͜͡☆➣ Sett
❂͜͡☆➣ Gcancel: number
❂͜͡☆➣ Masuk / Join
❂͜͡☆➣ Sayang
❂͜͡☆➣ Beb
❂͜͡☆➣ Cinta
❂͜͡☆➣ Sayang pulang
❂͜͡☆➣ Pulang
❂͜͡☆➣ Ban @ target
❂͜͡☆➣ Uban @ target
❂͜͡☆➣ Ban -> send contact
❂͜͡☆➣ Unban -> send contact
❂͜͡☆➣ Comment bl/wl
❂͜͡☆➣ Banlist
❂͜͡☆➣ Cekban
❂͜͡☆➣ Clear ban
❂͜͡☆➣ Kill
❂͜͡☆➣ Kill ban
❂͜͡☆➣ Speed
❂͜͡☆➣ Ambilin @ Steal dp target
❂͜͡☆➣ Sampul @ Steal cover target
❂͜͡☆➣ Copy @ All bot copy target
❂͜͡☆➣ Mycopy @ Copy target profile
❂͜͡☆➣ Keluar @ target
❂͜͡☆➣ music
❂͜͡☆➣ .reboot
❂͜͡☆➣ Wikipedia
❂͜͡☆➣ Cleanse
❂͜͡☆➣ Ybot
❂͜͡☆➣ Ycancel
❂͜͡☆➣ Y1-Y18 Contact Bot
❂͜͡☆➣ Y1-Y2 tl:
❂͜͡☆➣ Y1-Y2 say
❂͜͡☆➣ Y1-Y2 tag
❂͜͡☆➣ Y1-Y2 invite:
❂͜͡☆➣ Y1-Y3 mid
❂͜͡☆➣ Y1-Y2 gurl
❂͜͡☆➣ Y1-Y5 gift
❂͜͡☆➣ Y1-Y18 rename:
❂͜͡☆➣ All: rename all:
❂͜͡☆➣ Allbio: Isi bio:
❂͜͡☆➣ Y1-Y10 rgroup
❂͜͡☆➣ Y1-Y5 join
❂͜͡☆➣ Y1-Y5 bye
❂͜͡☆➣ Y1-Y2 link on/off

     ༺•㏒ COMMAND Protect ㏒•༻

❂͜͡☆➣ Qr on/off
❂͜͡☆➣ Backup on/off
❂͜͡☆➣ Protect On/off
❂͜͡☆➣ Namelock On/off

        
  
      ☆ Ķ͈̤̱͎̱̤̞̭͂̐͒́̀͗͞Ị̵̻̝̘͍͛̏̃͊̉͠ T̩͖͎̹̫͈̿̆̏́̑́S̤̲̯̤̹̲̲̘̏̋̈́̿͒ͅŲ̶̼̲̺̣̬̔̿͐̾̾͘Ṇ̶̨̛̲̭̝̲̝̪̎̾̈́͘͢͜͞É͎̱̺̜̐̀̿͘̕̕͢  B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆


[By.❦〖Pђëŧ〗☞ᵀËÄMທஇລ❂قB❂T✓]

"""

KAC=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl,km,kn,ko,kp,kq,kr,ks,kt]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Gmid = kg.getProfile().mid
Hmid = kh.getProfile().mid
Jmid = kj.getProfile().mid
Lmid = kl.getProfile().mid
Mmid = km.getProfile().mid
Nmid = kn.getProfile().mid
Omid = ko.getProfile().mid
Pmid = kp.getProfile().mid
Qmid = kq.getProfile().mid
Rmid = kr.getProfile().mid
Smid = ks.getProfile().mid
Tmid = kt.getProfile().mid
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots = ["u00f827ce6641038d7c9b6704a9777dfa",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid]
self = ["u00f827ce6641038d7c9b6704a9777dfa",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid]
admin = "u00f827ce6641038d7c9b6704a9777dfa"
owner = "u00f827ce6641038d7c9b6704a9777dfa"
admsa = "u00f827ce6641038d7c9b6704a9777dfa"

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me MY NAME IS PHET",
    "lang":"JP",
    "comment":"AutoLike by Phet",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"༺ ㏒ Ᵽɧëȶ ㏒ ༻",
    "status":False,
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}


setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kd.getProfile()
backup = kd.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ke.getProfile()
backup = ke.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kf.getProfile()
backup = kf.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kg.getProfile()
backup = kg.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kh.getProfile()
backup = kh.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kj.getProfile()
backup = kj.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kl.getProfile()
backup = kl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = km.getProfile()
backup = km.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kn.getProfile()
backup = kn.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ko.getProfile()
backup = ko.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kp.getProfile()
backup = kp.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kq.getProfile()
backup = kq.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
backup = kr.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kt.getProfile()
backup = kt.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


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

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
	aa = ""
	bb = ""
	strt = int(0)
	akh = int(0)
	nm = nama
	print nm
	for mm in nm:
		akh = akh + 3
		aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M","""+json.dumps(mm)+"),"""
		strt = strt + 4
		akh = akh + 1
		bb += "@x \n"
	aa = (aa[:int(len(aa)-1)])
	msg = Message()
	msg.to = to
	msg.from_ = admin
	msg.text = bb
	msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
	print msg
	try:
		cl.sendMessage(msg)
	except Exception as error:
		print error

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
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
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
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
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))


        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kd.getGroup(op.param1)
				    except:
					try:
                                            G = ke.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        kd.updateGroup(G)
                                    except:
                                        try:
                                            ke.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group Name Lock")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wekawekaweka (Har Har)")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

#        if op.type == 17:
#            group = cl.getGroup(op.param1)
#            cb = Message()
#            cb.to = op.param1
#            cb.text = cl.getContact(op.param2).displayName + "สวัสดีครับ😁\nยินดีต้อนรับครับ"
#            cl.sendMessage(cb)
#
#        if op.type == 15:
#            if op.param2 in Bots:
#                return
#            cl.sendText(op.param1, "บายจร้าโชคดีนะครับ😢\nเเล้วพบกันใหม่😢")
#            print "MemberLeft"


        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Jmid:
                        X = kj.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Nmid:
                        G = kn.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)

                if op.param3 in Nmid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)

                if op.param3 in Omid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                if op.param3 in Pmid:
                    if op.param2 in Qmid:
                        X = kq.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                        kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                if op.param3 in Qmid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                if op.param3 in Rmid:
                    if op.param2 in Smid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in Smid:
                    if op.param2 in Tmid:
                        X = kt.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                if op.param3 in Tmid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kn,ko,kp,kq,kr,ks,kt]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
            if Bmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kn,ko,kp,kq,kr,ks,kt]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ticket = kk.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ticket = kc.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kd.updateGroup(X)
                    Ticket = kd.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ticket = ke.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kf.updateGroup(X)
                    Ticket = kf.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kg.updateGroup(X)
                    Ticket = kg.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kj.updateGroup(X)
                    Ti = kj.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kh.updateGroup(X)
                    Ticket = kh.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kj.updateGroup(X)
                    Ticket = kj.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Nmid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ko.updateGroup(G)
                    Ti = ko.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kn.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kn.updateGroup(X)
                    Ti = kn.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Omid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kp.updateGroup(X)
                    Ti = kp.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ticket = ko.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Pmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kq.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kq.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kq.updateGroup(X)
                    Ti = kq.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kp.updateGroup(X)
                    Ticket = kp.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Qmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kr.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kr.updateGroup(X)
                    Ti = kr.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kq.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kq.updateGroup(X)
                    Ticket = kq.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Rmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    Ticket = kr.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Smid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kt.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = ks.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Tmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kt.updateGroup(X)
                    Ticket = kt.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kp.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u00f827ce6641038d7c9b6704a9777dfa":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        wait["dblack"] = False
                        
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        
                        wait["dblacklist"] = False
                        
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Hp","Help","คำสั่ง"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:"," ")
                klist=[kt,ks,kr,kq,kp,ko,kn,kj,kh,kg,kf,ke,kd,kc,kk,ki,cl]
                kicker = random.choice(klist)
                kicker.kickoutFromGroup(msg.to,[midd])

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:"," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Y1 invite:" in msg.text:
                midd = msg.text.replace("Y1 invite:"," ")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Y2 invite:" in msg.text:
                midd = msg.text.replace("Y2 invite:"," ")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif msg.text.lower() == 'hack bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Mmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Nmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Omid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Qmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Rmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Smid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Tmid}
                cl.sendMessage(msg)
                
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "Y1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "Y2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif "Y3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif "Y4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kd.sendMessage(msg)
            elif "Y5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ke.sendMessage(msg)
            elif "Y6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kf.sendMessage(msg)
            elif "Y7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                kg.sendMessage(msg)
            elif "Y8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                kh.sendMessage(msg)
            elif "Y9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                kj.sendMessage(msg)
            elif "Y10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}
                kl.sendMessage(msg)
            elif "Y11" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Mmid}
                km.sendMessage(msg)
            elif "Y12" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Nmid}
                kn.sendMessage(msg)
            elif "Y13" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Omid}
                ko.sendMessage(msg)
            elif "Y14" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid}
                kp.sendMessage(msg)
            elif "Y15" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Qmid}
                kq.sendMessage(msg)
            elif "Y16" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Rmid}
                kr.sendMessage(msg)
            elif "Y17" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Smid}
                ks.sendMessage(msg)
            elif "Y18" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Tmid}
                kt.sendMessage(msg)

            elif msg.text in ["ของขวัญ"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Gift","Y1gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Y2 gift","Y2gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["Y3 gift","Y3gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["Y4 gift","Y4gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                kd.sendMessage(msg)
            elif msg.text in ["Y5 gift","Y5gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                ke.sendMessage(msg)
            elif msg.text in ["Allgift","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                kd.sendMessage(msg)
                ke.sendMessage(msg)
                kf.sendMessage(msg)
                kg.sendMessage(msg)
                kh.sendMessage(msg)
                kj.sendMessage(msg)
                kn.sendMessage(msg)
                ko.sendMessage(msg)
                kp.sendMessage(msg)
                kq.sendMessage(msg)
                kr.sendMessage(msg)
                ks.sendMessage(msg)
                kt.sendMessage(msg)
#==================================================
            elif "#ชื่อบอท:" in msg.text:
                string = msg.text.replace("#ชื่อบอท:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kd.getProfile()
                    profile.displayName = string
                    kd.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ke.getProfile()
                    profile.displayName = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kf.getProfile()
                    profile.displayName = string
                    kf.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kg.getProfile()
                    profile.displayName = string
                    kg.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kh.getProfile()
                    profile.displayName = string
                    kh.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kj.getProfile()
                    profile.displayName = string
                    kj.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kl.getProfile()
                    profile.displayName = string
                    kl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = km.getProfile()
                    profile.displayName = string
                    km.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kn.getProfile()
                    profile.displayName = string
                    kn.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ko.getProfile()
                    profile.displayName = string
                    ko.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kp.getProfile()
                    profile.displayName = string
                    kp.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kq.getProfile()
                    profile.displayName = string
                    kq.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kr.getProfile()
                    profile.displayName = string
                    kr.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kt.getProfile()
                    profile.displayName = string
                    kt.updateProfile(profile)
                    cl.sendText(msg.to,"nama berubah menjadi " + string + "")
            elif "#ตัสบอท:" in msg.text:
                string = msg.text.replace("#ตัสบอท:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kd.getProfile()
                    profile.statusMessage = string
                    kd.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kf.getProfile()
                    profile.statusMessage = string
                    kf.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kg.getProfile()
                    profile.statusMessage = string
                    kg.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kh.getProfile()
                    profile.statusMessage = string
                    kh.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kj.getProfile()
                    profile.statusMessage = string
                    kj.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kl.getProfile()
                    profile.statusMessage = string
                    kl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = km.getProfile()
                    profile.statusMessage = string
                    km.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kn.getProfile()
                    profile.statusMessage = string
                    kn.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kp.getProfile()
                    profile.statusMessage = string
                    kp.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kq.getProfile()
                    profile.statusMessage = string
                    kq.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kr.getProfile()
                    profile.statusMessage = string
                    kr.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kt.getProfile()
                    profile.statusMessage = string
                    kt.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
                if msg.text == "setttttt":
                    sendMessage(msg.to, "I have set a read point ♪\n「tes」I will show you who I have read ♪")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    print wait
            elif "#ชื่อตัวเอง:" in msg.text:
                string = msg.text.replace("#ชื่อตัวเอง:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names Menjadi : " + string + "")
#==================================================
            elif 'testpic ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('testpic ','')
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
            elif 'wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif msg.text.lower() == '.reboot':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
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
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'music:' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music:','')
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
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            elif msg.text in ["ยกเลิก"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["บอทยกเลิก"]:
                if msg.toType == 2:
                    klist=[kj,kh,kg,kf,ke,kd,kc,kk,ki,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kicker.sendText(msg.to,"No one is inviting")
                        else:
                            kicker.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kicker.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kicker.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["!Link on"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Y1 link on"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"done")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Y2 link on"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"done")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["!Link off"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Y1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"done")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Y2 link off"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"done")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == '!ginfo':
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif msg.text in ["!Glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = kk.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kk.getGroup(i).name + " | [ " + str(len (kk.getGroup(i).members)) + " ]")
                kk.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = kc.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kc.getGroup(i).name + " | [ " + str(len (kc.getGroup(i).members)) + " ]")
                kc.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif msg.text in ["Creator"]:
				msg.contentType = 13
				msg.contentMetadata = {'mid': mid}
				cl.sendMessage(msg)
				cl.sendText(msg.to,"My Creator 👉Tamii PSD T&Z TEAM ")
            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)
            elif "!Bot mid" == msg.text:
		#	cl.sendText(msg.to,mid)
			ki.sendText(msg.to,Amid)
			kk.sendText(msg.to,Bmid)
			kc.sendText(msg.to,Cmid)
			kd.sendText(msg.to,Dmid)
			ke.sendText(msg.to,Emid)
			kf.sendText(msg.to,Fmid)
			kg.sendText(msg.to,Gmid)
			kh.sendText(msg.to,Hmid)
			kj.sendText(msg.to,Jmid)
			kl.sendText(msg.to,Lmid)
			km.sendText(msg.to,Mmid)
			kn.sendText(msg.to,Nmid)
			ko.sendText(msg.to,Omid)
			kp.sendText(msg.to,Pmid)
			kq.sendText(msg.to,Qmid)
			kr.sendText(msg.to,Rmid)
			ks.sendText(msg.to,Smid)
			kt.sendText(msg.to,Tmid)
				
            elif ("Hack " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" + key1)

            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)





            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)			
            elif "Y1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Y2 mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Y3 mid" == msg.text:
                kc.sendText(msg.to,Cmid)
				
            #elif "Respon" in msg.text:
                #ki.sendText(msg.to,"")
                #kk.sendText(msg.to,"")
#======================================
            elif "Tl: " in msg.text:
                tl_text = msg.text.replace("Tl: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Y1 tl: " in msg.text:
                tl_text = msg.text.replace("Y1 tl: ","")
                ki.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ki.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Y2 tl: " in msg.text:
                tl_text = msg.text.replace("Y2 tl: ","")
                kk.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kk.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Protect:on","Protect on"]:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:off","Qr off"]:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:on","Qr on"]:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:off","Protect off"]:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                else:
                    cl.sendText(msg.to,"bone..")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"bone..")
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Done..")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Done..")
				except:
					pass
            elif "Cn: " in msg.text:
                string = msg.text.replace("Cn: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif "Y1 rename: " in msg.text:
                string = msg.text.replace("Y1 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y2 rename: " in msg.text:
                string = msg.text.replace("Y2 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y3 rename: " in msg.text:
                string = msg.text.replace("Y3 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kc.getProfile()
                    profile_B.displayName = string
                    kc.updateProfile(profile_B)
                    kc.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y4 rename: " in msg.text:
                string = msg.text.replace("Y4 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kd.getProfile()
                    profile_B.displayName = string
                    kd.updateProfile(profile_B)
                    kd.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y5 rename: " in msg.text:
                string = msg.text.replace("Y5 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ke.getProfile()
                    profile_B.displayName = string
                    ke.updateProfile(profile_B)
                    ke.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y6 rename: " in msg.text:
                string = msg.text.replace("Y6 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kf.getProfile()
                    profile_B.displayName = string
                    kf.updateProfile(profile_B)
                    kf.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y7 rename: " in msg.text:
                string = msg.text.replace("Y7 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kg.getProfile()
                    profile_B.displayName = string
                    kg.updateProfile(profile_B)
                    kg.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y8 rename: " in msg.text:
                string = msg.text.replace("Y8 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kh.getProfile()
                    profile_B.displayName = string
                    kh.updateProfile(profile_B)
                    kh.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y9 rename: " in msg.text:
                string = msg.text.replace("Y9 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kj.getProfile()
                    profile_B.displayName = string
                    kj.updateProfile(profile_B)
                    kj.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y10 rename: " in msg.text:
                string = msg.text.replace("Y10 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kl.getProfile()
                    profile_B.displayName = string
                    kl.updateProfile(profile_B)
                    kl.sendText(msg.to,"Name " + string + " Done Bosqu")                                
            elif "Y11 rename: " in msg.text:
                string = msg.text.replace("Y11 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = km.getProfile()
                    profile_B.displayName = string
                    km.updateProfile(profile_B)
                    km.sendText(msg.to,"Name " + string + " Done Bosqu")                                
            elif "Y12 rename: " in msg.text:
                string = msg.text.replace("Y2 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kn.getProfile()
                    profile_B.displayName = string
                    kn.updateProfile(profile_B)
                    kn.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y13 rename: " in msg.text:
                string = msg.text.replace("Y13 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ko.getProfile()
                    profile_B.displayName = string
                    ko.updateProfile(profile_B)
                    ko.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y14 rename: " in msg.text:
                string = msg.text.replace("Y14 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kp.getProfile()
                    profile_B.displayName = string
                    kp.updateProfile(profile_B)
                    kp.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y15 rename: " in msg.text:
                string = msg.text.replace("Y15 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kq.getProfile()
                    profile_B.displayName = string
                    kq.updateProfile(profile_B)
                    kq.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y16 rename: " in msg.text:
                string = msg.text.replace("Y16 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kr.getProfile()
                    profile_B.displayName = string
                    kr.updateProfile(profile_B)
                    kr.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y17 rename: " in msg.text:
                string = msg.text.replace("Y17 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ks.getProfile()
                    profile_B.displayName = string
                    ks.updateProfile(profile_B)
                    ks.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Y18 rename: " in msg.text:
                string = msg.text.replace("Y18 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kt.getProfile()
                    profile_B.displayName = string
                    kt.updateProfile(profile_B)
                    kt.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif msg.text in ["K on","Contact:on","Contact on","K:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["K:off","Contact:off","Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif msg.text in ["Auto join on","Join on","Join:on","Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Join off","Auto join off","Auto join:off","Join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Leave:on","Auto leave on","Auto leave:on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Leave:off","Auto leave off","Auto leave:off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")

            elif msg.text in ["共有:オン","Share on","Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["共有:オフ","Share off","Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Auto like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Like off","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")


            elif msg.text in ["Sett"]:
                print "Setting pick up..."
                md = "✯= ꧁ 🐯हईທຮຮๅજईह🐯 ꧂=✯\n\n"
                if wait["likeOn"] == True: md+="􀜁􀇔􏿿 Auto like : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto like : off 􀜁􀄰􏿿\n"
#                if wait["copy"] == True: md+="�� Mimic : on\n"
#                else:md+=" �� Mimic : off\n"
                if wait["winvite"] == True: md+=" �� Invite : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Invite : off 􀜁􀄰􏿿\n"
                if wait["pname"] == True: md+="􀜁􀇔􏿿 Namelock : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Namelock : off 􀜁􀄰􏿿\n"
                if wait["contact"] == True: md+="􀜁􀇔􏿿 Contact : on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Contact : off 􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀜁􀇔􏿿 Auto join : on 􀜁􀄯􏿿\n"
                else: md +="􀜁􀇔􏿿 Auto join : off 􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇔􏿿 Group cancel :" + str(wait["autoCancel"]["members"]) + " 􀜁􀄯􏿿\n"
                else: md+= "􀜁􀇔􏿿 Group cancel : off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇔􏿿 Auto leave : on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Auto leave : off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀜁􀇔􏿿 Share : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Share : off 􀜁􀄰􏿿\n"
                if wait["clock"] == True: md+="􀜁􀇔􏿿 Clock Name : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Clock Name : off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀜁􀇔􏿿 Auto add : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto add : off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀜁􀇔􏿿 Comment : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Comment : off 􀜁􀄰􏿿\n"
                if wait["Backup"] == True: md+="􀜁􀇔􏿿 Backup : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Backup : off 􀜁􀄰􏿿\n"
                if wait["qr"] == True: md+="􀜁􀇔􏿿 Protect QR : on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Protect QR : off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
#========================================
#------------------------------------------------
            elif msg.text in ["Gcreator:inv","เชิญเเอทมิน"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif msg.text in ["Backup:on","Backup on","เปิดการเชิญกลับ"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off","ปิดการเชิญกลับ"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Reject"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y1 rgroups","Y1 rgroup"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Bot All invitations is clean")
                else:
                    ki.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Add:on","Auto add on","Auto add:on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah on Bosqu")
            elif msg.text in ["Add:off","Auto add off","Auto add:off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah off Bosqu")
#========================================
#========================================
            elif "Message: " in msg.text:
                wait["message"] = msg.text.replace("Message: ","")
                cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message: " in msg.text:
                wait["message"] = msg.text.replace("Add message: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Message"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Comment: " in msg.text:
                c = msg.text.replace("Comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment: " in msg.text:
                c = msg.text.replace("Add comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["Comment on","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Comment off","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Comment"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        uye.updateGroup(x)
                    gurl = uye.reissueGroupTicket(msg.to)
                    uye.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================
            elif msg.text.lower() == 'botname':
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + ""
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + ""
                kc.sendText(msg.to, text)
                profile = kd.getProfile()
                text = profile.displayName + ""
                kd.sendText(msg.to, text)
                profile = ke.getProfile()
                text = profile.displayName + ""
                ke.sendText(msg.to, text)
                profile = kf.getProfile()
                text = profile.displayName + ""
                kf.sendText(msg.to, text)
                profile = kg.getProfile()
                text = profile.displayName + ""
                kg.sendText(msg.to, text)
                profile = kh.getProfile()
                text = profile.displayName + ""
                kh.sendText(msg.to, text)
                profile = kj.getProfile()
                text = profile.displayName + ""
                kj.sendText(msg.to, text)
                profile = kn.getProfile()
                text = profile.displayName + ""
                kn.sendText(msg.to, text)
                profile = ko.getProfile()
                text = profile.displayName + ""
                ko.sendText(msg.to, text)
                profile = kp.getProfile()
                text = profile.displayName + ""
                kp.sendText(msg.to, text)
                profile = kq.getProfile()
                text = profile.displayName + ""
                kq.sendText(msg.to, text)
                profile = kr.getProfile()
                text = profile.displayName + ""
                kr.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName + ""
                ks.sendText(msg.to, text)
                profile = kt.getProfile()
                text = profile.displayName + ""
                kt.sendText(msg.to, text)
                profile = kl.getProfile()
                text = profile.displayName + ""
                kl.sendText(msg.to, text)
                profile = km.getProfile()
                text = profile.displayName + ""
                km.sendText(msg.to, text)
            elif "Ambil QR: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Ambil QR: ","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Not for use less than group")
            elif "Y1 gurl: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Y1 gurl: ","")
                    x = ki.getGroup(gid)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(gid)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    ki.sendText(msg.to,"Not for use less than group")
            elif "Y2 gurl: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Y2 gurl: ","")
                    x = kk.getGroup(gid)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(gid)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    kk.sendText(msg.to,"Not for use less than group")
#========================================
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Clock:on","Clock on","Jam on","Jam:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")

            elif msg.text in ["Clock:off","Clock off","Jam off","Jam:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")

            elif "Cc: " in msg.text:
                n = msg.text.replace("Cc: ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Changed to:\n\n" + n)
            elif msg.text in ["!Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Refresh to update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

#========================================
            elif "Hack3 @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Hack3 @","")
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
                        except:
                            pass
                print "[Command]dp executed"
            elif "Hack2mid" in msg.text:
                umid = msg.text.replace("Hack2mid:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Hack2 " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Hack2 ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")

#===============================================
            elif msg.text in ["Sp","sp"]:
                cl.sendText(msg.to, "Restarting......")
                start = time.time()
                time.sleep(0.001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"

            elif msg.text in ["Keyy"]:
                cl.sendText(msg.to, "[SELFBOT PHET HACK BOT]\n\n❂͜͡☆➣ Namelock on\n❂͜͡☆➣ Namelock off\n❂͜͡☆➣ Blockinvite on\n❂͜͡☆➣ Blockinvite off\n❂͜͡☆➣ Backup on\n❂͜͡☆➣ Backup off\n\n[By.เพชร ทีมทดลองบอท]")
















#========================================
            elif msg.text in ["!Botbb"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    kd.updateDisplayPicture(backup.pictureStatus)
                    kd.updateProfile(backup)
                    ke.updateDisplayPicture(backup.pictureStatus)
                    ke.updateProfile(backup)
                    kf.updateDisplayPicture(backup.pictureStatus)
                    kf.updateProfile(backup)
                    kg.updateDisplayPicture(backup.pictureStatus)
                    kg.updateProfile(backup)
                    kh.updateDisplayPicture(backup.pictureStatus)
                    kh.updateProfile(backup)
                    kj.updateDisplayPicture(backup.pictureStatus)
                    kj.updateProfile(backup)
                    kl.updateDisplayPicture(backup.pictureStatus)
                    kl.updateProfile(backup)
                    km.updateDisplayPicture(backup.pictureStatus)
                    km.updateProfile(backup)
                    kn.updateDisplayPicture(backup.pictureStatus)
                    kn.updateProfile(backup)
                    ko.updateDisplayPicture(backup.pictureStatus)
                    ko.updateProfile(backup)
                    kp.updateDisplayPicture(backup.pictureStatus)
                    kp.updateProfile(backup)
                    kq.updateDisplayPicture(backup.pictureStatus)
                    kq.updateProfile(backup)
                    kr.updateDisplayPicture(backup.pictureStatus)
                    kr.updateProfile(backup)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    ks.updateProfile(backup)
                    kt.updateDisplayPicture(backup.pictureStatus)
                    kt.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#----------------------------------------------
            elif "!Botcopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("!Botcopy @","")
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
                                    ki.cloneContactProfile(target)
                                    kk.cloneContactProfile(target)
                                    kc.cloneContactProfile(target)
                                    kd.cloneContactProfile(target)
                                    ke.cloneContactProfile(target)
                                    kf.cloneContactProfile(target)
                                    kg.cloneContactProfile(target)
                                    kh.cloneContactProfile(target)
                                    kj.cloneContactProfile(target)
                                    kl.cloneContactProfile(target)
                                    km.cloneContactProfile(target)
                                    kn.cloneContactProfile(target)
                                    ko.cloneContactProfile(target)
                                    kp.cloneContactProfile(target)
                                    kq.cloneContactProfile(target)
                                    kr.cloneContactProfile(target)
                                    ks.cloneContactProfile(target)
                                    kt.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#===============================================
            elif "!Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("!Mycopy @","")
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
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#=================================================
            elif msg.text in ["!Mebb"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#=================================================
            elif msg.text == "!ตั้งเวลา":
                    cl.sendText(msg.to, "!โปรดรอ..กรุณาพิมพ์ !อ่าน")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "!อ่าน":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Lurking dulu dudul Baru bilang result Point.")
						
#========================================
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
            elif "!Kickall" in msg.text:
              if msg.from_ in Bots:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("!Kickall","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"🔸We come to destroy your group🔸")
                    kk.sendText(msg.to,"Relax slow slow no baper...😂😂")
                    kc.sendText(msg.to,"Kenapa diem aja..??")
                    ks.sendText(msg.to,"Tangkis Bego Jangan Gemeter...😂😂")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kn,ko,kp,kq,kr,ks,kt]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kl.sendText(msg.to,"H")
                                km.sendText(msg.to,"A")
                                kl.sendText(msg.to,"L")
                                km.sendText(msg.to,"O")
#================================================
#========================================
            elif msg.text.lower() == 'wc':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#=======================================
#-------------------Fungsi spam start--------------------------
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])

#-------------------Fungsi spam finish----------------------------
#-----------------------------------------------
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#================================================
#===============================================
#=================================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#-----------------------------------------------
            elif "!Mid @" in msg.text:
                _name = msg.text.replace("!Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-------------------------------------------------
            elif "!ส่งข้อความ:" in msg.text:
					bctxt = msg.text.replace("Cbroadcast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "!ส่งข้อความกลุ่ม" in msg.text:
					bctxt = msg.text.replace("Gbroadcast ", "")
					n = cl.getGroupIdsJoined()
					for manusia in n:
						cl.sendText(manusia,(bctxt))
										 
#========================================
            elif msg.text in ["Gu Tar","!Phet","#phet","มาหำ"]:
					G = cl.getGroup(msg.to)
					info = cl.getGroup(msg.to)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					invsend = 0
					Ticket = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kk.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kd.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ke.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kf.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kg.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kh.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kj.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kn.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ko.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kp.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kq.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kr.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ks.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kt.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					print "All_Kickers_Ok!"
					G.preventJoinByTicket(G)
					cl.updateGroup(G)
            elif msg.text in ["Y1 join","P1 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)                 
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  print "Kicker1_Ok!"
                  Ticket = ki.reissueGroupTicket(msg.to)
            elif msg.text in ["Y2 join","P2 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)                 
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kk.reissueGroupTicket(msg.to)
            elif msg.text in ["Y3 join","P3 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)                 
                  G = kc.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  print "Kicker3_Ok!"
                  Ticket = kc.reissueGroupTicket(msg.to)
            elif msg.text in ["Y4 join","P4 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kd.acceptGroupInvitationByTicket(msg.to,Ti)                 
                  G = kd.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kd.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kd.reissueGroupTicket(msg.to)
            elif msg.text in ["Y5 join","P5 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)                 
                  G = ke.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = ke.reissueGroupTicket(msg.to)
            elif msg.text in ["Go1"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kd.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  G = ke.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  print "Algojo_Ready!"
                  Ticket = ke.reissueGroupTicket(msg.to)
            elif msg.text in ["Go2"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kf.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kg.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kh.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kj.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kn.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  G = kn.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kn.updateGroup(G)
                  print "Algojo_Ready!"
                  Ticket = kn.reissueGroupTicket(msg.to)
            elif msg.text in ["Go3"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ko.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kp.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kq.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kr.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  kt.acceptGroupInvitationByTicket(msg.to,Ti)
                  time.sleep(0.01)
                  G = kt.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kt.updateGroup(G)
                  print "Algojo_Ready!"
                  Ticket = kt.reissueGroupTicket(msg.to)
            elif msg.text in ["บอทออกทั้งหมด","บอทออกทุกกลุ่ม"]:
				gid = cl.getGroupIdsJoined()
				gid = ki.getGroupIdsJoined()
				gid = kk.getGroupIdsJoined()
				gid = kc.getGroupIdsJoined()
				gid = kd.getGroupIdsJoined()
				gid = ke.getGroupIdsJoined()
				gid = kf.getGroupIdsJoined()
				gid = kg.getGroupIdsJoined()
				gid = kh.getGroupIdsJoined()
				gid = kj.getGroupIdsJoined()
				gid = kn.getGroupIdsJoined()
				gid = ko.getGroupIdsJoined()
				gid = kp.getGroupIdsJoined()
				gid = kq.getGroupIdsJoined()
				gid = kr.getGroupIdsJoined()
				gid = ks.getGroupIdsJoined()
				gid = kt.getGroupIdsJoined()
				for i in gid:
					ki.leaveGroup(i)
					kk.leaveGroup(i)
					kc.leaveGroup(i)
					kd.leaveGroup(i)
					ke.leaveGroup(i)
					kf.leaveGroup(i)
					kg.leaveGroup(i)
					kh.leaveGroup(i)
					kj.leaveGroup(i)
					kn.leaveGroup(i)
					ko.leaveGroup(i)
					kp.leaveGroup(i)
					kq.leaveGroup(i)
					kr.leaveGroup(i)
					ks.leaveGroup(i)
					kt.leaveGroup(i)
				if wait["lang"] == "JP":
					ki.sendText(msg.to,"KAMI PAMIT TEMAN👋😂")
				else:
					ki.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Gu bye","!bye","!Bye","#Bye","#bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ki.leaveGroup(msg.to)
                     kk.leaveGroup(msg.to)
                     kc.leaveGroup(msg.to)
                     kd.leaveGroup(msg.to)
                     ke.leaveGroup(msg.to)
                     kf.leaveGroup(msg.to)
                     kg.leaveGroup(msg.to)
                     kh.leaveGroup(msg.to)
                     kj.leaveGroup(msg.to)
                     kl.leaveGroup(msg.to)
                     km.leaveGroup(msg.to)
                     kn.leaveGroup(msg.to)
                     ko.leaveGroup(msg.to)
                     kp.leaveGroup(msg.to)
                     kq.leaveGroup(msg.to)
                     kr.leaveGroup(msg.to)
                     ks.leaveGroup(msg.to)
                     kt.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y1 @bye","Y1 pulang","P1 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ki.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y2 @bye","Y2 pulang","P2 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kk.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y3 @bye","Y3 pulang","P3 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kc.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y4 @bye","Y4 pulang","Y4 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kd.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y5 @bye","Y5 pulang","P5 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ke.leaveGroup(msg.to)
                except:
                     pass
            elif "Hm " in msg.text:
                  if msg.from_ in admin:                                        
                       mk0 = msg.text.replace("Hm ","")
                       mk1 = mk0.lstrip()
                       mk2 = mk1.replace("@","")
                       mk3 = mk2.rstrip()
                       _name = mk3
                       gs = ki.getGroup(msg.to)
                       targets = []
                       for h in gs.members:
                           if _name in h.displayName:
                              targets.append(h.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                               try:
                                 if msg.from_ not in target:
                                   ki.kickoutFromGroup(msg.to,[target])
                               except:
								   random.choice(KAC).kickoutFromGroup(msg.to,[target])
								
#==========================================
            elif "ยูทูป:" in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif "Youtube:" in msg.text:
                 query = msg.text.replace("Youtube:","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
#==========================================
            elif msg.text in ["Mimic on","mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off","mimic:off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list","Mic check"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#==========================================
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,kd,ke,cl,kf,kg,kh,kj,kn,ko,kp,kq,kr,ks,kt]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "!!Phet!!" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("!!Phet!!","")
                    klist=[km,kl,kj,kh,kg,kf,ke,kd,kc,kk,ki,cl,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kn.getGroup(msg.to)
                    gs = ko.getGroup(msg.to)
                    gs = kp.getGroup(msg.to)
                    gs = kq.getGroup(msg.to)
                    gs = kr.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = kt.getGroup(msg.to)
                    kicker.sendText(msg.to,"􂀁􀄃「 Cleanse 」 is Starting")
                    kicker.sendText(msg.to,"Group Anda Pantas Di Bersihkan.")
                    kicker.sendText(msg.to,"Good Bye (*´･ω･*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                               klist=[km,kl,kj,kh,kg,kf,ke,kd,kc,kk,ki,cl,kn,ko,kp,kq,kr,ks,kt]
                               kicker = random.choice(klist)
                               kicker.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                kk.sendText(msg,to,"Group cleanse")
                            pass
            elif ("#PK " in msg.text):
				if msg.from_ in admin:
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
							
            elif "!KK " in msg.text:
                       nk0 = msg.text.replace("!NK ","")
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
                       kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
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
                                    kl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kl.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
							
            elif "!KK1 " in msg.text:
                       nk0 = msg.text.replace("!KK1 ","")
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
                       km.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
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
                                    km.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    km.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif ("2PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ke.kickoutFromGroup(msg.to,[target])
                       except:
                           kie.sendText(msg.to,"Error")
            elif ("3PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           kd.kickoutFromGroup(msg.to,[target])
                       except:
                           kd.sendText(msg.to,"Error")

            elif "Phet@@" in msg.text:
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


            elif ("!PK " in msg.text):
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
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kk.sendText(msg.to,"Success Boss")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Masuk daftar orang bejat Boss")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Sudah di keluarkan dari daftar bejat Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear ban","ล้างดำ"]:
				wait["blacklist"] = {}
				cl.sendText(msg.to,"clear")
				
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
			
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["!Me ban","Cekban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["!Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        kd.kickoutFromGroup(msg.to,[jj])
                        ke.kickoutFromGroup(msg.to,[jj])
                        
                    cl.sendText(msg.to,"Blacklist user")
#=============================================
#=============================================
#=============================================
            elif "Hack4" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#=============================================
            elif msg.text in ["!Sp"]:
                start = time.time()
                cl.sendText(msg.to, "Access time Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s<==Tamii Server" % (elapsed_time))
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Bl " in msg.text):
              if msg.from_ in admin:
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
                      cl.sendText(msg.to,"Succes Banned Bos")
                   except:
                      pass        
#============================================
            #elif msg.text in ["Clear"]:
                #if msg.toType == 2:
                    #group = cl.getGroup(msg.to)
                    #gMembMids = [contact.mid for contact in group.invitee]
                    #for _mid in gMembMids:
                        #random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                    #cl.sendText(msg.to,"Clear boss!!!")
            elif msg.text in ["!@tag"]:
				if msg.toType == 2:
					if msg.contentType == 0:
						group = cl.getGroup(msg.to)
						nama = [contact.mid for contact in group.members]
						nm1, nm2, jml = [], [], len(nama)
						if jml <= 100:
							mention(msg.to, nama)
						if jml > 100 and jml < 200:
							for i in range(0.99):
								nm1 += [nama[i]]
							mention(msg.to, nm1)
							for j in range(100, len(nama)-1):
								nm2 += [nama[j]]
							mention(msg.to, nm2)
						if jml > 200 and jml < 300:
							for i in range(0.99):
								nm1 += [nama[i]]
							mention(msg.to, nm1)
							for j in range(100, 199):
								nm2 += [nama[j]]
							mention(msg.to, nm2, jml)
							for k in range(200, len(nama)-1):
								nm3 += [nama[k]]
							mention(msg.to, nm3, jml)
						if jml > 300:
							print " terlalu banyak mem 300+"
						cnt = message()
						cnt.text =  "Done:"+str(jml)
						cont.to = msg.to
						cl.sendMessage(cnt)
					
            elif msg.text in ["!Tar@@","!Phet@@"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    name = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in name:
                       akh = akh + int(5)
                       cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                       strt = strt + int(6)
                       akh = akh + 1
                       cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
            elif msg.text in ["!Y1tag","!Y1 tag"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    name = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in name:
                       akh = akh + int(5)
                       cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                       strt = strt + int(6)
                       akh = akh + 1
                       cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        ki.sendMessage(msg)
                    except Exception as error:
                        print error
            elif msg.text in ["!Y2tag","!Y2 tag"]:
                if msg.toType == 2:
                    group = kk.getGroup(msg.to)
                    name = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in name:
                       akh = akh + int(5)
                       cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                       strt = strt + int(6)
                       akh = akh + 1
                       cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        kk.sendMessage(msg)
                    except Exception as error:
                        print error
#===========================================
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = "u00f827ce6641038d7c9b6704a9777dfa"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				kd.kickoutFromGroup(op.param1,[op.param2])
				ke.kickoutFromGroup(op.param1,[op.param2])
				kf.kickoutFromGroup(op.param1,[op.param2])
				kg.kickoutFromGroup(op.param1,[op.param2])
				kh.kickoutFromGroup(op.param1,[op.param2])
				kj.kickoutFromGroup(op.param1,[op.param2])
				kn.kickoutFromGroup(op.param1,[op.param2])
				ko.kickoutFromGroup(op.param1,[op.param2])
				kp.kickoutFromGroup(op.param1,[op.param2])
				kq.kickoutFromGroup(op.param1,[op.param2])
				kr.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kt.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#===========================================
#        if op.type == 55:
#            try:
#				if op.param1 in wait2['readPoint']:
#					Name = cl.getContact(op.param2).displayName
#					if Name in wait2['readMember'][op.param1]:
#						pass
#					else:
#						wait2['readMember'][op.param1] += "\n╠" + Name
#						wait2['ROM'][op.param1][op.param2] = "╠" + Name
#				else:
#					cl.sendText
#            except:
#                pass
#						
#						
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n✪ " + Nama
                        wait2['ROM'][op.param1][op.param2] = "✪ " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass




#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
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
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
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
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
