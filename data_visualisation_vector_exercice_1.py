import math
from typing import List

Vector = List[float]

def add(v,w):
    """Add  the following elements"""
    # Vector should have the same lenght
    assert len(v) == len(w)
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def substract(v,w):
    """Substract following elements"""
    # Validation of vector lenght
    assert len(v)==len(w)
    return [v_i - w_i for v_i,w_i in zip(v,w)]

def scalar_multiply(c:float,v:Vector) -> Vector:
    "Multiply each element by c"
    return [c*v_i for v_i in v]

def vector_sum(vectors:List[Vector]) -> Vector:
    """Add  all the elements"""
    # None vector given
    assert vectors , "None Vector"
    num_elments = len(vectors[0])
    # All vectors needs to be the same size
    assert all(len(v) == num_elments for v in vectors),"Vectors have diffrents size" 
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elments)]

def vector_mean(vectors:List[Vector])-> Vector:
    """Barycenter of the vector element"""
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v:Vector,w:Vector)->float:
    """Calculate v_1*w_1"""
    assert len(v) == len(w),"The vector should have the same size"
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v:Vector)-> float:
    """Return v_1*v_1 +...+v_n*v_n"""
    return dot(v,v)

def magnitude(v:Vector)->float:
    """Magnitude or pythagore theoreme"""
    return math.sqrt(sum_of_squares(v))

def squared_distance(v:Vector,w:Vector)->float:
    """Calculate (v_1-w_1)**2+...+(v_n - w_n)**2"""
    return sum_of_squares(substract(v,w))

def distance(v:Vector,w:Vector)->float:
    return math.sqrt(squared_distance(v,w))
     



assert scalar_multiply(2,[1,2,3]) == [2,4,6]

assert add([1,2,3],[4,5,6]) == [5,7,9]
assert substract([5,7,9],[4,5,6])== [1,2,3]
assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]
assert vector_mean([[1,2],[3,4],[5,6]])==[3,4]
assert dot([1,2,3], [4,5,6])==32
assert sum_of_squares([1,2,3]) ==14
assert magnitude([3,4])==5


