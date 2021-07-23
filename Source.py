#this is the correct one without double negatives
import requests
import urllib.request
import urllib3
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pandas as pd
import io
import base64
import nbt
import time
import datetime
import os
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
def decode_inventory_data(raw):
   data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw)))
   #print(data.pretty_tree())
   return (data.pretty_tree())
   #print(data)

print("(c) 2021 Armoured Egg LLC")
x = "New Year Cake"
print("input api key to get this type /api in hypixel")
apik= input()
print("input expected maximum pages you may exeed the real value but it will slow the proccess its advised to select somewhere above 80 but less than 100")
expg=int(input())-1
print("enable audio y/n")
audioset=input()

pag=0
while True:
    time.sleep(1)
    if pag > int(expg):
        pag = 0
    pag= pag+1
    mod = 0
    cakes=0
    dateofcreationmath= []
    timeindaymath=[]
    numb2 = 0
    year =[]
    trueyear=0
    nam = 0
    word = '/'
    auctioneer= "none"

    oglist = []
    item = 0
    numb= 0
    b = (re.split("",str(x)))
    for z in b:
        oglist.append(z)
    n = oglist[1]
    cabbage = []
    nap = 0
    numb3=0
    maj = []
    for no in oglist:
        nap = nap+1
        if nap > 1:
            if nap < len(oglist):
                maj.append(no)
    #os.system('cls')
    
    maj = "".join(maj)
    time.sleep(1)
    page ="https://api.hypixel.net/skyblock/auctions?page="+str(pag)
    data = requests.get(page)
    ls = []
    html = BeautifulSoup(data.text,"html.parser")
    rawtext = data.text
    finishedstr = rawtext.split('"')

    for h in finishedstr:
        timekeeper = item
        if h == maj:
            cakes = cakes+1
            auctioneer= 'none'
            numb = 0
            for num in finishedstr:
                try:
                    if (finishedstr[item+numb] == 'auctioneer'):
                        auctioneer = finishedstr[item+numb+2]
                except:
                    
                    continue
                numb = numb-1
                if (auctioneer != 'none'):
                    numb = numb+1
                    break
            try:
                rw = finishedstr[item+22]
                startbid=finishedstr[item+19]
            except:
                item = 0
            inter = str(decode_inventory_data(rw))
            inter = re.sub('\s+',' ',inter)
            year=inter.split(" ")
            numb3=0
            for nu in year:
                try:
                    if (year[numb3] =='''TAG_Int('new_years_cake'):'''):
                        #print("i"+str(item))
                        #print("n"+str(numb))
                        trueyear = year[numb3+1]
                    #print(year[numb3])
                    numb3 = numb3+1
                except:
                    numb3 = numb3+1
                    continue
            refinter = (inter.split(' '))
            playerdata = requests.get("https://api.hypixel.net/player?key="+apik+"&uuid="+ auctioneer)
            finishedplayerdata = (playerdata.text).split('"')
            numb2 = 0
            time.sleep(.25)
            for numy in finishedplayerdata:
                try:
                    if (finishedplayerdata[numb2] == 'playername'):
                        #print("i"+str(item))
                        #print("n"+str(numb))
                        nam = finishedplayerdata[numb2+2]
                    numb2 = numb2+1
                except:
                    numb2 = numb2+1
                    continue
            numb2=0
            if nam == 0:
                for numy in finishedplayerdata:
                    try:
                        if (finishedplayerdata[numb2] == 'displayname'):
                            #print("i"+str(item))
                            #print("n"+str(numb))
                            nam = finishedplayerdata[numb2+2]
                        numb2 = numb2+1
                    except:
                        numb2 = numb2+1
                        continue
                
            dateofcreation = (refinter[len(refinter)-10])
            timeinday = (refinter[len(refinter)-9])
            ampm=(refinter[len(refinter)-8])
            dateofcreationmath=dateofcreation.split('/')
            timeindaymath=timeinday.split(':')
            if ampm == "PM":
                mod = 12
            else:
                mod = 0
            madegameyear = (((int(dateofcreationmath[0])*(2629743))+(int(dateofcreationmath[1])*86400)+((int(dateofcreationmath[2])+30)*31556926)+((int(timeindaymath[0])+mod)*3600))+int(timeindaymath[1]))
            finalmadegameyear = (((madegameyear-1560718500)/446400)+1)-6
            if (finalmadegameyear+.2<int(trueyear)):
                if audioset == "y":
                    speak.Speak("glitched cake identified owner is:" +str(nam))
                print(finalmadegameyear)
                print('glitched cake identified owner is: '+str(nam))
                print("date of creation: "+dateofcreation)
                print("time of day: "+timeinday)
                print(ampm)
                print("edition: "+trueyear)
                print("name: /ah "+str(nam))
                print("auctioneer: "+auctioneer)
                print("starting bid: "+startbid)
            if nam == 0:
                print ("begin")
                for numy in finishedplayerdata:
                    try:
                        if (finishedplayerdata[numb2] == 'playername'):
                            nam = finishedplayerdata[numb2+2]
                        numb2 = numb2+1
                    except:
                        numb2 = numb2+1
                        continue
        item = timekeeper
        item = item+1
    print("page"+ str(pag))
