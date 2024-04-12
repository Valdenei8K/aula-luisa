# O código abaixo é uma tentativa de criar uma calculadora de Índice de Massa Corporal (IMC).
# No entanto, ele está incompleto e contém erros.
# Modifique o código para que ele solicite ao usuário seu peso em quilogramas e altura em metros.
# Seu programa deve calcular e imprimir o IMC do usuário seguindo a fórmula IMC = peso / (altura ** 2).
# Além disso, deve classificar o resultado em: Baixo peso, Peso normal, Sobrepeso ou Obesidade, 
# baseando-se nos valores de IMC.
#fonte imc https://ge.globo.com/eu-atleta/nutricao/post/2022/08/17/veja-qual-e-o-imc-ideal-e-como-calcular.ghtml

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura*altura)  # Cálculo do IMC precisa ser corrigido

# Classificação do IMC (faltam informações)
if imc < 18.5:
    classificacao = "Baixo peso"
elif imc < 24.9:
    classificacao = "Peso Normal"
elif imc< 29.9:
    classificacao = "Sobrepeso"    
elif imc< 34.9:
    classificacao = "Obesidade grau 1"
elif imc < 39.9:
    classificacao = "Obesidade grau 2"            
else:
    classificacao = "Obesidade Extrema"

print(f"Seu IMC é {imc} e sua classificação é: {classificacao}")
