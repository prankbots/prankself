# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia

cl = LINETCR.LINE()
cl.login(token="EmZMiC3V1ZV70KrEMMw6.TZBfSxLpwQmajTfI0hZL5G.11k6S1sUlX9SbdA8oDJustBIJVGyobI+e3SFkBE2g8g=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmfUsg0drkp2fEBi9Qrb.BNyZ+h9RxCUErhI47z2TsW.zP88/CrIW13pa4qwh5FWcAP0dO+OfD820zCPF4pX5oc=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EmspKirwbEjemqqHJUb7.PxA11UvF6+oIj1J2xHVgHW.DD+N4SDD7wvuasJsGnmW5plCMBHpI1kffIFV9ma44Kc=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EmdpE54Je1ojetkXmKQd.3ZijQj/+HYJ/+9NTGXTdBq.Dkv3tBOnJ4DsvFu6ER5mK2zR7h0FRAW0/FJyZiSD2Fs=")
kc.loginResult()

kd = LINETCR.LINE()
kd.login(token="Emesgp6g4xLptFAcKEe2.HczpEpY3698wuSB+TzCDKG.vFtZpDippE+ZkQxxVEDn1BmpjyM+z+f/x4/Lo+cAFlk=")
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token="EmMtwsiInIfBXPVS5fYa.i/2QVqxGpVzmWQXItt4HYG.cfbtejgIlGQE3TTAg7FlMWcE1/6kwokKNe3wDg1gztM=")
ke.loginResult()

kf = LINETCR.LINE()
kf.login(token="EmCxepD4zQoJp5IhDbta.DP7HM0ARnuIu/2g0+3pMUG./+3rQ+luem39IsiuASywPOVjmG+0TpJhMpmZowgn8yI=")
kf.loginResult()

kg = LINETCR.LINE()
kg.login(token="Eme45nZDSATx9C6vYxRa.M5S4YxDWvhoYOasbMPWroG.Tq/iSCV68m9567XK4xxEGSXOAOVJEPwNW+odUm/BwT4=")
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token="EmIRhD60WnHD3t4FET34.9gH7ABV+xQLJo9i7SbFX5a.Yr0Yii0G3ouW7kOEMdXrPongIIs0Q2ab9Q0xUiRLfHI=")
kh.loginResult()

kj = LINETCR.LINE()
kj.login(token="EmLppwNR3nIRHTOtPilb.8udcfgLi7ehlJbE2o+xCkW.QzwPU+t85FDCd/TcU0H5NdPq0MUzuCXRzaZPRp1O/mY=")
kj.loginResult()

kl = LINETCR.LINE()
kl.login(token="EmYDhAhUQqmCaUB8SZA4.XzkQX6Z6SKas/aWEdxhG9a.HTgYRulRHxXSc+72zLVfT2VLIRVZvh4ImQvEtU6KxBg=")
kl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""
S̵̩̥̬̳͎̥͗̇̿́͛͑͛̓͢͝e̢̡͈̥͒̈̍̓́̍͆͜͡l̛̟͓̺̲̝̳̫̩̠̅̈́̍̿͘͝ḟ̴͔͈̜͓̪̊́̋̉̇͗͐̚͠ C̷̡͖̭͕̗̐̓̎̿̚̕͜͜͢͡ͅo̧̩̙̙̹̰͇̅̑̿͘͝ṃ̵̫͔̣̣̬͇̄̅͛͗̕m̷̜͕̣͎͔̤͗̍̿̐͞͞͝ą̸̛͚̹̫̯̖̈͑͊̕n̝̟͎͉͍̪͚̪͖̈́̑͌̇̀̏d̛̥̙͕̯̲͔͙͍̾̍̓͘͞ I̛͕̮̝͉̞̯̞̜̓̎̂͐͒̒̕͢ń̵̨͇͙͙̺̲͇͖̯͕̆͗̓́̍͘̚͞͞ Ḡ̢̖̙͖̮̀̄͑̃̓́̆̚r̴̻̝͕̭̘̎̐͑͆͟͜͜͝o̫̞̤͉̪͉̿͐̏̓̕̕ú̝͖̠͎̅́̌͊̀̏̊͟͠͠p̷̝̮̰̺̫̬̤̗̒͒̉̾̀̅̾͊̿̈́ͅ

