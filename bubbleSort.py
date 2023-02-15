import time

def bubble_sort(data, drawData):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                drawData(data, ['green' if x == j + 1 else 'yellow' for x in range(len(data))])
                time.sleep(0.5)
    drawData(data,  ['green' for x in range(len(data))])
    

