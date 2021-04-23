import outlook
import config

def fetchMail():
    mail = outlook.Outlook()
    mail.login(config.user_name, config.password)
    mail.inbox()

    emailFrom,sub = mail.unreadEmailFromAndSubject()
    start = emailFrom.find("<")
    end = emailFrom.find(">")
    fromId = emailFrom[start+1:end]
    sepList = sub.split()
    sepList = [each_string.lower() for each_string in sepList]
    if 'ooo' in sepList:
        return sub,fromId

    return "not ooo case!!", "not required!!"