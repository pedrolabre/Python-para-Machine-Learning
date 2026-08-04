notas_rock = [
    5, 1, 4, 0, 2, 5, 2, 1, 0, 5,
    5, 3, 5, 2, 5, 5, 3, 5, 4, 4
]

notas_pop = [
    3, 2, 5, 1, 2, 1, 4, 1, 5, 0,
    4, 2, 1, 2, 5, 2, 4, 4, 0, 1
]

def categorizar(nota):
    if 0 <= nota <= 1:
        return "ruim"
    elif 2 <= nota <= 3:
        return "mediana"
    elif 4 <= nota <= 5:
        return "boa"


print(categorizar(1))
print(categorizar(3))
print(categorizar(5))

input ("\nPressione Enter para encerrar...")