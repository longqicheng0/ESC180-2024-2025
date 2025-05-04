import numpy as np

#def print_matrix(M_lol):
    #matrix_array = np.array(M_lol)
    #print(matrix_array)
    
def test_infinite_loop(input_string):
    if input_string == "Calculus":
        print("inf")
        while True:  # Infinite loop
            pass
    else:
        return "pass"

def get_lead_ind(row):
    for i in range (len(row)):
        if row[i] != 0:
            return i
    return len(row)

def get_row_to_swap(M, start_i):
    refIDX = get_lead_ind(M[start_i])
    res = []
    
    for i in range(start_i,len(M)):
        leadingIDX = get_lead_ind(M[i])
        diff = leadingIDX - refIDX
        res.append(diff)

    return start_i + res.index(min(res))

def add_rows_coefs(r1, c1, r2, c2):
    if len(r1) != len(r2):
        return
    
    res = [0] * len(r1)
    
    for i in range(len(r1)):
        res[i] = c1 * r1[i] + c2 * r2[i]
        
    return res

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        target_value = M[i][best_lead_ind]
        
        if target_value != 0:
            # tv != M[r][b]
            row_factor = target_value / M[row_to_sub][best_lead_ind]
            
            M[i] = add_rows_coefs(M[row_to_sub], -row_factor, M[i], 1.0)
    
    return M
   
def print_matrix(M):
    for row in M:
        print(row)
    print()
     
def forward_step(M):
    for i in range(len(M)):
        row_to_swap = get_row_to_swap(M,i)
        
        
        if row_to_swap != i:
            print(f"Swapping row {i} with row {row_to_swap}")
            M[i],M[row_to_swap] = M[row_to_swap],M[i]
            print("Matrix after swapping")
            print_matrix(M)
        
        best_lead_ind = get_lead_ind(M[i])
        if best_lead_ind < len(M[0]):
            print(f"Eliminating entries below row {i} in column {best_lead_ind}")
            eliminate(M,i,best_lead_ind)
            print("Matrix after elimination:")
            print_matrix(M)
            
    return M

def backward_step(M):
    """Applies the backward step of Gaussian Elimination to matrix M in place."""
    num_rows = len(M)
    for i in range(num_rows - 1, -1, -1):
        # Find the pivot in the current row
        lead_index = get_lead_ind(M[i])
        
        if lead_index >= len(M[i]):
            continue

        pivot_value = M[i][lead_index]
        M[i] = [x/pivot_value for x in M[i]] #make the pivot 1
        print(f"Normalizing row {i} to make pivot 1 at column {lead_index}")
        print_matrix(M)
        
        # col
        for j in range(i - 1, -1, -1):
            target_value = M[j][lead_index]
            if target_value != 0:
                print(f"Eliminating entry in row {j}, column {lead_index} using row {i}")
                M[j] = add_rows_coefs(M[i], -target_value, M[j], 1.0)
                print_matrix(M)
    
    print("backward step complete:")
    print_matrix(M)
    return M
        
        
    


'''        
# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
print(M)

#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)        

print(M)
print(b)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist() 
'''

#print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]
#print_matrix(M)
#test_infinite_loop("Calculus")
M=[[0, 0, 1, 0, 2], [1, 0, 2, 3, 4], [3, 0, 4, 2, 1],[1, 0, 1, 1, 2]]
#M = [[1,-2,3,22],[3,10,1,314],[1,5,3,92]]
print_matrix(M)
print(forward_step(M))
#backward_step(M)