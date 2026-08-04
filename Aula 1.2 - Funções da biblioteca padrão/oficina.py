import re


registros_log = """2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida"""

padrao_erros = (
    r"\d{4}-\d{2}-\d{2} "
    r"\d{2}:\d{2}:\d{2},\d{3} "
    r"\| ERROR -> .+"
)

erros_encontrados = re.findall(padrao_erros, registros_log)

print("Quantidade de erros encontrados:", len(erros_encontrados))

print("\nHorários em que ocorreram erros:")

horarios_dos_erros = []

for erro in erros_encontrados:
    horario_encontrado = re.search(r"\d{2}:", erro)
    horario = horario_encontrado.group(0)
    horarios_dos_erros.append(horario)
    print(horario)

print("\nQuantidade de erros por horário:")

horarios_contabilizados = []

for horario in horarios_dos_erros:
    if horario not in horarios_contabilizados:
        quantidade = horarios_dos_erros.count(horario)
        print(horario, "-", quantidade, "erro(s)")
        horarios_contabilizados.append(horario)

maior_quantidade = 0
horarios_com_mais_erros = []

for horario in horarios_contabilizados:
    quantidade = horarios_dos_erros.count(horario)

    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        horarios_com_mais_erros = [horario]
    elif quantidade == maior_quantidade:
        horarios_com_mais_erros.append(horario)

print("\nHorário(s) com mais erros:")

for horario in horarios_com_mais_erros:
    print(horario, "-", maior_quantidade, "erro(s)")

input("\nPressione Enter para encerrar...")