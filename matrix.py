import linear_algebra as lin
import numpy as np
import math

def apply(MATRIX, FUNCTION):
    dim = dimensions(MATRIX)
    print("dim =",dim)
    result = np.zeros(dim)
    for i in range(dim[0]):
        for j in range(dim[1]):
            result[i][j] = FUNCTION(MATRIX[i][j])
    return result

def identity(dim):
    result = np.zeros((dim,dim))
    for i in range(dim):
        result[i][i] = 1
    return result

def dimensions(MATRIX):
    return (len(MATRIX), len(MATRIX[0]))

def transpose(MATRIX):
    dim = dimensions(MATRIX)
    dim = (dim[1],dim[0])
    result = np.zeros(dim)
    for m in range(dim[0]):
        for n in range(dim[1]):
            result[m][n] = MATRIX[n][m]
    return result

def multiply(MTX0,MTX1):
    if (dimensions(MTX0)[1] != dimensions(MTX1)[0]):
        print("matrix.multiply: These two matrices are not multipliable")
        return
    dim = (dimensions(MTX0)[0],dimensions(MTX1)[1])
    result = np.zeros(dim)
    for m in range(dim[0]):
        for n in range(dim[1]):
            result[m][n] = lin.dot_product(MTX0[m,:],MTX1[:,n])
    return result

def submatrix(MATRIX, OMIT):
    dim = dimensions(MATRIX)[0]-1
    offset = []
    for i in range(dim+1):
        if(i != OMIT[0]):
            for j in range(dim+1):
                if(j != OMIT[1]):
                    offset.append((i,j))
    result = np.zeros((dim, dim))
    for i in range(offset.__len__()):
        offsetted_index = offset[i]
        result[math.trunc(i/dim)][i%dim] = MATRIX[offsetted_index[0]][offsetted_index[1]]
    return result

def determinant(MATRIX):
    dim = dimensions(MATRIX)[0]
    if(dim == 1):
        return MATRIX[0][0]
    total = 0
    for i in range(0,dim):
        total = total + (-1)**(i) * MATRIX[i][0]*determinant(submatrix(MATRIX,(i,0)))
    return total

def inverse(MATRIX):
    dim = dimensions(MATRIX)
    if(dim[0] != dim[1]):
        print("matrix.inverse: square matrix required")
        return
    dim = dim[0]
    combined = np.zeros((dim,dim*2))
    combined[:,range(dim)] = MATRIX
    combined[:,range(dim, dim*2)] = identity(dim)
    mult = 1
    
    # SWAP: FIRST & SECOND
    # combined[[0, 1], :] = combined[[1, 0], :]
    
    # ADD/SUBTRACT: FIRST = FIRST + 2*SECOND
    # combined[0,:] = combined[0,:] + 2*combined[1,:]
    
    # MULTIPLY/DIVIDE FIRST = FIRST/5
    # combined[0,:] = combined[0,:]/5
    
    for i in range(dim):
        # Swap rows if pivot is empty
        if(combined[i,i] == 0):
            for j in range(i+1, dim):
                if(combined[j,i] != 0):
                    combined[[i, j], :] = combined[[j, i], :]
                    mult = mult*-1
                    break
            if(combined[i][i] == 0):
                # If there is no valid pivot value, return
                return None
        
        # use row division/multiplication to set the pivot to 1
        mult = mult*combined[i,i]
        combined[i,:] = combined[i,:]/combined[i,i]
        for j in range(i+1, dim):
            # eliminate all entries below the pivot
            combined[j,:] = combined[j,:] - combined[i,:] * (combined[j,i]/combined[i,i])
    
    # eliminate all entries above the reduced pivots
    for i in range(dim-1, 0, -1):
        for j in range(dim-2, -1, -1):
            combined[j,:] = combined[j,:] - combined[i,:] * (combined[j,i]/combined[i,i])
    
    return combined[:,range(dim,dim*2)], mult