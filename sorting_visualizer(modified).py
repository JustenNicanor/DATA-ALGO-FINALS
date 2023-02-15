from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('SORTING ALGORITHM VISUALIZATION')
root.maxsize(980, 680)
root.config(bg='black')

selected_alg = StringVar()
 
def Generate():
    print('Alg Selected: ' + selected_alg.get())

UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = Canvas(root, width=600, height = 380, bg='white')
canvas.grid(row=1, column = 0, padx = 10, pady = 5)

Label (UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable= selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx= 5, pady=5)
algMenu.current(0)
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=7, padx=5, pady=5)

Label (UI_frame, text="Min Value: ", bg='grey').grid(row=0, column=3, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=0, column = 4, padx=5, pady=5, sticky=W)

Label (UI_frame, text="Max Value: ", bg='grey').grid(row=0, column=5, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=0, column = 6 , padx=5, pady=5, sticky=W)

root.mainloop()