def sum_array(arr):
    if arr == None:
        return 0
    elif arr == []:
        return 0
    arr_min = min(arr)
    arr_max = max(arr)
    sum = 0
    if arr.count(arr_min) > 1:
        sum += arr_min
    elif arr.count(arr_max) > 1:
        sum += arr_max
    for i in range(len(arr)):
        if arr[i] == arr_min:
            sum += 0
        elif arr[i] == arr_max:
            sum += 0
        else:
            sum += arr[i]
    return sum
if __name__=="__main__":
    print(sum_array([6, 0, 1, 10, 10]))