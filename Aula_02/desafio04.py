try:
    nome = input("Digite seu nome: ")
    
    if len(nome)  == 0:
        raise ValueError("O nome não pode ser vazio.")
        exit()
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não pode conter números.")
        exit()
    elif any(char.isalpha() for char in nome):
        raise ValueError("O nome não pode conter caracteres especiais.")
        exit()
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print("Erro:", e)
    exit()
    
try:
    salario = float(input("Digite seu salário mensal: "))
    if salario < 0:
        print("Digite um salário válido.")
except ValueError:
    print("Erro: Por favor, digite um número válido para o salário.")
    exit()
    
try:
    bonus = float(input("Digite o bônus anual: "))
    if bonus < 0:
        print("Digite um bônus válido.")
except ValueError:
    print("Erro: Por favor, digite um número válido para o bônus.")
    exit()
    
salario_anual = (salario * 12) + bonus
print(f"O salário anual de {nome} é: R$ {salario_anual:.2f}")
