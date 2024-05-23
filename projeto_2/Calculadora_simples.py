# Crie uma calculadora simples em Python que permita ao usuário realizar operações básicas, como adição, subtração, multiplicação e divisão.
# O programa deve solicitar ao usuário dois números e a operação desejada.
# Em seguida, exiba o resultado da operação solicitada.

def calculadora_simples():
    try:

        #menu
        while True:
            num1 = float(input("digite o primeiro numero: "))
            num2 = float(input("digite o segundo numero: "))
            print("digite a operacao que deseja: ")
            print("1 - adicao")
            print("2 - subtracao")
            print("3 - multiplicacao")
            print("4 - divisao")
            print("5 - sair")
            op = int(input("escolha a operacao: "))
            if op == 1:
                print(f"{num1} + {num2} = {num1 + num2}")
            elif op == 2:
                print(f"{num1} - {num2} = {num1 - num2}")
            elif op == 3:
                print(f"{num1} * {num2} = {num1 * num2}")
            elif op == 4:
                print(f"{num1} / {num2} = {num1 / num2}")
            elif op == 5:
                break
            else:
                print("opcao invalida")

    except ValueError:
        print("digite um valor valido")

    except ZeroDivisionError:
        print("Não e possivel fazer divisao por zero")

    except:
        print("ocorreu um erro")

calculadora_simples()