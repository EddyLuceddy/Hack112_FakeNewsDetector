#call with big stack to reduce time
# events-example0.py
# Barebones timer, mouse, and keyboard events
# source: https://www.cs.cmu.edu/~112/notes/events-example0.py

from tkinter import *
from PIL import Image, ImageTk
#print("OK")
from main import actualMain, getWebsites
#print("Alright!")
import os
from openURL import openURL

####################################
# customize these functions
####################################
class Button(object):
    def __init__(self, cx, cy, halfWidth, halfHeight, text, 
    color = "white", textColor = "violet"):
        self.cx = cx
        self.cy = cy
        self.halfWidth = halfWidth
        self.halfHeight = halfHeight
        self.text = text
        self.textColor = textColor
    
    def drawButton(self, canvas):
        canvas.create_rectangle(self.cx-self.halfWidth, self.cy-self.halfHeight, 
        self.cx+self.halfWidth, self.cy+self.halfHeight, width = 0, fill = "white")
        canvas.create_text(self.cx, self.cy, text = self.text, font = "TimesNewRoman 24", fill = self.textColor)

    def isButtonPressed(self, event):
        if self.cx-self.halfWidth<=event.x<=self.cx+self.halfWidth and self.cy-self.halfHeight<=event.y<=self.cy+self.halfWidth:
            return True
    
