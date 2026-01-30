import csv

caminho = "exemplo.csv"
arquivo_csv = []

with open(caminho, mode = 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        arquivo_csv.append(linha)
print(arquivo_csv)