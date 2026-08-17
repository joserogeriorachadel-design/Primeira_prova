num_pessoas = int(input())
pessoa_e_presentes = dict()

for _ in range(num_pessoas):
    pessoa,*presentes = input().split()
    pessoa_e_presentes[pessoa] = tuple(presentes) #relaciona a pessoas e seus presentes no dicionario
    
while True:
    pessoa_sorteada, presente_comprado = input().split()
    if pessoa_sorteada == 'fim':
        break 
    if presente_comprado in pessoa_e_presentes[pessoa_sorteada]: #confere se o presente que ela comprou esta na lista de desejos da pessoa sorteda
        acertou_presente = 'Uhul! Seu amigo secreto vai adorar o/'
    else:
        acertou_presente = 'Tente Novamente!' 
    
    print(acertou_presente)