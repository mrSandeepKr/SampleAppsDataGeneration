import time
import pyautogui as gui 
import cv2
import numpy as np

def pause(dur):
    time.sleep(dur)

def close_card():
    tries_left = 4
    while(tries_left >  0):
        cross = gui.locateOnScreen('images\cross.PNG')
        if(cross != None):
            gui.moveTo(cross)
            gui.leftClick()
            return 1
        tries_left -= 1
    return 0

def open_card(point):
    if(point == None):
        return
    gui.moveTo(point)
    gui.leftClick()

def test_card(point):
    if(point == None ):
        return 2
    open_card(point)
    pause(5)
    if(close_card()):
        return 1
    print('some bug occured the scenario  is saved as bug.PNG')
    bug = gui.screenshot()
    bug.save('bug.PNG')
    return 0

def move_screen_centre():    
    w = gui.size().width
    h = gui.size().height
    gui.moveTo(w/2,h/2,1)
    return

def right_side_click():   
    sz = gui.size()
    gui.moveTo(9.5*(sz.width/10),5*sz.height/10,0.5)
    gui.leftClick()
    pause(0.5)
    gui.leftClick()
    pause(0.5)
    gui.leftClick()


def scrolldown():
    move_screen_centre()
    gui.scroll(-200)

def checkandScroll():
    move_screen_centre()
    time.sleep(1)
    gui.screenshot().save('images/prior.PNG')

    scrolldown()
    time.sleep(1)

    gui.screenshot().save('images/post.PNG')

    x = cv2.imread('images/prior.PNG') 
    y = cv2.imread('images/post.PNG') 
    
    if(np.subtract(x,y).any() == False):
        print('Attempting to create a CustomApp as no room to scroll. Will go back to top then')
        return 0
    
    return 1

def scrollToTop():
    for i in range (20):
        gui.scroll(1000)
        pause(0.3)
    
def moveAndClick(location):
    gui.moveTo(location)
    gui.leftClick()

def check_view_for_customapp(appList):
    move_screen_centre()
    
    poll = test_card(gui.locateOnScreen('images\CardButton\poll.PNG'))
    if( poll== 0):
        return
    elif(poll == 1) :
        appList['poll']+=1
        appList['total']+=1

    checklist = test_card(gui.locateOnScreen('images\CardButton\checklist.PNG'))
    if(checklist == 0):
        return
    elif(checklist == 1) :
        appList['checklist']+=1
        appList['total']+=1

    survey = test_card(gui.locateOnScreen('images\CardButton\survey.PNG'))
    if(survey == 0):
        return
    elif(survey == 1) :
        appList['survey']+=1
        appList['total']+=1