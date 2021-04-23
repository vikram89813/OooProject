import email
import imaplib
import smtplib
import datetime
import email.mime.multipart
import config
import base64


class Outlook():
    def __init__(self):
        pass

    def login(self, username, password):
        self.username = username
        self.password = password
        login_attempts = 0
        while True:
            try:
                self.imap = imaplib.IMAP4_SSL(config.imap_server,config.imap_port)
                r, d = self.imap.login(username, password)
                assert r == 'OK', 'login failed: %s' % str (r)
                print(" > Signed in as %s" % self.username, d)
                return
            except Exception as err:
                print(" > Sign in error: %s" % str(err))
                login_attempts = login_attempts + 1
                if login_attempts < 3:
                    continue
                assert False, 'login failed'

    def inbox(self):
        return self.imap.select("Inbox")

    def logout(self):
        return self.imap.logout()

    def getEmail(self, id):
        r, d = self.imap.fetch(id, "(RFC822)")
        self.raw_email = d[0][1]
        self.email_message = email.message_from_string(self.raw_email)
        return self.email_message
    
    def getEmailUnreadSubject(self, id):
        r, d = self.imap.fetch(id, "(RFC822)")
        self.raw_email = d[0][1]
        self.email_message = email.message_from_string(self.raw_email)
        return self.email_message['Subject']
    
    def getEmailUnreadFromIdandSub(self, id):
        r, d = self.imap.fetch(id, "(RFC822)")
        self.raw_email = d[0][1]
        self.email_message = email.message_from_string(self.raw_email)
        fromId = self.email_message['From']
        subject = self.email_message['Subject']
        return fromId,subject

    def unread(self):
        list = self.unreadIds()
        latest_id = list[-1]
        return self.getEmail(latest_id)

    def unreadEmailSubject(self):
        list = self.unreadIds()
        latest_id = list[-1]
        return self.getEmailUnreadSubject(latest_id)

    def unreadEmailFromAndSubject(self):
        list = self.unreadIds()
        latest_id = list[-1]
        return self.getEmailUnreadFromIdandSub(latest_id)

    def read(self):
        list = self.readIds()
        latest_id = list[-1]
        return self.getEmail(latest_id)

    def mailbodydecoded(self):
        return base64.urlsafe_b64decode(self.mailbody())

    def unreadIds(self):
        r, d = self.imap.search(None, "UNSEEN")
        list = d[0].split(' ')
        return list
