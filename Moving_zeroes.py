def move_zeroes(n):
    arr = [1,0]*n
    write = 0

    for i in arr:
        if i:
            arr[write] = i
            write+= 1
    arr[write:] = [0]*(len(arr) - write)
    return arr

a = int(input('Enter number: '))
print('Sorted array:',move_zeroes(a))