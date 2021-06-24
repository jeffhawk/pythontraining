'''from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="Hello World")
        self.msg.pack ()
        self.bye = Button (self, text="Bye", command=self.quit)
        self.bye.pack ()
        self.pack()

app = Application()

mainloop()
'''
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

print(__name__)
root = tk.Tk()
app = Application(master=root)
app.mainloop()
print(__name__)

'''from tkinter import Tk, Label, Button, StringVar

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()'''


from pubsub import pub
import tkinter as Tk
########################################################################
class OtherFrame(Tk.Toplevel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("otherFrame")
        
        # create the button
        btn = Tk.Button(self, text="Close", command=self.onClose)
        btn.pack()
        
    #----------------------------------------------------------------------
    def onClose(self):
        """
        closes the frame and sends a message to the main frame
        """
        self.destroy()
        pub.sendMessage("otherFrameClosed", arg1="data")
    
########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
                
        btn = Tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()
        
        pub.subscribe(self.listener, "otherFrameClosed")
        
    #----------------------------------------------------------------------
    def listener(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()
        
    #----------------------------------------------------------------------
    def hide(self):
        """
        hides main frame
        """
        self.root.withdraw()
        
    #----------------------------------------------------------------------
    def openFrame(self):
        """
        opens other frame and hides main frame
        """
        self.hide()
        subFrame = OtherFrame()
            
    #----------------------------------------------------------------------
    def show(self):
        """
        shows main frame
        """
        self.root.update()
        self.root.deiconify()
        
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()