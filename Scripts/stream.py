import var

import cv2, sys, os
import numpy as np


stream = "rtsp://192.168.1.101:554/12"


#Start Video Stream
def show_stream(stream_id):
    vcap = cv2.VideoCapture(stream_id)
    while(1):
        ret, frame = vcap.read()
        cv2.imshow('VIDEO', frame)

        #esc keypress closes the process
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    vcap.release()

#Start Video Stream With Centered Dot
def show_stream_dot(stream_id):
    vcap = cv2.VideoCapture(stream_id)
    while(1):
        ret, frame = vcap.read()
        cv2.imshow('VIDEO', frame)

        #esc keypress closes the process
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    vcap.release()
    


#Filter Red
def show_stream_red(stream_id):
    vcap = cv2.VideoCapture(stream_id)

    while(1):
        _, frame = vcap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([30,96,66])
        upper_red = np.array([45,150,100])
        
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)
    
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    
    cv2.destroyAllWindows()
    vcap.release()


#Capture Images From Stream by id_no
def cap_image(id_no):
    
    #check to see if var.dir_name exists.
    dir_name = "Images - " + var.currdatetime
    if not os.path.exists(dir_name):
        print (dir_name + " Doesn't Exists.")
    else:
        print (dir_name + " Exist")

        #Image Camera 101.
        if id_no == ("101"):
            print ("Imaging: " + str(id_no))
            s, im = var.vcap101.read()
            cv2.imwrite(dir_name + "\\" + var.img_name + id_no + "-" + var.currdatetime + ".png",im)
            cv2.waitKey()    
    
        if id_no == ("102"):
            print ("Imaging: " + str(id_no))
            s, im = var.vcap102.read()
            cv2.imwrite((dir_name + "\\" + var.img_name + id_no + "-" + var.currdatetime + ".png"),im)
            cv2.waitKey()    


def init_img_vcap(id_no):
        
    print ("Init VCap: "+ id_no)
    stream_id = "rtsp://192.168.1." + str(id_no) + ":554/11"
    if id_no == str(101):
        print ("Starting VCap: " + id_no)
        var.vcap101 = cv2.VideoCapture(stream_id)
        print (id_no + " - " + var.currdatetime)
        
        
    if id_no == str(102):
        print ("Starting VCap: " + id_no)
        var.vcap102 = cv2.VideoCapture(stream_id)
        print (id_no + " - " + var.currdatetime)
        


def cap_img(id_no):
    print ("Imaging " + id_no)
    if id_no == str(101):
        s, im101 = var.vcap101.read()
        cv2.imwrite("!test1 - " + var.currtime + ".png", im101)
    if id_no == str(102):
        s, im102 = var.vcap102.read()
        cv2.imwrite("!test2 - " + var.currtime + ".png", im102)
        
def start_cap():
    init_img_vcap("101")
    init_img_vcap("102")
    cap_img("101")
    cap_img("102")