print("===== CALCULADORA PYTHON =====\n")


# Função para validar a entrada do usuário
def obter_numero(mensagem):
    while True:
        try:
            # retorna a msg convertida para float
            return float(input(mensagem))
        except ValueError:
            print("Erro: digite um número válido.")
            
def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        # retorna None se o segundo número for 0
        # Obs: na matemática não pode dividir por 0
        return None
    return num1 / num2

def exibir_menu():
     while True:
        print("\n===== OPERAÇÕES =====")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        operacao = input("Escolha uma operação: ")

        if operacao in ["1", "2", "3", "4"]:
            return operacao

        print("Opção inválida. Escolha uma opção de 1 a 4.")

def calcular(num1, num2, operacao):
    if operacao == "1":
        resultado = somar(num1, num2)
    elif  operacao == "2":
        resultado = subtrair(num1, num2)
    elif  operacao == "3":
        resultado = multiplicar(num1, num2)
    elif  operacao == "4":
        resultado = dividir(num1,num2)

        # divisão por zero 
        if resultado is None:
            return None, False, "Não é possível dividir por zero."
    
    else:
        # operação inválida
        return None, False, "Operação inválida."
    
    return resultado, True, "Operação realizada com sucesso."

    
# Função main
def main():
    
    while True:

        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")
            

        operacao = exibir_menu()

        resultado, sucesso, mensagem = calcular(num1, num2, operacao)
        if sucesso:
            print(f"Resultado: {resultado:.2f}")
        else:
            print(mensagem)

        while True:
            continuar = input("Deseja realizar outro cálculo? (s/n): ")

            if continuar.lower() =="n":
                print("Calculadora encerrada.")
                break
            elif continuar.lower() == "s":
                break
            else:
                print("Opção inválida. Digite apenas 's' ou 'n'. ")
        # encerra o segundo loop
        if continuar.lower() == "n":
            break  

main()


