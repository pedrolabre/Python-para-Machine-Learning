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

        print(f"\nSua jogada -> {jogada_jogador}")
    else:
        print("\nOpção inválida.")

input("\nPressione Enter para encerrar...")