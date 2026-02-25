# ====================================
# CONVERSOR DE TEMPERATURA
# Exercício - Engenharia de Software
# ====================================

def celsius_para_fahrenheit(celsius):
    """
    RF01: Converter Celsius para Fahrenheit
    Fórmula: F = (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """
    RF02: Converter Fahrenheit para Celsius
    Fórmula: C = (F - 32) × 5/9
    """
    return (fahrenheit - 32) * 5/9


# ====================================
# PROGRAMA PRINCIPAL
# ====================================
print("="*40)
print("  CONVERSOR DE TEMPERATURA")
print("="*40)

print("Escolha a conversão:")
print("1 - Celsius → Fahrenheit")
print("2 - Fahrenheit → Celsius")

opcao = input("Opção: ")

if opcao == "1":
    c = float(input("Digite a temperatura em Celsius: "))
    f = celsius_para_fahrenheit(c)
    print("="*40)
    print(f"{c:.1f}°C = {f:.1f}°F")

elif opcao == "2":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = fahrenheit_para_celsius(f)
    print("="*40)
    print(f"{f:.1f}°F = {c:.1f}°C")

else:
    print("Opção inválida!")

print("="*40)
