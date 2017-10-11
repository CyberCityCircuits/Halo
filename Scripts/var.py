# -*- coding: utf-8 -*-
'''
Project HALO
Started by David A Ray
DREAM-Enterprise.com

David@DREAM-Enterprise.com
'''

import os
import datetime as dt

#set varibales
app_name = "HALO"
ver = "0.01.00"
build = "03180217"

name = app_name + " V" + ver
email = "David@DREAM-Enterprise.com"

currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M%S")
currdatetime = currdate + "-" + currtime


#set system varibles
width = 300
lines = 300

os_name = os.name

cam_grid_bit = 0
count_camera = 5

dir_name = "Images - " + currdatetime
img_name = "IMG-"
id_no_list = []
ip_s_camera = "192.168.1."

list_ping = [0] * count_camera
list_ping_read = []            

ping = 0

stream = "rtsp://192.168.1.101:554/12"

vcap101 = vcap102 = vcap103 = vcap104 = vcap105 = ""
vcap_list = []
