# Exercício 75 # Aula 16
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os numeros pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print('\nAcabou!')