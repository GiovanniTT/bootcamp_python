tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    if True:
        print("Operação bem-sucedida!")
        break
    tentativa += 1
else:
    print("Número máximo de tentativas atingido. Operação falhou.")