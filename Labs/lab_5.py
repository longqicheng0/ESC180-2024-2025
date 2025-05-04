import random
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

def list1_starts_with_list2(l1,l2):
    if l1<l2:
        return False
    
    for i in range(len(l2)):
        if l1[i] != l2[i]:
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

def duplicates(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i + 1]:
            return True 
    
    return False

def ins_V(x,i):
    if len(x) < 5 or len(t) != len(x):
        return 
    
    v = []
    
    for i in range(2,len(x)-4):
        temp1 = (x[i+1] - x[i-1])/0.2
        temp2 = (x[i+2] - x[i-2])/0.4
        avrtemp = (temp1+temp2)/2
        v.append(avrtemp)
        
    return v

def ins_V_noise(t,x):
    if len(x) < 5 or len(t) != len(x):
        return 
    
    v_org = []
    v = []
    for i in range(len(t)):
        t[i] = t[i]+0.1*random.random()
        x[i] = i[i]+0.1*random.random()
    for i in range(len(x)-1):
        temp = (x[i+1] - x[i])/(t[i])
        v_org.append(temp)
    for i in range(2,len(x)-4):
        temp1 = (x[i+1] - x[i-1])/(t[i+1] - t[i-1])
        temp2 = (x[i+2] - x[i-2])/(t[i+2] - t[i-2])
        avrtemp = (temp1+temp2)/2
        v.append(avrtemp)
        
    return v,v_org
    
    
    

if __name__ == '__main__':
    print(match_pattern([1,2,3,4,5,6,7,8,9,10],[7,8,9,10]))