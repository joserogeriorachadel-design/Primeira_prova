# Minha primeira prova da faculdade!
## Prova com 5 questões, feitas em python, questões escolhidas no beecrowd pelo professor:
- questão 1 - beecrowd | 2535
- questão 2 - beecrowd | 1533
- questão 3 - foi feita pelo professor: descrição abaixo
- questão 4 - beecrowd | 2492
- questão 5 - beecrowd | 2478, mas com uma alteração: "Diferente do descrito acima, ao final dos dados de entrada há uma linha que indica o término, no formato: "fim fim""
## Descrição questão 3: 
- Nos jogos de baralho uma ação inicial é o embaralhamento das cartas, sendo que há diversas técnicas possíveis de serem utilizadas pelos jogadores. Uma das formas de medir a qualidade do embaralhamento é observar o resultado e contar quantas cartas consecutivas há do mesmo naipe ou do mesmo número.  A título de exemplo, se considerarmos um limite de 3 ocorrências similares, notamos que o baralho abaixo não está adequadamente embaralhado visto que apresenta 4 cartas de paus em sequência (independente do número), assim como também apresenta 3 cartas de número 10 em sequência (independente do naipe).

-Escreva, então, um programa que leia os dados de uma sequência de cartas e indique se elas estão adequadamente embaralhadas ou não.
Na primeira linha dos dados de entrada estão dois número N e L, ambos maiores do que zero, que indicam, respectivamente, o número de cartas da sequência
e o número limite de ocorrências a partir do qual o baralho é considerado não estar adequadamente embaralhado. Em seguida estão N linhas,
cada uma delas indicando o número e o naipe de uma das N cartas.

-O resultado esperado é o valor True caso as cartas estejam adequadamente embaralhas e False em caso contrário.

Entrada:
12 3
5 copas
3 paus
7 paus
4 paus
2 paus
8 ouros
8 espadas
10 copas
10 paus
10 ouros
1 paus
5 espadas

Saída:
False
