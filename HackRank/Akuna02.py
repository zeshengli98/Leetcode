## alternating prime sequence
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

## find if arr is alternating prime sequence
def minPenalty(arr):
    prime = []
    non_prime = []
    for n in arr:
        if isPrime(n):
            prime.append(n)
        else:
            non_prime.append(n)

    print(prime,non_prime)

    if abs(len(prime)-len(non_prime))<=1:
        return 0
    else:
        if len(prime)>len(non_prime):
            return min(prime)
        else:
            return min(non_prime)






if __name__ == '__main__':
    arr = [7,10,5,3,10,1,4,8]
    result = minPenalty(arr)
    print(result)