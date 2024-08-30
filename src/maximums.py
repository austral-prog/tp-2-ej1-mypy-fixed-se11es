def max_of_two(x: int, y: int) -> int:
    if x >= y:
        biggest: int = x
    else:
        biggest: int = y
    return biggest



def max_of_three(x: int, y: int, z: int) -> int:
    if x >= y and x >= z:
        biggest: int = x
    elif y >= z:
        biggest: int = y
    else:
        biggest: int = z
    return biggest
