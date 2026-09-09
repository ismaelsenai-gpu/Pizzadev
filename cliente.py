clientes = []

def cadastrar_clientes():
    nome = input("Digite o nome do cliente: ").strip()

    if nome == "":
        print("Nome não pode ser vazio. Por favor, digite um nome válido.")
        return

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

cadastrar_clientes()
