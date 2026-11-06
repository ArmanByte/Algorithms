from random import randint
a = [randint(0,500) for i in range(10)]
print(a)

def buildmax(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
            a = maxheapify(a, i, n)
    return a

def maxheapify(a,i,n):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and a[left] > a[largest]:
            largest = left
    if right < n and a[right] > a[largest]:
            largest = right
    if largest != i:
            a[i],a[largest] = a[largest], a[i]
            a = maxheapify(a, largest, n)
    return a

def heapsort(a):
    n = len(a)
    buildmax(a)
    for i in range(n-1,0,-1):
            a[0],a[i] = a[i], a[0]
            maxheapify(a,0,i)
heapsort(a)
print(a)