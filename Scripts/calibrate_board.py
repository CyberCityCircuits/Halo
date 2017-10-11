import cv2
import os, subprocess
import datetime as dt
#from time import sleep
import glob
import numpy as np

#IP Camera Information
scheme = "192.168.1."
stream = "12"

#Checkboard Inside Corner Dimensions
row = 6
col = 9

currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M%S")
currdatetime = currdate + "-" + currtime   

dir_name = "Images"

camera_id = input("Camera to Calibrate: (1-40): ")
camera_id = int(camera_id)
    
#Start Video Stream
def image(id):
    global wdir_name
    print ("Use the OpenCV checker board image.")
    print ("The more pictures you take the better.")
    print ("Space Bar = Takes Picture")
    print ("Escape = Ends Process")
    
    currdate = dt.date.today().strftime("%Y%m%d")
    currtime = dt.datetime.now().strftime("%H%M%S")
    currdatetime = currdate + "-" + currtime 
    
    wdir_name = str(id+100) + " - " + dir_name + "-" + currdatetime #working directory

    if not os.path.exists(wdir_name):
        os.makedirs(wdir_name)
    
    
    x=0
    id_no = id+100
    host = scheme + str(id_no)
    
    
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        host_conn = 0
        print ("Camera "+id_no+" Unreachable")
        
    else:
        host_conn = 1

    if host_conn == 1:    
        cap = cv2.VideoCapture("rtsp://"+host+":554/"+stream)  
        
        while(1):
            ret, frame = cap.read()
            cv2.imshow('VIDEO', frame)
    
            #esc keypress closes the process
            k = cv2.waitKey(5) & 0xFF
            if k == 27: #esc key ends process
                break
            elif k == 32: #space bar takes picture
                currdate = dt.date.today().strftime("%Y%m%d")
                currtime = dt.datetime.now().strftime("%H%M%S-%f")[:-3]
                currdatetime = currdate + "-" + currtime        
                cv2.imwrite(wdir_name+"\\"+str(id_no)+"-"+currdatetime+" - Image"+".png", frame)
        
                x += 1                
                print ("Image Count: "+str(x))
            
        
    cv2.destroyAllWindows()
    cap.release()  
    
def calibrate():
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((col*row,3), np.float32)
    objp[:,:2] = np.mgrid[0:col,0:row].T.reshape(-1,2)
    
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    
    #finds images
    images = glob.glob(wdir_name+"\\"+'*.png')
    
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (col,row),None)
    
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
    
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners2)
    
            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (col,row), corners2,ret)
            cv2.imshow('calibrate',img)
            cv2.waitKey(500)
            print ("Collecting Data: "+fname)
    
    print ("Data Capture Complete...  Start Processing...")
    cv2.destroyAllWindows()
    
    
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    

    lst_file = []
    lst_count = []
    
    for file in os.listdir(wdir_name):
        
        #print (file)
        lst_file.append(file)
        
    count = range(len(lst_file))
    
    for i in count:
        lst_count.append(i)
    
    x=0    
    for file in lst_file:
        if not file.endswith('.py'):
       
            img = cv2.imread(wdir_name+"\\"+file)
            h,  w = img.shape[:2]
            newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
            
            # undistort
            dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
            
            # crop the image
            x,y,w,h = roi
            dst = dst[y:y+h, x:x+w]
            cv2.imwrite(wdir_name+"\\"+"Cal - "+file,dst)
        
    mean_error = 0
    tot_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        #print (error)
        tot_error += error
        #print (tot_error)
        #print ("Current Mean Error: "+str(i)+" - "+str(tot_error/i))
    
    mean_error = tot_error/len(objpoints)    
    print ("The total error should be close to zero.")
    print ("total Error: ", mean_error)    

if __name__ =="__main__":
    image(camera_id)
    calibrate()    
    