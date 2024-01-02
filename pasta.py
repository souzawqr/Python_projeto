import random 
#introducion to funcionality 
print('Bem-Vindo ao seu Gerador de Senhas!')

#string to ramdom characters 
chars = 'abcdefghijklmnopqrstuvxzABCDEFGHIJKLMNOPQRSTUVXZ/*&#@!()0123456789'

number = int(input('Amount of passwords to generate: '))
length = int(input('Input your password length: '))

print('\nhere are your passwords: ')

for pwd in range(number): 
    passwords = ''
    for i in range(length): 
        passwords += random.choice(chars)
    print(passwords)