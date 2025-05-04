def duplicates(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False

def repeated_order():
    print("wuo")
    user = input().lower()
    print(user)
    cnt = 0
    print(cnt)
    while user != "pumpkin spice latte":
        cnt += 1
        print("wuo")
        user = input().lower()
    print(cnt)
    
def matrix_sum(A, B):
    # Check if dimensions match
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "ERROR"
    
    # Initialize result matrix with the same dimensions as A and B
    res = []
    for row in range(len(A)):
        res.append([0] * len(A[0]))
    
    print(res)

    # Add the elements of matrices A and B
    for row in range(len(A)):
        for col in range(len(A[0])):
            res[row][col] = A[row][col] + B[row][col]
    
    return res
    
if __name__ == '__main__':
    print(duplicates([1,0,0]))
    #repeated_order()
    A = [[5, 0, 0], [0, 0, 1]]
    B = [[1, 2, 3], [4, 5, 6]]

    result = matrix_sum(A, B)
    print(result)
    
    s = "acbd"
    print(s)
    sorted(s)
    print(s)
    
    L = [1, [2, 3], 4 ]
    L1 = L[:]
    print(L1)
    L[0] = 7
    L[1][0] = 8
    L1[1][1] = 9
    print(L)
    print(L1)