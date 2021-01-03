def find_max_idx(arr):
    for idx, val in enumerate(arr):
        if arr[idx+1] < val:
            return val

arr = [0, 1, 50, 100, 90]

print(find_max_idx(arr))
