

def p1(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 99:
                return i, j

def lookup(L,num):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == num:
                return i, j
            

def p2(L):
    global res
    
    res = []
    for i in range(len(L)):
        for j in range(len(L[i])): 
           if type(L[i][j]) == int:
               res.append(L[i][j])
    
    return res


#HOPFIELD NETWORK
def print_all_energies(w01, w02, w12):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print("x: (", x0, x1, x2, ")", "E:", E(x0, x1, x2, w01, w02, w12))

def adjust_weights(x0, x1, x2, w01, w02, w12):
    if x0 * x1 > 0:
        w01 += 0.1
    else:
        w01 -= 0.1
    
    if x0 * x2 > 0:
        w02 += 0.1
    else:
        w02 -= 0.1
    
    if x1 * x2 > 0:
        w12 += 0.1
    else:
        w12 -= 0.1
        
    return w01,w12,w02

def E(x0, x1, x2, w01, w02, w12):
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    return -(term1 + term2 + term3)

def adjust_weights_iterations(x0,x1,x2,w01,w02,w12,it):
    for i in range (it):
        print(f"\nIteration {i+1}")
        print("====================")
        
        w01,w02,w12 = adjust_weights(x0, x1, x2, w01, w02, w12)
        
        print_all_energies(w01,w02,w12)
        
    return w01,w02,w12
    
if __name__ == '__main__':
    L = [["CIV", 92],
     ["180", 98],
     ["103", 99],
     ["194", 95]]
    
    print(p1(L))
    print(p2(L))
    
    w01 = 2
    w02 = -1
    w12 = 1
    print_all_energies(w01, w02, w12)
    
    print(adjust_weights_iterations(1,-1,1,w01,w02,w12,4))
    
    
    #4a - since the value returned in function E is negative, bigger term 1 smaller return value
