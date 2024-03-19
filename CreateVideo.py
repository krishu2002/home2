import os
import cv2
S = "C:/Users/lenovo/OneDrive/Desktop/problem statements/image prosesing/PRO-105-Reference-Code-Student-Activity-main/img"
images = []
for i in os.listdir(S):
    name,ext = os.path.splitext(i)
    if ext in [".gif",".png",".jpg",".jpeg",".jfif"] :
        filename = S + "/" + i
        images.append(filename)
count = len(images)
frame = cv2.imread(images[0])
H,W,Channel = frame.shape
size = (W,H)
out = cv2.VideoWriter("test.mp4",cv2.VideoWriter_fourcc(*"DIVX"),10,size)
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("done")