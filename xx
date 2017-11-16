# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess

cl = LINETCR.LINE()
cl.login(token="EmPn6g2yCBFb7mN0MSWb.DjQ94pUyqtQmL0sAV/1wAW.Tm1nAUMqWbrE/G0fCf35G5XWlvX1Upy70ofsu+bKOn0=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmbMzIZVteIo87FpvRn4.k1WtkBIShaP94cVijXsF1a.Ew/nuI+gxA1ebcphzy2Ljc6qaszwR8q9ANJOEAIWJ20=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EmU2rLHiOERAVFhjPIye.EZIRBGsChIPRt5OApsUtFG.jn1izy3SxMelHdjew0UzhAv+IUbnqRxK4aB+ACHH1zg=")
kk.loginResult()

ks = LINETCR.LINE()
ks.login(token="Em8MIwwL8a1GKT8Ls9Wc.GgoZWtM4MTfhxSPF+iWdda.nqHMFusF3Rav1y8aDzqDH5eT225TnSTm3DxwWFGqg6E=")
ks.loginResult()

kc = LINETCR.LINE()
kc.login(token="EmLHVpU1AvKdavOuCOGd.psJD9o1i3h6Uv4u3LyhPpq.Wb5ESMYFUAmrG+aRy8r7OOGa4JUnlU33VO/AsJcFInY=")
kc.loginResult()

ka = LINETCR.LINE()
ka.login(token="EmpCLC78lJ3f0Tk3VDja.eNeK42Htvw7YX9Yfr4bAIG.98KEtp29XC6haju3wyg0Q5uqW/jHCV+QBA3e0L6vAd0=")
ka.loginResult()

