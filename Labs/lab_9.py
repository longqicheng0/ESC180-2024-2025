def binary_search(L, e):
    cnt = 0
    low = 0
    high = len(L)-1
    while high-low >= 2:
        mid = (low+high)//2 #e.g. 7//2 == 3
        if L[mid] > e:
            high = mid-1
            cnt += 1
        elif L[mid] < e:
            low = mid+1
            cnt += 1
        else:
            cnt += 1
            return mid, cnt
    if L[low] == e:
        return low, cnt+1
    elif L[high] == e:
        return high, cnt+1
    else:
        return None,cnt+1
    
#reg
L = [1,3,5,7,9,11,13]
e = 3
print(binary_search(L,e))
L = [1,3,5,7,9,11,13]
e = 5
print(binary_search(L,e))
#worst cases

#edge cases
L = [1,3,5,7,9,11,13]
e = 1
print(binary_search(L,e))
#mid+1
L = [1,3,5,7,9,11,13]
e = 9
print(binary_search(L,e))
#none
L = [1,3,5,7,9,11,13]
e = 2
print(binary_search(L,e))