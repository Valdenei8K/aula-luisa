# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

while True:
    valor1 = input("Digite um número (ou -1 para sair): ")
    if valor1 == '-1':
        print("Programa encerrado.")
        break
    
    operador = input("Digite o operador (+, -, *, /): ")
    valor2 = input("Digite outro número: ")

  
    valor1 = float(valor1)
    valor2 = float(valor2)

    resultado = 0
    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        if valor2 != 0: 
            resultado = valor1 / valor2
        else:
            print("Não é possível dividir por zero.")
            continue  
    else:
        print('Operador inválido')
        continue 

    print("Resultado:", resultado)
