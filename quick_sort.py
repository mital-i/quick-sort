#quick sort
n=int(input())
a=input().split()
a = [int(i) for i in a]

def done_sort(a): 
    for i in range(1, len(a)): 
        if a[i] < a[i-1]: 
            return False
    
    return True

def qsort(a): 
    j=len(a)-1
    i=0
    piv=a[j]
    found_swap=False
    while j>i:
        if a[i] < piv: 
            i=i+1    
        if a[i] > piv:
            while not found_swap:
                if a[j] > piv: 
                    j=j-1
                elif a[j] < piv: 
                    found_swap=True
                    a[i], a[j] = a[j], a[i]
    return a
    
print(qsort(a))