❄ Me 
❄ Id
❄ Mid
❄ Gift
❄ Mid @
❄ Cn: Display Name
❄ Cc: Clock Name
❄ Mc
❄ Mc:
❄ Mybio: "text"
❄ Allbio: "text"
❄ Myname: "text"
❄ All: "text"
❄ Tl: "text"
❄ Auto join: on/off
❄ Auto add: on/off
❄ Auto leave: on/off
❄ Clock: on/off
❄ Share on/off
❄ Add message: text
❄ Message:
❄ Add comment: text
❄ Comment: 
❄ Cbroadcast text
❄ Gbroadcast text
❄ Reject
❄ Copy @
❄ Backup copy
❄ Admin add @
❄ Unadmin @
❄ Staff add @
❄ Unstaff @
❄ Spam change: @ 
❄ Spam add: @
❄ Spam: @
❄ Test @
❄ Creator
❄ Gn: text
❄ Invite: mid
❄ mybot
❄ Allgift 
❄ All mid
❄ Cancel
❄ Link on/off
❄ ginfo
❄ Glist
❄ Kepo @
❄ Say
❄ User
❄ Set
❄ Gcancel: number
❄ Join (Rian)
❄ Soldier
❄ Byeall
❄ Ban @ target
❄ Uban @ target
❄ Ban -> send contact
❄ Unban -> send contact
❄ Banlist
❄ Cekban
❄ Clear ban
❄ Kill
❄ Kill ban
❄ Sp
❄ Target list
❄ Target @
❄ Mimic target me/target
❄ Del target @
❄ Mimic on/off
❄ Steal @
❄ Steal cover @
❄ Mentionall
❄ Youtube: "teks"
❄ Nk @ target
❄ Mk: @ target
❄ Keluar @ target
❄ Bunuh @ target
❄ Buang1-Buang @ target
❄ .lyrik
❄ .reboot
❄ .instagram "text"
❄ wikipedia "text"
❄ music "text'
❄ Lurking
❄ result
❄ responsebot
❄ Ycancel
❄ Y1-Y2 tl:
❄ Y1-Y2 say
❄ Y1-Y2 tag
❄ Y1-Y2 invite:
❄ Y1-Y3 mid
❄ Y1-Y2 gurl
❄ Y1-Y5 gift
❄ Y1-Y10 rename:
❄ Y1-Y10 rgroup
❄ Y1-Y5 join
❄ Y1-Y5 bye
❄ Sticker-Sticker10
❄ Y1-Y2 link on/off
❄ Destroy

Ç̴̡̙͈͕͈͖͇̈̅́̍͗̌̀͠Ô̴̝̺̠̦̄̈́̌̀͂͟͡ͅM̡̢̖̲̳͇͙͗̿̈́͂͐͞͠M̵͇̻̩̯͍̫̺̰͋̄̀̀̿̈́̈̃͟͜͝Ą͖̘̪̪̼̖͕̺̏̈̊́͋̂́̃͜͞͝Ṉ̡̣̺̺͑̑͑̒͌ͅD̢̧̬͕̪̘̺͖͎̉͗̾́̃͗̑̃̂͡ P̢̹̗̖̲̈́́̍̿̾͗͂̂̕͜R̵̻̬͇̪̥̯͓̘͑̋̎̍͢͝O̧̙̳͕͔͙̰̬̪̒͋͑̈̔͞Ț̵̼̲͉̞̌̉̓̐̀̓E̩̘̩̠̩̱̔̈͆͌̏C̶̡̳̫͓̜̲̏̾́͡͝ͅT̩͉̲̝̩̤̬̙̫̽̓̏͆̈́

❄ Qr on/off
❄ Backup on/off
❄ Protect On/off
❄ Cancel on/off
❄ Name lock on/off

��✒ Creator 👇👇
��✒ http://line.me/ti/p/jlEouH0zr3

