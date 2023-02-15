from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort


root = Tk()
root.title('SORTING ALGORITHM VISUALIZATION')
root.maxsize(980, 680)
root.config(bg='white')

selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizeData = [i / max(data) for i in data]
    for i, height in enumerate(normalizeData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340

        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()



def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(20)

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, ['yellow' for x in range(len(data))])
   
def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData)
        drawData(data, ['green' for x in range(len(data))])

    elif  algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData)

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData)
        drawData(data, ['green' for x in range(len(data))])


    


UI_frame = Frame(root, width= 700, height=200, bg='light grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

canvas = Canvas(root, width=600, height = 380, bg='white')
canvas.grid(row=1, column = 0, padx = 10, pady = 10)

Label (UI_frame, text="ALGORITHM:", bg='light grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable= selected_alg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx= 0, pady=5)
algMenu.current(0)
Button(UI_frame, text="START", command=StartAlgorithm, bg='light green').grid(row=0, column=8, padx=10, pady=5)


minEntry = Scale(UI_frame, from_=1, to=25, resolution=1, orient=HORIZONTAL, label="LOWEST NUM", bg='red')
minEntry.grid(row=0, column = 4, padx=10, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="HIGHEST NUM", bg = 'orange')
maxEntry.grid(row=0, column = 6 , padx=10, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='light blue').grid(row=0, column=7, padx=10, pady=5)
root.mainloop()