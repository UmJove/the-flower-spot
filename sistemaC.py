#Sistema carrinho de compra:

produtos = {
    1: {"nome": "Buquê com 3 Rosas Brancas", "preco": 100.00},
    2: {"nome": "Buquê com 3 Rosas vermelhas", "preco": 100.0},
    3: {"nome": "Buquê com 3 Rosas cor de Rosa", "preco": 100.00},
    4: {"nome": "Buquê Mix de Flores M (colorido)", "preco": 220.00},
    5: {"nome": "Buquê Paris", "preco": 380.00}
}

carrinho = {}

def listar_produtos():
    print("\nProdutos disponíveis:")
    for id, info in produtos.items():
        print(f"{id}: {info['nome']} - R${info['preco']:.2f}")

def adicionar_ao_carrinho():
    listar_produtos()
    try:
        id = int(input("Digite o ID do produto para adicionar: "))
        if id in produtos:
            quantidade = int(input("Quantidade: "))
            if id in carrinho:
                carrinho[id]["quantidade"] += quantidade
            else:
                carrinho[id] = {
                    "nome": produtos[id]["nome"],
                    "preco": produtos[id]["preco"],
                    "quantidade": quantidade
                }
            print(f"{quantidade}x {produtos[id]['nome']} adicionado ao carrinho.")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def remover_do_carrinho():
    if not carrinho:
        print("\nCarrinho vazio.")
    else:
        ver_carrinho()
        try:
            id = int(input("Digite o ID do produto para remover: "))
            if id in carrinho:
                del carrinho[id]
                print("Produto removido do carrinho.")
            else:
                print("Produto não está no carrinho.")
        except ValueError:
            print("Entrada inválida.")

def ver_carrinho():
    print("\nCarrinho atual:")
    if not carrinho:
        print("Carrinho vazio.")
    else:
        total = 0
        for id, item in carrinho.items():
            subtotal = item["preco"] * item["quantidade"]
            total += subtotal
            print(f"{item['quantidade']}x {item['nome']} - R${item['preco']:.2f}")
        print(f"Total: R${total:.2f}")

def finalizar_compra():
    ver_carrinho()
    if carrinho:
        print("\nCompra finalizada! Obrigado pela preferência.")
        carrinho.clear()
    else:
        print("Seu carrinho está vazio.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Listar produtos")
        print("2. Adicionar ao carrinho")
        print("3. Remover do carrinho") #SE TIVER VAZIO SAIR DA ROTINA
        print("4. Ver carrinho")
        print("5. Finalizar compra")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            adicionar_ao_carrinho()
        elif opcao == "3":
            remover_do_carrinho()
        elif opcao == "4":
            ver_carrinho()
        elif opcao == "5":
            finalizar_compra()
        elif opcao == "6":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def inicio():
    print("\nSeja bem-vindo à 'The Flower Spot', sua floricultura digital!")
    menu()

# Iniciar o sistema
inicio()