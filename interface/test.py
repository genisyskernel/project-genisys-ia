import tkinter as Tkinter

root = Tkinter.Tk()
photo = Tkinter.PhotoImage(file = "../resources/images_gui/genisys_init.gif")
imagefilename = "../resources/images_gui/genisys_init.gif"
frame2 = Tkinter.PhotoImage(file=imagefilename, format="gif -index 2")
frame3 = Tkinter.PhotoImage(file=imagefilename, format="gif -index 3")
frame4 = Tkinter.PhotoImage(file=imagefilename, format="gif -index 4")
label = Tkinter.Label(image = frame2)

label.pack()
root.mainloop()
label.configure(image=frame3)
label.configure(image=frame4)

