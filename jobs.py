import smtplib, json, os
from urllib2 import build_opener
from bs4 import BeautifulSoup as bs
from datetime import datetime


from SMTPConnection import *

opener = build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
with open("/Users/phrayezzen/Documents/Projects/Website-Listener-Framework/webs.json") as data:
	webs = json.load(data)
smtp = SMTPConnection()
smtp.login(webs["username"], webs["password"], webs["smtpServer"])
timestamp = datetime.now()

for site in webs["sites"]:
	for job_id in webs["sites"][site]:
		job = webs["sites"][site][job_id]
		target = bs(opener.open(job["URL"]).read())

		is_present = True
		for tag in job["path"]:
			try:
				target = target.find(tag["name"], id=tag["id"], class_=tag["class"]) if "class" in tag else \
					target.find(tag["name"], id=tag["id"])
			except:
				is_present = False
				break
		if not is_present:
			continue

		if job["target"] in target.get_text():
			message = "You have a new website update! The listener sends you a message:\n\n" + \
				"Description: " + job["description"] + \
				"\n" + job["target"] + " was found on the website.\n" + job["message"] + \
				"\n\nHope that helps! Thanks for using this website listener! Contact alexliu7@yahoo.com for problems." + \
				"\nSent at " + str(datetime.now())
			smtp.send_message(webs["username"], job["recipients"], message)

smtp.logout()