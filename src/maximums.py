def max_of_two(x: float, y: float) -> float:
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        biggest: float = x
    else:
        biggest: float = y
    return biggest


def max_of_three(x: float, y: float, z: float) -> float:
    """Given x, y, and z, that are 3 numbers, return the biggest number of the three."""
    
    biggest: float = x  # Asumimos que x es el mayor inicialmente
    
    if y > biggest:
        biggest = y
    
    if z > biggest:
        biggest = z
    
    return biggest
