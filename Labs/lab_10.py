#base case: 0

def power(x,n):
    if n == 0:
        return 1
    if x == 0:
        return 0
    
    return x * power(x,n-1)

#power(2,3):
#2*power(2,2)
#2*2*power(2,1)
#2*2*2*power(2,0)
#2*2*2*1

def sum_digit(x):
    if x / 10 < 1:
        return x
    return(x % 10 + sum_digit(x // 10))

print(sum_digit(123))

def get_splitted(x,start,end):
    return x[start:end]
def split_list(x,y):
    index_of_boundries = [-1]
    for i in range(len(y)):
        index_of_boundries.append(x.index(y[i]))
        
    index_of_boundries.sort()
    index_of_boundries.append(len(x))
    #now split
    print(index_of_boundries)
    res = []
    for j in range(1,len(index_of_boundries)):
        res.append(get_splitted(x,index_of_boundries[j-1] + 1,index_of_boundries[j]))
    return res
        
if __name__ == '__main__':
    x = [1, 2, 6, 4, 5, 3, 7,8]
    y = [3,6]
    print(split_list(x,y))