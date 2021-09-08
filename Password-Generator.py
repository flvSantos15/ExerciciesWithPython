#PASSWORD GENERATOR
'''
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '[]{}()*;/,_-'

all = lower + upper + number + symbols

length = 16
password = ''.join(random.sample(all,length))

print(password)
'''

user = input('Digite seu usuario: ')
password = input('Digite sua senha: ')

print(f'Seu usuario é {user} e sua senha é {password}')
print('Você foi hackeado')