'''n=int(input())
a=input().split()
a=[int(i) for i in a]'''

a=[8, 1, 2, 7, 1, 5, 2, 7, 4, 4]

def partition(a, s, e):
        x = a[e]
        i = s - 1
        for j in range(s, e):
            #print(i, j)
            if a[j] <= x:
                i = i + 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[e] = a[e], a[i+1]
        return i + 1

def qsort(a, s, e):
    if s < e:
        p = partition(a, s, e)
        arr_string = ""
        for i in a: 
            arr_string+=str(i)
            arr_string+=" "
        print(arr_string.strip())

        qsort(a, s, p-1)
        qsort(a, p+1, e)
        
qsort(a, 0, 9)
