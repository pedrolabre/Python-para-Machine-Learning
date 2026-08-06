import random

def identificar_jogada_mais_usada(historico):
    quantidade_pedra = 0
    quantidade_papel = 0
    quantidade_tesoura = 0

    for jogada in historico:
        if jogada == "Pedra":
            quantidade_pedra += 1
        elif jogada == "Papel":
            quantidade_papel += 1
        else:
            quantidade_tesoura += 1

    if quantidade_pedra >= quantidade_papel and quantidade_pedra >= quantidade_tesoura:
        return "Pedra"
    elif quantidade_papel >= quantidade_pedra and quantidade_papel >= quantidade_tesoura:
        return "Papel"
    else:
        return "Tesoura"

opcoes = ["Pedra", "Papel", "Tesoura"]
historico_jogadas = []

while True:
    print("\nEscolha uma opção (1, 2, 3 ou 4):")
    print("1-Pedra")
    print("2-Papel")
    print("3-Tesoura")
    print("4-Sair")

    escolha_jogador = input()

    if escolha_jogador == "4":
        print("\nJogo encerrado.")
        break
    elif escolha_jogador == "1" or escolha_jogador == "2" or escolha_jogador == "3":
        if escolha_jogador == "1":
            jogada_jogador = "Pedra"
        elif escolha_jogador == "2":
            jogada_jogador = "Papel"
        else:
            jogada_jogador = "Tesoura"

        if len(historico_jogadas) < 5:
            jogada_maquina = random.choice(opcoes)
        else:
            jogada_mais_usada = identificar_jogada_mais_usada(historico_jogadas)

            if jogada_mais_usada == "Pedra":
                jogada_maquina = "Papel"
            elif jogada_mais_usada == "Papel":
                jogada_maquina = "Tesoura"
            else:
                jogada_maquina = "Pedra"

        print(f"\nSua jogada -> {jogada_jogador}")
        print(f"Jogada da máquina -> {jogada_maquina}")

        if jogada_jogador == jogada_maquina:
            print("Empate!")
        elif (
            jogada_jogador == "Pedra" and jogada_maquina == "Tesoura"
            or jogada_jogador == "Papel" and jogada_maquina == "Pedra"
            or jogada_jogador == "Tesoura" and jogada_maquina == "Papel"
        ):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

        historico_jogadas.append(jogada_jogador)

        print(f"Histórico do jogador -> {historico_jogadas}")
    else:
        print("\nOpção inválida.")

input("\nPressione Enter para encerrar...")