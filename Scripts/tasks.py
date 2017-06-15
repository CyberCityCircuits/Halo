# -*- coding: utf-8 -*-
'''
Project HALO
Started by David A Ray
DREAM-Enterprise.com

David@DREAM-Enterprise.com
'''


import var, stream

import os, re, sys
import datetime as dt
import cv2, multiprocessing
from time import sleep
from shutil import copyfile
from shutil import rmtree as rm_dir
from pathlib import Path
from bs4 import BeautifulSoup as bs
import lxml.etree as et
import subprocess

#from tkinter import *
from tkinter import messagebox, Label
from tkinter import simpledialog


var.currdate = dt.date.today().strftime("%Y%m%d")
var.currtime = dt.datetime.now().strftime("%H%M%S")


#checks if file exists in var.dir_temp
def chk_file_temp(file_name):
    if not Path(var.dir_temp + "/" + file_name).is_file():
        msg_error("T04: Check Error\nFile Not Found. \n ")   
        
        
def client_exit():
    option = messagebox.askquestion("Exit", "Are You Sure?", icon="question")
    if option =="yes":
        sys.exit()
        

#copy files
def copy(fn1,fn2):
    if os.path.isfile(fn1):
        copyfile(fn1,fn2)
    else:
        msg_error("T03: Copy Error\nFile Doesn't Exit")
    
        
#delete a directory
def delete_dir(dir_name):
    if os.path.exists(dir_name):
        rm_dir(dir_name)
    #else:
    #    msg_error("T01: Delete Error\nDirectory Doesn't Exist")
    
        
#delete file
def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        msg_error("T02: Delete Error\nFile Doesn't Exit")

        
#make directories as needed
def mk_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

        
def mk_log():
    #creates and writes to log file
    f = open(var.dir_temp + "\\" + var.log_name + ".txt","w")
    log_currdate = dt.date.today().strftime("%m/%d/%Y")
    log_currtime = dt.datetime.now().strftime("%H:%M:%S")
    f.write(var.app_name + " V" + var.version + "\n"
            "Starting Date - " + log_currdate + "\n"
            "Starting Time - " + log_currtime + "\n"
            "\n")
    f.close()    
    
    
def msg(text):
    messagebox.showinfo(var.app_name, text)
    
    
def msg_error(text):
    messagebox.showerror(var.app_name, text)

    
#set wait command
def pause(value):
    if value == 0:   #if 0 is entered it creates a press any key prompt.
        os.system("pause")
    elif int(value):
        sleep(value)



def set_date_time():
    var.currdate = dt.date.today().strftime("%Y%m%d")
    var.currtime = dt.datetime.now().strftime("%H%M%S")
    var.currdatetime = var.currdate + "-" + var.currtime
    
#pings all cameras
def ping_all():
    var.list_ping_read = []
    var.list_ping = [0] * var.count_camera
    status = "UNK"
    x = 0
    list_cameras = list(range(var.count_camera))
    for c in list_cameras:
        ping_camera(str(c+1))
    #msg("Ping All Complete")
    
    for i in var.list_ping:
        x += 1
        #print (x)
        if i == (0):
            status = ("DOWN".rjust(6))
        elif i == (1):
            status = ("UP".rjust(6))
        text = ("Camera " + str(x).zfill(3) +": " + status + "\n")
        #print (text)
        var.list_ping_read.append(text)

    #text_ping_read = str(var.list_ping_read)
    #text_ping_read = text_ping_read.replace("'","")
    #msg(text_ping_read)
    
#pings a camera
def ping_camera(camera_id):
    id_no = int(camera_id.zfill(3))+100
    #id_no = int(id_no) + 100
    host = var.ip_s_camera + str(id_no)
    print("Pinging " + host)
    #msg("Pinging " + host)
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        var.list_ping[int(camera_id)-1] = 0
        print (camera_id + " is DOWN")
    else:
        var.list_ping[int(camera_id)-1] = 1
        print (camera_id + " is UP")


def test_cap2():

    ping_all()
    set_date_time()
    var.dir_name = "Images - " + var.currdatetime
    mk_dir(var.dir_name)
    #stream.dir_name = var.dir_name
    for i in range(var.count_camera):
        print(i)
        camera_list = range(var.count_camera)

    for i in camera_list:
        id_no = str(int(str(i).zfill(3))+101)
        var.id_no_list.append(id_no)
        if var.list_ping[i] == 1: 
            print("Initializing VCAP: " + id_no)
            p = multiprocessing.Process(target=stream.init_img_vcap, args=(id_no,))
            p.start()
            
        else:
            print("Skipping: " + id_no)
            
      
    
    
if __name__ == '__main__':
    print ("")
    #test_cap2()