import tkinter

class SymbolDisplay:
    def __init__(self, master, relativeHeight):
        #initialize the container for all non-video controls
        self.master = master
        self.container = tkinter.Frame(master)
        self.relativeHeight = relativeHeight
        self.container.place(relx = 0, rely = 1 - self.relativeHeight)
        self.container.place(relwidth = 1, relheight = self.relativeHeight)
        #initialize the components of the symbol display
        #first, whether or not the user wants to encrypt/decrypt
        self.encDecContainer = tkinter.Frame(self.container)
        self.encDecContainer.place(relx = 0.8, rely = 0, relwidth = 0.2, relheight = 1)
        self.encDecVar = tkinter.IntVar()
        self.encryptRadio = tkinter.Radiobutton(self.encDecContainer)
        self.encryptRadio.configure(text = "Encrypt", variable = self.encDecVar, value = 1)
        self.encryptRadio.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)
        self.decryptRadio = tkinter.Radiobutton(self.encDecContainer)
        self.decryptRadio.configure(text = "Decrypt", variable = self.encDecVar, value = 2)
        self.decryptRadio.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)
        self.encryptRadio.select()
        #then, the boxes for password & message
        self.inputContainer = tkinter.Frame(self.container)
        self.inputContainer.place(relx = 0.2, rely = 0, relwidth = 0.6, relheight = 1)
        self.messageVar = tkinter.StringVar()
        self.passwordVar = tkinter.StringVar()
        self.messageLabel = tkinter.Label(self.inputContainer, text="Message")
        self.messageLabel.place(relx = 0, rely = 0, relwidth = 0.2, relheight = 0.5)
        self.messageField = tkinter.Entry(self.inputContainer)
        self.messageField.place(relx = 0.2, rely = 0, relwidth = 0.8, relheight = 0.5)
        self.passwordLabel = tkinter.Label(self.inputContainer, text="Password")
        self.passwordLabel.place(relx = 0, rely = 0.5, relwidth = 0.2, relheight = 0.5)
        self.passwordField = tkinter.Entry(self.inputContainer)
        self.passwordField.place(relx = 0.2, rely = 0.5, relwidth = 0.8, relheight = 0.5)
        #finally, the field for the letter that the user is signing
        self.gestureContainer = tkinter.Frame(self.container)
        self.gestureContainer.place(relx = 0, rely = 0, relwidth = 0.2, relheight = 1)
        self.currentGestureVar = tkinter.StringVar()
        self.currentGesture = tkinter.Label(self.gestureContainer, textvariable = self.currentGestureVar)
        self.currentGesture.place(relx = 0, rely = 0.4, relwidth = 1, relheight = 0.6)
        self.isInputtedVar = tkinter.BooleanVar(False)
        self.isInputted = tkinter.Label(self.gestureContainer, textvariable = self.isInputtedVar)
        self.isInputted.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.4)
        
        self.currentGestureVar.set("AAA")
        self.isInputtedVar.set(False)
        
    