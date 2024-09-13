from tkinter import *
from tkinter import ttk
import random
import time

def bubble_sort(data, timeTick):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            drawComparison(data, j, j + 1, i, timeTick)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawSwap(data, j, j + 1, i, timeTick)
        drawCorrectPositionGreaterEqualThanOuterLoop(data, i, timeTick)

def drawComparison(data, pos1, pos2, outerLoopIndex, timeTick):
    colorArray = ['slategrey' if x == pos1 or x == pos2 else 'green' if x > len(data) - outerLoopIndex - 1 else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)
    
def drawSwap(data, pos1, pos2, outerLoopIndex, timeTick):
    colorArray = ['blue' if x == pos1 or x == pos2 else 'green' if x > len(data) - outerLoopIndex - 1 else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

def drawCorrectPositionGreaterEqualThanOuterLoop(data, outerLoopIndex, timeTick):
    colorArray = ['green' if x >= len(data) - outerLoopIndex - 1 else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')
#variables
selected_alg = StringVar()
data = []

#function
def drawData(data, colorArray, timeTick):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * (c_height - 40)
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update()
    time.sleep(timeTick)

def generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))], 0.1) #['red', 'red' ,....]

def StartAlgorithm():
    global data
    bubble_sort(data, speedScale.get())

#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()