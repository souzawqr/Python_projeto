import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Um triângulo que possui dois lados com medidas iguais recebe o nome de triângulo isósceles. O lado restante, que não foi observado ou que é diferente, é comumente chamado de base.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} A identidade de Euler é considerada a mais bela fórmula matemática, principalmente no meio acadêmico.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}  Segundo o filósofo grego Platão, a matemática é a forma com que Deus se comunica com o homem. {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} O teorema de Pitágoras diz que o quadrado da hipotenusa é igual à soma dos quadrados dos catetos. Podemos utilizar esse teorema para facilitar o cálculo da diagonal de um quadrado e altura de um triângulo equilátero (triângulo com os lados iguais).{os.linesep}')
    else: 
        print('Digite apenas 1, 2, 3 ou 4! ')

def start():
    # apresentar o chatbot 
    print('Olá! Bem-vindo ao chat de respostas!') 

    # pedir o nome
    nome = input('Informe seu nome: ')

    # pedir o email 
    email = input('Informe seu email: ')
    
    while True: 
        # oferecer o menu de opções 
        resposta = input(f'O que gostaria de saber hoje?'
                         f'{os.linesep}[1] - O que define um triângulo isósceles?'
                         f'{os.linesep}[2] - Qual é considerada a mais bela fórmula matemática?'
                         f'{os.linesep}[3] - Segundo Platão qual é a definição de matemática?'
                         f'{os.linesep}[4] - O que diz o teorema de Pitágoras?')

        # processar resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__': 
    start()