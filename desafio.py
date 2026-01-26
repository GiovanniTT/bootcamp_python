constante_bonus = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite o bônus recebido: "))
salario_total = constante_bonus + salario * bonus
print(f"Olá {nome}, o seu bonus foi de R$ {salario_total:.2f}")