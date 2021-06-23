#quick_sort3.py

a=[8, 1, 2, 7, 1, 5, 2, 7, 4, 4]
def qSort(a, low, high):
    if low >= high:
        return 

    j=high-2
    i=low

    piv=a[j+1]

    found_swap=False
    while j>i+2:
        if a[i] <= piv: 
            i=i+1    
        
        if a[i] > piv:
            found_swap=False
            while not found_swap:
                if a[j] > piv: 
                    j=j-1
                elif a[j] <= piv: 
                    found_swap=True
                    a[i], a[j] = a[j], a[i]
                    i=i+1
                    j=j-1

    a[i+1], a[high-1] = a[high-1], a[i+1]

    print(a)
    
    qSort(a, low, i+1)
    qSort(a, i+high-2, high)

qSort(a, 0, 10)
