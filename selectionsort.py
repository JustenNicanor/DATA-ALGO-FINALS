import time

def selection_sort(data, drawData):
    for i in range(0, len(data) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[cur_min_idx]:
                cur_min_idx = j
            drawData(data, ['green' if x == j  + 1 else 'yellow' for x in range(len(data))])
            time.sleep(0.4) 
        data[i], data[cur_min_idx] = data[cur_min_idx], data[i]
    
       
