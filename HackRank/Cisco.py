## alternating prime sequence
def meanandmode(arr):
    arr = sorted(arr)
    n = len(arr)
    mean = sum(arr)/n
    mode = arr[0]
    count = 1
    max_count = 1
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            count = 1
        if count>max_count:
            max_count = count
            mode = arr[i]
    return mean, mode

def countofBitssets(n):
    #convert to binary
    bin_n = bin(n)
    print()



if __name__ == '__main__':
    arr = [1,2,3,4,2,2]
    result = meanandmode(arr)
    print(result)