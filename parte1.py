
#mostra o que cada número é
print("0: Sair")
print("1: Adicionar Item")
print("2: Remover Item")
print("3: Alterar Item")
print("4: Imprimir Estoque")

print("No git! Vai Corinthians!!!")

#escolha do usuario
menu_inicial= int(input("Escolha o Numero: "))

#checando 
#print(menu_inicial) 
#criando um estoque inicial dos produtos
produtos = {
        'batata': {'Quantidade': 0},
        'cenoura': {'Quantidade': 0},
        'pepino': {'Quantidade': 0},
        }

if menu_inicial == 0:
    print("Até Mais")
    
elif menu_inicial == 1:
    novo_produto = input("Novo Produto: ")
    quantidade = int(input("Quantidade Inicial: "))
    while quantidade < 0:
        print("Quantidade Inválida")
        quantidade = int(input("Quantidade Inicial: "))
    produtos[novo_produto]= {"Quantidade":quantidade}
    print("Item Adicionado")
    
elif menu_inicial == 2:
    remove_produto = input("Retirar o Produto: ")
    del produtos[remove_produto]
    print("Item Removido")
    
elif menu_inicial == 3:
    produto_alterado = input("Nome do Produto: ")
    while produto_alterado not in produtos:
        print("Produto Não Encontrado")
        produto_alterado = input("Nome do Produto: ")
    nova_quantidade = int(input("Nova Quantidade: "))
    produtos[produto_alterado] = {"Quantidade":nova_quantidade}

elif menu_inicial == 4:
    for p, q in produtos.items():
        print("{0}: {1}".format(p, q["Quantidade"]))
    
    
    
