while True:
    num_conexoes = int(input())
    if num_conexoes == 0:
        break

    conexao = dict()
    funcao = 'Invertible.' #assume que a função é invertível

    for _ in range(num_conexoes):
        ilhas = input().split()

        if ilhas[0] in conexao:  #confere se há dois valores iguais nos dominios
            funcao = 'Not a function.'  

        elif ilhas[-1] in conexao.values():  # confere se há duas imagens iguais
            if funcao != 'Not a function.':  
                funcao = 'Not invertible.' 

        conexao[ilhas[0]] = ilhas[-1]  #registra a conexão mesmo quando já encontrou um problema

    print(funcao)