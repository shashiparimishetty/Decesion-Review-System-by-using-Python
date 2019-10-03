import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time


stream = cv2.VideoCapture('video.mp4')
def play(speed):
    print(f'Speed of play is {speed}')
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)

    grabbed,frame = stream.read()
    # frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread('ds.png'),cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. wait for 1 second
    time.sleep(1)
    # 3. Display sponsor image.
    frame = cv2.cvtColor(cv2.imread('sponsor.jpg'),cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 4. wait for 1.5 second
    time.sleep(1.5)
    # 5. Display out/notout images
    if decision == 'out':
        decisionImg = 'out.png'
    else:
        decisionImg = 'notout.png'
    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target = pending, args = ('out',))
    thread.daemon = 1
    thread.start()
    print('batsman is out')

def not_out():
    thread = threading.Thread(target = pending, args = ('notout',))
    thread.daemon = 1
    thread.start()
    print('batsman is not out')
#width and height of our main screen
SET_WIDTH = 600
SET_HEIGHT = 400

#TKinter gui starts here
window = tkinter.Tk()
window.title('Decision Review System')
cv_img = cv2.cvtColor(cv2.imread("drs.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho = tkinter.NW, image = photo)
canvas.pack()

#including buttons
btn = tkinter.Button(window, text = '<< previous(fast)', width = 50, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text = '<< previous(slow)', width = 50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text = 'Next(fast) >>', width = 50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text = ' Next(slow)>>', width = 50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text = ' Give Out', width = 50, command = out)
btn.pack()

btn = tkinter.Button(window, text = 'Give Notout', width = 50, command = not_out)
btn.pack()

window.mainloop()
