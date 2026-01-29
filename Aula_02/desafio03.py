entrada_lista = input("Digite uma lista de números separados por vírgulas: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num_str in numeros_str:
        numeros_int.append(float(num_str.strip()))
    print("Números convertidos com sucesso:", numeros_int)
except ValueError:
    print("Erro: Certifique-se de que todos os valores são números floats válidos.")