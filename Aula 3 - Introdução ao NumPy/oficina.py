import numpy as np


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

input("\nPressione Enter para encerrar...")