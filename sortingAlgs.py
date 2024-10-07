from tkinter import *
from tkinter import ttk
import random
import time

def bubble_sort(data, timeTick):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            drawBubbleSortComparison(data, j, j + 1, i, timeTick)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawBubbleSortSwap(data, j, j + 1, i, timeTick)
        drawCorrectPositionGreaterEqualThanOuterLoop(data, i, timeTick)

def selection_sort(data, timeTick):
    for i in range(len(data)):
        minIndex = i
        drawSelectionSortCompletedSection(data, i, timeTick)
        for j in range(i + 1, len(data)):
            drawSelectionSortIter(data, i, j, minIndex, timeTick)
            if data[j] < data[minIndex]:
                minIndex = j
        data[i], data[minIndex] = data[minIndex], data[i]
        drawSelectionSortSwap(data, i, minIndex, timeTick)

def merge_sort(data, timeTick):
    merge_sort_alg(data, 0, len(data) - 1, timeTick)

def merge_sort_alg(data, left, right, timeTick):
    if left < right:
        drawSplit(data, left, right, timeTick)
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, timeTick)
        merge_sort_alg(data, middle + 1, right, timeTick)
        merge(data, left, middle, right, timeTick)

def merge(data, left, middle, right, timeTick):
    drawMergeStart(data, left, middle, right, timeTick)
    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    drawSwapMerge(data, left, right, timeTick)

########################################################################################################################
### Bubble Sort Drawing Methods ########################################################################################

def drawBubbleSortComparison(data, pos1, pos2, outerLoopIndex, timeTick):
    """Method that should be called after each iteration of the INNER loop to show the comparison between two elements 
    in pos1 and pos2. This will highlight the elements being compared in gray

    Args:
        data (int[])
        pos1 (int): The position of the first element being compared
        pos2 (int): The position of the second element being compared
        outerLoopIndex (int): The current index of the outer loop
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['slategrey' if x == pos1 or x == pos2 else 'green' 
                  if x > len(data) - outerLoopIndex - 1 else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)
    
def drawBubbleSortSwap(data, pos1, pos2, outerLoopIndex, timeTick):
    """Method that should be called after two elements are swapped in pos1 and pos2. 
    This will highlight the elements in blue

    Args:
        data (int[])
        pos1 (int): The position of the first element being swapped
        pos2 (int): The position of the second element being swapped
        outerLoopIndex (int): The current index of the outer loop
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['blue' if x == pos1 or x == pos2 else 'green' 
                  if x > len(data) - outerLoopIndex - 1 else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

def drawCorrectPositionGreaterEqualThanOuterLoop(data, outerLoopIndex, timeTick):
    """Method that should be called at each iteration of the OUTER loop to which elements are in the correct position

    Args:
        data (int[])
        outerLoopIndex (int): The current index of the outer loop
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['green' if x >= len(data) - outerLoopIndex - 1 else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

########################################################################################################################
### Selection Sort Drawing Methods #####################################################################################

def drawSelectionSortCompletedSection(data, index, timeTick):
    """Method that should be called at each iteration of the OUTER loop to show the completed section of the array

    Args:
        data (int[])
        index (int): outer loop index
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['green' if x < index else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

def drawSelectionSortIter(data, outerLoopIndex, innerLoopIndex, minIndex, timeTick):
    """Method that should be called after each iteration of the INNER loop to show the comparison between two elements

    Args:
        data (int[])
        outerLoopIndex (int): outer loop index
        innerLoopIndex (int): inner loop index
        minIndex (int): smallest element index
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['green' if x < outerLoopIndex else 'lightskyblue' if x == outerLoopIndex else 'slategrey' if x == innerLoopIndex else 'cornflowerblue' if x == minIndex else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)
    
def drawSelectionSortSwap(data, outerLoopIndex, minIndex, timeTick):
    """Method that should be called after the smallest element is found and swapped with the outer loop index

    Args:
        data (int[])
        outerLoopIndex (int): outer loop index
        minIndex (int): smallest element index
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    if outerLoopIndex != minIndex:
        colorArray = ['blue' if x == outerLoopIndex or x == minIndex else 'green' if x < outerLoopIndex else 'red' for x in range(len(data))]
        drawData(data, colorArray, timeTick)

########################################################################################################################
### Merge Sort Drawing Methods #########################################################################################

def drawSplit(data, left, right, timeTick):
    """Method that should be called to visualise the splting the data array into a left and right part

    Args:
        data (int[])
        left (int): left index of data
        right (int): right index of data
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['slategrey' if left <= x <= right else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

def drawMergeStart(data, left, middle, right, timeTick):
    """Method that should be called before the merge process to visualise the left and right part of the section being merged

    Args:
        data (int[])
        left (int): left index of data
        middle (int): middle index of data
        right (int): right index of data
        timeTick (_type_): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['cornflowerblue' if left <= x < middle + 1 else 'lightsteelblue' if middle + 1 <= x <= right else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

def drawSwapMerge(data, left, right, timeTick):
    """Method that should be called after the merge process to visualise the merged section

    Args:
        data (int[])
        left (double): left index of data
        right (double): right index of data
        timeTick (double): The time delay between each iteration of the algorithm as defined on the UI
    """
    colorArray = ['blue' if left <= x <= right else 'red' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

########################################################################################################################
### Other Methods ######################################################################################################

def drawComplete(data, timeTick):
    colorArray = ['green' for x in range(len(data))]
    drawData(data, colorArray, timeTick)

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')
#variables
selected_alg = StringVar()
data = []

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
    global generateButton

    generateButton['state'] = 'disabled'
    if algMenu.get() == 'Bubble Sort':
        bubble_sort(data, speedScale.get())
    elif algMenu.get() == 'Selection Sort':
        selection_sort(data, speedScale.get())
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, speedScale.get())

    if isSorted(data):
        drawComplete(data, speedScale.get())
    else:
        drawData(data, ['red' for x in range(len(data))], 0.1)

    generateButton['state'] = 'normal'

def isSorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Selection Sort', 'Merge Sort'])
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

generateButton = Button(UI_frame, text="Generate", command=generate, bg='white')
generateButton.grid(row=1, column=3, padx=5, pady=5)

root.mainloop()

