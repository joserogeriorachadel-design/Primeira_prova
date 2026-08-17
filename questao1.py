num_filhotes = int(input())
contador_filhotes = 0 #usado pra ver quantos serao os filhotes que seguem a regra
for _ in range(num_filhotes):
    especie = input()
    raca = input()
    nome_inteiro = input().split()
    espaço = input()
    if especie == 'cachorro' and len(nome_inteiro) > 1: #confere a especie e se o nome é composto
        for nome in nome_inteiro: #confere se a primeira letra dos nomes é igual a da raça
            if nome[0] == raca[0]:
                contador_filhotes += 1 #se for verdade soma um na quantidade de filhotes
                break

print(contador_filhotes)