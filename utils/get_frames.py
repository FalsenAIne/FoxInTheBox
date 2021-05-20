import os
import cv2
from pathlib import Path
from PIL import Image

path = "../data/action_720p.mp4"
cap = cv2.VideoCapture(path)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
lst_frames = []
for i in range(length):
    ret, frame = cap.read()
    if i % 100 == 0:
        lst_frames.append(frame)

path_data = Path('../dataset')

if not os.path.exists(path_data):
    os.mkdir(path_data)

frames_cnt = 0
for f in lst_frames:
    num = "frame{0}.jpg".format(frames_cnt)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    f = Image.fromarray(f)
    if not os.path.exists((path_data/num).__str__()):
        f.save((path_data/num).__str__())

    frames_cnt += 1
