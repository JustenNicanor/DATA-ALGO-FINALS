import time

def insertion_sort(data, drawData):
    for index in range(1, len(data)):
        value = data[index]
        i = index - 1
        while  i >= 0:
            if value < data[i]:
                data [i + 1] = data [i]
                data[i] = value
                i = i - 1
            else:
                break
            drawData(data, ['green' if x == i + 1 else 'yellow' for x in range(len(data))])
            time.sleep(0.2)
        