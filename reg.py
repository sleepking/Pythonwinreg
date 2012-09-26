import _winreg
import string
import sys

#print sys.argv
q=[_winreg.HKEY_CURRENT_USER,_winreg.HKEY_LOCAL_MACHINE,_winreg.HKEY_USERS,_winreg.HKEY_PERFORMANCE_DATA,_winreg.HKEY_CURRENT_CONFIG]

subkey=[]
for i in range(len(q)):
	for j in range(_winreg.QueryInfoKey(q[i])[0]):
		subkey.append( _winreg.EnumKey(q[i],j))
		print subkey

w="S-1-5-21-576782987-4290462806-2937597302-1001\Software\Microsoft\Internet Explorer\InternetRegistry\REGISTRY\USER\S-1-5-21-576782987-4290462806-2937597302-1001\SOFTWARE\JavaSoft\Java Runtime Environment\Security Baseline"
key=string.replace(w," ","*")
print key
key=string.replace(w,"\\"," ")
key=w.split("\\")
print key
x=len(key)

for i in key:
	print i


#b=_winreg.CreateKey( _winreg.HKEY_USERS, a)

q=_winreg.HKEY_USERS
_winreg.CreateKey(q,w)

h= _winreg.OpenKey(q, w, 0, _winreg.KEY_READ)
if h != 0 :
	b= _winreg.QueryValue(q, w)
	print b
	print _winreg.QueryInfoKey(h)

for i in range(_winreg.QueryInfoKey(h)[1]):
	s = _winreg.EnumValue(h,i)
	#a = _winreg.EnumKey(_winreg.HKEY_USER,i)
	print s