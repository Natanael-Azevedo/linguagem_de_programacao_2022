'''
Paolo quer criar novos sabores de pizza e decidiu usar a seguinte estratégia: a partir da lista de ingredientes de uma pizza, ele vai selecionar alguns ingredientes para criar uma nova pizza.

Dada uma lista de pizzas, para as pizzas em índices pares Paolo vai fazer uma nova pizza utilizando somente os ingredientes cujo nome tenha um comprimento menor do que N. Já para as pizzas em índices ímpares, Paolo vai fazer uma nova pizza utilizando somente os ingredientes cujo nome tenha um comprimento maior do que N.

O seu programa deve ler um valor inteiro L e em seguida uma lista de L pizzas, cada uma em uma linha, onde cada pizza é formada por uma lista de ingredientes. Em seguida, seu programa deve ler um valor inteiro N.

Seu programa deve imprimir as L pizzas que Paolo criou usando a estratégia anterior.

Cada lista de ingredientes será fornecida em uma linha e os ingredientes serão separados por espaços.


- Exemplo de Entrada 1:
4
queijo cogumelo pimenta presunto
pimenta milho queijo
queijo mel brócolis palmito
escarola muzzarela
7

- Exemplo de Saída 1:
['queijo']
[]
['queijo', 'mel']
['escarola', 'muzzarela']
'''
n = int(input())
pizzas = []
for x in range(n):
    pizza = input()
    pizzas.append(pizza.split())
tamanho = int(input())

for i, x in enumerate(pizzas):
    if i % 2 == 0:
        novaPizza = []
        for y in x:
            if len(y) < tamanho:
                novaPizza.append(y)
        print(novaPizza)
    else:
        novaPizza = []
        for y in x:
            if len(y) > tamanho:
                novaPizza.append(y)
        print(novaPizza)
  
