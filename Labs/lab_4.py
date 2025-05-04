

#3-------------------
temp = 0

for i in range (501):
    temp += i

print (temp)

#4-------------------
temp2 = 0

while i < 501:
    temp2 += i
    i += 1

print (temp2)

def gcd(n,m):
    v = min(n,m)
    div = 1
    
    for i in range (v):
        if n % i == 0 and m % i == 0:
            div = i
    
    return (div)

def gcd2(n,m):
    v = min(n,m)
    i = v
    
    while i > 0:
        if n % i == 0 and m % i == 0:
            return i
        i -= 1

def simplify_fraction(n,m):
    if m/gcd2(n,m) == 1:
        return "the most simplified fraction is: " + n/gcd2(n,m) + "/" + m
    return"the most simplified fraction is: " + n/gcd2(n,m) + "/" + m/gcd2(n,m)

import math 

def pi(n):
    app = 0.0
    tidx = 0
    factor = 10 ** n
    
    while True:
        t = (-tidx ** n) /(2 * n + 1) 
        app += t
        
        temp = 4 * app
        
        if int(temp * factor) == (math.pi * factor):
            return tidx + 1 
        
    tidx += 1
    
    
def leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
def daysInMonth(y,m):
    if m == 2:
        if leap(y):
            return 29
        else:
            return 28
    elif m in [4,6,9,11]:
        return 30
    return 31   
def next_day(y,m,d):
    temp = daysInMonth(y,m)
    if d < temp:
        return (y,m,d+1)
    else:
        if d == 12:
            return (y+1,1,1)
        return(y,m+1,1)
        
def step(y1, m1, d1, y2, m2, d2):
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        if m1 == m2:
            return d1 < d2
    return False
 
def days_between(fY, fM, fD, tY, tM, tD):
    # Initialize the count of days
    cnt = 0
    
    # Count the number of next_day calls needed to reach the target date
    while step(fY,fM,fD,tY,tM,tD):
        fY,fM,fD = next_day(fY,fM,fD)
        cnt += 1
    
    return cnt

def sum_nums(L):
  for num in L:
    s += num
    return s
def count_evens(L):
    cnt = 0
    for num in L:
        if num % 2 == 0: 
            cnt += 1  
    return cnt

def list_to_str(lis):
    if len(lis) == 0:
        return "[]"
    
    result = "["
    for i in range(len(lis)):
        result += str(lis[i])
        
        if i != len(lis) - 1:
            result += ", "
    result += "]"
    
    return result

def lists_are_the_same(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:  
            return False
    return True

def match_pattern(list1, list2):
    if len(list2) == 0:
        return True
    
    for i in range(len(list1) - len(list2) + 1):
        match = True
        for j in range(len(list2)):
            if list1[i + j] != list2[j]:
                match = False
                break
        if match:
            return True
    return False

def list1_starts_with_list2(l1,l2):
    if l1<l2:
        return False
    
    for i in range(len(l2)):
        if l1[i] != l2[i]:
            return False
    return True


def duplicates(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i + 1]:
            return True 
    
    return False
        
        
    
    
