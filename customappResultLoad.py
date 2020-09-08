import pyautogui as gui
import time
import cv2
import numpy as np
from Utils import *

def main():
    scrollcount= 5000
    appList = {}
    appList['poll']=0
    appList['survey']=0
    appList['checklist']=0
    appList['total']=0

    while(scrollcount>0):    
        scrollcount-=1
        
        check_view_for_customapp(appList)

        print(appList)

        if(checkandScroll() == 0):
            for i in range (20):
                gui.scroll(1000)
                time.sleep(0.3)
            
main()