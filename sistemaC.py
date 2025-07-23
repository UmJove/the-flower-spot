#Sistema carrinho de compra:

produtos = {
    1: {"nome": "Buquê com 3 Rosas Brancas", "preco": 100.00, "Quantidade": 20},
    2: {"nome": "Buquê com 3 Rosas vermelhas", "preco": 100.0, "Quantidade": 20},
    3: {"nome": "Buquê com 3 Rosas cor de Rosa", "preco": 100.00, "Quantidade": 20},
    4: {"nome": "Buquê Mix de Flores M (colorido)", "preco": 220.00, "Quantidade": 20},
    5: {"nome": "Buquê Paris", "preco": 380.00, "Quantidade": 20}
}

# def cadastrar_produtos():
#     id = input("Digite o id do produto no sistema: ")
#     produtos[id] = 
    
carrinho = {}
dados_do_pedido = {}
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
            print(f"\n{quantidade}x {produtos[id]['nome']} adicionado ao carrinho.")
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
            print(f"{item['quantidade']}x {item['nome']} - R${item['preco']:.2f} (id = {id})") # imprimindo id dos produtos
        print(f"Total: R${total:.2f}")

def finalizar_compra():
    ver_carrinho()
    if carrinho:
        formulario_compra() # função de preenchimento de formulário para finalização do pedido
        pedido_confirmado = confirmar_pedido() # ver dados de formulário + carrinho com total
        
        if pedido_confirmado == True:
            print("\n "\
            "\n Compra finalizada! Obrigado pela preferência.")
            carrinho.clear()
        
        elif pedido_confirmado == "menu":
            menu()
        
        elif pedido_confirmado == False:
            print("PEDIDO CANCELADO")
            sair()   
    else:
        print("Seu carrinho está vazio.")

def formulario_compra(): # incluir verificações de valores (try/except)
        print("\nPara finalizar sua compra forneça as informações a seguir: \n")
        comprador = input("Nome do comprador: ")
        cpf = input("CPF: ") 
        email = input("E-mail: ")
        endereco_rua = input("Endereço(logradouro): ")
        endereco_numero = input("Endereço(numero): ")
        endereco_complemento = input("Endereço (complemento): ")
        forma_pagamento = input("Escolha uma forma de pagamento:\n 1 - Crédito\n 2 - Débito\n 3 - Pix\n ")
        entrega = input("Escolha uma forma de entrega:\n 1 - Retirar na loja\n 2 - Receber em casa\n ")
        
        dados_do_pedido["comprador"] = comprador
        dados_do_pedido["cpf"] = cpf
        dados_do_pedido["e-mail"] = email
        dados_do_pedido["endereço"] = [endereco_rua, endereco_numero, f"complemento: {endereco_complemento}"]
        if forma_pagamento == "1":
            dados_do_pedido["forma de pagamento"] = "crédito"
        elif forma_pagamento == "2":
            dados_do_pedido["forma de pagamento"] = "débito"
        elif forma_pagamento == "3":
            dados_do_pedido["forma de pagamento"] = "pix"
        # fazer estrutura de erro para permitir ao comprador "ajustar" a opção escolhida   
        # else:
        #     raise ValueError ("opção inválida, escolha novamente") 
        
        if entrega == "1":
            dados_do_pedido["entrega"] = "retirar na loja"
        elif entrega == "2":
            dados_do_pedido["entrega"] = "receber em casa"

def confirmar_pedido():
    print("\n Confirme as informações a seguir para finalizar seu pedido"
    "\n >> Dados do pedido <<")
    for c,v in dados_do_pedido.items():
        print(f"{c} - {v}")
    ver_carrinho()
    confirmacao = input("\nConfirmar pedido(S/N): "
    "\n sim - confirmar"
    "\n não - cancelar pedido e encerrrar programa"
    "\n voltar - voltar ao menu\n ")
    if confirmacao.lower() == "sim":
        return True
    elif confirmacao.lower() == "não" or confirmacao.lower() == "nao":
        return False
    elif confirmacao.lower() == "voltar":
        return "menu"
    else: #aprimorar
        print("Resposta não identificada, tente novamente!")
        confirmar_pedido()



def sair():
    print("Encerrando o sistema. Até logo!")
    exit()

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Listar produtos")
        print("2. Adicionar ao carrinho")
        print("3. Remover do carrinho") #SE TIVER VAZIO SAIR DA ROTINA (Já alterado)
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
            sair()
            break
        else:
            print("Opção inválida. Tente novamente.")

def inicio():
    print("\nSeja bem-vindo à 'The Flower Spot', sua floricultura digital!")
    menu()

    

# Iniciar o sistema
inicio()