def init(data):
    # load data.xyz as appropriate
    data.windowLocation = (data.width//2, 50)
    data.titleFont = "TimesNewRoman %d" % (data.width//20)
    data.textFont = "TimesNewRoman %d" % (data.width//40)
    data.subtitleFont = "TimesNewRoman %d" % (data.width//30)
    data.timerFiredIn1 = False
    data.mainScreenButton = Button(data.width//2, data.height-100, \
    3*data.width//8, 50, "Analyze News")
    data.outputScreenButton = Button(data.width//2, data.height - 100, 3*data.width//8, 50, "Back to Homepage") 
    # store all images in an images folder
    # data.images is a dictionary of the images with the file name as key
    # use canvas.create_image(x, y, image=data.images[filename], anchor=...)
    data.images = {}
    #imageFiles = os.listdir('images')
    #for file in imageFiles:
    #    try:data.images[file] = Image.open('images/'+file)
    #    except:pass
    data.startScreenTimer = 0
def mousePressed(event, data):
    if data.screenState == 0 and data.mainScreenButton.isButtonPressed(event):
        data.screenState = 1
    elif data.screenState == 2 and data.outputScreenButton.isButtonPressed(event):
        data.screenState = 0
    elif data.screenState == 2:
        return mousePressedLinks(event, data)
    # use event.x and event.y
    pass

def mousePressedLinks(event, data):
    margin = .2*data.width
    linkStart = 130
    indent = 150
    dLinkStart = 80
    #linkStart += dLinkStart
    for i in range(min(len(data.URLs), 3)):
        linkStart += dLinkStart
        if margin<event.x<data.width-margin and linkStart<event.y<linkStart+dLinkStart-5:
            openURL(data.URLs[i])
            return

def keyPressed(canvas, event, data):
    # use event.char and event.keysym
    # DO NOT USE CANVAS
    #print(event.keysym)
    if (event.keysym == "Return" and data.screenState == 1):
        data.screenState += 0.5
        data.URL = data.entry.get()
        data.entry.delete(0, len(data.URL))
    #print(data.screenState)
#    elif data.screenState == 0:
#        data.screenState = 1
#        canvas.delete(ALL)
#        redrawAll(canvas, data)

def timerFired(data):
    if data.screenState == 1:
        data.timerFiredIn1 = True
    if data.screenState == 1.5:
        data.URLs, data.score, data.titles = actualMain(data.URL)
        #loadingScreen(canvas, data)
        #process(data)
        data.screenState += 0.5
    # write timerFired like normal here
        
def process(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "pink", width = 0)
    if data.screenState == 0:
        drawStateZero(canvas, data)
    elif data.screenState == 1:
        canvas.create_window(*data.windowLocation, window = data.entry, anchor=N)
        drawStateOne(canvas, data)
    elif data.screenState == 1.5:
        drawStateOnePointFive(canvas, data)
    elif data.screenState == 2:
        drawStateTwo(canvas, data)
        data.outputScreenButton.drawButton(canvas)
        
def drawStateZero(canvas, data):
    canvas.create_text(data.width//2, 100, text="Fake News Detector",\
    font=data.titleFont, fill = "white")
    canvas.create_rectangle(0, 215, data.width, 315, fill = "white", width = 0)
    canvas.create_text(data.width//2, 250, text="\"Best fake news detector we've ever seen! 5/5\"",\
    font= "TimesNewRoman 20 italic")
    canvas.create_text(data.width - 45, 280, anchor = E, text=" - The New York Times",\
    font= "TimesNewRoman 16")
    data.mainScreenButton.drawButton(canvas)
    
def drawStateOne(canvas, data):
    pos = [*data.windowLocation]
    canvas.create_text(*pos, text="Enter the URL:", anchor=SE)

def drawStateOnePointFive(canvas, data):
    canvas.create_text(data.width//2, data.height//2, text = "Loading...", font = "TimesNewRoman 24", fill = "violet")


def drawStateTwo(canvas, data):
    # barVar is the probability
    barVar = data.score/100
    relatedLinks = data.URLs
    headlines = data.titles
    
    margin = .2*data.width
    barHt = 30
    barY = 30
    width = barVar*(data.width-2*margin)+margin
    px = 1
    
    # create bar
    gradient(canvas, (255,0,0), (0,128,0), margin, 30, \
    data.width-margin, barY+barHt)
    canvas.create_text(width, barY+barHt, anchor=N, text='^', font='Arial 30')
    canvas.create_text(margin, barY+.5*barHt, anchor=E, text="Trash ",\
     font=data.textFont)
    canvas.create_text(data.width-margin, barY+.5*barHt, \
    anchor=W, text="Legitimate", font=data.textFont)
    canvas.create_rectangle(width-px, barY, width+px, barY+barHt, \
    fill="black", width=0)
    
    # make text
    canvas.create_text(data.width//2, barY-.5*barHt, \
    text="Probability that the article is legitimate: %.2f" % barVar, \
    font=data.textFont)
    
    drawLinks(canvas, data, relatedLinks, headlines  )
    
def drawLinks(canvas, data, relatedLinks, headlines):
    margin = .2*data.width
    linkStart = 130
    indent = 150
    dLinkStart = 80
    canvas.create_text(data.width//2 - indent, linkStart, \
    text="Related Links:", anchor=W, font=data.titleFont)
    #linkStart += dLinkStart
    for i in range(min(len(relatedLinks), 3)):
        linkStart += dLinkStart
        canvas.create_rectangle(margin, linkStart, data.width-margin,\
         linkStart+dLinkStart-5, fill='white')
        canvas.create_text(data.width//2, linkStart+.5*dLinkStart, \
        text=headlines[i][:min(len(headlines[i]), 35)]+"...",font=12)


def gradient(canvas, clr1, clr2, x1, y1, x2, y2):
    width = int(x2 - x1 - 1)
    for i in range(width):
        clr = [(i*clr2[j]+(width-i)*clr1[j])//width for j in range(3)]
        canvas.create_rectangle(x1+i, y1, x1+i+1, y2, fill=rgbString(clr), \
        width=0)
    
# converts rgb into hexadecimal
def rgbString(rgb):
    return "#%02x%02x%02x" % (rgb[0], rgb[1], rgb[2])
        
def loadingScreen(canvas, data):
    #canvas.delete(ALL)
    pass
    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    
    
    def mousePressedWrapper(event, canvas, data):
        if data.screenState % 2 == 0:
            mousePressed(event, data)
            redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(canvas, event, data)
        if data.screenState != 1:
            redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        if data.screenState != 1 and not data.timerFiredIn1:
            timerFired(data)
            redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    data.screenState = 0
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    data.entry = Entry(canvas)
    canvas.pack()
    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 700)