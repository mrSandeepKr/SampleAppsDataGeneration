import pyautogui as gui
from Utils import *

PAUSE_FOR_CREATION_VIEW_POLL = 5
PAUSE_FOR_CREATION_VIEW_SURVEY = 5
PAUSE_FOR_CREATION_VIEW_CHECKLIST = 5
PAUSE_POST_SEND  = 5
PAUSE_AFTER_CLICKING_NEXT = 3

def openAppPanel():
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
    return 1

def pollApp():
    if(openAppPanel()==False):
        return 0

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
    
    nextButton = gui.locateOnScreen('images/Poll/Next.PNG')
    if(nextButton == None):
        print('cant find Next')
        close_card()
        return 0
    moveAndClick(nextButton)
    
    pause(PAUSE_AFTER_CLICKING_NEXT)

    sendButton = gui.locateOnScreen('images/send.PNG')

    if(sendButton == None):
        print('cant find send button')
        return 0

    gui.moveTo(sendButton)
    gui.leftClick()
    pause(PAUSE_POST_SEND)
    return 1

def surveyApp():
    move_screen_centre()
    openAppPanel()

    surveyApp = gui.locateOnScreen('images/AppIcon/survey.PNG')
    if(surveyApp==None):
        print('couldnt find the survey icon')
        return 0
        
    moveAndClick(surveyApp)
    pause(PAUSE_FOR_CREATION_VIEW_SURVEY)

    #need to add a while statement to make this work
    #incase the things not loaded in 5 secs on  just make it click on the cross 

    enterTitle = gui.locateOnScreen('images/Survey/enterTitle.PNG')
    if(enterTitle == None):
        print('cant find \"Enter Survey Title\"')
        close_card()
        return 0

    moveAndClick(enterTitle)
    gui.write('Automated Survey',interval = 0.05)

    addQuestionButton = gui.locateOnScreen('images/Survey/addQuestionButton.PNG')
    if(addQuestionButton==None):
        print('cant find \"Add Question\" Button')
        close_card()
        return 0
    
    moveAndClick(addQuestionButton)
    pause(1)

    enterQuestion = gui.locateOnScreen('images/Survey/enterQuestion.PNG')
    if(enterQuestion == None):
        print('cant find \" Add your Question \"')
        close_card()
        return 0
    
    moveAndClick(enterQuestion)
    gui.write('can you see the icon on this survey?' , interval=0.05)
    
    choice = gui.locateAllOnScreen('images/Survey/enterChoice.PNG')
    if(choice == None):
        print('cant find \"Choice \"')
        close_card()
        return 0

    choice = list(choice)
    choicenumber = 1
    for box in choice:
        moveAndClick(box)
        gui.write("hardcodedchoice " + str(choicenumber),interval = 0.05)
        choicenumber+=1

    requiredButton = gui.locateOnScreen('images/Survey/required.PNG')
    if(requiredButton == None):
        print('cant find the required button')
        close_card()
        return 0
    
    moveAndClick(requiredButton)
    
    nextButton = gui.locateOnScreen('images/Survey/next.PNG')
    if(nextButton == None):
        print('cant find Next')
        close_card()
        return 0

    moveAndClick(nextButton)
    pause(PAUSE_AFTER_CLICKING_NEXT)

    sendButton = gui.locateOnScreen('images/send.PNG')
    if(sendButton == None):
        print('cant find the send button')
        close_card()
        return 0
    
    moveAndClick(sendButton)
    pause(PAUSE_POST_SEND)
    return 1

def checklistApp():
    move_screen_centre()
    openAppPanel()

    checklistApp = gui.locateOnScreen('images/AppIcon/checklist.PNG')
    if(checklistApp==None):
        print('couldnt find the checklist icon')
        return 0
        
    moveAndClick(checklistApp)
    pause(PAUSE_FOR_CREATION_VIEW_CHECKLIST)

    #need to add a while statement to make this work
    #incase the things not loaded in 5 secs on  just make it click on the cross 

    nameYourChecklist = gui.locateOnScreen('images/Checklist/nameYourChecklist.PNG')
    if(nameYourChecklist == None):
        print('cant find \"Name your checklist\"')
        close_card()
        return 0

    moveAndClick(nameYourChecklist)
    gui.write('Automated checklist',interval = 0.05)

    firstBox = gui.locateOnScreen('images/Checklist/firstBox.PNG')
    if(firstBox == None):
        print('cant find the first box')
        close_card()
        return 0
    moveAndClick(firstBox)
    gui.write('item 1',0.03)

    for i in range(2,5):
        addItem = gui.locateOnScreen('images/Checklist/addItem.PNG')
        if(addItem == None):
            break
        moveAndClick(addItem)
        gui.write('item '+str(i),0.03)
    
    nextButton = gui.locateOnScreen('images/Checklist/next.PNG')
    if(nextButton == None):
        print('cant find Next')
        close_card()
        return 0

    moveAndClick(nextButton)
    pause(PAUSE_AFTER_CLICKING_NEXT)

    sendButton = gui.locateOnScreen('images/send.PNG')
    if(sendButton == None):
        print('cant find the send button')
        close_card()
        return 0
    
    moveAndClick(sendButton)
    pause(PAUSE_POST_SEND)
    return 1
