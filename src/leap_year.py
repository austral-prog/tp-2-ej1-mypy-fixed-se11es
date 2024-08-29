def is_leap_year() -> bool:
    year: int = int(input("Ingrese un año: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        es_bisiesto: bool = True
    else:
        es_bisiesto: bool = False
    print(f"El año {year} es {'bisiesto' if es_bisiesto else 'no bisiesto'}")
    return es_bisiesto
