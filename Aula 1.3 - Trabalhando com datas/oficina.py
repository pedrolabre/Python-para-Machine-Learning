import locale
from datetime import date, datetime

locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

aniversarios = [
    "01/02/1990",
    "22 de Maio de 1991",
    "04/Abr/1995",
    "1995-Outubro-10",
    "12 Julho 1989",
    "16 de Junho de 1987",
    "04/07/1990"
]

formatos = [
    "%d/%m/%Y",
    "%d de %B de %Y",
    "%d/%b/%Y",
    "%Y-%B-%d",
    "%d %B %Y",
    "%d de %B de %Y",
    "%d/%m/%Y"
]

datas_aniversarios = []

for i in range(len(aniversarios)):
    data = datetime.strptime(aniversarios[i], formatos[i])
    datas_aniversarios.append(data)

print("Aniversários convertidos:")

for data in datas_aniversarios:
    print(data)

aniversarios_ordenados = sorted(
    datas_aniversarios,
    key=lambda data: (data.month, data.day)
)

print("\nAniversários ordenados por mês e dia:")

for data in aniversarios_ordenados:
    print(data)

hoje = date.today()
tem_aniversario = False

for aniversario in aniversarios_ordenados:
    if aniversario.month == hoje.month and aniversario.day == hoje.day:
        tem_aniversario = True

print(f"\nData de hoje: {hoje}")
print(f"Há aniversário hoje? {tem_aniversario}")

if tem_aniversario:
    print(
        hoje.strftime(
            "\nHoje, %A %d de %B de %Y, tem aniversário!"
        )
    )

input("\nPressione Enter para encerrar...")