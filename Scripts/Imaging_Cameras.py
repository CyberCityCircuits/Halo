# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 02:23:43 2017

@author: DREAM
"""

#import var, tasks

#import tasks, var

import cv2, os, subprocess
import numpy as np
import multiprocessing
import datetime as dt
from time import sleep
from shutil import copyfile

dir_name = "Images"


#dir_name = var.dir_name

#tasks.mk_dir(dir_name)

font=cv2.FONT_HERSHEY_SIMPLEX

def camera1():

    id_no = 101
    host = "192.168.1." + str(id_no)
    
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        host_conn = 0

    else:
        host_conn = 1

    if host_conn == 1:    
        #global cap1
        cap = cv2.VideoCapture("rtsp://192.168.1.101:554/12")  
        
        x=0
        while True:
            _, frame = cap.read()
            cv2.circle(frame, (320,180), 3, (0,255,0), 2)  
            cv2.putText(frame, '101', (0,50), font, 1, (255,255,255),2,cv2.LINE_AA)
            
            currdate = dt.date.today().strftime("%Y%m%d")
            currtime = dt.datetime.now().strftime("%H%M%S")
            currdatetime = currdate + "-" + currtime        
               
            #cv2.imshow('frame1', frame1)
            
            if x%20 == 0:
                cv2.imwrite(currdatetime + " - Image 1" + ".png", frame)
        
            x += 1
            #sleep(0.5)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
            elif x == 300:
                break
    
        cap.release()

def camera2():
    id_no = 102
    host = "192.168.1." + str(id_no)
    
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        host_conn = 0

    else:
        host_conn = 1


    if host_conn == 1:
        cap = cv2.VideoCapture("rtsp://192.168.1.102:554/12")
        x=0
        
        while True:
    
            _, frame = cap.read()
            cv2.circle(frame, (320,180), 3, (0,255,0), 2) 
            cv2.putText(frame, '102', (0,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            currdate = dt.date.today().strftime("%Y%m%d")
            currtime = dt.datetime.now().strftime("%H%M%S")
            currdatetime = currdate + "-" + currtime        
            
            if x%20 == 0:
                cv2.imwrite(currdatetime + " - Image 2" + ".png", frame)
                
            x += 1         
            #sleep(0.5)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
            elif x == 300:
                break
                
        cap.release()

def camera3():
    id_no = 103
    host = "192.168.1." + str(id_no)
    
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        host_conn = 0

    else:
        host_conn = 1


    if host_conn == 1:
        cap = cv2.VideoCapture("rtsp://192.168.1.103:554/12")
        x=0
        
        while True:
    
            _, frame = cap.read()
            #cv2.circle(frame, (320,180), 3, (0,255,0), 2) 
            #cv2.putText(frame, '103', (0,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            currdate = dt.date.today().strftime("%Y%m%d")
            currtime = dt.datetime.now().strftime("%H%M%S")
            currdatetime = currdate + "-" + currtime        
            
            if x%20 == 0:
                cv2.imwrite(currdatetime + " - Image 3" + ".png", frame)
                
            x += 1         
            #sleep(0.5)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
            elif x == 300:
                break
                
        cap.release()
        
    
def camera4():
    id_no = 104
    host = "192.168.1." + str(id_no)
    
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        host_conn = 0

    else:
        host_conn = 1

    if host_conn == 1:
        cap = cv2.VideoCapture("rtsp://192.168.1.104:554/12")
        x=0
            
        while True:
    
            _, frame = cap.read()
            cv2.circle(frame, (320,180), 3, (0,255,0), 2) 
            cv2.putText(frame, '104', (0,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            currdate = dt.date.today().strftime("%Y%m%d")
            currtime = dt.datetime.now().strftime("%H%M%S")
            currdatetime = currdate + "-" + currtime        
            
            if x%20 == 0:
                cv2.imwrite(currdatetime + " - Image 4" + ".png", frame)
                
            x += 1         
            #sleep(0.5)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
            elif x == 300:
                break
                
        cap.release()


def cap_images():
    _, img1 = p1.cap1.read()
    _, img2 = p2.cap2.read()
    cv2.imwrite("Image1.png", img1)
    cv2.imwrite("Image2.png", img2)
    

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=camera1)
    p1.start()
    p2 = multiprocessing.Process(target=camera2)
    p2.start()
    p3 = multiprocessing.Process(target=camera3)
    p3.start()     
    p4 = multiprocessing.Process(target=camera4)
    p4.start()
        
    sleep(20)
    
    print ("  Imaging Complete")
    
    sleep (1)
    
    currdate = dt.date.today().strftime("%Y%m%d")
    currtime = dt.datetime.now().strftime("%H%M%S")
    currdatetime = currdate + "-" + currtime   
    
    dir_name = dir_name + "-" + currdatetime
    
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    for root, dirs, files in os.walk(os.getcwd()):

        for file in files:
            if file.endswith('.png'):
                print ("Copying " + file)
                copyfile(file, dir_name + "\\" + file)
                sleep(.25)
                if os.path.isfile(file):
                    print ("Deleting " + file)
                    os.remove(file)