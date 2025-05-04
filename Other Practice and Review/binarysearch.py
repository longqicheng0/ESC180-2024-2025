def bsearch1(L : list, low: int, high: int, x: int):
    
    #base case
    if high >= low:
        mid = (low + high) // 2

        #found it
        if L[mid] == x:
            return mid
        #upper halve
        elif L[mid] < x:
            return bsearch1(L,mid+1,high,x)
        #lower halve
        elif L[mid] > x:
            return bsearch1(L,low,mid-1,x)
    #out of bounds
    else:
        return -1
    
def bsearch2(L,x):
    low = 0
    high = len(L) - 1
    
    while high >= low:
        mid = (low + high)//2

        if L[mid] == x:
            return mid
        elif L[mid] <= x:
            low = mid + 1
        elif L[mid] >= x:
            high = mid - 1
    
    return -1