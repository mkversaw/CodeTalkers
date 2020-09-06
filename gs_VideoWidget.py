import gs_VideoProcessor
import tkinter
import cv2

# VideoWidget creates the widget that displays the camera stream

class VideoWidget:
    
    def __init__(self, master, videoProcessor, relativeHeight):
        #init basic details about the widget, as well as the video processor that it displays
        self.master = master    #parent window
        self.relativeHeight = relativeHeight
        self.vidProcessor = videoProcessor  #processor to pull frames from
        self.videoLabel = tkinter.Label(master)     #create the actual label/widget itself
        self.videoLabel.place(relx = 0, rely = 0)
        self.videoLabel.place(relwidth = 1, relheight = self.relativeHeight)     #adjust widget to correct position
        
    def redraw(self, inputFrame):
        #get camera data and convert to tkinter-readable format after resizing to fit window
        height, width, depth = inputFrame.shape
        resizeFactorX = self.videoLabel.winfo_width() / width
        resizeFactorY = self.videoLabel.winfo_height() / height     #get how much each axis has to be resized
        resizeFactorActual = min(resizeFactorX, resizeFactorY)  #pick the min so that the vidstream isn't too big
        resizeDimensions = (int(resizeFactorActual * width), int(resizeFactorActual * height))
        resizedFrame = cv2.resize(inputFrame, resizeDimensions) #resize, then convert
        convertedFrame = gs_VideoProcessor.convertToTK(resizedFrame)
        #then redraw the widget
        self.videoLabel.configure(image = convertedFrame)
        self.videoLabel.image = convertedFrame