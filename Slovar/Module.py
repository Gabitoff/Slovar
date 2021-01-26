import os
#import sys
#import fileinput
from gtts import *
import time
from tkinter import*
import tkinter as tk
from tkinter import ttk

def loe_fail(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    #print(mas)
    return mas
    #print(mas)

#loe_fail("rus.txt")

def kirjuta_rus(f,rida,anslblwrus,mas):
    rusw=rida.get()
    fail=open(f,'a',encoding="utf-8-sig")
    #if rida in fail:
    #    pass
    #else:
    #    fail.write(rida+'\n')
    fail.write(rusw+'\n')
    mas.append(rusw.strip())
    fail.close()
    return mas
    anslblwrus.configure(text=f"Слово \"{rusw}\" добавлено")

def kirjuta_eng(f,rida,anslblweng,mas):
    engw=rida.get()
    fail=open(f,'a',encoding="utf-8-sig")
    #if rida in fail:
    #    pass
    #else:
    #    fail.write(rida+'\n')
    fail.write(engw+'\n')
    mas.append(engw.strip())
    fail.close()
    return mas
    anslblweng.configure(text=f"Слово \"{engw}\" добавлено")

def tolkimine(sonavar,s1,s2,anslbl):
    sona=sonavar.get()
    if sona in s1:
        anslbl.configure(text=f"{sona}-{s2[s1.index(sona)]}")
    elif sona in s2:
        anslbl.configure(text=f"{sona}-{s1[s2.index(sona)]}")
    else:
        anslbl.configure(text=f"Слово \"{sona}\" не найдено")

def paranda(rus,rmas,rv,ro,eng,emas,ev,eo,ok):
    rusnepr=rv.get()
    ruspr=ro.get()
    engnepr=ev.get()
    engpr=eo.get()
    fail=open(rus, "rt", encoding="utf-8-sig")
    data=fail.read()
    data=data.replace(rusnepr,ruspr)
    fail.close()
    fail=open(rus, "wt", encoding="utf-8-sig")
    fail.write(data)
    fail.close()
    fail=open(eng, "rt", encoding="utf-8-sig")
    data=fail.read()
    data=data.replace(engnepr,engpr)
    fail.close()
    fail=open(eng, "wt", encoding="utf-8-sig")
    fail.write(data)
    fail.close()
    #rmas=[]это можно довести до ума и укоротить функцию
    #rmas=loe_fail(rus)
    #emas=[]
    #emas=loe_fail(eng)
    rmas.remove(rusnepr)
    emas.remove(engnepr)
    rmas.append(ruspr)
    emas.append(engpr)
    ok.configure(text="Исправления внесены")
    return emas,rmas

def audio(sonavar,s1,s2,anslbl):
    text=sonavar.get()
    if text in s1:
        anslbl.configure(text=f"{text}-{s2[s1.index(text)]}")
        audio1=str(f"{text}")
        audio2=str(f"{s2[s1.index(text)]}")
        speech1=gTTS(text=audio1, lang="ru", slow=False)
        speech2=gTTS(text=audio2, lang="en", slow=False)
        speech1.save("voice1.mp3")
        speech2.save("voice2.mp3")
        os.system("start voice1.mp3")
        time.sleep(2)
        os.system("start voice2.mp3")
    elif text in s2:
        anslbl.configure(text=f"{text}-{s1[s2.index(text)]}")
        audio1=str(f"{text}")
        audio2=str(f"{s1[s2.index(text)]}")
        speech1=gTTS(text=audio1, lang="en", slow=False)
        speech2=gTTS(text=audio2, lang="ru", slow=False)
        speech1.save("voice1.mp3")
        speech2.save("voice2.mp3")
        os.system("start voice1.mp3")
        time.sleep(2)
        os.system("start voice2.mp3")
    else:
        anslbl.configure(text=f"Слово \"{text}\" не найдено")


    
    
