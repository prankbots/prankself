# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re
#🔸Me
cl = LINETCR.LINE()
cl.login(token="Em3hlsvvyhF3TM1ew4gd.kPCC2cheTsBk4ifKqk7WRq.aMoCL/4VM6VwLDomE+VUgWBjq3l/LH5Z3CnyrvCSpjo=")
cl.loginResult()
#🔸Ram
ki = LINETCR.LINE()
#ki.login(token="Em6MITqfeIg8cOFaYUxa.faf8coH1ZHEEFhQt+Oz6wG.LyQvyBh9UfW7Caf0eViUQmjyvgQKRsRpscdITDwVnxU=")
ki.login(token="Em6LJVPFvzakBJ83Y0hb.eYEa7xHBtex0js+NkxbMMW.MvHdHuiDYApzCCNZujf71btRQY13isgZKIS+UYfmVX4=")
ki.loginResult()
#🔸Rem
kk = LINETCR.LINE()
kk.login(token="Eml40CYx7jcwTSZGLFUb.qcURbB0UMDI4dQBAOcnMUW.ddgUovzYYHPN6oqGrdKPOKYkZCLEfrz99MtVfBJuUQ4=")
kk.loginResult()
#🔸Emilia
kc = LINETCR.LINE()
kc.login(token="EmbVYzagls78AvX4i4y7.oQ3qV4oMI0TEZAtwnLvkXW.wrHSKb31Aypk6uzuFax3zlWPQsddX60VzibzMQFDXRQ=")
kc.loginResult()
#🔸Raphi
ks = LINETCR.LINE()
ks.login(token="Emj2LZ7gcfQ0KvibAi1c.PbGVtJjdxHS3kIJJN01VBa.MRnCfC8OLz1P8LdU2vjbw5pxgQdgKzQ0umZXgeDsZIQ=")
ks.loginResult()
#🔸Gabriel
ka = LINETCR.LINE()
ka.login(token="EmPNbye64wsbI7WnFUs7.57LdoM1EOU0JLa4AUA56zW.LLN74QiS5T/SNDnc+zjma6y7aM/VJ2i0uNbUOjLY/s8=")
ka.loginResult()
#🔸Vigne
kb = LINETCR.LINE()
kb.login(token="EmFL33Q423JKLcbDBo52.3MsxcnpmiZzgxx/TSK+HeG.kXlyXmJ0jSvUhaJefsiOAJwhgJP54mOfItisWoe3jEw=")
kb.loginResult()
#🔸Satania
ko = LINETCR.LINE()
ko.login(token="EmieKUQD2hIiUYqHVxma.xwINC1s/Umx4wOsHkqVHsG.9vldkW2PaVrZx6ej1glb058XVgQvRBlI8dFfy4KTXS4=")
#ko.login(token="EmxOBSPpmJtYvWox11P4.CHow4h2s16rfeE+exRmTXa.pTDVJqOkhjc7hkdiI8jxlh8aN5C7hlLLwxKimO/hWZA=")
ko.loginResult()
#🔸Sagiri
ke = LINETCR.LINE()
ke.login(token="EmLnJgCbROb2iNVYlW1a.faf8coH1ZHEEFhQt+Oz6wG.cSjW+wiwbPU0nQ61J6PNwDKawvLJeI0kTZK1XkbXcgw=")
ke.loginResult()
#🔸Ange
ku = LINETCR.LINE()
ku.login(token="Em4VEyzbP9ookYldveV3.XbawOba/1IEMt9uJ/RP7mW.cQTaHviMqmFdCBW1Mbxc+YIK4mWavc8pejyeszPQD5s=")
ku.loginResult()
#🔸Mirai
kv = LINETCR.LINE()
kv.login(token="EmndHVanPB9GFgMJrzha.lt8pcTTQRbVkJgydiWCigG.VOeb5UXjsBl6/BGugfAt6VIQrF92DCjw+FyeTffNolU=")
kv.loginResult()
#🔸Sakura
kw = LINETCR.LINE()
kw.login(token="EmV0OwqkJcJXFp014Aj4.bewvvZj84AEMBtt17nh7ja.83skiIcTD7foqYkqV5alTSuAJnj9zq5aEZ/EDuqsQXA=")
kw.loginResult()

print "👋Welcome to emilia bot👍"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 
              🔸🔸🔸Emilia bot🔸🔸🔸
🔯 Mid
🔯 My mid
🔯 All mid
🔯 Mid @
🔯 Check:<mid>
🔯 Me
🔯 Contact off/on
🔯 Join off/on
🔯 Gcancel:<number>
🔯 Gcancel:on/off
🔯 Say <teks>
🔯 <name bot> say <teks>
🔯 Leave︎ on/off
🔯 Share on/off
🔯 Like on/off
🔯 Comment on/off
🔯 Add on/off
🔯 Add comment:<teks>
🔯 Message
🔯 Message change:<Teks>
🔯 Message check
🔯 Up
🔯 Bom (@)
🔯 Gift
🔯 Spam gift
🔯 Open
🔯 <name bot> Open
🔯 Close
🔯 <name bot> Close
🔯 Url
🔯 Invite <mid>
🔯 <name bot> Invite <mid>
🔯 Kick <mid>
🔯 <name bot> Kick <mid>
🔯 Ginfo
🔯 Cancel
🔯 <name bot> Cancel
🔯 Gn <group name>
🔯 <name bot> Gn <group name>
🔯 Create group <0-100> <name group>
🔯 Emilia group
🔯 Invite group:<name group>
🔯 Spam invit <10-100> <mid>
🔯 Copy <@mention>
🔯 Backup
🔯 Woi/Tagall/Mention
         🔸🔸🔸🔸🔸🔯🔸🔸🔸🔸🔸
