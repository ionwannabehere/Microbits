from microbit import *
import time
import math
import random
import music

set_volume(0)

vol = 0

#Static Inital
class hrtValues:
    pass
class globalValues:
    pass
    
    
eventHandList = []
def hrtFnCh(n,z):
    if math.trunc((time.ticks_ms()/1000)*z) > getattr(hrtValues,n):
        setattr(hrtValues,n,math.trunc((time.ticks_ms()/1000)*z))
        eventHandList.append(n)
def rowF(x,y,z):
    for i in range(y):
        display.set_pixel(i,x,z)

aAct = False
bAct = False
gAct = False
p1Act = False

pongA = True
menuA = False
settA = False

def settI():
    setattr(globalValues,"settSide",0)
    for i in range(vol):
        rowF(4-i,2,9)

def settABtn():
    global vol
    settSide = getattr(globalValues,"settSide")
    if vol < 5:
        vol += 1
        set_volume(vol * 51)
        music.play('d')
        for x in range(vol):
            rowF(4-x,2, 9)
def settBBtn():
    global vol
    settSide = getattr(globalValues,"settSide")
    if settSide == 0:
        if vol > 0:
            vol -= 1
            set_volume(vol * 51)
            music.play('d')
            for v in range(5-vol):
                rowF(v,2, 0)
            for x in range(vol):
                rowF(4 - x,2, 9)
def settP1T():
    global vol
    settSide = getattr(globalValues,"settSide")
    if settSide == 1:
        settSide = 0
        for x in range(vol):
            rowF(4-x,2, 9)

    else:
        settSide = 1
        for x in range(vol):
            rowF(4-x,2, 5)

        
    setattr(globalValues,"settSide",settSide)  



def menuI():
    setattr(globalValues,"tabA",0)
    for q in range(3):
        rowF(q,5,6)
    rowF(0,5,9)

def menuABtn():
    tabA = getattr(globalValues,"tabA")
    if tabA > 0:
        rowF(tabA,5,6)
        tabA-=1
        rowF(tabA,5,9)
        setattr(globalValues,"tabA",tabA)
def menuBBtn():
    tabA = getattr(globalValues,"tabA")
    if tabA < 2:
        rowF(tabA,5,6)
        tabA+=1
        rowF(tabA,5,9)
        setattr(globalValues,"tabA",tabA)

def pongI():
    setattr(hrtValues,"H",0)
    
    r1 = random.randint(1,2)
    r2 = random.randint(1,2)
    ball = [r1,r2]
    if random.choice([True, False]):
        ballDir = -1
    else:
        ballDir = 1
    ballRef = 1
    display.set_pixel(r1,r2,5)
    
    plrD = 2
    display.set_pixel(0,2,9)
    display.set_pixel(0,3,9)
    cmpD = 2
    display.set_pixel(4,2,9)
    display.set_pixel(4,3,9)
    setattr(globalValues,"ball",ball)
    setattr(globalValues,"ballDir",ballDir)
    setattr(globalValues,"ballRef",ballRef)
    setattr(globalValues,"plrD",plrD)
    setattr(globalValues,"cmpD",cmpD)
    
def pongABtn():
    plrD = getattr(globalValues,"plrD")
    ball = getattr(globalValues,"ball")
    if plrD >0 and not (ball[0] == 0 and ball[1] == plrD-1):
        display.set_pixel(0,plrD+1,0)
        setattr(globalValues,"plrD",plrD-1)
        display.set_pixel(0,plrD-1,9)
def pongBBtn():
    plrD = getattr(globalValues,"plrD")
    ball = getattr(globalValues,"ball")
    if plrD < 3 and not (ball[0] == 0 and ball[1] == plrD+2):
        display.set_pixel(0,plrD,0)
        setattr(globalValues,"plrD",plrD+1)
        display.set_pixel(0,plrD+2,9)
