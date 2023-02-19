# 5. Faça um programa que dado um valor, apresente:
# O seu Antecessor
# O seu Sucessor
# O seu quadrado
# A sua raiz

from math import pow, sqrt

num = int(input('Digite o seu número: '))
quadrado = pow(num, 2)
raiz = sqrt(num)
print(f'O antecessor de {num} é {num -1}')
print(f'O sucessor de {num} é {num +1}')
print(f'O quadrado de {num} é {quadrado}')
print(f'A raiz de {num} é {raiz}\n')
