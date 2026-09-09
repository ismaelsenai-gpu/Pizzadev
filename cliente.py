clientes = []

def cadastrar_clientes():
    cliente  = {
        "nome": input("Digite o nome do cliente: "),
        "telefone": input(f"Digite o telefone do cliente: ")
    }

    clientes.append(cliente)

cadastrar_clientes()
