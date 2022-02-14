import datetime

import cv2
import numpy as np
from PIL import ImageGrab
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
heigth = GetSystemMetrics(1)
print(width,heigth)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
print(time_stamp)
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
captured_video = cv2.VideoWriter(file_name,fourcc,20.0,(width,heigth))

while True:
    img = ImageGrab.grab(bbox=(0 ,0 ,width, heigth))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Piyush Project',img_final)
    captured_video.write(img_final)
    if cv2.waitKey(15) == ord('p'):
        break


