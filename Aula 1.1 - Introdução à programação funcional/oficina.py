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


categorias_rock = list(map(categorizar, notas_rock))
categorias_pop = list(map(categorizar, notas_pop))

print("Categorias de Rock:")
print(categorias_rock)

print("\nCategorias de Pop:")
print(categorias_pop)

rock_ruins = list(
    filter(lambda categoria: categoria == "ruim", categorias_rock)
)

rock_medianas = list(
    filter(lambda categoria: categoria == "mediana", categorias_rock)
)

rock_boas = list(
    filter(lambda categoria: categoria == "boa", categorias_rock)
)

pop_ruins = list(
    filter(lambda categoria: categoria == "ruim", categorias_pop)
)

pop_medianas = list(
    filter(lambda categoria: categoria == "mediana", categorias_pop)
)

pop_boas = list(
    filter(lambda categoria: categoria == "boa", categorias_pop)
)

print("\nRock:")
print("Ruins:", rock_ruins)
print("Medianas:", rock_medianas)
print("Boas:", rock_boas)

print("\nPop:")
print("Ruins:", pop_ruins)
print("Medianas:", pop_medianas)
print("Boas:", pop_boas)

input("\nPressione Enter para encerrar...")