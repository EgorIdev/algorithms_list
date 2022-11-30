# Наибольший общий делитель

def gcd(a, b):  # Методом деления
    while b > 0:
        c = a % b
        a = b
        b = c
    return a


def gcd(a, b):  # Методом вычитания
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