��✒ C͍͇̪̲͎̯͎̫̩̽̅̈́̅̌́̍̐ŗ̛͔̳͔̦́̋͛̎e̶̮̳͕͍̺̼̱͎͛̃̾̍̑̐ǻ͕͍̻̭̟̪͒́́̎̕͘̕͟t̢̠̻̗̠͙̦͒̉̈̎͂̐͒͑o̸̡̲̜̯̤͚̠̬͊̓̌̄̒͠r̵̺̲̗̩͙̐̇̾̐͐̏̃̓́̊ B̝̪̭͓͍̺͐͂̑̅̓͗͗̈́͢y͚͔̝͖̮̤͚̅̉̑̐̓̀̋̊͂͜͜͢͞:̶̨̻̪͓̦̻̋̾̂̽̎͘͜͜ Ţ̸̡̫̙͎̰̜͎͚̎̀͗̌̏͛͌͜a̛̛̪̱̳͉͚̹̣̦̼͒͗͆̿͋͡͠m̰̬͇̭̔̓́̓͢͞ĩ̡̢̥̰̤̗̩̥̥̫́̐̔̾̾͂̚͠͝i̴͙̦̹̫̾̈̿̈́̊̃̆͒͜͢͞ 
"""


KAC=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl]
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
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid]
admin = ["u9d498bad444f96197f182055d27a733d",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid]
owner = ["ub736c5b1794f5aa30026d162d07ce5e6",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,Lmid]
staff = ["",cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl]
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me fans",
    "lang":"JP",
    "comment":"Auto LIke by Tamii",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "winvite":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "likeOn":False,
    "cancelbot":False,
    "Backup":False,
    "protectionOn":False
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
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Jmid:
                        X = kj.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj]
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
#------------------------------------------------------------------------------------					
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist = [ki,kk,kc,kd,ke,kf,kg,kh,kj]
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
                    klist = [ki,kk,kc,kd,ke,kf,kg,kh,kj]
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
                    klist = [ki,kk,kc,kd,ke,kf,kg,kh,kj]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)

        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["cancelbot"] == True:  
                    klist = [ki,kk,kc,kd,ke,kf,kg,kh,kj]
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
                       klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.001)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl.leaveGroup(op.param1)
                       kicker.updateGroup(X)
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
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
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
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
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
                if msg.from_ == admin:
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
                    #cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メNzets々•┅─────")
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メNzets々•┅─────")
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
            elif msg.text in ["Key","key"]:
                if msg.toType == 0:
                    cl.sendText(msg.to, helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: "," ")
                klist=[kj,kh,kg,kf,ke,kd,kc,kk,ki,cl]
                kicker = random.choice(klist)
                kicker.kickoutFromGroup(msg.to,[midd])
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: "," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Y1 invite: " in msg.text:
                midd = msg.text.replace("Y1 invite: "," ")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Mey invite: " in msg.text:
                midd = msg.text.replace("Mey invite: "," ")
                random.choice(Bots).findAndAddContactsByMid(midd)
                random.choice(Bots).inviteIntoGroup(msg.to,[midd])
            elif msg.text.lower() == 'mybot':
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

            elif msg.text in ["Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Y1 gift","Y1gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
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

            elif msg.text in ["Cancel"]:
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
            elif msg.text in ["Bot cancel","Ycancel","Botcancel"]:
                if msg.toType == 2:
                    klist=[kj,kh,kg,kf,ke,kd,kc,kk,ki]
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

            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
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

            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
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
            elif msg.text.lower() == 'ginfo':
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
            elif msg.text in ["Glist"]:
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
            elif msg.text in ["Allglist"]:
                gs1 = cl.getGroupIdsJoined()
                gs2 = ki.getGroupIdsJoined()
                gs3 = kk.getGroupIdsJoined()
                gs4 = kc.getGroupIdsJoined()
                gs5 = kd.getGroupIdsJoined()
                gs6 = ke.getGroupIdsJoined()
                gs7 = kf.getGroupIdsJoined()
                gs8 = kg.getGroupIdsJoined()
                gs9 = kh.getGroupIdsJoined()
                gs10 = kj.getGroupIdsJoined()
                L1 = "☫『 Groups List 』☫\n"
                L2 = "☫『 Groups List 』☫\n"
                L3 = "☫『 Groups List 』☫\n"
                L4 = "☫『 Groups List 』☫\n"
                L5 = "☫『 Groups List 』☫\n"
                L6 = "☫『 Groups List 』☫\n"
                L7 = "☫『 Groups List 』☫\n"
                L8 = "☫『 Groups List 』☫\n"
                L9 = "☫『 Groups List 』☫\n"
                L10 = "☫『 Groups List 』☫\n"
                for i in gs1:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                for i in gs2:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                for i in gs3:
                    L += "[⭐] %s \n" % (kk.getGroup(i).name + " | [ " + str(len (kk.getGroup(i).members)) + " ]")
                for i in gs4:
                    L += "[⭐] %s \n" % (kc.getGroup(i).name + " | [ " + str(len (kc.getGroup(i).members)) + " ]")
                for i in gs5:
                    L += "[⭐] %s \n" % (kd.getGroup(i).name + " | [ " + str(len (kd.getGroup(i).members)) + " ]")
                for i in gs6:
                    L += "[⭐] %s \n" % (ke.getGroup(i).name + " | [ " + str(len (ke.getGroup(i).members)) + " ]")
                for i in gs7:
                    L += "[⭐] %s \n" % (kf.getGroup(i).name + " | [ " + str(len (kf.getGroup(i).members)) + " ]")
                for i in gs8:
                    L += "[⭐] %s \n" % (kg.getGroup(i).name + " | [ " + str(len (kg.getGroup(i).members)) + " ]")
                for i in gs9:
                    L += "[⭐] %s \n" % (kh.getGroup(i).name + " | [ " + str(len (kh.getGroup(i).members)) + " ]")
                for i in gs10:
                    L += "[⭐] %s \n" % (kj.getGroup(i).name + " | [ " + str(len (kj.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                kk.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                kc.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                kd.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                ke.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                kf.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                kg.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                kh.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                kj.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif msg.text in ["Creator"]:
	       msg.contentType = 13
               msg.contentMetadata = {'mid': 'u9d498bad444f96197f182055d27a733d'}
               cl.sendMessage(msg)
               cl.sendText(msg.to,"Creator zetsu PSD T&Z TEAM ")
            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)
            elif "All mid" == msg.text:
	       cl.sendText(msg.to,mid)
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
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)			
            elif "Y1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Y2 mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Y3 mid" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif "Sticker" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker1" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker2" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker3" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker4" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker5" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "104",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker6" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker7" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker8" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker9" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Sticker10" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif "Say " in msg.text:
	        bctxt = msg.text.replace("Say ","")
	        ki.sendText(msg.to,(bctxt))
	        kk.sendText(msg.to,(bctxt))
	        kc.sendText(msg.to,(bctxt))
	        kd.sendText(msg.to,(bctxt))
	        ke.sendText(msg.to,(bctxt))
	        kf.sendText(msg.to,(bctxt))
	        kg.sendText(msg.to,(bctxt))
	        kh.sendText(msg.to,(bctxt))
	        kj.sendText(msg.to,(bctxt))
	        kl.sendText(msg.to,(bctxt))
            elif "Y1 say " in msg.text:
	       saytxt = msg.text.replace("Y1 say ","")
	       ki.sendText(msg.to,(saytxt))
            elif "Y2 say " in msg.text:
	       saytext = msg.text.replace("Y2 say ","")
	       kk.sendText(msg.to,(saytext))
            elif msg.text in ["Y say hi"]:
                ki.sendText(msg.to," Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to," Hi buddy 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Family Room 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Jangan nakal oklek 􀨁􀄻double thumbs up􏿿")
            elif "User" in msg.text:
                r1 = ki.getProfile()
                r2 = kk.getProfile()
                ki.sendText(msg.to, "User 121")
                kk.sendText(msg.to, "User 122")
                kc.sendText(msg.to, "User 123")
                kd.sendText(msg.to, "User 124")
                ke.sendText(msg.to, "USer 125")
                kf.sendText(msg.to, "User 126")
                kg.sendText(msg.to, "User 127")
                kh.sendText(msg.to, "User 128")
                kj.sendText(msg.to, "User 129")
                kl.sendText(msg.to, "Kicker 01")
                
#======================================
            elif '.lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.lyric ','')
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
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
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
            elif msg.text in ["Cancel:off","Cancel off"]:
                if wait["cancelbot"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection cancel PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["cancelbot"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection cancel PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Cancel:on","Cancel on"]:
                if wait["cancelbot"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection cancel PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["cancelbot"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection cancel PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
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
            elif "Cn: " in msg.text:
                string = msg.text.replace("Cn: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name " + string + " done")
            elif "Y1 rename: " in msg.text:
                string = msg.text.replace("Y1 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"Name " + string + " done")
            elif "Y2 rename: " in msg.text:
                string = msg.text.replace("Y2 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"Name " + string + " done")
            elif "Y3 rename: " in msg.text:
                string = msg.text.replace("Y3 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kc.getProfile()
                    profile_B.displayName = string
                    kc.updateProfile(profile_B)
                    kc.sendText(msg.to,"Name " + string + " done")
            elif "Y4 rename: " in msg.text:
                string = msg.text.replace("Y4 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kd.getProfile()
                    profile_B.displayName = string
                    kd.updateProfile(profile_B)
                    kd.sendText(msg.to,"Name " + string + " done")
            elif "Y5 rename: " in msg.text:
                string = msg.text.replace("Y5 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ke.getProfile()
                    profile_B.displayName = string
                    ke.updateProfile(profile_B)
                    ke.sendText(msg.to,"Name " + string + " done")
            elif "Y6 rename: " in msg.text:
                string = msg.text.replace("Y6 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kf.getProfile()
                    profile_B.displayName = string
                    kf.updateProfile(profile_B)
                    kf.sendText(msg.to,"Name " + string + " done")
            elif "Y7 rename: " in msg.text:
                string = msg.text.replace("Y7 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kg.getProfile()
                    profile_B.displayName = string
                    kg.updateProfile(profile_B)
                    kg.sendText(msg.to,"Name " + string + " done")
            elif "Y8 rename: " in msg.text:
                string = msg.text.replace("Y8 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kh.getProfile()
                    profile_B.displayName = string
                    kh.updateProfile(profile_B)
                    kh.sendText(msg.to,"Name " + string + " done")
            elif "Y9 rename: " in msg.text:
                string = msg.text.replace("Y9 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kj.getProfile()
                    profile_B.displayName = string
                    kj.updateProfile(profile_B)
                    kj.sendText(msg.to,"Name " + string + " done")
            elif "Y10 rename: " in msg.text:
                string = msg.text.replace("Y10 rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kl.getProfile()
                    profile_B.displayName = string
                    kl.updateProfile(profile_B)
                    kl.sendText(msg.to,"Name " + string + " done")                                
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
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
                    cl.sendText(msg.to,"Display name update to " + string + "")
	    elif "Mybio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"My status update to " + string + "")
	    elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
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
                    cl.sendText(msg.to,"Status update to " + string + "")
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
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["K:off","Contact:off","Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Auto join on","Join on","Join:on","Auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","Auto join off","Auto join:off","Join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
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

            elif msg.text in ["Set"]:
            	print "Setting pick up..."
                md = "[☸]�� SETTING ADMIN ONLY ��[☸]\n"
                
                
                if wait3["copy"] == True: md+="��Mimic : on\n"
                else:md+="��Mimic : off\n"
                if wait["winvite"] == True: md+="��Invite : on\n"
                else:md+="��Invite : off\n"
                if wait["pname"] == True: md+="��Namelock : on\n"
                else:md+="��Namelock : off\n"
                if wait["contact"] == True: md+="��Contact : on\n"
                else: md+="��Contact : off\n"
                if wait["autoJoin"] == True: md+="��Auto join : on\n"
                else: md +="��Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="��Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "��Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="��Auto leave : on\n"
                else: md+="��Auto leave : off\n"
                if wait["timeline"] == True: md+="��Share : on\n"
                else:md+="��Share : off\n"
                if wait["clock"] == True: md+="��Clock Name : on\n"
                else:md+="��Clock Name : off\n"
                if wait["autoAdd"] == True: md+="��Auto add : on\n"
                else:md+="��Auto add : off\n"
                if wait["commentOn"] == True: md+="��Comment : on\n"
                else:md+="��Comment : off\n"
                if wait["Backup"] == True: md+="��Backup : on\n"
                else:md+="��Backup : off\n"
                if wait["qr"] == True: md+="��Protect QR : on\n"
                else:md+="��Protect QR : off\n"
                if wait["protectionOn"] == True: md+="��Protection : on\n\n"+ datetime.today().strftime('%H:%M:%S')
                else:md+="��Protection : off\n\n"+ datetime.today().strftime('%H:%M:%S')
                cl.sendText(msg.to,md)
#========================================
            elif msg.text in ["Backup:on","Backup on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
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
            elif msg.text in ["Y2 rgroups","Y2 rgroup"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kk.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y3 rgroups","Y3 rgroup"]:
                gid = kc.getGroupIdsInvited()
                for i in gid:
                    kc.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kc.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kc.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y4 rgroups","Y4 rgroup"]:
                gid = kd.getGroupIdsInvited()
                for i in gid:
                    kd.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kd.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kd.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y5 rgroups","Y5 rgroup"]:
                gid = ke.getGroupIdsInvited()
                for i in gid:
                    ke.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ke.sendText(msg.to,"Bot All invitations is clean")
                else:
                    ke.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y6 rgroups","Y6 rgroup"]:
                gid = kf.getGroupIdsInvited()
                for i in gid:
                    kf.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kf.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kf.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y7 rgroups","Y7 rgroup"]:
                gid = kg.getGroupIdsInvited()
                for i in gid:
                    kg.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kg.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kg.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y8 rgroups","Y8 rgroup"]:
                gid = kh.getGroupIdsInvited()
                for i in gid:
                    kh.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kh.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kh.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y9 rgroups","Y9 rgroup"]:
                gid = kj.getGroupIdsInvited()
                for i in gid:
                    kj.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kj.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kj.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y10 rgroups","Y10 rgroup"]:
                gid = kl.getGroupIdsInvited()
                for i in gid:
                    kl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kl.sendText(msg.to,"Bot All invitations is clean")
                else:
                    kl.sendText(msg.to,"拒绝了全部的邀请。")                                    
            elif msg.text in ["Add:on","Auto add on","Auto add:on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Add:off","Auto add off","Auto add:off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
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
            elif msg.text.lower() == 'responsebot':
                profile = ki.getProfile()
                text = profile.displayName + "💣"
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + "💣"
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + "💣"
                kc.sendText(msg.to, text)
                profile = kd.getProfile()
                text = profile.displayName + "💣"
                kd.sendText(msg.to, text)
                profile = ke.getProfile()
                text = profile.displayName + "💣"
                ke.sendText(msg.to, text)
                profile = kf.getProfile()
                text = profile.displayName + "💣"
                kf.sendText(msg.to, text)
                profile = kg.getProfile()
                text = profile.displayName + "💣"
                kg.sendText(msg.to, text)
                profile = kh.getProfile()
                text = profile.displayName + "💣"
                kh.sendText(msg.to, text)
                profile = kj.getProfile()
                text = profile.displayName + "💣"
                kj.sendText(msg.to, text)
                profile = kl.getProfile()
                text = profile.displayName + "💣"
                kl.sendText(msg.to, text)
                profile = km.getProfile()
                text = profile.displayName + "💣"
                km.sendText(msg.to, text)
            elif "Ambil qr: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Gourl: ","")
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
                    nowT = datetime.strftime(now2,"[%H:%M]")
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
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"[%H:%M]")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Refresh to update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

#========================================
            elif msg.text == "Lurking":
                    cl.sendText(msg.to, "Set point.")
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
            elif msg.text == "result":
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
            elif "Destroy" in msg.text:
              if msg.from_ in Bots:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Destroy","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"🔸We come to destroy your group🔸")
                    kk.sendText(msg.to,"Relax slow slow no baper...😂😂")
                    kc.sendText(msg.to,"Kenapa diem aja...?")
                    kc.sendText(msg.to,"Tangkis Bego Jangan Gemeter...😂😂")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ki.sendMessage(msg)
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
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print "error"
#========================================
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
            elif msg.text in ["Target list"]:
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
            elif ("Test" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                	   msg.contentType = 9
                           msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                           msg.text = None
                           cl.sendMessage(msg)
                           cl.sendMessage(msg,target)
                       except:
			   cl.sendText(msg.to,"Gift send to member")
            elif "youtube:" in msg.text.lower():
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
            elif "Steal @" in msg.text:
                if msg.from_ in admin:
                   _name = msg.text.replace("Steal @","")
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
                           except Exception as e:
                               cl.sendText(msg.to, str(e))
            elif "Steal cover @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Steal cover @","")
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
                               cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
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
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-------------------------------------------------
            elif "Cbroadcast " in msg.text:
					bctxt = msg.text.replace("Cbroadcast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Gbroadcast " in msg.text:
					bctxt = msg.text.replace("Gbroadcast ", "")
					n = cl.getGroupIdsJoined()
					for manusia in n:
						cl.sendText(manusia,(bctxt))
										 
#========================================
            elif msg.text in ["Masuk","Join","เข้ามา"]:
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
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					print "All_Kickers_Ok!"
					G.preventJoinByTicket(G)
					cl.updateGroup(G)
            elif msg.text in ["Y1 join","Y1 in"]:
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
            elif msg.text in ["Y2 join","Y2 in"]:
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
            elif msg.text in ["Y3 join","Y3 in"]:
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
            elif msg.text in ["Y4 join","Y4 in"]:
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
            elif msg.text in ["Y5 join","Y5 in"]:
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
	    elif msg.text in ["Y6 join","Y6 in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kl.acceptGroupInvitationByTicket(msg.to,Ti)                 
                  G = ke.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kl.updateGroup(G)
                  print "Kicker2_Ok!"
                  Ticket = kl.reissueGroupTicket(msg.to)	  
            elif msg.text in ["Sayang"]:
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
                  kc.updateGroup(G)
                  print "Algojo_Ready!"
                  Ticket = kc.reissueGroupTicket(msg.to)
            elif msg.text.lower() == 'all out':
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
				gid = kl.getGroupIdsJoined()
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
					kl.leaveGroup(i)
				if wait["lang"] == "JP":
					random.choice(KAC).sendText(msg.to,"good bye all")
				else:
					random.choice(KAC).sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Bye all","pulang all"]:
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
                except:
                     pass
            elif msg.text in ["Y1 @bye","Y1 pulang","Y1 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ki.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y2 @bye","Y2 pulang","Y2 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     kk.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Y3 @bye","Y3 pulang","Y3 bye"]:
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
            elif msg.text in ["Y5 @bye","Y5 pulang","Y5 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ke.leaveGroup(msg.to)
                except:
                     pass
            elif "Mk:" in msg.text:
                  if msg.from_ in admin:                                        
                       mk0 = msg.text.replace("Mk:","")
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
                            klist=[ki,kk,kc,kd,ke,cl,kf,kg,kh,kj]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif ("Keluar " in msg.text):
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
							
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
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
#-----------------------------------------------------------
            elif ("Bunuh " in msg.text):
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
                                cl.sendText(msg.to,"Success Boss")
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
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear ban"]:
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
            elif msg.text in ["Ban cek","Cekban"]:
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
            elif msg.text in ["Kill ban"]:
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
                        cl.sendText(msg.to,"Blacklist user")
#-------------------------------------------------
#=============================================
            elif "Kepo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#=============================================
            elif msg.text in ["Sp","speed"]:
                start = time.time()
                cl.sendText(msg.to, "AccessWait...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s s 􏿿" % (elapsed_time))
#============================================
            elif msg.text in ["@tag"]:
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
					
            elif msg.text in ["Mentionall"]:
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
            elif msg.text in ["Y1tag","Y1 tag"]:
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
            elif msg.text in ["Y2tag","Y2 tag"]:
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
                       cb2 += "@\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        kk.sendMessage(msg.to) 
                    except Exception as error:
                        print error
#===========================================
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
#=====
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi","Coba tanya lagi","Mungkin iya","Mungkin tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#======
            elif msg.text in ["Kembali"]:
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
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#----------------------------------------------
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
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
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#===============================================
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
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
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#=======
            elif msg.text in ["tess","debug speed"]:
                cl.sendText(msg.to, "Measuring...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif msg.text in ["zzz","Bot speed"]:
                cl.sendText(msg.to, "Measuring...")
                start = time.time()
                time.sleep(0.00009)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif "Speed respon" in msg.text:
                cl.sendText(msg.to, "Measuring...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"				
            elif "turunin" in msg.text:
                cl.sendText(msg.to, "Sek lurr")
                start = time.time()
                time.sleep(0.02)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"
            elif "ancurin lagi" in msg.text:
                cl.sendText(msg.to, "Sek lurr")
                start = time.time()
                time.sleep(0.1)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))   
                print "[Command]Speed palsu executed"
            elif "turun lagi" in msg.text:
                cl.sendText(msg.to, "Sek lurr")
                start = time.time()
                time.sleep(0.5)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))  
                print "[Command]Speed palsu executed"
            elif ".speed" in msg.text:
                time.sleep(0.5)
                cl.sendText(msg.to, "Sek lurr")
                start = time.time()
                time.sleep(2.32)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))     	
                print "[Command]Speed palsu executed"
            elif msg.text in ["Sp asli","Bot Sp","Bot sp","Bot speed 1"]:
                start = time.time()                   
                cl.sendText(msg.to, "Sek")                    
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed asli executed"
#=====
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#======
            elif msg.text in ["Auto like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
#=====
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
#====
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠN")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ OFF")
#======
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
#===========================================
            elif msg.text in ["List pengurus"]:
	     if msg.from_ in Bots or msg.from_  in admin or msg.from_ in staff:
	      try:
                if staff == []:
			print "nothing"

                try:
                    mb = ""
                    for mi_d in admin:
                        mb += "->" +cl.getContact(mi_d).displayName + "\n"
                    mc = ""
                    for mi_d in staff:
			if mintaprotectgrup == []:
			  mc = "nothing"
			else:
                          mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"-ϔOwner: \n" + mid.displayName + "\n\n-ϔadmin: \n" + mb + "\n\n-ϔstaff: \n" + mc)
		except Exception as a:
			print a
			cl.sendText(msg.to,str(a))
	      except Exception as e:
		print e
		cl.sendText(msg.to,str(e))
            elif "Staff add @" in msg.text:
		if msg.from_ in Bots or msg.from_ in admin or msg.from_ or msg.from_ in staff:
                    print "[Staff]ok"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
		    print _name
		    print _nametarget
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
				staff.append(target)
				cl.sendText(msg.to, "added to list")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unstaff @" in msg.text:
		if msg.from_ in Bots or msg.from_ in admin or msg.from_ or msg.from_ in staff:
                    print "[Unstaff]ok"
                    _name = msg.text.replace("Unstaff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Coy")
                    else:
                        for target in targets:
                            try:
				staff.remove(target)
				cl.sendText(msg.to,"succes unstaff")
                            except:
                                cl.sendText(msg.to,"Gagal")
            elif "Admin add @" in msg.text:
		if msg.from_ in Bots:
                    print "[Admin]ok"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
		    print _name
		    print _nametarget
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
				admin.append(target)
				cl.sendText(msg.to, "added to list")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unadmin @" in msg.text:
		if msg.from_ in Bots:
                    print "[Unadmin]ok"
                    _name = msg.text.replace("Unadmin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Coy")
                    else:
                        for target in targets:
                            try:
				admin.remove(target)
				cl.sendText(msg.to,"succes unadmin")
                            except:
                                cl.sendText(msg.to,"Gagal")    
        if op.type == 55:
            try:
	       if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
			pass
                    else:
			wait2['readMember'][op.param1] += "\n╠" + Name
			wait2['ROM'][op.param1][op.param2] = "╠" + Name
	       else:
		pass
            except:
                pass

        if op.type == 26:
            msg = op.message
            if msg.text is None:
                return
            elif msg.from_ in wait3["target"] and wait3["copy"] == True and wait3["copy2"] == "target":
                try:
                    for i in range(1):
                        cl.sendText(msg.to,msg.text)
                        wait3["copy"] = False
                    wait3["copy"] = True
                except Exception as e:
                    print e				
        
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
def autoSta():
#  count = 1
  while True:
    for zx in range(0,20):
	hasil = cl.activity(limit=20)
	if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
	    try:
		cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
		cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["comment"] )
		print "Like"
		
	    except:
		pass
	else:
	    print "Already liked"
    time.sleep(180)
thread2 = threading.Thread(target=autoSta)
thread2.daemon = True
thread2.start()
#        try:
 #          for posts in cl.activity(1)["result"]["posts"]:
  #              if posts["postInfo"]["liked"] is False:
   #                if wait["likeOn"] == True:
    #                  cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
     #                 if wait["commentOn"] == True:
      #                   if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
       #                       pass
        #                 else:
         #                    cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#        except:
 #           count += 1
  #          if(count == 50):
   #             sys.exit(0)
    #        else:
     #           pass
#thread2 = threading.Thread(target=autoSta)
#thread2.daemon = True
#thread2.start()
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"[%H:%M]")
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
