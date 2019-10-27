import os
import pyAesCrypt
import subprocess
import getpass
import datetime 
import sys
from func import *
ard=''
try:
    ard=sys.argv[1]
except IndexError:
    print("please spacify gen pass date")
    sys.exit(2)
#if(ard!=None):
 #   print(ard)
try:
    pyAesCrypt.decryptFile("master_pass.aes", "dat",ard,1024*64)
except ValueError:
    print("Wrong Password")
    sys.exit(1)
f = open("dat","r")
pwd=f.read()
pwd=pwd.strip("\n")
print(pwd)
print()
buf=1024*64
#os.remove("dat")
prLightPurple("Enter Master password")
master_pass=getpass.getpass()
print(master_pass)
if(master_pass==pwd):
    prGreen("Welocome")
else:
    prGreen("Not you Out")
    sys.exit(23)
format()
path = '/home/sangamesh/gitProj/clidiary/logs'
os.chdir(path)
ll = os.listdir()
print (ll)
summed_up=[]
for l in ll:
    pyAesCrypt.decryptFile(l,"tmp",master_pass,buf)
    f=open("tmp","r")
    d=f.read()
    f.close()
    os.remove("tmp")
    i1=d.find('[1]')
    index=d.find('[4]')+4
    summed_up.append(d[:i1]+'\n'+d[index:])
cl_put("-")
for l in summed_up:
    print(l)
    cl_put("-")

