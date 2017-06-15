# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:21:48 2017

@author: DREAM
"""

#import libraries
import os
import sys
import datetime as dt
from time import sleep
import subprocess


application = "Ping_Halo"
version = "0.01.00"
name = application + "  V" + version
email = "David@DREAM-Enterprise.com"

count_camera = 5

#Set IP Scheme
scheme = "192.168.1."

list_ping = [0] * count_camera
list_ping_read = ["UNK"] * count_camera            
                 
list_ping_read = []  
list_id_no = []
list_ping_read = []    

width = 40
lines = count_camera + 7
cent_width = int(width)-1
dev_width = 10

scan = 31

#define cosole size and color
os.system("mode con: cols=" + str(width) + " lines=" + str(lines))
os.system("color F")
os.system("cls")
os.system("echo off")

#set start times
currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H:%M:%S")
start_time = dt.datetime.now().strftime("%H%M%S")

#set wait command
def pause(value):
    if value == 0:   #if 0 is entered it creates a press any key prompt.
        os.system("pause")
    elif int(value):
        sleep(value)


def set_id_list():
    global camera_list
    for i in range(count_camera):
        camera_list = range(count_camera)
    
    for i in camera_list:
        id_no = int(str(i).zfill(3))+101
        #print (id_no)
        list_id_no.append(id_no)               
            
        
#pings all cameras
def ping_all():   
    global list_ping_read
    list_ping_read = ["UNK"] * count_camera

    for c in list_id_no:

        host = scheme + str(c)
        #print("Pinging " + host)

        ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
        if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
            list_ping[int(c)-101] = 0
            #print ("Camera " + str(c) + " is DOWN")
            list_ping_read[int(c)-101] = "DOWN"
        else:
            list_ping[int(c)-101] = 1
            #print ("Camera " + str(c) + " is UP")
            list_ping_read[int(c)-101] = "UP"
    #pause(0.5)
            
        
def ui():
    os.system("cls")
    os.system("echo off")
    global scan
    print()
    print(name.center(cent_width))
    print(email.center(cent_width))
    print ()
    
    if scan == 22:
        print (("<**               >").center(cent_width))
    elif scan == 23 or scan == 21:
        print (("<***              >").center(cent_width))
    elif scan == 24 or scan == 20:
        print (("< ***             >").center(cent_width))
    elif scan == 25 or scan == 19:
        print (("<  ***            >").center(cent_width))
    elif scan == 26 or scan == 18:
        print (("<   ***           >").center(cent_width))
    elif scan == 27 or scan == 17:
        print (("<    ***          >").center(cent_width))
    elif scan == 28 or scan == 16:
        print (("<     ***         >").center(cent_width))
    elif scan == 29 or scan == 15:
        print (("<      ***        >").center(cent_width))
    elif scan == 30 or scan == 14:
        print (("<       ***       >").center(cent_width))
    elif scan == 31 or scan == 13:
        print (("<        ***      >").center(cent_width))
    elif scan == 0 or scan == 12:
        print (("<         ***     >").center(cent_width))
    elif scan == 1 or scan == 11:
        print (("<          ***    >").center(cent_width))
    elif scan == 2 or scan == 10:
        print (("<           ***   >").center(cent_width))
    elif scan == 3 or scan == 9:
        print (("<            ***  >").center(cent_width))
    elif scan == 4 or scan == 8:
        print (("<             *** >").center(cent_width))
    elif scan == 5 or scan == 7:
        print (("<              ***>").center(cent_width))
    elif scan == 6:
        print (("<               **>").center(cent_width))
        
    print ()
    
    for c in camera_list:
        print (("Camera " + str(list_id_no[c]) + ": " + (str(list_ping_read[c]).ljust(4))).center(cent_width))
        

    scan += 1
    if scan == 32:
        scan = 0    

def logo():
    global count_camera
    global list_ping, list_ping_read, lines
    os.system("cls")
    os.system("echo off")
    print()
    print(name.center(cent_width))
    print(email.center(cent_width))
    print ()
    print ("  Current Camera Count: " + str(count_camera))
    option = input("  Camera Count ")
    if option == "":
        count_camera = count_camera
    else:
        count_camera = int(option)
    
    list_ping = [0] * count_camera
    list_ping_read = ["UNK"] * count_camera   
    
    lines = count_camera + 7
    os.system("mode con: cols=" + str(width) + " lines=" + str(lines))

if __name__ == '__main__':
    logo()
    set_id_list()
    while 1 == 1:
        ui()
        ping_all()
        #pause(0.5)

        
    
    