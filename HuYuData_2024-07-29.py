def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初始化间隔

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # 减少间隔
    return arr


def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初始化间隔

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # 减少间隔
    return arr


def sort_subarrays(arr):
    # 对每个子数组进行希尔排序
    for i in range(len(arr)):
        arr[i] = shell_sort(arr[i])

    # 按排序后子数组的第一个元素进行排序
    arr.sort(key=lambda x: x[0])
    return arr


# 测试
arr = [
    [5, 2, 9, 1],
    [10, 4, 7, 6],
    [3, 8, 2, 11, 15, 1],
    [20, 0, 18]
]

sorted_arr = sort_subarrays(arr)
print(sorted_arr)