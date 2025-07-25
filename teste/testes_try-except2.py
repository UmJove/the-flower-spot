## Testes de try-except

dados_do_pedido = {"Comprador":"", "CPF":"", "E-mail":""}
def formulario_compra(): # incluir verificações de valores (try/except)
    print("\nPara finalizar sua compra forneça as informações a seguir: \n")
    
    # Dados do comprador
    for campo in dados_do_pedido:
        dados_do_pedido[campo] = pedir(campo)    
    endereço = {"CEP":"", "Logradouro":"", "Número":"", "Complemento":"", "Cidade":""}
    
    for campo in endereço:
        endereço[campo] = pedir(campo)
    print(endereço)        
    
    dados_do_pedido["Endereço"] = endereço

    # Dados da compra
    while True:
        try:
            forma_pagamento = input("Escolha uma forma de pagamento:\n 1 - Crédito\n 2 - Débito\n 3 - Pix\n ").strip()
            if forma_pagamento == "1":
                dados_do_pedido["Forma de pagamento"] = "crédito"
            elif forma_pagamento == "2":
                dados_do_pedido["Forma de pagamento"] = "débito"
            elif forma_pagamento == "3":
                dados_do_pedido["Forma de pagamento"] = "pix"
            else:
                raise ValueError("Opção inválida!")
            break

        except ValueError as e:
                print(f"Erro: {e}")
                continue           
                
    while True:
        try:
            entrega = input("Escolha uma forma de entrega:\n 1 - Retirar na loja\n 2 - Receber em casa\n ").strip()
            if entrega == "1":
                dados_do_pedido["Entrega"] = "retirar na loja"
            elif entrega == "2":
                dados_do_pedido["Entrega"] = "receber em casa" #adicionar taxa de entrega
                #calcular_entrega()
            else:
                raise ValueError("Opção inválida!")
            break

        except ValueError as e:
                print(f"Erro: {e}")
                continue
    
    # Fim da função
    return

def pedir(campo_pedido):
    while True:
        try:
            resposta = input(f"{campo_pedido}: ").strip()
            if input_vazio(resposta) == False:
                break 
            else:
                raise ValueError(f"Campo obrigatório não preenchido!!")
        except ValueError as e:
            print(f"Erro: {e}")
            continue
    return resposta 
                

def input_vazio(resposta):
    if resposta == "":
        return True
    else:
        return False



formulario_compra()
print(dados_do_pedido)