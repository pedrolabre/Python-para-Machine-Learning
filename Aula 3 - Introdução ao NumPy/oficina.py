import numpy as np
import numpy.ma as ma


visualizacao_stories = np.array([
    [187, 120, 88, 70, 130, 168, 213],
    [0, 0, 42, 0, 0, 55, 77],
    [91, 0, 61, 0, 71, 121, 271],
    [0, 0, 0, 0, 187, 0, 0],
    [42, 23, 34, 0, 39, 29, 36]
])

pessoas = ['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson']
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']


media_visualizacoes_dia = visualizacao_stories.mean(axis=0)

print("Média de visualizações por dia:")

for i in range(len(dias_semana)):
    print(f"{dias_semana[i]}: {media_visualizacoes_dia[i]}")

soma_visualizacoes_dia = visualizacao_stories.sum(axis=0)
indice_dia_mais_visualizacoes = soma_visualizacoes_dia.argmax()

print("\nDia com mais visualizações:")
print(
    f"{dias_semana[indice_dia_mais_visualizacoes]}: "
    f"{soma_visualizacoes_dia[indice_dia_mais_visualizacoes]}"
)

soma_visualizacoes_pessoa = visualizacao_stories.sum(axis=1)
indice_pessoa_mais_visualizacoes = soma_visualizacoes_pessoa.argmax()

print("\nPessoa com mais visualizações:")
print(
    f"{pessoas[indice_pessoa_mais_visualizacoes]}: "
    f"{soma_visualizacoes_pessoa[indice_pessoa_mais_visualizacoes]}"
)

visualizacao_stories_invalidos = np.array([
    [52, 68, 97, 55, -1, 98, -1],
    [53, -1, 38, -1, -1, 72, 49],
    [88, -1, 64, -1, 77, 130, 43],
    [-1, 30, -1, -1, -1, 182, -1],
    [41, 20, 33, -1, 37, 23, 7]
])

visualizacao_stories_mascarados = ma.masked_where(
    visualizacao_stories_invalidos == -1,
    visualizacao_stories_invalidos
)

print("\nDados da segunda semana com valores inválidos mascarados:")
print(visualizacao_stories_mascarados)

visualizacao_stories_duas_semanas = np.array([
    visualizacao_stories,
    visualizacao_stories_invalidos
])

visualizacao_stories_duas_semanas = ma.masked_where(
    visualizacao_stories_duas_semanas == -1,
    visualizacao_stories_duas_semanas
)

visualizacao_stories_por_dia = visualizacao_stories_duas_semanas.reshape((10, 7))

media_visualizacoes_dia_duas_semanas = visualizacao_stories_por_dia.mean(axis=0)

print("\nMédia de visualizações por dia nas duas semanas:")

for i in range(len(dias_semana)):
    print(f"{dias_semana[i]}: {media_visualizacoes_dia_duas_semanas[i]}")


soma_visualizacoes_dia_duas_semanas = visualizacao_stories_por_dia.sum(axis=0)
indice_dia_mais_visualizacoes_duas_semanas = (
    soma_visualizacoes_dia_duas_semanas.argmax()
)

print("\nDia com mais visualizações nas duas semanas:")
print(
    f"{dias_semana[indice_dia_mais_visualizacoes_duas_semanas]}: "
    f"{soma_visualizacoes_dia_duas_semanas[indice_dia_mais_visualizacoes_duas_semanas]}"
)


soma_visualizacoes_pessoa_dia = visualizacao_stories_duas_semanas.sum(axis=0)
soma_visualizacoes_pessoa_duas_semanas = soma_visualizacoes_pessoa_dia.sum(axis=1)
indice_pessoa_mais_visualizacoes_duas_semanas = (
    soma_visualizacoes_pessoa_duas_semanas.argmax()
)

print("\nPessoa com mais visualizações nas duas semanas:")
print(
    f"{pessoas[indice_pessoa_mais_visualizacoes_duas_semanas]}: "
    f"{soma_visualizacoes_pessoa_duas_semanas[indice_pessoa_mais_visualizacoes_duas_semanas]}"
)

input("\nPressione Enter para encerrar...")