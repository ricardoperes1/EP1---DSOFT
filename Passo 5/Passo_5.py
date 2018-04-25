#============================== IMPORTS =======================================

import json

#========================== LOG IN ===========================================

print('0: Acessar Estoque de Uma Loja')
print('1: Cadastrar Nova Loja')
login = int(input('Escolha o Número: '))

#========================= ESCOLHA DA LOJA ====================================

if login == 0:
    loja = input("Escolha a unidade que você deseja acessar: ")
    with open('{0}.json'.format(loja),'r') as dados:#abre o arquivo
        produtos = json.load(dados)#lê o arquivo e salva na variável 'produtos'em dict

else:
    loja = input('Qual é o nome da nova loja: ')
    with open('{0}.json'.format(loja),'w') as dados:
        dados.write('{}')
    with open('{0}.json'.format(loja),'r') as dados:#abre o arquivo
        produtos = json.load(dados)

#============================ MENU INICIAL ====================================

c = True

while c:
    #mostra o que cada número é
    print("0: Sair")
    print("1: Adicionar Item")
    print("2: Remover Item")
    print("3: Alterar Quantidade de um Item")
    print("4: Alterar o Preço de um Produto")
    print("5: Imprimir Estoque Completo")
    print("6: Imprimir Lista de Produtos em Estoque Negativo")
    print("7: Imprimir Valor Monetário Total do Estoque")
    
    #escolha do usuario
    menu_inicial= int(input("Escolha o Numero: "))
    
    
    #================================ OPÇÕES ======================================
    
    if menu_inicial == 0:
        print("Até Mais")
        c = False
        
    elif menu_inicial == 1:
        novo_produto = input("Novo Produto: ")
        quantidade = int(input("Quantidade Inicial: "))
        preco = float(input("Preço do Produto: "))       
        while preco < 0:
            print("Preço Inválido")
            preco = float(input("Preço do Produto:"))
        produtos[novo_produto]= {"Quantidade":quantidade, "Preco": preco}
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
        produto_alterado = input("Nome do Produto: ")
        while produto_alterado not in produtos:
            print("Produto Não Encontrado")
            produto_alterado = input("Nome do Produto: ")    
        print('Preço Registrado: {0}'.format(produtos[produto_alterado]['Preco']))
        novo_preco = float(input("Novo Preço: "))
        produtos[produto_alterado] = {"Quantidade":novo_preco}
        print("Preço Alterado")
                                        
    elif menu_inicial == 5:
       for p, q in produtos.items():
           print(' ')
           print(p)
           print("Estoque: {0}".format(q["Quantidade"]))
           print("Preço: {0}".format(q["Preco"]))
           print(' ')
                                                
    elif menu_inicial == 6:
        est_neg=[]
        for e in produtos:    
            if produtos[e]['Quantidade'] < 0:
                est_neg.append(e)
        if len(est_neg) > 0:
            for e in est_neg:
                print("{0}: {1}".format(e, produtos[e]["Quantidade"]))
        else:
            print("Nenhum Produto Em Estoque Negativo")
                            
    elif menu_inicial == 7:
        valor = 0
        for e in produtos:
            valor += produtos[e]["Quantidade"] * produtos[e]["Preco"]
        print("{0} Reais".format(valor))
                                    
                                    
#+============================ SALVANDO O ARQUIVO =============================

    with open('{0}.json'.format(loja),'w') as dados:
        # Converte de volta em string, organiza o arquivo e lista em ordem alfabética
        produtos_alterados = json.dumps(produtos,indent=2,sort_keys=True)
        # Salva Produtos em json
        dados.write(produtos_alterados)
        
