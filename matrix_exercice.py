from typing import Tuple
from typing import List
from typing import Callable

Matrix = List[List[float]]
Vector = List[float]
def shape(A:Matrix) -> Tuple[int,int]:
    """Returns (number of lines A, number of columns B)"""
    num_rows = len(A)
    # Count the elments of the first line
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1,2,3],[4,5,6]]) == (2,3)

# Matrix is not n*n but n*k
def get_row(A:Matrix,i:int)-> Vector:
    """Return the line of the matrix as a vector"""
    return A[i]

def get_column(A:Matrix, j:int)->Vector:
    """Return j line as vector"""
    return [A_i[j]
        for A_i in A]

def make_matrix(num_rows : int, num_cols:int,entry_fn:Callable[[int,int],float])-> Matrix:
    """Returns one matrix with n rows and k column"""
    return [[entry_fn(i,j) 
        for j in range(num_cols)]
        for i in range(num_rows)] # list for any i

def identity_matrix(n:int)->Matrix:
    """Return matrix n*n"""
    return make_matrix(n,n,lambda i,j:1 if i == j else 0)

assert identity_matrix(5)== [[1,0,0,0,0],
                             [0,1,0,0,0],
                             [0,0,1,0,0],
                             [0,0,0,1,0],
                             [0,0,0,0,1]]




