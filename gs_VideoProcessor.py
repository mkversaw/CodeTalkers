import cv2
from PIL import Image, ImageTk

# VideoProcessor handles the video stream, as well as the functions for gesture recognition

class VideoProcessor:
    
    def __init__(self, source):
        self.rawStream = cv2.VideoCapture(source)   #video source (webcam)
        if((self.rawStream is None) or (not self.rawStream.isOpened())):
            raise IOError("No webcam detected")
        self.currentFrame = None    #the current frame that the webcam sees
        
    def refreshFrame(self):     #refreshes currentFrame from video source
        streamIsActive, receivedFrame = self.rawStream.read() #get frame, check if there's input
        if streamIsActive and not (receivedFrame is None):
            self.currentFrame = receivedFrame   #assign to currentFrame if valid
        
def evalLetter(inputFrame):     #evaluate what letter that the hand gesture in inputFrame is
    return #letter

#this function could be nice for display purposes, but kinda ignores the theme
#def getLabeledFrame(inputFrame):    #marks the fingers visible in the frame (primarily for the video widget)
#    return #frame w/ fingers marked
    
def convertToTK(frameRaw):      #converts the raw frame given (openCV-readable) to a tk-friendly format
    frameRecolored = cv2.cvtColor(frameRaw, cv2.COLOR_BGR2RGB)  #recolor
    framePIL = Image.fromarray(frameRecolored)  #convert to PIL-readable
    frameDisplayed = ImageTk.PhotoImage(framePIL)   #convert to tk-friendly
    return frameDisplayed
