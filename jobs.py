import json
from urllib2 import build_opener
from bs4 import BeautifulSoup as bs
from datetime import datetime
from SMTPConnection import *



opener = build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
with open('/Users/phrayezzen/MASTER/Projects/Website-Listener-Framework/webs.json') as data:
    webs = json.load(data)
smtp = SMTPConnection()
smtp.login(webs['username'], webs['password'], webs['smtpServer'])

for site in webs['sites']:
    for job in webs['sites'][site]:
        desc = job['description']
        print 'Polling for ' + desc
        target = bs(opener.open(job['URL']).read())

        is_present = True
        for tag in job['path']:
            try:
                target = target.find(tag['name'], id=tag['id'], class_=tag['class']) if 'class' in tag else \
                    target.find(tag['name'], id=tag['id'])
            except Exception as e:
                print e
                is_present = False
                break
        if not is_present:
            continue

        if job['target'] in target.get_text():
            message = 'You have a new website update! The listener sends you a message:\n\n' + \
                'Description: ' + desc + \
                '\n' + job['target'] + ' was found on the website.\n' + job['message'] + \
                '\n\n' + job['URL'] + \
                '\n\nHope that helps! Thanks for using this website listener! Contact xaliu7@gmail.com for problems.' + \
                '\nSent at ' + str(datetime.now())
            print 'Sending message now for ' + desc
            smtp.send_message(webs['username'], job['recipients'], message)

smtp.logout()
