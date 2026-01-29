try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalem a {fahrenheit}°F.")
except ValueError: 
    print("Por favor, digite um número válido.")