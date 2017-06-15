   # -*- coding: utf-8 -*-
'''
Project HALO
Started by David A Ray
DREAM-Enterprise.com

David@DREAM-Enterprise.com
'''


import var, tasks

import os, sys
import datetime as dt
from pathlib import Path
#from bs4 import BeautifulSoup as bs
#import lxml.etree as et

#from tkinter import *
from tkinter import Menu, Frame, BOTH, W
from tkinter import Tk, Label, messagebox
from tkinter import simpledialog


#set varibles:

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        
        
        self.init_window()
        

    def init_window(self):
        self.master.title(var.name)
        
        topbar = Menu(self.master)
        self.master.config(menu=topbar)
        
        file_menu = Menu(topbar)
        option_menu = Menu(topbar)
        #camera_menu = Menu(topbar)
        tools_menu = Menu(topbar)
        help_menu = Menu(topbar)
        
        file_menu.add_command(label="Exit", command=tasks.client_exit)
        topbar.add_cascade(label="File", menu=file_menu)

        
        option_menu.add_command(label ="Set Camera Count", 
                                command=set_camera_count)
        topbar.add_cascade(label="Options", menu=option_menu)
        
        
        tools_menu.add_command(label ="Check Camera Connectivity", 
                               command=run_ping_all)
        tools_menu.add_command(label="Open Camera Views")
        tools_menu.add_command(label="Center Cameras")
        topbar.add_cascade(label="Tools", menu=tools_menu)
        
        
        help_menu.add_command(label="Overview", command=funct_not_supp)
        help_menu.add_command(label="About", command=show_about)
        topbar.add_cascade(label="Help", menu=help_menu)
        
def funct_not_supp():
    msg_error("Function Not Yet Supported")
    
def msg(text):
    messagebox.showinfo(var.app_name, text)
    
def msg_error(text):
    messagebox.showerror(var.app_name, text)

#command for help > about
def show_about():
    msg(var.name + "\n"
        "Build: " + var.build + "\n\n"
        "By David Ray \n"
        "\n" + var.email + "\n\n"
        "www.DREAM-Enterprise.com")
    
    
def run_ping_all():
    global cam_grid
    tasks.ping_all()
    
    if var.cam_grid_bit == 1:
        reset_grid(cam_grid)
        var.cam_grid_bit = 0
    
    for i, txt in enumerate(var.list_ping_read):
        cam_grid = Label(root, text=txt)
        row, col = divmod(i, 2)
        cam_grid.grid(row=row+1, column=col, sticky=W)
        var.cam_grid_bit = 1
        print (cam_grid.grid_slaves())
    #tasks.msg(var.list_ping_read)
    
    
def reset_grid(label):
    print (root.grid_size())
    #for i in label.grid_slaves(label, row=0, column=1):
    label.destroy()

        
def set_camera_count():
    cnt = simpledialog.askinteger(var.name, 
     "Current Setting: " + str(var.count_camera) + 
     "\n How many cameras are connected?")
    var.count_camera = cnt
                
root = Tk()

#cam_grid = Label(root)

w = var.width # width for the Tk root
h = var.lines #height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/4) - (w/2)
y = (hs/2.5) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


    
app = Window(root)    

root.mainloop()

     