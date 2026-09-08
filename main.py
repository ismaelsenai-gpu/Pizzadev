pizzas = ["Calabresa", "Frango com Catupiry", "Portuguesa", "Marguerita", "Chocolate"]

precos = [30.0, 35.0, 40.0, 30.0, 45.0]

print("-- Cardápio de Pizzas --")
for i in range(len(pizzas)):
    print(f"{i + 1}. {pizzas[i]} - R$ {precos[i]:.2f}")

while True:
    escolha = input("Escolha o numero da pizza que deseja pedir (ou 'sair' para encerrar): ")
    if escolha.lower() == 'sair':
        print("Obrigado por visitar nosso cardapio! VOLTE SEMPREEE")
        break
    elif escolha.isdigit() and 1 <= int (escolha) <= len(pizzas):
        indice = int(escolha) - 1
        print(f"Voce escolheu a pizza {pizzas[indice]} que custa R$ {precos[indice]:.2f}, qual a forma de pagamento? (1 - Dinheiro, 2 - Cartão)")
        input_pagamento = input("Digite o numero correspondente a forma de pagamento: ")
    elif input_pagamento == '1':
        print("Pagamento em dinheiro selecionado. Obrigado pela compra!")
    elif input_pagamento == '2':
            print("Pagamento com cartão selecionado. Obrigado pela compra!")
    elif input_pagamento not in ['1', '2']:
         print("Forma de pagamento invalida. Por favor, tente novamente.")
    else:
        print("Escolha inválida. Por favor, tente novamente.")
           