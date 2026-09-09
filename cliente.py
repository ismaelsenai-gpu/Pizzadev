clientes = []

def cadastrar_clientes():
    while True:
        print("\n-- Cadastro de Clientes --")
        escolha = input("Deseja cadastrar um novo cliente? (s/n): ").strip().lower()
        if escolha == 'n':
            break
        nome = input("Digite o nome do cliente: ").strip()

        if nome == "":
            print("Nome não pode ser vazio. Por favor, digite um nome válido.")
            return
        try:
            int(nome)
            print("Nome nao pode ser um numero. Por favor, digite um nome valido")
        except ValueError:
            pass
        telefone = input("Digite o telefone do cliente: ").strip()

        if telefone == "":
            print("Telefone não pode ser vazio. Por favor, digite um telefone válido.")
            return

        try:
            telefone = int(telefone)
        except ValueError:
            print("Telefone deve ser um número inteiro. Digite um número válido.")
            return

        cliente = {
            "nome": nome,
            "telefone": telefone
        }

        if cliente not in clientes:
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")
        else:
            print("Cliente já cadastrado.")
def mostrar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("-- LISTA DE CLIENTES --")
        for i, cliente in enumerate(clientes):
            print(f"{i + 1}. Nome: {cliente['nome']}, telefone: {cliente['telefone']}")

cadastrar_clientes()
mostrar_clientes()