🔯 Kicker - [kicker join group]
🔯 Kicker<1-11>
🔯 Leave - [kicker leave group]
🔯 Leave<1-11>
🔯 Leave all group - [bot leave all group]
🔯 Nk - [Ehm...]
🔯 Nk <nama> - [Ehm...]
🔯 Hallo/Hushus <@> - [Ehmm...]
🔯 Ban <@> - [blacklist member]
🔯 Ban<send kontak>
🔯 Kill/Kill ban - [ehm.. user blacklist]
🔯 Unban <@> - [whitelist user]
🔯 Unban<Send kontak>
🔯 Ban list - [cek user blacklist]
🔯 Destroy - [kalo ini ehm...]
"""

Setgroup ="""
🔯 Protect Group - Protect on/off
🔯 Protect Qr - Qr on/off
🔯 Block invite - Cancel on/off
🔯 Protect cancel - Cancl on/off
🔯 Notifed - Notifed on/off
🔯 Timeline - Share on/off
🔯 Auto join - Join on/off
🔯 Contact - Contact on/off
🔯 Auto like - Like on/off
🔯 Auto comment - Comment on/off
"""
KAC=[ki,kk,kc,ks,ka]
KIK=[kb,ko,ke,ku,kv,kw]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = ko.getProfile().mid
Hmid = ke.getProfile().mid
Imid = ku.getProfile().mid
Jmid = kv.getProfile().mid
Kmid = kw.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Kmid]
admin=["u2a971cd821c4b526cae0816440aef0ad"]
Admin=["u2a971cd821c4b526cae0816440aef0ad"]
Creator=["u2a971cd821c4b526cae0816440aef0ad"]

contact = cl.getProfile()
profile = cl.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":10},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True ,
    'message':"よろしく\nThanks For Add Me..:v",
    "lang":"JP",
    "comment":"こんにちは\nAutolike By Emilia\nhttp://line.me/ti/p/YQ2uhrdbZ2",
    "comment2":"こんにちは:v",
    "Autolike":True,
    "likeOn":True,
    "commentOn":True,
    "comment2":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "cName9":"🔸Sagiriシールド",
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectGroup":True,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True,
    "Notifed":False,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

          
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

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                ki.findAndAddContactsByMid(op.param1)
                kk.findAndAddContactsByMid(op.param1)
                kc.findAndAddContactsByMid(op.param1)
                ks.findAndAddContactsByMid(op.param1)
                ka.findAndAddContactsByMid(op.param1)
                kb.findAndAddContactsByMid(op.param1)
                ko.findAndAddContactsByMid(op.param1)
                ke.findAndAddContactsByMid(op.param1)
                ku.findAndAddContactsByMid(op.param1)
                kv.findAndAddContactsByMid(op.param1)
                kw.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    ki.sendText(op.param1,str(wait["message"]))
                    kk.sendText(op.param1,str(wait["message"]))
                    kc.sendText(op.param1,str(wait["message"]))
                    ks.sendText(op.param1,str(wait["message"]))
                    ka.sendText(op.param1,str(wait["message"]))
                    kb.sendText(op.param1,str(wait["message"]))
                    ko.sendText(op.param1,str(wait["message"]))
                    ke.sendText(op.param1,str(wait["message"]))
                    ku.sendText(op.param1,str(wait["message"]))
                    kv.sendText(op.param1,str(wait["message"]))
                    kw.sendText(op.param1,str(wait["message"]))

        #--------FUNGSI PROTECT QR KICK -------#
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(KAC).updateGroup(G)
        #-------------Fungsi Block invite-----------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  group = cl.getGroup(op.param1)
                  gMembMids = [contact.mid for contact in group.invitee]
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Invite User Kick Finish------#

        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
            
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)

            if op.param3 in Dmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    
            if op.param3 in Fmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)

            if op.param3 in Gmid:
                if op.param2 in Emid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                   
            if op.param3 in Hmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ku.updateGroup(X)
                    Ti = ku.reissueGroupTicket(op.param1)
                   
            if op.param3 in Jmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kv.updateGroup(X)
                    Ti = kv.reissueGroupTicket(op.param1)
                    
            if op.param3 in Kmid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kw.updateGroup(X)
                    Ti = kw.reissueGroupTicket(op.param1)
            
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
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
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = ki.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ko.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
        # ----------------- NOTIFED LEAVE GROUP---#
        if op.type == 15:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                kc.sendText(op.param1,cl.getContact(op.param2).displayName + "\nJangan pergi meninggalkanku\n(´･ω･`)")
                print "MEMBER OUT GROUP"
        
        # ----------------- NOTIFED JOIN GROUP---#
        if op.type == 17:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                   return
                kc.sendText(op.param1,cl.getContact(op.param2),displayName + "\nWelcome\n↖(^ω^)↗")
                print "MEMBER HAS JOIN THE GROUP"
        #-----------------NOTIFED KICKOUT GROUP--------#
        if op.type == 19:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                kc.sendText(op.param1,cl.getContact(op.param2).displayName + "\nWahhh....Kikill!!!\n😱😱😱")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

       #------------PROTECT GROUP KICKER----------#
        if op.type == 19:
            if wait["ProtectGroup"] == True:
                if op.param2 not in Admin and Bots:
                  G = cl.getGroup(op.param1)
                  random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                  print error

        if op.type == 19:
           if op.param3 in admin:
              random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
              ki.inviteIntoGroup(op.param1,admin)
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
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
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True      
              
                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ku.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ku.updateGroup(G)
                    Ticket = ku.reissueGroupTicket(op.param1)
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
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kv.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kv.updateGroup(G)
                    Ticket = kv.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True                    

                if Kmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    kv.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kw.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kw.updateGroup(G)
                    Ticket = kw.reissueGroupTicket(op.param1)
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
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = ki.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
            if Bmid in op.param3:
                G = kk.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
            if Cmid in op.param3:
                G = kc.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message

        #------FUNGSI PROTECT CANCEL------#
        if op.type == 32:
            if wait["Protectcancel"] == True:
            	if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    random.choice(KIK).kickoutFromGroup(op.param1,[op.param2])
        #-----Cancel User Kick Finish------#

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
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
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
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Set"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
                    #--------------FUNGSI CHANGE GROUP NAME----------#
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Ram gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Ram gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Rem gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Rem gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Emilia gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Emilia gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
                    #------------FUNGSI KICK BY (MID]----------#
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Ram kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Ram kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Rem kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Rem kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Emilia kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Emilia kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Raphi kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Raphi kick ","")
                ks.kickoutFromGroup(msg.to,[midd])
            elif "Gabriel kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Gabriel kick ","")
                ka.kickoutFromGroup(msg.to,[midd])
            elif "Vigne kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Vigne kick ","")
                kb.kickoutFromGroup(msg.to,[midd])
            elif "Satania kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Satania kick ","")
                ko.kickoutFromGroup(msg.to,[midd])
            elif "Sagiri kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Sagiri kick ","")
                ke.kickoutFromGroup(msg.to,[midd])
            elif "Ange kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Ange kick ","")
                ku.kickoutFromGroup(msg.to,[midd])
            elif "Mirai kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Mirai kick ","")
                kv.kickoutFromGroup(msg.to,[midd])
            elif "Sakura kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Sakura kick ","")
                kw.kickoutFromGroup(msg.to,[midd])
                #-----------FUNGSI INVITE BY MID-------#
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Ram invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Ram invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Rem invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Rem invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Emilia invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Emilia invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif "Raphi invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Raphi invite ","")
                ks.findAndAddContactsByMid(midd)
                ks.inviteIntoGroup(msg.to,[midd])
            elif "Gabriel invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Gabriel invite ","")
                ka.findAndAddContactsByMid(midd)
                ka.inviteIntoGroup(msg.to,[midd])
            elif "Vigne invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Vigne invite ","")
                kb.findAndAddContactsByMid(midd)
                kb.inviteIntoGroup(msg.to,[midd])
            elif "Satania invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Satania invite ","")
                ko.findAndAddContactsByMid(midd)
                ko.inviteIntoGroup(msg.to,[midd])
            elif "Sagiri invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Sagiri invite ","")
                ke.findAndAddContactsByMid(midd)
                ke.inviteIntoGroup(msg.to,[midd])
            elif "Mirai invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Mirai invite ","")
                kv.findAndAddContactsByMid(midd)
                kv.inviteIntoGroup(msg.to,[midd])
            elif "Sakura invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Sakura invite ","")
                kw.findAndAddContactsByMid(midd)
                kw.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["Mybot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

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
                msg.contentMetadata = {'mid': Imid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Kmid}
                cl.sendMessage(msg)
            
            elif msg.text in ["gift","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'f44b6a1a-bdfa-47f7-a839-e7938eb71aac',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["ram gift","Ram gift","."]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'fa4056c4-d746-4d4f-8d69-6c1923635cc3',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '14'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["rem gift","Rem gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["Emilia gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '517174f2-1545-43b9-a28f-5777154045a6',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '11'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["Spam gift","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
                ks.sendMessage(msg)
                kb.sendMessage(msg)
                ko.sendMessage(msg)
                ke.sendMessage(msg)
                ku.sendMessage(msg)
                kv.sendMessage(msg)
                kw.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
                ks.sendMessage(msg)
                kb.sendMessage(msg)
                ko.sendMessage(msg)
                ke.sendMessage(msg)
                ku.sendMessage(msg)
                kv.sendMessage(msg)
                kw.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                ka.sendMessage(msg)
                ks.sendMessage(msg)
                kb.sendMessage(msg)
                ko.sendMessage(msg)
                ke.sendMessage(msg)
                ku.sendMessage(msg)
                kv.sendMessage(msg)
                kw.sendMessage(msg)
            elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		for i in gid:
		    cl.sendText(i,"(→→→☆BROADCAST☆←←←\n\n"+bc+"\n\nんんんんn")
		cl.sendText(msg.to,"Yosh \n Done。")
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Ram cancel","K1 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Rem cancel","K2 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        kk.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kk.sendText(msg.to,"No one is inviting")
                        else:
                            kk.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Emilia cancel","K3 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = kc.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kc.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kc.sendText(msg.to,"No one is inviting")
                        else:
                            kc.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Raphi cancel","K4 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ks.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ks.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ks.sendText(msg.to,"No one is inviting")
                        else:
                            ks.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ks.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Gabriel cancel","K5 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ka.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ka.sendText(msg.to,"No one is inviting")
                        else:
                            ka.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Vigne cancel","K6 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kb.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        kb.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kb.sendText(msg.to,"No one is inviting")
                        else:
                            kb.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kb.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kb.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Satania cancel","K7 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ko.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ko.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ko.sendText(msg.to,"No one is inviting")
                        else:
                            ko.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ko.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ko.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sagiri cancel","K8 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ke.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ke.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ke.sendText(msg.to,"No one is inviting")
                        else:
                            ke.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ke.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ke.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Ange cancel","K9 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ku.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ku.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ku.sendText(msg.to,"No one is inviting")
                        else:
                            ku.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ku.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ku.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Mirai cancel","K10 cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kv.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        kv.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kv.sendText(msg.to,"No one is inviting")
                        else:
                            kv.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kv.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kv.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Open","open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Ram open","K1 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Rem open","K2 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Emilia open","K3 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Raphi open","K4 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ks.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Done")
                    else:
                        ks.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ks.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Gabriel open","K5 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ks.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done")
                    else:
                        ka.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Vigne open","K6 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kb.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    if wait["lang"] == "JP":
                        kb.sendText(msg.to,"Done")
                    else:
                        kb.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        kb.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kb.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Satania open","K7 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ko.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    if wait["lang"] == "JP":
                        ko.sendText(msg.to,"Done")
                    else:
                        ko.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        ko.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ko.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sagiri open","K8 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ke.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    if wait["lang"] == "JP":
                        ke.sendText(msg.to,"Done")
                    else:
                        ke.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        ke.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ke.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Ange open","K9 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ku.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ku.updateGroup(X)
                    if wait["lang"] == "JP":
                        ku.sendText(msg.to,"Done")
                    else:
                        ku.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        ku.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ku.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Mirai open","K10 open"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kv.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kv.updateGroup(X)
                    if wait["lang"] == "JP":
                        kv.sendText(msg.to,"Done")
                    else:
                        kv.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        kv.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kv.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close","close url"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                    else:
                        cl.sendText(msg.to,"Already Close。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Ram close","K1 close"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Rem close","K2 link off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Emilia close","K3 link off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Raphi close","K4 close"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ks.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Done。")
                    else:
                        ks.sendText(msg.to,"Already Close。")
                else:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ks.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Gabriel close","K5 close"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done。")
                    else:
                        ka.sendText(msg.to,"Already Close。")
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Vigne close","K6 close"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kb.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    if wait["lang"] == "JP":
                        kb.sendText(msg.to,"Done。")
                    else:
                        kb.sendText(msg.to,"Already Close。")
                else:
                    if wait["lang"] == "JP":
                        kb.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kb.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
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
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
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
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
                 #---------------Show contact Group Creator------#
            elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {"mid":gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"👆Group Creator👆")
                 #------------Show contact dari mid-----------#
            elif "Check:" in msg.text:
                midd = msg.text.replace("Check:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":midd}
                cl.sendMessage(msg)
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "My mid" == msg.text:
                cl.sendText(msg.to, msg.from_)
            elif "Id Group" == msg.text:
                kk.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
                ko.sendText(msg.to,Gmid)
                ke.sendText(msg.to,Hmid)
                kv.sendText(msg.to,Jmid)
                kw.sendText(msg.to,Kmid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Ram mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Rem mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Emilia mid" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif "Raphi mid" == msg.text:
                ks.sendText(msg.to,Dmid)
            elif "Gabriel mid" == msg.text:
                ka.sendText(msg.to,Emid)
            elif "Vigne mid" == msg.text:
                kb.sendText(msg.to,Fmid)
            elif "Satania mid" == msg.text:
            	ko.sendText(msg.to,Gmid)
            elif "Sagiri mid" == msg.text:
            	ke.sendText(msg.to,Hmid)
            elif "Ange mid" == msg.text:
            	ku.sendText(msg.to,Imid)
            elif "Mirai mid" == msg.text:
            	ku.sendText(msg.to,Jmid)
            elif "Sakura mid" == msg.text:
            	kw.sendText(msg.to,Kmid)
            
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Ram rename "]:
                string = msg.text.replace("Ram rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Rem rename "]:
                string = msg.text.replace("Rem rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cancel on","Guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block invite on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block invite off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block invite off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect on","Kick on"]:
              if msg.from_ in admin:
                if wait["ProtectGroup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already on。")
                else:
                    wait["ProtectGroup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already on。")
            elif msg.text in ["Protect off","Kick off"]:
              if msg.from_ in admin:
                if wait["ProtectGroup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already off。")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already off。")
            elif msg.text in ["Protect cancel on","Cancl on"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Jangan cancel pend tar kecyduck")
                    else:
                        cl.sendText(msg.to,"Already on。")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Jangan cancel pend tar kecyduck")
                    else:
                        cl.sendText(msg.to,"Already on。")
            elif msg.text in ["Protect cancel off","Cancl off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already off。")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already off。")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Qr on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Qr on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nOff。")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nOff。")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
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
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
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
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Leave on","Auto leave:on"]:
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
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Auto leave off","Leave off"]:
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
            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off。")
                    else:
                        cl.sendText(msg.to,"はい\nDone。")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Notifed on","notifed off"]:
              if msg.from_ in admin:
                if wait["Notifed"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already On。")
                else:
                    wait["Notifed"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                    else:
                        cl.sendText(msg.to,"Already On。")
            elif msg.text in ["Notifed off","notifed off"]:
              if msg.from_ in admin:
                if wait["Notifed"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off。")
                    else:
                        cl.sendText(msg.to,"はい\nDone。")
                else:
                    wait["Notifed"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off。")
                    else:
                        cl.sendText(msg.to,"はい\nDone。")
            elif msg.text in ["Llike on","Cl like on"]:
                if wait["Autolike"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                else:
                    wait["Autolike"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on。")
            elif msg.text in ["Llike off","Cl like off"]:
                if wait["Autolike"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                else:
                    wait["Autolike"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off。")
            elif msg.text in ["Like on","Auto like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on。")
            elif msg.text in ["Auto like off","Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"はい\nDone。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off。")
            elif msg.text in ["Sett"]:
                md = ""
                if wait["ProtectGroup"] == True: md+="🔯 ProtectGroup : on\n"
                else: md+="🔯 ProtectGroup : off\n"
                if wait["ProtectQR"] == True: md+="🔯 Protect QR : on\n"
                else: md+="🔯 Protect QR : off\n"
                if wait["Protectcancel"] == True: md+="🔯 Protect cancel : on\n"
                else: md+="🔯 Protect cancel : off\n"
                if wait["Protectguest"] == True: md+="🔯 Block Invite : on\n"
                else: md+="🔯 Block Invite : off\n"
                if wait["Notifed"] == True: md+="🔯 Notifed    : on\n"
                else: md+="🔯 Notifed    : off\n"
                if wait["contact"] == True: md+="🔯 Contact    : on\n"
                else: md+="🔯 Contact    : off\n"
                if wait["autoJoin"] == True: md+="🔯 Auto join : on\n"
                else: md +="🔯 Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="🔯 Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "🔯 Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="🔯 Auto leave    : on\n"
                else: md+="🔯 Auto leave : off\n"
                if wait["timeline"] == True: md+="🔯 Share   : on\n"
                else:md+="🔯 Share   : off\n"
                if wait["autoAdd"] == True: md+="?? Auto add : on\n"
                else:md+="🔯 Auto add : off\n"
                if wait["likeOn"] == True: md+="🔯 Auto like : on \n"
                else:md+="🔯 Auto like : off \n" 
                if wait["Autolike"] == True: md+="🔯 Llike : on \n"
                else:md+="🔯 Llike : off \n" 
                if wait["commentOn"] == True: md+="🔯 Comment : on\n"
                else:md+="🔯 Comment : off\n"
                if wait["comment2"] == True: md+="🔯 Auto Comment : on\n"
                else:md+="🔯 Auto Comment : off\n"
                cl.sendText(msg.to,md)
         
            elif msg.text in ["My groups","Emilia gc","Group"]:
                if msg.from_ in admin:
                 gid = cl.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "▶。 %s  \n" % (cl.getGroup(i).name + " | : " + str(len (cl.getGroup(i).members)))
                 cl.sendText(msg.to, "◀My Groups▶\n"+ h +"▶Jumlah : " +str(len(gid)))
            elif msg.text in ["Ram groups"]:
                if msg.from_ in admin:
                 gid = ki.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "▶。 %s  \n" % (ki.getGroup(i).name + " | : " + str(len (ki.getGroup(i).members)))
                 ki.sendText(msg.to, "◀My Groups▶\n"+ h +"▶Jumlah : " +str(len(gid)))
            elif msg.text in ["Gid","Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            
            elif msg.text in ["Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
              if msg.from_ in admin:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Add message:" in msg.text:
                wait["message"] = msg.text.replace("Add message:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Add comment:" in msg.text:
              if msg.from_ in admin:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Comment on"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment off"]:
              if msg.from_ in admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))     
            elif msg.text in ["Url"]:
              if msg.from_ in admin:
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
            elif msg.text in ["Ram close","Cv1 close"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Rem close","Cv2 close"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Emilia close","Cv3 close"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
              if msg.from_ in admin:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Done jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#           
         
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#
         #----------------FUNGSI CEK SIDER-------------------#
            elif msg.text in ["Setlastpoint","Cek"]:
                cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
	            pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text in ["Viewlastseen","Sider"]:
		  if msg.to in wait2['readPoint']:
	            if wait2["ROM"][msg.to].items() == []:
	              chiya = ""
	            else:
	              chiya = ""
	              for rom in wait2["ROM"][msg.to].items():
	                print rom
	                chiya += rom[1] + "\n"

	            cl.sendText(msg.to, " %s\n\n◀◀◀◀⚫▶▶▶▶\n\n%s\n\nThese uesrs have seen at the lastseen\npoint(｀・ω・´)\n%s"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
	          else:
	            cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Kicker","Come here"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kv.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = ki.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "🔸Kicker Complete"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["Kicker1"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Kicker2"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Kicker3"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kc.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Kicker4"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ks.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(msg.to)
     
            elif msg.text in ["Kicker5"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ka.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ka.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ka.updateGroup(G)
                  Ticket = ka.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Kicker6"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kb.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kb.updateGroup(G)
                  Ticket = kb.reissueGroupTicket(msg.to)
                 
            elif msg.text in ["Kicker7"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ko.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ko.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ko.updateGroup(G)
                  Ticket = ko.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Kicker8"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ke.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(msg.to)
           
            elif msg.text in ["Kicker9"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ku.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ku.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ku.updateGroup(G)
                  Ticket = ku.reissueGroupTicket(msg.to)      
 
            elif msg.text in ["Kicker10"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kv.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kv.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kv.updateGroup(G)
                  Ticket = kv.reissueGroupTicket(msg.to)
 
            elif msg.text in ["Kicker11"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kw.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kw.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kw.updateGroup(G)
                  Ticket = kw.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Leave","Cabut"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	ki.sendText(msg.to, "Sayonara(*^﹏^*) " + str(ginfo.name))
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        kv.leaveGroup(msg.to)
                        kw.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave1"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave2"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave3"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave4"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ks.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave5"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ka.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave6"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kb.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave7"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ko.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave8"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave9"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ku.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave10"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kv.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leave11"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kw.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Byebye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            elif "Leave all group" == msg.text:
		gid = ki.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			ki.sendText(i,"Goodbye👋😭")
		  #      cl.leaveGroup(i)
			#ki.leaveGroup(i)
			kk.leaveGroup(i)
			kc.leaveGroup(i)
		    cl.sendText(msg.to,"Done leave all group")
		else:
		    cl.sendText(msg.to,"Khusus Creator")
    #-------------Fungsi Copy Kontak (@)---------------#
#--------------------------------------------------------
	    elif "Backup" in msg.text:
		try:
		    cl.updateDisplayPicture(profile.pictureStatus)
		    cl.updateProfile(profile)
		    cl.sendText(msg.to, "Profile telah di backup seperti semula")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
#--------------------------------------------------------
	    elif "Copy " in msg.text:
                copy0 = msg.text.replace("Copy ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
		group = cl.getGroup(msg.to)
		for contact in group.members:
		    cname = cl.getContact(contact.mid).displayName
		    if cname == _name:
			cl.CloneContactProfile(contact.mid)
			cl.sendText(msg.to, "Hey tebak aku siapa hayo􀜁􀅔Har Har􏿿。 ")
		    else:
			pass
		
#--------------------------------------------------------
    #-------------Fungsi Kick (@)tag---------------#
            elif ("Hallo " in msg.text):
               if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           klist=[kk,kc,ks,ka,kb,ko,ke,ku,kv]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                           print (msg.to,[g.mid])
                       except:
                           pass              
            elif ("Hushus " in msg.text):
               if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           klist=[cl]
                           kicker=random.choice(klist)
                           kicker.kickoutFromGroup(msg.to,[target])
                           print (msg.to,[g.mid])
                       except:
                           pass

    #-------------Fungsi Tagall User -------------#
            elif msg.text in ["Hai"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    cb = ""
                    cb3 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in nama:
                        akh = akh + int(5)
                        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                        strt = strt + int(6)
                        akh = akh + 1
                        cb3 += "@nlia\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb3
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error

            elif msg.text in ["Woi","Tagall","Mention"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in nama:
                        akh = akh + int(5)
                        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                        strt = strt + int(6)
                        akh = akh + 1
                        cb2 += "@nlia\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        ki.sendMessage(msg)
                    except Exception as error:
                        print error


         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,ks,kb,ko]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                
            elif ("Destroy" in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Destroy","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    ki.sendText(msg.to,"🔸We come to destroy your group🔸")
                    kb.sendText(msg.to,"Relax slow slow no baper...😂😂")
                    kc.sendText(msg.to,"Kenapa diem aja?")
                    ks.sendText(msg.to,"Tangkis Bego Jangan Gemeter...😘")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Error􀜁􀅔Har Har􏿿")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,kc,ks,ka,kb,ko,ku]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Hm..")
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"Target tdk ada")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc,ka,kb,ko,ke,kv]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    pass
        #----------------Fungsi Kick User Target Finish----------------------#      
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Target tdk ditemukan")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Done sukses blacklist")
                            except:
                                ki.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Target tdk ada")
                        ki.sendText(msg.to,"Target tdk ada")
                        kk.sendText(msg.to,"Target tdk ada")
                        kc.sendText(msg.to,"Target tdk ada")
                        ks.sendText(msg.to,"Target tdk ada")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Gc apa ini","Grup apaan ini","Ini apa?"]:
                ki.sendText(msg.to,"Ya group chat lah")
                kk.sendText(msg.to,"􀜁􀄃Hooh Ini Grup Chat")
                kc.sendText(msg.to,"Iya klo dh tau Grup chat Ga usah banyak tanya:v")
        #-------------Fungsi Spam Finish---------------------#
#---------------------------------------------
        #----------------- FUNGSI BROADCAST-----------#
            elif msg.text in ["haha","Haha","Haa..."]:
                ki.sendText(msg.to," 􀜁􀅔Har Har􏿿。􏿿")
                kk.sendText(msg.to," 􀜁􀅔􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"􀜁􀅔􀜁􀅔Har Har􏿿")
                ks.sendText(msg.to," 􀜁􀅔􀜁􀅔Har Har􏿿")
                ka.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                kb.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                ko.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                ku.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                kv.sendText(msg.to,"􀜁􀅔Har Har􏿿")
                kw.sendText(msg.to,"􀜁􀅔Har Har􏿿")
            elif "Ram say " in msg.text:
                bctxt = msg.text.replace("Ram say ","")
                ki.sendText(msg.to,(bctxt))
            elif "Rem say " in msg.text:
                bctxt = msg.text.replace("Rem say ","")
                kk.sendText(msg.to,(bctxt))
            elif "Emilia say " in msg.text:
                bctxt = msg.text.replace("Emilia say ","")
                kc.sendText(msg.to,(bctxt))
            elif "Raphi say " in msg.text:
                bctxt = msg.text.replace("Raphi say ","")
                ks.sendText(msg.to,(bctxt))
            elif "Gabriel say " in msg.text:
                bctxt = msg.text.replace("Gabriel say ","")
                ka.sendText(msg.to,(bctxt))
            elif "Vigne say " in msg.text:
                bctxt = msg.text.replace("Vigne say ","")
                kb.sendText(msg.to,(bctxt))
            elif "Satania say " in msg.text:
                bctxt = msg.text.replace("Satania say ","")
                ko.sendText(msg.to,(bctxt))
            elif "Sagiri say " in msg.text:
                bctxt = msg.text.replace("Sagiri say ","")
                ke.sendText(msg.to,(bctxt))
            elif "Ange say " in msg.text:
                bctxt = msg.text.replace("Ange say ","")
                ku.sendText(msg.to,(bctxt))
            elif "Mirai say " in msg.text:
                bctxt = msg.text.replace("Mirai say ","")
                kv.sendText(msg.to,(bctxt))
            elif "Sakura say " in msg.text:
                bctxt = msg.text.replace("Sakura say ","")
                kw.sendText(msg.to,(bctxt))
            elif "Say " in msg.text:
		bctxt = msg.text.replace("Say ","")
		ki.sendText(msg.to,(bctxt))
		kk.sendText(msg.to,(bctxt))
		kc.sendText(msg.to,(bctxt))
                ks.sendText(msg.to,(bctxt))
                ka.sendText(msg.to,(bctxt))
                ko.sendText(msg.to,(bctxt))
                kb.sendText(msg.to,(bctxt))
                ke.sendText(msg.to,(bctxt))
                ku.sendText(msg.to,(bctxt))
                kv.sendText(msg.to,(bctxt))
                kw.sendText(msg.to,(bctxt))
            elif msg.text in ["Respon","respon","Absen","absen"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Absen woi buru² ah lama")
                ki.sendText(msg.to,"Ram􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Rem􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Emilia􀜁􀅔Har Har􏿿")
                ks.sendText(msg.to,"Raphi􀜁􀅔Har Har􏿿")
                ka.sendText(msg.to,"Gabriel􀜁􀅔Har Har􏿿")
                kb.sendText(msg.to,"Vigne􀜁􀅔Har Har􏿿")
                ko.sendText(msg.to,"Satania􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to,"Sagiri􀜁􀅔Har Har􏿿")
                ku.sendText(msg.to,"Ange􀜁􀅔Har Har􏿿")
                kv.sendText(msg.to,"Mirai􀜁􀅔Har Har􏿿")
                kw.sendText(msg.to,"Sakura􀜁􀅔Har Har􏿿")
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ks.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ka.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kb.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ko.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ku.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ku.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kv.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kw.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
      #----------------- FUNGSI SPAM---------------------#
            elif "Bom @" in msg.text:
                _name = msg.text.replace("Bom @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Otw..wkwk")
                       ki.sendText(g.mid,"Duarr  􀜁􀅔Har Har􏿿")  
                       kk.sendText(g.mid,"DorrDorr  􀜁􀅔Har Har􏿿")  
                       kc.sendText(g.mid,"Darrr..  􀜁􀅔Har Har􏿿")
                       ks.sendText(g.mid,"Derrr  􀜁􀅔Har Har􏿿")
                       ka.sendText(g.mid,"Dorr  􀜁􀅔Har Har􏿿")
                       kb.sendText(g.mid,"Duarrrrrr  􀜁􀅔Har Har􏿿")
                       ko.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       ke.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       ku.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       kv.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       kw.sendText(g.mid,"Duarr  􀜁􀅔Har Har􏿿")  
                       ki.sendText(g.mid,"Awas ledakan  􀜁􀅔Har Har􏿿")
                       kk.sendText(g.mid,"Dorrrrrrrrrrrr  􀜁􀅔Har Har􏿿")
                       kc.sendText(g.mid,"Duarrrrr  􀜁􀅔Har Har􏿿")  
                       ks.sendText(g.mid,"Spam  􀜁􀅔Har Har􏿿")
                       ka.sendText(g.mid,"Awas ledakan  􀜁􀅔Har Har􏿿")
                       kb.sendText(g.mid,"Dorrrr  􀜁􀅔Har Har􏿿")
                       ko.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       ke.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       ku.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       kv.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       kw.sendText(g.mid,"Duarr  􀜁􀅔Har Har􏿿")  
                       ki.sendText(g.mid,"Deerrrrr!!  􀜁􀅔Har Har􏿿")
                       kk.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       kc.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ks.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ka.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       kb.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ko.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ke.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ku.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       kv.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       kw.sendText(g.mid,"Duarr  􀜁􀅔Har Har􏿿")  
                       cl.sendText(msg.to, "Done  􀜁􀅔Har Har􏿿")
                       print "Done spam" 
            elif "Anu @" in msg.text:
                _name = msg.text.replace("Anu @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Anu...")
                       ki.sendText(g.mid,"Duarr  􀜁􀅔Har Har􏿿")  
                       kk.sendText(g.mid,"DorrDorr  􀜁􀅔Har Har􏿿")  
                       kc.sendText(g.mid,"Darrr..  􀜁􀅔Har Har􏿿")
                       ks.sendText(g.mid,"Derrr  􀜁􀅔Har Har􏿿")
                       ka.sendText(g.mid,"Dorr  􀜁􀅔Har Har􏿿")
                       kb.sendText(g.mid,"Duarrrrrr  􀜁􀅔Har Har􏿿")
                       ko.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       ke.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       ku.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       kv.sendText(g.mid,"Boomm..!!  􀜁􀅔Har Har􏿿")
                       ki.sendText(g.mid,"Awas ledakan  􀜁􀅔Har Har􏿿")
                       kk.sendText(g.mid,"Dorrrrrrrrrrrr  􀜁􀅔Har Har􏿿")
                       kc.sendText(g.mid,"Duarrrrr  􀜁􀅔Har Har􏿿")  
                       ks.sendText(g.mid,"Spam  􀜁􀅔Har Har􏿿")
                       ka.sendText(g.mid,"Awas ledakan  􀜁􀅔Har Har􏿿")
                       kb.sendText(g.mid,"Dorrrr  􀜁􀅔Har Har􏿿")
                       ko.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       ke.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       ku.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       kv.sendText(g.mid,"Daarrrrr!!  􀜁􀅔Har Har??")
                       ki.sendText(g.mid,"Deerrrrr!!  􀜁􀅔Har Har􏿿")
                       kk.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       kc.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ks.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ka.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       kb.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ko.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ke.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       ku.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       kv.sendText(g.mid,"Doorrrrr!  􀜁􀅔Har Har􏿿")
                       cl.sendText(msg.to, "Cabut......  􀜁􀅔Har Har􏿿")
                       print "Done spam" 
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Emilia waifuku <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Ga bisa bego Kelewatan batas...! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Ehm...kelewatan batas bro...!")
       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["speed","Speed"]:
              if msg.from_ in admin:      	
                start = time.time()
                cl.sendText(msg.to, "Speed ku pelan hanya segini")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tdk ada akun ter blacklist")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        ks.kickoutFromGroup(msg.to,[jj])
                        ka.kickoutFromGroup(msg.to,[jj])
                        kb.kickoutFromGroup(msg.to,[jj])
                        ko.kickoutFromGroup(msg.to,[jj])
                        ke.kickoutFromGroup(msg.to,[jj])
                        ku.kickoutFromGroup(msg.to,[jj])
                        kv.kickoutFromGroup(msg.to,[jj])
                        kw.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Wkwk")
                    ki.sendText(msg.to,"User blacklist")
                    kk.sendText(msg.to,"Udah diusir")
                    kc.sendText(msg.to,"dari grup")

            elif msg.text in ["B","b","mangat"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"Asw sinyal gw lag bat")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
 
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n􀜁􀅔Har Har􏿿。" + Name
                        wait2['ROM'][op.param1][op.param2] = "􀜁􀅔Har Har􏿿。" + Name
                else:
                    cl.sendText
            except:
                  pass
                  
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
                if wait["Autolike"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["comment2"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()

def autoSta():
    count = 1
    while True:
        try:
           for posts in ki.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in kk.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in kc.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                           kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in ks.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   ks.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ks.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in ka.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   ka.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ka.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in kb.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   kb.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          kb.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in ko.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   ko.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ko.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in ke.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   ke.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ke.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in ku.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   ku.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ku.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in kv.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   kv.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          kv.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def autoSta():
    count = 1
    while True:
        try:
           for posts in kw.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   kw.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          kw.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"]) 
        except:
            count += 1
            if(count == 100):
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
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName5"]
                ks.updateProfile(profile5)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName6"]
                ka.updateProfile(profile6)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName7"]
                kb.updateProfile(profile7)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName10"]
                ku.updateProfile(profile10)
                
                profile4 = kk.getProfile()
                profile4.displayName = wait["cName11"]
                kv.updateProfile(profile11)
                
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"] + nowT
                kc.updateProfile(profile4)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
