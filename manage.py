"""
setup
create json file
ask for user/pass/serv
create crontab
"""
import json
import os


class ListenerUpdater(object):
    def __init__(self):
        self.webs = {}
        with open(os.path.join("/Users/phrayezzen/Documents/Projects/Website-Listener-Framework", 'webs.json')) as data:
            self.webs = json.load(data)
            self.num_sites = self.webs["numSites"]

    def setup(self):
        self.webs["username"] = raw_input("Enter Username:\n")
        self.webs["password"] = raw_input("Enter Password:\n")
        self.webs["smtpServer"] = raw_input("Enter mail server URL:\n")

    def add(self):
        URL = raw_input("Paste the URL on which you want to listen to:\n")
        root = self.get_root(URL)  # TODO get root
        if root in self.webs["sites"]:
            pass

    def save(self):
        json.dump(self.webs)

    def get_root(url):
        pass

if __name__ == "__main__":
    listener = ListenerUpdater()
    while True:
        choice = raw_input("What would you like to do? Enter a number.\n" +
                           "1 - Setup/change login info\n" +
                           "2 - Add new listeners\n" +
                           "3 - View/delete listeners\n" +
                           "4 - Exit")
        if choice == 1:
            listener.setup()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            break
    listener.save()
