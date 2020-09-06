import tkinter
import threading
import gs_VideoWidget
import gs_VideoProcessor
import gs_SymbolDisplay
#import gs_Cryptography
#Video capture code written by Adrian Rosebrock

bottomBarRelH = 0.1

class AppWindow:
    def __init__(self, window, windowTitle):
        #init window
        self.root = window
        self.root.title = windowTitle
        self.root.geometry("1000x600")
        #init components
        self.videoProcessor = gs_VideoProcessor.VideoProcessor(0)
        self.videoWidget = gs_VideoWidget.VideoWidget(self.root, self.videoProcessor, 1 - bottomBarRelH)
        self.symbolDisplay = gs_SymbolDisplay.SymbolDisplay(self.root, bottomBarRelH)
        #init threads
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()

    def update(self):
        while (not self.stopEvent.is_set()):
            self.videoProcessor.refreshFrame()
            #self.videoProcessor.evalLetter()
            self.videoWidget.redraw(self.videoProcessor.currentFrame)
        
    def onClose(self):
        print("Stop")
        self.stopEvent.set()
        self.videoProcessor.rawStream.release()
        self.root.quit()

win = AppWindow(tkinter.Tk(), "CodeTalker")
win.root.mainloop()
win.onClose()