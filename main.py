pizzas = ["Calabresa", "Frango com Catupiry", "Portuguesa", "Marguerita", "Chocolate"]

precos = [30.0, 35.0, 40.0, 30.0, 45.0]

print("-- Cardápio de Pizzas --")
for i in range(len(pizzas)):
    print(f"{i + 1}. {pizzas[i]} - R$ {precos[i]:.2f}")

while True:
    escolha = input("Deseja fazer um pedido? (s/n):").strip().lower()
    if escolha == 'n':
        break
    elif escolha == 's':
        try:
            numero_pizza = int(input("Digite o numero da pizza que deseja pedir (1-5): "))
            if 1 <= numero_pizza <= len(pizzas):
                pizza_escolhida = pizzas[numero_pizza - 1]
                preco_pizza = precos[numero_pizza - 1]
                print(f"Você escolheu a pizza {pizza_escolhida} que custa R$ {preco_pizza:.2f}.")
            else:
                print("Número de pizza inválido. Por favor, escolha um número entre 1 e 5. ")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    else:
        print("Opção invalida. Por favor, digite 's' para sim ou 'n' para não.")


def valor_total_pedido(pizza_escolhida):
    if pizza_escolhida in pizzas:
        index = pizzas.index(pizza_escolhida)
        return precos[index]
    else:
        return 0.0
             


valor_total_pedido(pizza_escolhida)