import smtplib, json
from urllib2 import build_opener
from bs4 import BeautifulSoup as bs
from datetime import datetime

from SMTPConnection import *

opener = build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
with open('webs.json') as data:
	webs = json.load(data)
smtp = SMTPConnection()
smtp.login(webs["username"], webs["password"], webs["smtpServer"])

for site in webs["sites"]:
	for job_id in webs["sites"][site]:
		job = webs["sites"][site][job_id]
		target = bs(opener.open(job["URL"]).read())
		for tag in job["path"]:
			target = target.find(tag["name"], id=tag["id"], class_=tag["class"]) if "class" in tag else \
				target.find(tag["name"], id=tag["id"])
		if job["target"] in target.get_text():
			message = "You have a new website update! The listener sends you a message:\n\n" + \
				"Description: " + job["description"] + "\n" + job["message"] + \
				"\n\nHope that helps! Thanks for using this website listener! Contact alexliu7@yahoo.com for problems." + \
				"\nSent at " + str(datetime.now())
			smtp.send_message(webs["username"], job["recipients"], message)

smtp.logout()