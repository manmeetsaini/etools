from tkinter import *
from tkinter import ttk
from etools import *

def calculate(*args):
    try:
        pass
def test():
    print ("yeah!!!")
root = Tk()
# Title of the Window
root.title("Py SSH")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

ip = ""
user = ""
password = ""


# Entry Field in UI
feet_entry = ttk.Entry(mainframe, width=16, textvariable=ip)
feet_entry.grid(column=2, row=2, sticky=(W, E))

feet_entry = ttk.Entry(mainframe, width=16, textvariable=user)
feet_entry.grid(column=2, row=3, sticky=(W, E))

feet_entry = ttk.Entry(mainframe, width=16, textvariable=password)
feet_entry.grid(column=2, row=4, sticky=(W, E))

#To Print result in UI 
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=6, sticky=(W, E))

#To Create Button
ttk.Button(mainframe, text="Connect", command=test).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="Disconnect", command=calculate).grid(column=3, row=5, sticky=W)

#Labels in UI
ttk.Label(mainframe, text="=======SSH=======").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="IP Address").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="User").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Password").grid(column=1, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
