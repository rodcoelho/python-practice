import yagmail, keyring
username = 'rodcpython@gmail.com'
password = 'Cogitoergosum1@#py'
yag = yagmail.SMTP(username,password)
providers = {'ATT':'txt.att.net', 'T-mobile':'tmomail.net', 'Verizon':'vtext.com', 'Sprint': 'messaging.sprintpcs.com', 'metroPCS':'metropcs.sms.us'}

def sendtext(phone, provider, subject, body):
    x = provider
    phonemail = phone+'@'+providers[x]
    sendemail(phonemail,subject,body)

def sendemail(to,subject, body):
    yagmail.SMTP(username).send(to, subject,body)

def main():
    if __name__ == "__main__":
        main( )