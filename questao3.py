numero_cartas, limite = [int(x) for x in input().split()]
num_do_baralho = [] #lista apenas para numeros
naipes_do_baralho = [] #lista apenas para naipes
embaralhado = True 

for _ in range(numero_cartas):
    numero, naipe = input().split()
    num_do_baralho.append(numero) #adiciona os numeros na lista de numeros
    naipes_do_baralho.append(naipe) #adiciona os naipes na lista de naipes
    
for i in range(len(num_do_baralho) - limite): #de numero em numero vai conferindo se seus sucessores sao iguais
    contador_de_num_iguais_seguidos = 1 #comeca com 1 porque ele mesmo entra na contagem
    for j in range(limite): #dado um numero confere seus proximos sucessores
        if num_do_baralho[i+j] == num_do_baralho[i+j+1]: 
            contador_de_num_iguais_seguidos += 1 #se ele for igual ao sucessor conta mais 1 igual seguido
        else:
            contador_de_num_iguais_seguidos = 1
        if contador_de_num_iguais_seguidos >= limite: 
            embaralhado = False #se o numero de seguidos iguais for maior ou igual ao limite, nao esta embaralhado
            break #se ja viu que nao esta embaralhado pode parar
    
if embaralhado == True: #confere se ainda tem chance de estar
    for i in range(len(naipes_do_baralho) - limite): #de naipe em naipe vai conferindo se seus sucessores sao iguais
        contador_de_naipes_iguais_seguidos = 1 #comeca com 1 porque ele mesmo entra na contagem
        for j in range(limite): #dado um naipe confere seus proximos sucessores
            if naipes_do_baralho[i+j] == naipes_do_baralho[i+j+1]:
                contador_de_naipes_iguais_seguidos += 1 #se ele for igual ao sucessor conta mais 1 igual seguido
            else:
                contador_de_naipes_iguais_seguidos = 1
        if contador_de_naipes_iguais_seguidos >= limite: 
            embaralhado = False #se o numero de seguidos iguais for maior ou igual ao limite, nao esta embaralhado
            contador_de_naipes_iguais_seguidos = 1 #se ja viu que nao esta embaralhado pode parar
        
print(embaralhado)