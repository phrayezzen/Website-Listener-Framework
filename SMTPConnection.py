import smtplib


class SMTPConnection(object):
    def login(self, username, password, server, port=587):
        self.s = smtplib.SMTP(server, port)
        self.s.ehlo()
        self.s.starttls()
        self.s.ehlo()
        self.s.login(username, password)

    def send_message(self, sender, recipients, message):
        self.s.sendmail(sender, recipients, message)

    def logout(self):
        self.s.quit()
