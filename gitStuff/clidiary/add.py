import subprocess
import pyAesCrypt
import getpass
import datetime
from func import *
from datetime import date
os.system('clear')
buffersize=64*1024
nextz=0
   
prLightPurple("Enter Master password")
master_pass=getpass.getpass()
def raw_inp():
    goal=[]
    while True:
        try:
            line=input()
        except KeyboardInterrupt:
            break            
            #nextz += 1          
        goal.append(line)
    return goal
def printz(y,str):
    slist=[]
    for i in range(1,int(y)):
        slist.append(' ')
    strz=''.join(slist)+str
    return strz
    
format()

prRed("Todays Goal:")
r=raw_inp()
goal=''
goal='\n'.join(r)
#print(goal)


os.system('clear')
cl_put("-")
#redisp()
prRed("Goal")
print(goal)
prRed("Describe the Day :")
print()
cl_put("-")
day=raw_inp()
dayz=''
dayz='\n'.join(day)


os.system('clear')
cl_put("-")
#redisp()
prRed("Goal")
print(goal)
cl_put("-")
#redisp()
prRed("This was your Day:")
print(dayz)
cl_put("-")

prCyan("learnt today:")
r=raw_inp()
sum = ''
sum = '\n'.join(r)
print()


os.system('clear')
cl_put("-")
#redisp()
prRed("Goal")
print(goal)

cl_put("-")
#redisp()
prRed("This was your Day:")
print(dayz)

cl_put("-")
#redisp()
prRed("Learnt:")
print(sum)
cl_put("-")


prCyan("just sum it up:")
r=raw_inp()
ll = ''
ll = '\n'.join(r)
#day=goal+dayz+sum+ll
print()


os.system('clear')
cl_put("-")
#redisp()
prRed("Goal")
print(goal)
#cl_put("*")
cl_put("-")
#redisp()
prRed("This was your Day:")
print(dayz)
#cl_put("*")
cl_put("-")
#redisp()
prRed("Learnt:")
print(sum)
#cl_put("*")
cl_put("-")
#redisp()
prRed("Summed :")
print(ll)
#cl_put("*")
print()
print()
cl_put("-")


day=str(datetime.datetime.now())[:19]+'\n'+'[1]:'+goal+'\n[2]:'+dayz+'\n[3]:'+sum+'\n[4]:'+ll
fname="/home/sangamesh/gitProj/clidiary/logs/logs "+str(date.today().day)+"-"+str(date.today().month)+"-"+str(date.today().year)
count =1
if(os.path.isfile(fname+".aes")):
    fnamez=fname+"-"+str(count)
    while(os.path.isfile(fnamez+".aes")):
        count =count+ 1
        fnamez=fname+"-"+str(count)
    fname=fnamez
fname=fname+".aes"
#password="temp"
file = open('new.txt','w')
file.write(day)
file.close()
#password=getpass.getpass()
pyAesCrypt.encryptFile("new.txt",fname,master_pass,buffersize)
os.remove('new.txt')
