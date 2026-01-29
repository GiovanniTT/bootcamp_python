numero = int(input("Digite um número inteiro: "))
while numero <= 1 or numero >= 100:
    print("Número inválido. Por favor, digite um número entre 1 e 100.")
    numero = int(input("Digite um número inteiro: "))

print(f"Obrigado! Você digitou o número {numero}.")