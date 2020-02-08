import math 
def find_euclidean_distance(x1, y1, x2, y2):
    '''
    (number)->number
    return the euclidean distance between a pair of points
    >>> find_euclidean_distance (3.0, 3.0, 2.0, 5.0)
    >>> find_euclidean_distance (5.0, 2.0, 4.0, 2.0)
    '''
    import math
    a= abs(x2-x1)
    b= abs(y2-y1)
    c= math.sqrt(a**2+b**2)
    return round(c,2)

def is_cow_within_bounds(cow_position,boundary_points):
    '''
    (number)-> number
    Check if the cow is within the bounds or not
    >>> boundary_points = [ [2, 5], [5, 5], [5, 1], [2, 1] ]
    >>> cow_position = [3, 3]
    >>> is_cow_within_bounds(cow_position,boundary_points)
    '''
    x= cow_position[0]
    y= cow_position[1]
    if boundary_points[0][0] <= x and boundary_points[1][0] >= x and boundary_points[2][1] <= y and boundary_points[1][1] >= y:
        return 1
    else:
        return 0
       
def find_cow_distance_to_boundary(cow_position,boundary_point):
    '''
    (number)-> number
    calculate the shortest distance between the cow and the boundary point and round it to two decimal places
    >>> cow_position = [3, 3]
    >>> boundary_point = [3, 3], [2, 5]
    >>> find_cow_distance_to_boundary(cow_position,boundary_point)
    '''
    import math
    a= abs(cow_position[0]-boundary_point[0])
    b= abs(cow_position[1]-boundary_point[1])
    c= math.sqrt(a**2+b**2)
    return round(c,2)
    

def find_time_to_escape(cow_speed,cow_distance):
    '''
    (number)--> number
    return the time it will take for the cow to reach the boundary and round the time to two decimal places
    >>> find_time_to_escape(2.0, 8.0)
    >>> find_time_to_escape(9.0, 111.0)
    ''' 
    if cow_speed > 0 and cow_distance > 0:
        return round(cow_distance/cow_speed, 2)
    elif cow_speed == 0:
        return -1
  
def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    '''
    (number)->number
    test if the cow is within the bound return the time it will take for the cow to travel
    >>> report_cow_status ([3, 3], [4, 4], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    >>> report_cow_status ([0, 0], [3, 7], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    >>> report_cow_status ([0, 0], [3, 3], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    >>> report_cow_status ([3, 3], [3, 6], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    '''
    distance = min(abs(boundary_points[2][0]-cow_position2[0]), abs(boundary_points[3][0]-cow_position2[0]), abs(boundary_points[2][1]-cow_position2[1]), abs(boundary_points[1][1]-cow_position2[1]))
    a= abs(cow_position2[0]-boundary_points[0][0])
    b= abs(cow_position2[1]-boundary_points[0][1])
    c= math.sqrt(a**2+b**2)
    if is_cow_within_bounds(cow_position1,boundary_points) == 1 and is_cow_within_bounds(cow_position2,boundary_points) == 1:
       return round(distance/ (find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1])/delta_t),2)
    elif is_cow_within_bounds(cow_position1,boundary_points) == 0 and is_cow_within_bounds(cow_position2,boundary_points) == 0:
        return round(c/(find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1])/delta_t),2)
    elif is_cow_within_bounds(cow_position1,boundary_points) == 0 and is_cow_within_bounds(cow_position2,boundary_points) == 1:
        return -1
    else:
        return 0



