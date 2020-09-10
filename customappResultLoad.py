import pyautogui as gui
import time
import cv2
import numpy as np
from Utils import *
from AppCreation import *

def main():
    move_screen_centre()
    right_side_click()
    scrollcount= 5000
    appList = {}
    appList['poll']=0
    appList['survey']=0
    appList['checklist']=0
    appList['total']=0
    appCreationCounter=0
    SCROLL_UP_PARAM = 2

    while(scrollcount>0):    
        scrollcount-=1
        
        check_view_for_customapp(appList)

        print(appList)

        if(checkandScroll() == 0):
            appCreationCounter+=pollApp()
            appCreationCounter+=checklistApp()
            appCreationCounter+=surveyApp()
            right_side_click()
            print("number of apps created: "+str(appCreationCounter))
            scrollToTop(SCROLL_UP_PARAM)
            
main()