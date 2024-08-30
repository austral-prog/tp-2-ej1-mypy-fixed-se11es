def max_of_two(x: float, y: float) -> float:

    if x >= y:
        biggest = x
    else:
        biggest = y
    return biggest

def max_of_three(x: float, y: float, z: float) -> float:

    max_value = x 

    if y > max_value:
        max_value = y
    if z > max_value:
        max_value = z

    return max_value
