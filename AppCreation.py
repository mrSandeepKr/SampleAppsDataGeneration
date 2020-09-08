import pyautogui as gui
from Utils import *

PAUSE_FOR_CREATION_VIEW_POLL = 5
PAUSE_POST_SEND  = 5
PAUSE_AFTER_CLICKING_NEXT = 3

def pollApp():
    right_side_click()
    pause(0.8)

    newConversation = gui.locateOnScreen('images/newConversation.PNG')
    if(newConversation==None):
        print('cant find New conversation')
        return 0

    gui.moveTo(newConversation)
    gui.leftClick()

    trippleDot = gui.locateOnScreen('images/trippleDot.PNG')

    if(trippleDot==None):
        print('couldnt find the tripple dot')
        return 0

    gui.moveTo(trippleDot)
    gui.leftClick()
    pollApp = gui.locateOnScreen('images/AppIcon/poll.PNG')

    if(pollApp==None):
        print('couldnt find the poll icon')
        return 0
        
    gui.moveTo(pollApp)
    gui.leftClick()
    pause(PAUSE_FOR_CREATION_VIEW_POLL)

    #need to add a while statement to make this work
    #incase the things not loaded in 5 secs on  just make it click on the cross 
    enter = gui.locateOnScreen('images/Poll/enterQuestion.PNG')
    if(enter == None):
        print('cant find \"Enter poll question \"')
        close_card()
        return 0

    gui.moveTo(enter)
    gui.leftClick()
    gui.write('Hi this is an automated process please dont mind',interval = 0.05)
    
    choice = gui.locateAllOnScreen('images/Poll/enterChoice.PNG')
    if(choice == None):
        print('cant find \"Choice \"')
        close_card()
        return 0

    choice = list(choice)
    
    choicenumber = 1
    for box in choice:
        gui.moveTo(box)
        gui.leftClick()
        gui.write("hardcodedchoice " + str(choicenumber),interval = 0.05)
        choicenumber+=1
    
    next = gui.locateOnScreen('images/Next.PNG')
    if(next == None):
        print('cant find Next')
        close_card()
        return 0

    gui.moveTo(next)
    gui.leftClick()
    
    pause(PAUSE_AFTER_CLICKING_NEXT)

    send = gui.locateOnScreen('images/send.PNG')
    gui.moveTo(send)
    gui.leftClick()
    pause(PAUSE_POST_SEND)
