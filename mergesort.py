import time

def merge_sort(data, drawData):
    merge_sort_alg(data,0, len(data)-1, drawData)


def merge_sort_alg(data, left, right, drawData):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData)
        merge_sort_alg(data, middle+1, right, drawData)
        merge(data, left, middle, right, drawData)

def merge(data, left, middle, right, drawData):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(0.5)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
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
    
    drawData(data, ["green" if x >= left and x <= right else "yellow" for x in range(len(data))])
    time.sleep(0.5)

def getColorArray(lenght, left, middle, right):
    colorArray = []

    for i in range(lenght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("purple")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("yellow")

    return colorArray