def pingHrt():
    if eventHandList[0] == "H":
        ball = getattr(globalValues,"ball")
        ballRef = getattr(globalValues,"ballRef")
        ballDir = getattr(globalValues,"ballDir")
        plrD = getattr(globalValues,"plrD")
        cmpD = getattr(globalValues,"cmpD")
        
        bNewX = ball[0] + ballRef
        bNewY = ball[1] + ballDir
    
    
        if bNewX == 5 or bNewX == -1:
            ballRef = ballRef * -1
            bNewX = ball[0] + ballRef
        if bNewY == 5 or bNewY == -1:
            ballDir = ballDir * -1
            bNewY = ball[1] + ballDir
        if (bNewX == 0) and (bNewY == plrD or bNewY == plrD +1):
            music.play("f",wait=False)
            ballRef = 1
            bNewX = ball[0] + ballRef
            if (ball[1] == plrD -1 or ball[1] == plrD +3) and (ball[1]!=0 and ball[1]!=4):
                ballDir = ballDir * -1
                bNewY = ball[1] + ballDir
        if (bNewX == 4) and (bNewY == cmpD or bNewY == cmpD +1):
            music.play("d",wait=False)
            ballRef = -1
            bNewX = ball[0] + ballRef
            if (ball[1] == cmpD -1 or ball[1] == cmpD +3) and (ball[1]!=0 and ball[1]!=4):
                ballDir = ballDir * -1
                bNewY = ball[1] + ballDir
        
        display.set_pixel(ball[0],ball[1],0)
        display.set_pixel(bNewX,bNewY,5)
        ball = [bNewX,bNewY]
    
        if bNewX == 4:
            music.play(music.POWER_UP,wait=False)
        elif bNewX == 0:
            music.play(music.POWER_DOWN,wait=False)
        
        eventHandList.pop(0)
    
        if random.choice([True, False]):
            if ball[1] > cmpD and cmpD < 3 and not (ball[0] == 4 and ball[1] == cmpD+2):
                display.set_pixel(4,cmpD,0)
                cmpD+=1
                display.set_pixel(4,cmpD+1,9)
            elif ball[1] < cmpD and cmpD >0 and not (ball[0] == 4 and ball[1] == cmpD-1):
                display.set_pixel(4,cmpD+1,0)
                cmpD-=1
                display.set_pixel(4,cmpD,9)
        setattr(globalValues,"ball",ball)
        setattr(globalValues,"ballRef",ballRef)
        setattr(globalValues,"ballDir",ballDir)
        setattr(globalValues,"plrD",plrD)
        setattr(globalValues,"cmpD",cmpD)

pongI()
while True:
    #HeartBeatHandle
    if pongA:  
        hrtFnCh("H",3)
    #EventHandler
    if len(eventHandList) > 0:
        nHrt = True
        while nHrt:
            if len(eventHandList) > 0:
                if eventHandList[0] == "G" or eventHandList[0] == "P1":
                    clrR = True
                    while clrR:
                        if len(eventHandList) > 1:
                            if eventHandList[1] == "G" or eventHandList[1] == "P1":
                                eventHandList.pop(1)
                            else:
                                clrR = False
                        else:
                            clrR = False

                    if menuA:
                        if eventHandList[0] == "G":
                            tabA = getattr(globalValues,"tabA")
                            if tabA == 0:
                                menuA = False
                                settA = True
                                sleep(100)
                                display.clear()
                                settI()
                            if tabA == 1:
                                menuA = False
                                pongA = True
                                sleep(100)
                                display.clear()
                                pongI()
                    else:
                        if eventHandList[0] == "G":
                            pongA = False
                            settA = False
                            menuA = True
                            sleep(100)
                            display.clear()
                            menuI()
                        elif eventHandList[0] == "P1":
                            if settA:
                                settP1T()
                    eventHandList.pop(0)
                else:
                    if eventHandList[0] == "A" or eventHandList[0] == "B":
                        if eventHandList[0] == "A":
                            if pongA:
                                pongABtn()
                            elif menuA:
                                menuABtn()
                            elif settA:
                                settABtn()
                        elif eventHandList[0] == "B":
                            if pongA:
                                pongBBtn()
                            elif menuA:
                                menuBBtn()
                            elif settA:
                                settBBtn()
                        eventHandList.pop(0)
                    else:
                        #HEARBEAT EVENT CALL ACTION
                        if pongA:
                            pingHrt()
                        nHrt = False
            else:
                nHrt = False
        
    if button_a.is_pressed():
        if not aAct:
            aAct = True
            eventHandList.append("A")
    else:
        if aAct:
            aAct = False
            
    if button_b.is_pressed():
        if not bAct:
            bAct = True
            eventHandList.append("B")
    else:
        if bAct:
            bAct = False
            
    if pin_logo.is_touched():
        if not gAct:
            gAct = True
            eventHandList.append("G")
    else:
        if gAct:
            gAct = False
    if pin1.is_touched():
        if not p1Act:
            p1Act = True
            eventHandList.append("P1")
    else:
        if p1Act:
            p1Act = False