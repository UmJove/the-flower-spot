# Testes de try-except

dados_do_pedido = {}
def formulario_compra(): # incluir verificações de valores (try/except)
        print("\nPara finalizar sua compra forneça as informações a seguir: \n")
        while True:
            try:
                # preenchumento de form
                comprador = input("* Nome do comprador: ").strip()
                cpf = input("* CPF: ") .strip()
                email = input("* E-mail: ").strip()
                print("Endereço ")
                endereco_cep = input("* CEP: ").strip()
                endereco_rua = input("* Logradouro: ").strip()
                endereco_numero = input("* Número: ").strip()
                endereco_complemento = input("Complemento: ").strip()
                endereco_cidade = input("* Cidade: ").strip()
                endereco_bairro = input("* Bairro: ").strip()
                
                if comprador == "" or cpf == "" or email == "" or endereco_cep == "" or endereco_rua == "" or endereco_numero == "" or endereco_bairro == "" or endereco_cidade == "":
                    raise ValueError("Campo(s) obrigatório(s) não preenchido(s)!!")

                # incluindo dados no form            
                dados_do_pedido["Comprador"] = comprador
                dados_do_pedido["CPF"] = cpf
                dados_do_pedido["E-mail"] = email
                dados_do_pedido["CEP"] = endereco_cep
                dados_do_pedido["Endereço"] = [endereco_rua, endereco_numero, f"Complemento: {endereco_complemento}", f"Bairro: {endereco_bairro}", endereco_cidade]
                
                
                forma_pagamento = input("Escolha uma forma de pagamento:\n 1 - Crédito\n 2 - Débito\n 3 - Pix\n ").strip()
                if forma_pagamento == "1":
                    dados_do_pedido["Forma de pagamento"] = "crédito"
                elif forma_pagamento == "2":
                    dados_do_pedido["Forma de pagamento"] = "débito"
                elif forma_pagamento == "3":
                    dados_do_pedido["Forma de pagamento"] = "pix"
                else:
                    raise ValueError("Opção inválida!") # fazer estrutura try-except para corrigir erro
                    
                
                entrega = input("Escolha uma forma de entrega:\n 1 - Retirar na loja\n 2 - Receber em casa\n ").strip()
                if entrega == "1":
                    dados_do_pedido["Entrega"] = "retirar na loja"
                elif entrega == "2":
                    dados_do_pedido["Entrega"] = "receber em casa" #adicionar taxa de entrega
                else:
                    raise ValueError("Opção inválida!") # fazer estrutura try-except para corrigir erro
                
                break

            except ValueError as e:
                print(f"Erro: {e}")
                continue
        return

def verificar_campo_vazio(input_form):
    if input_form.strip() == "":
        raise ValueError("Campo(s) obrigatório(s) não preenchido(s)!!")