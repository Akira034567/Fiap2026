# ====================================
# CONVERSOR DE TEMPERATURA - BÔNUS
# Exercício - Engenharia de Software
# ====================================

def celsius_para_fahrenheit(celsius):
    """RF01: Converter Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """RF02: Converter Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9


def celsius_para_kelvin(celsius):
    """RF04: Converter Celsius para Kelvin"""
    return celsius + 273.15


def kelvin_para_celsius(kelvin):
    """RF05: Converter Kelvin para Celsius"""
    return kelvin - 273.15


def ler_numero(mensagem):
    """
    RNF: Garantir validação de entrada numérica
    """
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")


# ====================================
# PROGRAMA PRINCIPAL
# ====================================

while True:
    print("="*40)
    print("  CONVERSOR DE TEMPERATURA")
    print("="*40)

    print("Escolha a conversão:")
    print("1 - Celsius → Fahrenheit")
    print("2 - Fahrenheit → Celsius")
    print("3 - Celsius → Kelvin")
    print("4 - Kelvin → Celsius")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        c = ler_numero("Digite a temperatura em Celsius: ")
        f = celsius_para_fahrenheit(c)
        print("="*40)
        print(f"{c:.2f}°C = {f:.2f}°F")

    elif opcao == "2":
        f = ler_numero("Digite a temperatura em Fahrenheit: ")
        c = fahrenheit_para_celsius(f)
        print("="*40)
        print(f"{f:.2f}°F = {c:.2f}°C")

    elif opcao == "3":
        c = ler_numero("Digite a temperatura em Celsius: ")
        k = celsius_para_kelvin(c)
        print("="*40)
        print(f"{c:.2f}°C = {k:.2f} K")

    elif opcao == "4":
        k = ler_numero("Digite a temperatura em Kelvin: ")
        c = kelvin_para_celsius(k)
        print("="*40)
        print(f"{k:.2f} K = {c:.2f}°C")

    elif opcao == "0":
        print("Encerrando o programa. Até mais! 👋")
        break

    else:
        print("❌ Opção inválida!")

    input("\nPressione ENTER para continuar...")
