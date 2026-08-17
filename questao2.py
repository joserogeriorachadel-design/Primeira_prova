while True:
    numero_de_sus = int(input())
    if numero_de_sus == 0:
        break
    suspeitos = [int(x) for x in input().split()]
    
    suspeitos_ordenados = sorted(suspeitos) #deixa em ordem de menor pra maior percentual
    segundo_suspeito = suspeitos_ordenados[-2] #ve qual o segundo maior em percentual
    indice_segundo_suspeito = suspeitos.index(segundo_suspeito) + 1 #pega o indice do segundo maior em percentual

    print(indice_segundo_suspeito)