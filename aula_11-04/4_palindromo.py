# O código abaixo é uma tentativa de criar um verificador de palíndromos.
# Palíndromos são palavras ou frases que são iguais quando lidas de trás para frente.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma palavra ou frase, e o programa deve imprimir se é um palíndromo ou não.
# Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.

texto = input("Digite um texto: ")

texto = texto.lower() #transforma em minuscula
texto = texto.replace(" ", "") #substitui espaços vazios e faz uma só string grande

texto_invertido = texto[::-1] # inverte o texto

if texto == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
