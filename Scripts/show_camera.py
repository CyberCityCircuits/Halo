# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 18:10:43 2017

@author: DREAM
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 02:23:43 2017

@author: DREAM
"""

#import var, tasks

import var

import cv2, subprocess

stream="12" #Select stream type 11 - HD, 12 - SubStream, 13 - Phone Stream

font=cv2.FONT_HERSHEY_SIMPLEX

id_no = 101

def camera(id_no):

    #id_no = 101
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
        cap = cv2.VideoCapture("rtsp://"+host+":554/"+stream)  
        
        while True:
            _, frame = cap.read()
            #cv2.circle(frame, (320,180), 3, (0,255,0), 2)  
            cv2.putText(frame, str(id_no), (20,50), font, 1, (255,255,255),2,cv2.LINE_AA)
    
            cv2.imshow(('Camera'+str(id_no)), frame)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
    
        cap.release()


