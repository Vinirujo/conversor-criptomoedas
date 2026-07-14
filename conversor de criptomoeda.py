def converter_para_reais(bitcoins, cotacao):
    return bitcoins * cotacao

def converter_para_bitcoins(reais, cotacao):
    return reais / cotacao

def menu():
    while True:
        print("\n==============================")
        print("    CONVERSÃO DE CRIPTOMOEDAS   ")
        print("==============================")
        print("1 - Converter Bitcoins em Reais")
        print("2 - Converter Reais em Bitcoins")
        print("3 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            bitcoins = float(input("\nDigite a quantidade de Bitcoins: "))
            cotacao = float(input("Digite a cotação do Bitcoin em Reais: "))
            resultado = converter_para_reais(bitcoins, cotacao)
            print(f"\n{bitcoins} BTC equivalem a R$ {resultado:.2f}")

        elif opcao == "2":
            reais = float(input("\nDigite o valor em Reais: "))
            cotacao = float(input("Digite a cotação do Bitcoin em Reais: "))
            resultado = converter_para_bitcoins(reais, cotacao)
            print(f"\nR$ {reais:.2f} equivalem a {resultado:.6f} BTC")

        elif opcao == "3":
            print("\nSaindo do programa... Até mais!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

# Executa o menu
menu()