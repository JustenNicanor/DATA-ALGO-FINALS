import time

def partition(data, head, tail, drawData):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(0.5)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(0.5)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(0.5)

    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(0.5)

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawData):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData)

        quick_sort(data, head, partitionIdx-1, drawData)

        quick_sort(data, partitionIdx+1, tail, drawData)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('grey')
        else:
            colorArray.append('yellow')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'orange'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray