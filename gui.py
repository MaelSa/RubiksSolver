from tkinter import *


class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

    def init_window(self):

        self.master.title("Rubik's solver")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit", command = self.quit)

        # placing the button on my window
        quitButton.place(x=0, y=0)
    def quit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
app.init_window()
root.mainloop()
