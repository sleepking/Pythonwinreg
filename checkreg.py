import _winreg
import string
import sys
import win32security

username = "Mark"
sid = win32security.ConvertSidToStringSid(win32security.LookupAccountName(None, username)[0])
f = open("hello.txt", "r")
key = ""
done = False
while done = False
	text = f.readline()
	if text != DONE | sid
		key = key + text
		else if text == "sid"
			key = key + "\\" + sid
		else if text == "DONE"
			done = True
print text

keyname1 = "\Software\Microsoft\Internet Explorer\InternetRegistry\REGISTRY\USER"
keyname2 = "\SOFTWARE\JavaSoft\Java Runtime Environment\Security Baseline"
print sid
finalkey = keyname1 + "\\" + sid + keyname2
print finalkey

try:
	key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, finalkey)
	print "key found"
except:
	print "key not found"
	