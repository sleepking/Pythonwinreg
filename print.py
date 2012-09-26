import _winreg
import string
import sys

q=[_winreg.HKEY_CURRENT_USER,_winreg.HKEY_LOCAL_MACHINE,_winreg.HKEY_USERS,_winreg.HKEY_PERFORMANCE_DATA,_winreg.HKEY_CURRENT_CONFIG]
w="S-1-5-21-2551796448-4277757654-932718426-1000\Software\Microsoft\Internet Explorer\InternetRegistry\REGISTRY\USER\S-1-5-21-2551796448-4277757654-932718426-1000\SOFTWARE\JavaSoft\Java Runtime Environment\Security Baseline"
key=string.replace(w," ","*")
key=string.replace(w,"\\"," ")
key=w.split("\\")
for i in range(len(key)):
    key[i]="\"+key[i]
    print key[i]

subkey=[]
#for i in range(len(q)):
#	print _winreg.QueryInfoKey(q[i])
for i in range(len(q)):
	for j in range(_winreg.QueryInfoKey(q[i])[0]):
			subkey.append( _winreg.EnumKey(q[i],j)+'\Software')
print subkey