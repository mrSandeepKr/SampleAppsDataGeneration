import pyautogui as gui
import time
import cv2
import numpy as np
from Utils import *

def main():
    scrollcount= 100

    while(scrollcount>0):    
        scrollcount-=1
        
        check_view_for_customapp()

        if(checkandScroll() == 0):
            gui.scroll(2500)
            
main()