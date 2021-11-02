import tkinter as tk
import cv2 as cv
import pyautogui
import numpy as np
import time

# getting the screen dimentions using the tkiner library inbiult
tk = tk.Tk()
screen_size = (tk.winfo_screenwidth(), tk.winfo_screenheight())
file_name = 'video.avi'
stopping_time = time.time()+360


# initializing the screen recording:
video = cv.VideoWriter(file_name, cv.VideoWriter_fourcc(*'XVID'), 20.0, screen_size)
while True:
    screen_shot = pyautogui.screenshot()#capturing the screenshots
    frame = np.array(screen_shot) # converting the screen shots to a numpy array
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #converting the frame to the normal colour scheme of rgb(red, green, blue)
    video.write(frame) # saving the recording into the file

    # breaking out of the loop when the intended time is hit
    if time.time() > stopping_time :
        break

cv.destroyAllWindows()# destroy all windows that are open
video.release()#ensure that there is no recording
