
produtos = {}

c = True

while c:
    #mostra o que cada número é
    print("0: Sair")
    print("1: Adicionar Item")
    print("2: Remover Item")
    print("3: Alterar Quantidade de um Item")
    print("4: Imprimir Estoque Completo")

    #escolha do usuario
    menu_inicial= int(input("Escolha o Numero: "))
    
    
    #================================ OPÇÕES ======================================
    
    if menu_inicial == 0:
        print("Até Mais")
        c = False
        
    elif menu_inicial == 1:
        novo_produto = input("Novo Produto: ")
        quantidade = int(input("Quantidade Inicial: "))
        produtos[novo_produto]= {"Quantidade":quantidade}
        print("Item Adicionado")
                
    elif menu_inicial == 2:
        remove_produto = input("Retirar o Produto: ")
        while remove_produto not in produtos:
            print("Produto Não Encontrado")
            remove_produto = input("Nome do Produto: ")    
        del produtos[remove_produto]
        print("Item Removido")
                        
    elif menu_inicial == 3:
        produto_alterado = input("Nome do Produto: ")
        while produto_alterado not in produtos:
            print("Produto Não Encontrado")
            produto_alterado = input("Nome do Produto: ")    
        print('Quantidade Registrada: {0}'.format(produtos[produto_alterado]['Quantidade']))
        nova_quantidade = int(input("Quantidade: "))
        produtos[produto_alterado] = {"Quantidade":produtos[produto_alterado]['Quantidade'] + nova_quantidade}
        print('Quantidade Alterada')
                
    elif menu_inicial == 4:
       for p, q in produtos.items():
           print(' ')
           print(p)
           print("Estoque: {0}".format(q["Quantidade"]))
           print(' ')

        