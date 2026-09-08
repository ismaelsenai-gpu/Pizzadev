pizzas = ["Calabresa", "Frango com Catupiry", "Portuguesa", "Marguerita"]

precos = [30.0, 35.0, 40.0, 30.0]

print("-- Cardápio de Pizzas --")
for i in range(len(pizzas)):
    print(f"{i + 1}. {pizzas[i]} - R$ {precos[i]:.2f}")


