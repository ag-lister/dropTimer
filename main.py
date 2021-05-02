from tkinter import *
import time


class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Black", font=("Helvetica", 45))
        self.label.grid(column=0, row=0)
        self.update_clock()
        self.update_background()

    def update_clock(self):
        now = time.strftime("%I:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

    def update_background(self):

        minute = time.strftime("%M")

        if minute == "6" or minute == "21" or minute == "36" or minute == "51":
            root.configure(bg='blue')
        elif minute == "7" or minute == "22" or minute == "37" or minute == "52":
            root.configure(bg='red')
        else:
            root.configure(bg='#F0F0F0')

        self.after(1000, self.update_background)


root = Tk()
app = App(root)
root.wm_title("Tkinter clock")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.attributes('-fullscreen', True)
root.after(1000, app.update_clock)
root.after(1000, app.update_background)
root.mainloop()
