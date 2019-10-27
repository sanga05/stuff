import subprocess
import os
import datetime
def printz(y,str):
    slist=[]
    for i in range(1,int(y)):
        slist.append(' ')
    strz=''.join(slist)+str
    return strz

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def format():
    os.system('clear')
    cols=subprocess.check_output(['tput','cols'])
    rows=subprocess.check_output(['tput','lines'])
    str=printz(int(cols)/2 -10,"Welcome to Cli Diary")
    prGreen(str) 
    print("\n")
    #prLightPurple(subprocess.check_output(['date']))
    prLightPurple(datetime.datetime.now())
def cl_put(ch):    
    cols=subprocess.check_output(['tput','cols'])
    rows=subprocess.check_output(['tput','lines'])
    sl=[]
    for i in range(1,int(int(cols)/2)):
        sl.append(ch)
        sl.append(" ")
    stra = ''.join(sl)
    prYellow(stra)
