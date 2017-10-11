# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 02:23:43 2017

@author: DREAM
"""

#import var, tasks

#import tasks, var

import var

import cv2, subprocess
import numpy as np
import multiprocessing


dir_name = "Images"


#dir_name = var.dir_name

#tasks.mk_dir(dir_name)

font=cv2.FONT_HERSHEY_SIMPLEX

def camera1_linux():

    id_no = 101
    host = "192.168.1." + str(id_no)
    
    if var.os_name == "nt":  #windows
        ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
        if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
            host_conn = 0
    
        else:
            host_conn = 1
            
    if var.os_name == "posix":
        ping = subprocess.Popen(["ping","-c","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
        if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)) or ('0 received' in str(ping)):
            host_conn = 0
            
        else:
            host_conn = 1
                

    if host_conn == 1:    
        cap = cv2.VideoCapture("rtsp://192.168.1.101:554/12")  
        
        while True:
            _, frame = cap.read()
            cv2.circle(frame, (320,180), 3, (0,255,0), 2)  
            cv2.putText(frame, '101', (20,50), font, 1, (255,255,255),2,cv2.LINE_AA)
            
            cv2.imshow(('Camera 101'), frame)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
    
        cap.release()
        
def camera1():
    id_no = 101
    host = "192.168.1." + str(id_no)
    
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        host_conn = 0

    else:
        host_conn = 1

    if host_conn == 1:
        cap = cv2.VideoCapture("rtsp://192.168.1.101:554/12")
        
        while True:
    
            _, frame = cap.read()
            cv2.circle(frame, (320,180), 3, (0,255,0), 2) 
            cv2.putText(frame, '102', (20,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            cv2.imshow(('Camera 102'), frame)
            
            k = cv2.waitKey(1)
            if k == 27:
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
        
        while True:
    
            _, frame = cap.read()
            cv2.circle(frame, (320,180), 3, (0,255,0), 2) 
            cv2.putText(frame, '102', (20,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            cv2.imshow(('Camera 102'), frame)
            
            k = cv2.waitKey(1)
            if k == 27:
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
            cv2.circle(frame, (320,180), 3, (0,255,0), 2) 
            cv2.putText(frame, '103', (20,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            cv2.imshow(('Camera 103'), frame)
            
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
                    
        while True:
    
            _, frame = cap.read()
            cv2.circle(frame, (320,180), 3, (0,255,0), 2) 
            cv2.putText(frame, '104', (20,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            cv2.imshow(('Camera 104'), frame)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
                
        cap.release()


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=camera1)
    p1.start()
    p2 = multiprocessing.Process(target=camera2)
    p2.start()
    #p3 = multiprocessing.Process(target=camera3)
    #p3.start()     
    #p4 = multiprocessing.Process(target=camera4)
    #p4.start()
        
