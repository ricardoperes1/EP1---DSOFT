#mostra o que cada número é
print("0: Sair")
print("1: Adicionar Item")
print("2: Remover Item")
print("3: Alterar Item")
print("4: Imprimir Estoque")

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
    novo_produto=input("Novo Produto: ")
    quantidade = int(input("Quantidade Inicial: "))
    while quantidade < 0:
        print("Quantidade inválida")
        quantidade = int(input("Quantidade Inicial: "))
    produtos[novo_produto]= {"Quantidade":quantidade}
    print("Item Adicionado")


