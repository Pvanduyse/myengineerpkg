import numpy as np
import math

def norm(VEC):
    square = 0
    for n in VEC:
        square  = square + n**2
    return np.sqrt(square)

def point_line_distance(P,R):
    R_M = R(1)-R(0)
    return norm(cross_product(P-R(0), R_M))/norm(R_M)

def cross_product(VEC_1, VEC_2):
    if(VEC_1.size == 2):
        if(VEC_2.size != 2):
            print("cross_product: The two vectors must be of the same dimensions")
            return
        results = np.zeros(2)
        results[0] = VEC_1[1]-VEC_2[1]
        results[1] = VEC_2[0]-VEC_1[0]
        return results
    elif(VEC_1.size == 3):
        if(VEC_2.size != 3):
            print("cross_product: The two vectors must be of the same dimensions")
            return
        results = np.zeros(3)
        results[0] = (VEC_1[1]*VEC_2[2] - VEC_1[2]*VEC_2[1])
        results[1] = -1 * (VEC_1[0]*VEC_2[2] - VEC_1[2]*VEC_2[0])
        results[2] = (VEC_1[0]*VEC_2[1] - VEC_1[1]*VEC_2[0])
        return results
    else:
        print("cross_product: The first vector is of the wrong dimensions")
        
def dot_product(VEC_1, VEC_2):
    if(VEC_1.size != VEC_2.size):
        print("dot_product: The two vectors must have the same dimensions")
        return
    total = 0
    for i in range(VEC_1.size):
        total = total + VEC_1[i]*VEC_2[i]
    return total