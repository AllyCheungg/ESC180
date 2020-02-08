def vector_from_points(p1, p2):
    '''
    (list)--> list
    Return a list of n components, where n is an integ
    >>>vector_from_points([0, 0], [1, 2])
    [1, 2]
    >>>vector_from_points([3, -1, 0], [10, 0, 1])
    [7, 1, 1]
    '''
    new_vector = []
    for i in range( len(p1) ):
        new_vector.append( p2[i]-p1[i] )
    print(new_vector)

def vector_length(v):
    '''
    (list)--> float
    Return a floating-point value indicating the magnitude of an n-element vector
    >>>vector_length([2, 1])
    2.23606797749979
    >>>vector_length([])
    -1
    '''
    element_len=[]
    for i in range( len(v) ):
        element_len.append( v[i] ** 2 )
    import math
    if len(v) == 0:
        return -1
    else:
        return math.sqrt(sum(element_len))

def angle_between(v, w):
    '''
    (list)--> float
    Return the angle, in degrees, between two vectors.
    >>>angle_between([-1], [2])
    180.0
    >>>angle_between([0, 1, 0, 1], [1, 3, 4, 5])
    37.61611202673532
    '''
    import math
    return math.degrees(math.acos((dot_product(v,w))/(vector_length(v)*vector_length(w))))
    
def dot_product(v,w):
    '''
    (list)--> number
    Return the dot product of two vectors.
    >>>dot_product( [-1], [2])
    -2
    >>>dot_product( [0, 1, 0, 1], [1, 3, 4, 5])
    8
    >>>dot_product([0, 0], [0, 0])
    0
    '''
    product = 0
    for i in range( len(v) ):
        product += (v[i]*w[i])
    return product
    
def unit_vector(v):
    '''
    (list)-->list
    return an n-element list that represents a unit vector in the same direction as c
    >>>unit_vector([2, 1])
    [0.8944271909999159, 0.4472135954999579]
    >>>unit_vector([])
    []
    '''
    component=[]
    for i in range( len(v) ):
        component += [1/vector_length(v)*v[i]]
    return component

def cross_product(v,w):
    '''
    Return the cross product of a 3-element list
    >>>cross_product([], [2])
    [0, 0, 0]
    >>>cross_product([2, 8], [1, 4, 3])
    [24, -6, 0]
    >>>cross_product([1, 1, 1], [5.5, 5.5, 5.5])
    [0.0, -0.0, 0.0]
    >>>cross_product( [1, 1, 1, 0], [1, 5.5])
    []
    '''
    from itertools import repeat
    if len(v) > 3 or len(w) > 3:
        return []
    if len(v) < 3:
        v.extend(repeat(0, 3-len(v)))
    if len(w) < 3:
        w.extend(repeat(0, 3-len(w)))

    product=[(v[1]*w[2])-(v[2]*w[1]),-v[0]*w[2]+v[2]*w[0],(v[0]*w[1])-(v[1]*w[0])]
    return product

def scalar_projection(v,w):
    '''
    Return the scalar projection w onto v
    >>> scalar_projection([-2], [1.5])
    -1.5
    >>> scalar_projection([0, 3], [1.5, 2])
    2.0
    '''
    return dot_product(v,w)/abs(vector_length(v))

def vector_projection(v,w):
    '''
    Return vector projection w onto v
    >>> vector_projection([-2], [1.5])
    [1.5]
    >>> vector_projection([0, 3], [1.5, 2])
    [0.0, 2.0]
    '''
    new_vector = []
    c=  dot_product(v,w)/(vector_length(v)**2)
    for i in range( len(v) ):
       new_vector += [c*v[i]]
    return new_vector

if __name__ == "__main__":
    # test your vector operations here
    v1 = [0, -2, 3]
    v2 = [1, 1, 1]
                                                         