print "ĸeвoтan вro..!!!"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""
╔════════════════╗
║〘ᏢᏌᏴᏞᏆᏟ ᏟᎾᎷᎷᎪNᎠ〙
╠════════════════╣
║                〘ᏆᎠ〙
║              〘ᎷᏆᎠ〙  
║             〘ᎪᏞᏞ ᎷᏆᎠ〙
║                〘ᎷᎬ〙
║             〘ᴊᎾᏆN ᎪᏞᏞ〙
║           〘ᏌᏚᏆᎡ 1/2/3/4〙
║             〘ᏩᎡᎾᏌᏢ ᏆᎠ〙
║              〘ᎢᏞ : "+"〙
║              〘ᏟᏞᎾᏟK :〙
║             〘ᏌᏢ ᏟᏞᎾᏟK〙
║             〘NᎪᎷᎬ : + 〙
║             〘ᎷᏆᏟ〙"ᎷᏆᎠ" 〙
║  〘ᎡᎬᏓᎬᏟᎢ〙"ᏆNᏙᏆᎢᎬ" 〙
║[Massage add: "text"]:
║[Add confirmasi]:
║[Comment set : "Text"]:
║[Comment check]:
║[Clock: on]: "Clock name on"
║[Clock: off]: "Clock name off"
║[Ban]: "Add blacklist"
║[Unban]: "Dalate blacklist"
║[Banlist]: "Check blacklist"
╠════════════╗
║〚C͓̳͓O͓̳͓M͓̳͓M͓̳͓A͓̳͓N͓̳͓D͓̳͓ ͓S͓̳͓E͓̳͓T͓̳͓〛  ║
╠════════════╝
║[Contact: on/off]: 
║[Auto join: on/off]: 
║[Auto join: on/off]: 
║[Cancel Invite: 1 on/off]:
║[Auto share: on/off]:
║[Auto leave: on/off]: 
║[Comment: on/off]: 
║[Auto add: on/off]: 
║[Auto like: on/off]: 
╠══════════════╗	
║⟦ϲ̳̳̋ο̳̳̋м̳̳̋м̳̳̋α̳̳̋и̳̳̋∂̳̳̋ ̳̳̋ι̳̳̋и̳̳̋ ̳̳̋g̳̳̋я̳̳̋ο̳̳̋υ̳̳̋ρ̳̳̋⟧║
╠══════════════╝
║[Ban " @Tag]: 
║[Unban " @Tag]: 
║[Urlon]: "Open urL"
║[Urloff]: "Closed urL"
║[Url]: " Check urL room"
║[Ginfo]: "~÷~ data room"
║[Invite: "mid"]: 
║[Say: "Text"]: "Kicker talk"
║[Cancel]: "Cancel invite"
║[Gn: "name"]:"Change Gname"
║[NK: "Name"]:
║[Dead]: "Kick Blacklist"
╚═════════════════╝
"""
helpMessage2 =""" C̸O̸M̸M̸A̸N̸D̸ P̸R̸O̸T̸E̸C̸T̸
╔═══════════════════╗
║[Protect: on/off]:    ║
║[Block url: on/off]:  ║
║[Namelock: on/off]:   ║
║[Blockinvite: on/off]:║ 
╚═══════════════════╝
"""
KAC = [cl,ki,kk,ks,kc,ka]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
kimid = kk.getProfile().mid
ki2mid = ks.getProfile().mid
Cmid = kc.getProfile().mid
Emid = ka.getProfile().mid
admin = ["u17ce7606c05a31e55cfccb35487cfbf3"]
me = cl.getProfile().mid
bot1 = cl.getProfile().mid
main = cl.getProfile().mid
kicker1 = ki.getProfile().mid
bots = me + kicker1
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []

admins = ["u749abde0fb98413a8c97449abfed566b"]
Rx5 = ["u127124e36853556ef2c7dc8547805a8a"]
Rx4 = ["u3d28ddf4ed48dc7eae5785379581e93d"]
Rx3 = ["u8063b3c139b89ad1475eca5ffc8c030c"]
Rx2 = ["u7b38ab6e049c1e2a6b4f9a1a3d2b937e"]
Rx1 = ["u2b5c1329b8ac1c0a7de02bc827149fd4"]
Administrator = admins + Rx5 + Rx4 + Rx3 + Rx2 + Rx1
AS = Rx2 + Rx1 + Rx3 + Rx4 + Rx5
adminsA = admins + Rx3 + Rx5

omikuzi = ["大吉","中吉","小吉","末吉","大凶","凶"]

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"T̺͆q̺͆ 4 a̺͆d̺͆d̺͆..;\nm̺͆y̺͆ c̺͆r̺͆e̺͆a̺͆t̺͆o̺͆r̺͆..;\nhttp://line.me/ti/p/~aries_jabrik",
    "lang":"JP",
    "comment":"тєαм ¢ιтℓ ∂єѕιgи..α∂∂ oa..;\n👉 https://line.me/R/ti/p/%40inp9841n\n👉https://line.me/R/ti/p/%40gca6303t\nмy creaтor...;\nhttp://line.me/ti/p/~aries_jabrik",
    "likeOn":False,
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{}, 
    "wblacklist":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},    
    "dblacklist":False
}

wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False
    
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
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
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
                    kk.cancelGroupInvitation(op.param1, matched_list)
                    ks.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 17:
            if mid in op.param3:
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
                    cl.sendText(msg.to,"Blacklist user flushing is complete")

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
                                    G = ks.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki.getGroup(op.param1)
				    except:
					try:
                                            G = kc.getGroup(op.param1)
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
                                    ks.updateGroup(G)
                                except:
                                    try:
                                        kc.updateGroup(G)
                                    except:
                                        try:
                                            ka.updateGroup(G)
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
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"G̺͆r̺͆o̺͆u̺͆p̺͆ N̺͆a̺͆m̺͆e̺͆ L̺͆o̺͆c̺͆k̺͆..!!!")
                                        ki.sendText(op.param1,"D̺͆i̺͆k̺͆u̺͆n̺͆c̺͆i̺͆ P̺͆e̺͆'A̺͆")
                                        kk.sendText(op.param1,"W̺͆K̺͆W̺͆K̺͆W̺͆K̺͆W̺͆K̺͆W̺͆ 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL can not be changed")
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass                
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u17ce7606c05a31e55cfccb35487cfbf3":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ks.acceptGroupInvitationByTicket(list_[1],list_[2])							
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = kk.getGroup(list_[1])
                            X = ks.getGroup(list_[1])							
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            kk.updateGroup(X)
                            ks.updateGroup(X)							
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1002)                    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"I̺͆'t̺͆s̺͆ i̺͆n̺͆c̺͆l̺͆u̺͆d̺͆e̺͆d̺͆ i̺͆n̺͆ a̺͆ b̺͆l̺͆a̺͆c̺͆k̺͆l̺͆i̺͆s̺͆t̺͆ a̺͆l̺͆r̺͆e̺͆a̺͆d̺͆y̺͆。")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"N̺͆o̺͆ C̺͆O̺͆M̺͆M̺͆E̺͆N̺͆T̺͆。")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"I̺͆t̺͆ w̺͆a̺͆s̺͆ e̺͆l̺͆i̺͆m̺͆i̺͆n̺͆a̺͆t̺͆e̺͆d̺͆ f̺͆r̺͆o̺͆m̺͆ a̺͆ b̺͆l̺͆a̺͆c̺͆k̺͆l̺͆i̺͆s̺͆t̺͆。")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"I̺͆t̺͆ i̺͆s̺͆n̺͆'t̺͆ i̺͆n̺͆c̺͆l̺͆u̺͆d̺͆e̺͆d̺͆ i̺͆n̺͆ a̺͆ b̺͆l̺͆a̺͆c̺͆k̺͆l̺͆i̺͆s̺͆t̺͆。")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"I̺͆'t̺͆s̺͆ i̺͆n̺͆c̺͆l̺͆u̺͆d̺͆e̺͆d̺͆ i̺͆n̺͆ a̺͆ b̺͆l̺͆a̺͆c̺͆k̺͆l̺͆i̺͆s̺͆t̺͆ a̺͆l̺͆r̺͆e̺͆a̺͆d̺͆y̺͆.。")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"I̺͆t̺͆ w̺͆a̺͆s̺͆ a̺͆d̺͆d̺͆e̺͆d̺͆ t̺͆o̺͆ t̺͆h̺͆e̺͆ b̺͆l̺͆a̺͆c̺͆k̺͆l̺͆i̺͆s̺͆t̺͆.。")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"I̺͆t̺͆ w̺͆a̺͆s̺͆ e̺͆l̺͆i̺͆m̺͆i̺͆n̺͆a̺͆t̺͆e̺͆d̺͆ f̺͆r̺͆o̺͆m̺͆ a̺͆ b̺͆l̺͆a̺͆c̺͆k̺͆l̺͆i̺͆s̺͆t̺͆。")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"I̺͆'t̺͆s̺͆ i̺͆n̺͆c̺͆l̺͆u̺͆d̺͆e̺͆d̺͆ i̺͆n̺͆ a̺͆ b̺͆l̺͆a̺͆c̺͆k̺͆l̺͆i̺͆s̺͆t̺͆ a̺͆l̺͆r̺͆e̺͆a̺͆d̺͆y̺͆。")
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
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["#key","#Key","#KEY"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["#key1","#Key1","#KEY1"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    cl.sendText(msg.to,helpt)
          #  elif msg.text in ["#key","#Key","#KEY"]:
          #      if wait["lang"] == "JP":
          #          cl.sendText(msg.to,helpMessage)
          #      else:
          #          cl.sendText(msg.to,helpt)
          #  elif msg.text in ["#key1","#Key1","#KEY1"]:
          #      if wait["lang"] == "JP":
          #          cl.sendText(msg.to,helpMessage2)
          #      else:
          #          cl.sendText(msg.to,helpt)                   
            elif ("#gn:"in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("#gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"I̺͆t̺͆ c̺͆a̺͆n̺͆'t̺͆ b̺͆e̺͆ u̺͆s̺͆e̺͆d̺͆ b̺͆e̺͆s̺͆i̺͆d̺͆e̺͆s̺͆ t̺͆h̺͆e̺͆ G̺͆R̺͆O̺͆U̺͆P̺͆.")
            elif ("#pdr1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("#pdr1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"I̺͆t̺͆ c̺͆a̺͆n̺͆'t̺͆ b̺͆e̺͆ u̺͆s̺͆e̺͆d̺͆ b̺͆e̺͆s̺͆i̺͆d̺͆e̺͆s̺͆ t̺͆h̺͆e̺͆ G̺͆R̺͆O̺͆U̺͆P̺͆.")
            elif ("#pdr2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("#pdr2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"I̺͆t̺͆ c̺͆a̺͆n̺͆'t̺͆ b̺͆e̺͆ u̺͆s̺͆e̺͆d̺͆ b̺͆e̺͆s̺͆i̺͆d̺͆e̺͆s̺͆ t̺͆h̺͆e̺͆ G̺͆R̺͆O̺͆U̺͆P̺͆.")
            elif "#kick:" in msg.text:
                midd = msg.text.replace("kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "#invite:" in msg.text:
                midd = msg.text.replace("#invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "#me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "#pdr1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "#pdr2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                kk.sendMessage(msg)
            elif "#pdr3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ks.sendMessage(msg)    
            elif msg.text in ["#gift","#GIFT"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["愛のプレゼント","#gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["愛のプレゼント","#gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["愛のプレゼント","#gift4"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ks.sendMessage(msg)
            elif msg.text in ["#cancel","#CANCEL"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ᴛʜᴇʀᴇ ɪsɴ'ᴛ ᴀɴ ɪɴᴠɪᴛᴇᴅ ᴘᴇʀsᴏɴ。")
                        else:
                            cl.sendText(msg.to,"ʏᴏᴜ sᴀᴛᴏ ғᴀᴄᴇ-ʟɪᴋᴇ ᴘᴇʀsᴏɴ ᴀʙsᴇɴᴄᴇ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴜᴘ。")
                    else:
                        cl.sendText(msg.to,"ɪᴍᴘᴏssɪʙʟᴇ ᴜsᴇ ʙᴇsɪᴅᴇs")

            elif msg.text in ["#cv1 cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"ᴛʜᴇʀᴇ ɪsɴ'ᴛ ᴀɴ ɪɴᴠɪᴛᴇᴅ ᴘᴇʀsᴏɴ。")
                        else:
                            ki.sendText(msg.to,"ʏᴏᴜ sᴀᴛᴏ ғᴀᴄᴇ-ʟɪᴋᴇ ᴘᴇʀsᴏɴ ᴀʙsᴇɴᴄᴇ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴜᴘ。")
                    else:
                        cl.sendText(msg.to,"ɪᴍᴘᴏssɪʙʟᴇ ᴜsᴇ ʙᴇsɪᴅᴇs")
                        
            elif "#komen set:" in msg.text:
                c = msg.text.replace("#komen set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"ᴇʀʀᴏʀ")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴄʜᴀɴɢᴇᴅ。\n\n" + c)
            elif msg.text in ["#cek komen"]:
                cl.sendText(msg.to,"ᴀɴ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄᴏᴍᴍᴇɴᴛ ɪs ᴇsᴛᴀʙɪʟɪsʜᴇᴅ ᴀs ғᴏʟʟᴏᴡs ᴀᴛ ᴘʀᴇsᴇɴᴛ。\n\n" + str(wait["comment"]))
            elif msg.text in ["コメント:オン","#komen on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴅᴏɴᴇ。")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ。")
            elif msg.text in ["コメント:オフ","#komen off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴅᴏɴᴇ。")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ。")          
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["#blockurl on"]:
                protecturl.append(msg.to)
                cl.sendText(msg.to,"sɪᴀᴘ..!!")
            elif msg.text in ["#blockurl off"]:
                if msg.from_ in Administrator:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"ᴅɪ ɪᴢɪɴᴋᴀɴ...!!!")
                else:
                    cl.sendText(msg.to,"sᴜᴅᴀʜ")
            elif msg.text in ["#url on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴜʀʟ ᴏᴘᴇɴ。")
                    else:
                        cl.sendText(msg.to,"ᴜʀʟ ʀᴇᴀᴅʏ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴏᴜᴘ。")
                    else:
                        cl.sendText(msg.to,"ɪᴍᴘᴏssɪʙʟᴇ ᴜsᴇ ʙᴇsɪᴅᴇs")
            elif msg.text in ["#url off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴜʀʟ ᴄʟᴏsᴇᴅ。")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴜʀʟ。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴏᴜᴘ。")
                    else:
                        cl.sendText(msg.to,"ɪᴍᴘᴏssɪʙʟᴇ ᴜsᴇ ʙᴇsɪᴅᴇs")
            elif msg.text in ["#ginfo","#GINFO"]:
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
                            u = "refusal"
                        else:
                            u = "許可"
                        cl.sendText(msg.to,"〘ɢʀᴏᴜᴘ〙\n" + str(ginfo.name) + "\n\n〘ɢ.ɪᴅ〙\n" + msg.to + "\n\n〘ɢ.ᴄʀᴇᴀᴛᴏʀ〙\n" + gCreator + "\n\n〘ɢ.ᴘʀᴏғɪʟ〙\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n〘ᴍᴇᴍʙ.〙:" + str(len(ginfo.members)) + "ᴇᴋᴏʀ\nᴘᴇɴᴅɪɴɢ:" + sinvitee + "ᴇᴋᴏʀ\nɪɴᴠɪᴛ ᴜʀʟ:" + u + "ɪᴛs ᴛʜᴇ ɪɴsɪᴅᴇ.")
                    else:
                        cl.sendText(msg.to,"[名字]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[小组的作成者]\n" + gCreator + "\n[小组图标]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ。")
                    else:
                        cl.sendText(msg.to,"ɪᴍᴘᴏssɪʙʟᴇ ᴜsᴇ ʙᴇsɪᴅᴇs")
            elif "#id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "#mid" == msg. text:
                cl.sendText(msg.to,mid)
            elif "#all mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,kimid)
                ks.sendText(msg.to,ki2mid)      
            elif "Wkwk" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "Sue" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "Welcome" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ks.sendMessage(msg)
            elif "#TL:" in msg.text:
                tl_text = msg.text.replace("#TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "#name:" in msg.text:
                string = msg.text.replace("#name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
            elif "#last name" in msg.text:
                string = msg.text.replace("#last name","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
#---------------------------------------------------------
            elif "#pdr1 upname:" in msg.text:
                string = msg.text.replace("#pdr1 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "#pdr2 upname:" in msg.text:
                string = msg.text.replace("#pdr2 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "#pdr3 upname:" in msg.text:
                string = msg.text.replace("#pdr3 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "#pdr1 upstatus: " in msg.text:
                string = msg.text.replace("#pdr1 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"display message " + string + " done")
            elif "#pdr2 upstatus: " in msg.text:
                string = msg.text.replace("#pdr2 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = kk.getProfile()
                    profile_C.statusMessage = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"display message " + string + " done")
            elif "#pdr3 upstatus: " in msg.text:
                string = msg.text.replace("#pdr3 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_C = ks.getProfile()
                    profile_C.statusMessage = string
                    ks.updateProfile(profile_C)
                    ks.sendText(msg.to,"display message " + string + " done")
            elif "#mic:" in msg.text:
                mmid = msg.text.replace("#mic:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["#contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴏɴ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ。")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏɴ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏɴ。")
            elif msg.text in ["#contact off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴏғғ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ。")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏғғ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏғғ。")
            elif msg.text in ["#auto join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴊᴏɪɴ ᴏɴ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ。")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏɴ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏɴ。")
            elif msg.text in ["#auto join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴊᴏɪɴ ᴏғғ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ。")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏғғ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏғғ。")
            elif "#cancel invite:" in msg.text:
                try:
                    strnum = msg.text.replace("#cancel invite:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refusal was turned off。\non, please designate and send the number of people.")
                        else:
                            cl.sendText(msg.to,"number of people")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "A group below the person made sure that I'll refuse invitation automatically。")
                        else:
                            cl.sendText(msg.to,strnum + "Self- you for below shinin-like small.")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"The price is wrong。")
                    else:
                        cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["#auto leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʟᴇᴀᴠᴇ ᴏɴ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ。")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏɴ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏɴ。")
            elif msg.text in ["#auto leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʟᴇᴀᴠᴇ ᴏғғ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ。")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏғғ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏғғ。")
            elif msg.text in ["共有:オン","共有：オン","#auto share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ。")
            elif msg.text in ["共有:オフ","共有：オフ","#auto share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ")
                    else:
                        cl.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ。")                        
            elif "#set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="〘ᴄᴏɴᴛᴀᴄᴛ〙📸\n"       
                else: md+="〘ᴄᴏɴᴛᴀᴄᴛ〙 \n"      
                if wait["autoJoin"] == True: md+="〘ᴀᴜᴛᴏ ᴊᴏɪɴ〙📸\n" 
                else: md +="〘ᴀᴜᴛᴏ ᴊᴏɪɴ〙\n"
                if wait["autoCancel"]["on"] == True:md+="〘ᴄᴀɴᴄᴇʟ ɪɴᴠɪᴛᴇ〙📸" + str(wait["autoCancel"]["members"]) + " \n"     
                else: md+= "〘ᴄᴀɴᴄᴇʟ ɪɴᴠɪᴛᴇ〙\n"  
                if wait["leaveRoom"] == True: md+="〘ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ〙📸\n"   
                else: md+="〘ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ〙\n"
                if wait["timeline"] == True: md+="〘ᴀᴜᴛᴏ sʜᴀʀᴇ〙📸\n"  
                else:md+="〘ᴀᴜᴛᴏ sʜᴀʀᴇ〙\n" 
                if wait["commentOn"] == True: md+="〘ᴄᴏᴍᴍᴇɴᴛ〙📸\n"   
                else:md+="〘ᴄᴏᴍᴍᴇɴᴛ〙\n"    
                if wait["autoAdd"] == True: md+="〘ᴀᴜᴛᴏ ᴀᴅᴅ〙📸\n"  
                else:md+="〘ᴀᴜᴛᴏ ᴀᴅᴅ〙\n"   
                if wait["likeOn"] == True: md+="〘ᴀᴜᴛᴏ ʟɪᴋᴇ〙📸\n"
                else:md+="〘ᴀᴜᴛᴏ ʟɪᴋᴇ〙\n" 
                if wait["pnharfbot"] == True: md+="〘ᴘʀᴏᴛᴇᴄᴛ〙📸\n"   
                else:md+="〘ᴘʀᴏᴛᴇᴄᴛ〙\n"    
                if wait["pname"] == True: md+="〘ɴᴀᴍᴇʟᴏᴄᴋ〙📸\n"  
                else:md+="〘ɴᴀᴍᴇʟᴏᴄᴋ〙\n"   
                if wait["poni"] == True: md+="〘ʙʟᴏᴄᴋɪɴᴠɪᴛᴇ〙📸\n"
                else:md+="〘ʙʟᴏᴄᴋɪɴᴠɪᴛᴇ〙\n"                   
                cl.sendText(msg.to,md)
            elif msg.text in ["#G id","#g id"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)
            elif msg.text in ["#reject"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ᴄᴏᴍᴘʟᴇᴛɪᴏɴs。")
                else:
                    cl.sendText(msg.to,"ᴋᴇʏ ɪs ᴡʀᴏɴɢ。")
            elif msg.text in ["#like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴅᴏɴᴇ。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ。")
            elif msg.text in ["いいね:オフ","#like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴅᴏɴᴇ。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ。")

            elif msg.text in ["#auto add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ's ᴏɴ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴏɴ ᴀʟʀᴇᴀᴅʏ。")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏɴ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏɴ。")
            elif msg.text in ["#auto add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ's ᴏғғ ᴀʟʀᴇᴀᴅʏ。")
                    else:
                        cl.sendText(msg.to,"ᴏғғ ᴀʟʀᴇᴀᴅʏ。")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴡᴀs ᴛᴜʀɴᴇᴅ ᴏғғ。")
                    else:
                        cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏғғ。")
            elif "#message add:" in msg.text:
                wait["message"] = msg.text.replace("#message add:","")
                cl.sendText(msg.to,"ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴡᴀs ᴄʜᴀɴɢᴇᴅ。")
            elif "#auto addition→" in msg.text:
                wait["message"] = msg.text.replace("#auto addition→","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴡᴀs ᴄʜᴀɴɢᴇᴅ。")
                else:
                    cl.sendText(msg.to,"was change already。")
            elif msg.text in ["#add confirmasi","自動追加問候語確認"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,".automatic message is established as follows。\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"One  of weeds on the surface below the self- additional breath image。\n\n" + wait["message"])
            elif msg.text in ["#change","言語變更"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"ᴄᴏᴜɴᴛʀʏ ʟᴀɴɢᴜᴀɢᴇ ᴅᴜʀɪɴɢ ᴀ ᴄʜᴀɴɢᴇ。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,". ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ ᴡᴀs ᴍᴀᴅᴇ ᴇɴɢʟɪsʜ。")
            elif msg.text in ["#url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴏᴜᴘ。")
                    else:
                        cl.sendText(msg.to,"ɪᴍᴘᴏssɪʙʟᴇ ᴜsᴇ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴏᴜᴘ。")
            elif "#gurl:" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl:","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴏᴜᴘ。")
            elif msg.text in ["#cv1 gurl"]:
                if msg.toType == 2:
                    x = ki.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ᴏᴜᴛsɪᴅᴇ ᴛʜᴀɴ ɢʀᴏᴜᴘ。")
                    else:
                        cl.sendText(msg.to,"ɴᴏᴛ ғᴏᴛ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
            elif msg.text in ["#cb"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["#cbd"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send the phone number of the person who adds it to the blacklist.")
            elif msg.text in ["#cbc"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"There isn't a person made a blacklist。")
                else:
                    cl.sendText(msg.to,"Below is a blacklist。")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["#clock on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"It's on already。")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was turned on")
            elif msg.text in ["#clock off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"It's off already.。")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"It was tuned off。")
            elif "#clock:" in msg.text:
                n = msg.text.replace("Clock:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"Last name clock。")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"It was renewed\n\n" + n)
            elif msg.text in ["#up clock"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was renewed。")
                else:
                    cl.sendText(msg.to,"Please turn on a name clock.。")
            elif "#tyank-tyank" in msg.text:
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
            elif "#pdr on" in msg.text:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  ka.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
            elif msg.text in ["#pdr1 join"]:
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

            elif msg.text in ["#pdr2 join"]:
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
				  
            elif msg.text in ["#pdr3 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = ks.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(msg.to)                           

            elif msg.text in ["#pdr off"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                cl.sendText(msg.to,"ʙᴜʙᴀʀ...\nᴀᴅᴀ ʀᴀᴢɪᴀ..!!")
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
					ks.leaveGroup(msg.to)
					kc.leaveGroup(msg.to)
					ka.leaveGroup(msg.to)
                except:
                     pass            
            elif "#nk:" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("#nk:","")
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                KAC = [ki,kk,ks,kc,ka]
                                kicker = random.choice(KAC)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"ᴇʀʀᴏʀ")
#-----------------------------------------------------------                          
            elif "#cipox" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass
            elif "pdr1 fuck" in msg.text:
				OWN = "u406133ad4d3fbe50a2f4d51ea081d050"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("pdr1 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ki.kickoutFromGroup(msg.to, [target])							   
							except:
									ki.kickoutFromGroup(msg.to, [target])							   
									pass
            elif "pdr2 fuck" in msg.text:
				OWN = "ua51ba06b0dd18c0bfe2cc6caa3458202"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("pdr2 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									kk.kickoutFromGroup(msg.to, [target])							   
							except:
									kk.kickoutFromGroup(msg.to, [target])							   
									pass

            elif "pdr3 fuck" in msg.text:
				OWN = "u34a9af3a18784280147fc413a68a77fd"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("pdr3 fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = ki.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"ᴜsᴇʀ ᴅᴏs ɴᴏᴛ ᴇxɪsᴛ")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									ks.kickoutFromGroup(msg.to, [target])							   
							except:
									ks.kickoutFromGroup(msg.to, [target])							   
									pass									
            elif "#bann " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:                                        
                       ban0 = msg.text.replace("#bann ","")
                       ban1 = ban0.lstrip()
                       ban2 = ban1.replace("@","")
                       ban3 = ban2.rstrip()
                       _name = ban3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ")
                           pass
                       else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"͡° ͜ʖ ͡° sᴜᴋsᴇs")
                                except:
                                    cl.sendText(msg.to,"͡° ͜ʖ ͡° sᴜᴋsᴇs")
            elif ("UBL " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Un Banned")
                   except:
                      pass        
                                   
           #-----------------------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            elif "#lupyu:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("#lupyu:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"ʟᴏᴠᴇ ʏᴏᴜ ᴏɴ")
            			else:
            				cl.sendText(msg.to,"ʟᴏᴠᴇ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"ʟᴏᴠᴇ ʏᴏᴜ ᴏғғ")
            			else:
            				cl.sendText(msg.to,"ʟᴏᴠᴇ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴏғғ")
                	elif "add:" in cmd:
            			target0 = msg.text.replace("#lupyu:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						cl.sendMessageWithMention(msg.to,target)
            						#break
            					except:
            						cl.sendText(msg.to,"Failed")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("#lupyu:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "#listTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<List Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)

                                #---------------------Fungsi spam start--------------------------
            elif "#spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "#spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "#spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])

#-------------------Fungsi spam finish----------------------------
                          
#-----------------------------------------------
            elif "#spam " in msg.text:
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
#------------------------------------------------
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"()Update Names👉 " + string + "👈")
            
                                
#-----------------------------------------------------------
            elif "#mid @" in msg.text:
                _name = msg.text.replace("#mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
                      
#-----------------------------------------------------------
     #       elif "midb:" in msg.text:
     #           midd = msg.text.replace("midb:","")
     #           wait["blacklist"][midd] = True
                                           
#-----------------------------------------------------------

     # ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("#bl " in msg.text):
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
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass        
            elif "#ubl " in msg.text:
               if msg.toType == 2:
                  if msg.from_ in admin:                                        
                       unb0 = msg.text.replace("Unban ","")
                       unb1 = unb0.lstrip()
                       unb2 = unb1.replace("@","")
                       unb3 = unb2.rstrip()
                       x_name = unb3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if x_name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"͡° ͜ʖ ͡° sᴜᴋsᴇs")
                                except:
                                    cl.sendText(msg.to,"͡° ͜ʖ ͡° sᴜᴋsᴇs")
#-----------------------------------------------------------
            elif "#protect on" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏɴ")
            elif "#protect off" == msg.text:
				try:
					if msg.from_ in Administrator:
						protection.remove(msg.to)
						cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏғғ")
					else:
						cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ")
				except:
					pass
            elif "#namelock on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ᴛᴜʀɴᴇᴅ ᴏɴ.")
                else:
                    cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "#namelock off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ᴛᴜʀɴ ᴏғғ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ")
					
            elif "#blockinvite on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ")
            elif "#blockinvite off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏғғ")
				except:
					pass                                 
#-----------------------------------------------------------
            elif "#END" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "#spam @" in msg.text:
                _name = msg.text.replace("#spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"ᴏᴛᴡ sᴘᴀᴍ ᴛᴀʀɢᴇᴛ 😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       kk.sendText(g.mid,"Spam  😂")  
                       ks.sendText(g.mid,"Spam  😂")
                       kc.sendText(g.mid,"Spam  😂")
                       ka.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")
                       kk.sendText(g.mid,"Spam  😂")
                       ks.sendText(g.mid,"Spam  😂")
                       kc.sendText(g.mid,"Spam  😂")  
                       ka.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")
                       kk.sendText(g.mid,"Spam  😂")
                       ks.sendText(g.mid,"Spam  😂")
                       kc.sendText(g.mid,"Spam  😂")
                       ka.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       kk.sendText(g.mid,"Spam  😂")  
                       ks.sendText(g.mid,"Spam  😂")
                       kc.sendText(g.mid,"Spam  😂")
                       ka.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")
                       kk.sendText(g.mid,"Spam  😂")
                       ks.sendText(g.mid,"Spam  😂")
                       kc.sendText(g.mid,"Spam  😂")  
                       ka.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")
                       kk.sendText(g.mid,"Spam  😂")
                       ks.sendText(g.mid,"Spam  😂")
                       kc.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ka.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ks.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(msg.to, "ƊƠƝЄ ƧƤƛM  😂")
                       print "Done spam" 
#-----------------------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"ᴘᴏɴɢ 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"ᴘᴏɴɢ 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ks.sendText(msg.to,"ᴘᴏɴɢ 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#----------------------------------------------------------
            elif msg.text in ["#respon","respon","#responsename"]:
                cl.sendText(msg.to,"ʙᴏᴛ ʟɪɴᴇ ᴘᴅʀ ɴɪʜ👇👇")
                ki.sendText(msg.to,"ᴘᴀsᴜᴋᴀɴ")
                kk.sendText(msg.to,"ᴅᴀᴅᴀ")
                ks.sendText(msg.to,"ʀᴀᴛᴀ")	
                kc.sendText(msg.to,"sᴇᴘᴇʀᴛɪ")
                ka.sendText(msg.to,"ᴋɪᴛᴀ...!!!(｡♥‿♥｡)")
#----------------------------------------------------------
            elif msg.text == "#cek":
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
            elif msg.text == "#cctv":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═════════════%s\n╠══════════════\n%s╠═════════════\n║Readig point creation:\n║ [%s]\n╚══════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "ᴋᴇᴛɪᴋ #ᴄᴇᴋ ᴅᴜʟᴜ...,ʙᴀʀᴜ #ᴄᴄᴛᴠ...!!!\nᴛᴀᴍᴘᴏʟ ᴏɢᴇʙ ʟᴏᴇ...!!!")
#-----------------------------------------------------------speed
            elif msg.text in ["#ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ʀᴇɢɪsᴛᴇʀᴇᴅ ᴡɪᴛʜ ᴀ ʙᴀɴɴᴇᴅ。")
            elif msg.text in ["#unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ʀᴇɢɪsᴛᴇʀᴇᴅ ᴡɪᴛʜ ᴀ ᴜɴʙᴀɴɴᴇᴅ。")
            elif msg.text in ["#banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ᴛʜᴇʀᴇ ɪsɴ'ᴛ ᴀ ᴘᴇʀsᴏɴ ᴍᴀᴅᴇ ᴀ ʙᴀɴɴʟɪsᴛ。")
                else:
                    cl.sendText(msg.to,"ʙᴇʟᴏᴡ ɪs ʙᴀɴɴʟɪsᴛ。")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["#blist"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "But it's a blacklist.。")
            elif msg.text in ["#cipox ban"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"There wasn't a blacklist user。")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,ks,kc,ka]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass							
            elif msg.text in ["#single"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I have feigned and have canceled it。")
            elif "#random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("#random:","")
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
                        cl.sendText(msg.to,"ᴇʀʀᴏʀ")
            elif "#album making" in msg.text:
                try:
                    albumtags = msg.text.replace("Album making","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "An album was made。")
                except:
                    cl.sendText(msg.to,"ᴇʀʀᴏʀ")
            elif "fakec→" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakec→","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass                
#-----------------------------------------------
            elif "#say " in msg.text:
                string = msg.text.replace("#say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
                    ks.sendText(msg.to," " + string + " ")
                    kc.sendText(msg.to," " + string + " ")
                    ka.sendText(msg.to," " + string + " ")
#-----------------------------------------------
            elif "#test" in msg.text:
                ks.sendText(msg.to,"ok")
#-----------------------------------------------
            elif "#speed" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "ᴠᴘs ɢʀᴀᴛɪsᴀɴ...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
#-----------------------------------------------             
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False

                elif op.param3 in op.param3:
                    if op.param1 in protection:
                        OWN = "u2144f4eca089e5888899ad5d0551c085","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","u34a9af3a18784280147fc413a68a77fd"
                    if op.param2 in OWN:
                        kicker1 = [cl,ki,kk,ks,kc,ka,km,kn,ko]
                        G = random.choice(kicker1).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)
                    else:
                        G = random.choice(kicker1).getGroup(op.param1)

                        random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)


                elif op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        
                elif op.param3 in Amid:
                    if op.param2 in kimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in ki2mid:
                    if op.param2 in kimid:
                        if op.param4 in Cmid:
                            if op.param5 in Emid:
                                G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        
                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)


                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in ki2mid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
             
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
                    
        if op.param1 in autocancel:
			OWN = "ua7fc5964d31f45ac75128fc2b8deb842","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","uc7f32bb28dc009916d40af87c9910ddc"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				cl.cancelGroupInvitation(op.param1,InviterX)
				ki.cancelGroupInvitation(op.param1,InviterX)
				kk.cancelGroupInvitation(op.param1,InviterX)
				ks.cancelGroupInvitation(op.param1,InviterX)
				kc.cancelGroupInvitation(op.param1,InviterX)
				ka.cancelGroupInvitation(op.param1,InviterX)
				cl.kickoutFromGroup(op.param1,[op.param2])
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ka.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = "ua7fc5964d31f45ac75128fc2b8deb842","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","uc7f32bb28dc009916d40af87c9910ddc"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ka.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠☑" + Name
                        wait2['ROM'][op.param1][op.param2] = "╠☑" + Name
                else:
                    cl.sendText
            except:
                  pass
                  
#-----------------------------------------------------------
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
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
#----------------------------------------

#-------------------------------
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
