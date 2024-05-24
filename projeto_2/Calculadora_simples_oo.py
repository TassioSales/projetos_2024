# Crie uma calculadora simples em Python que permita ao usuário realizar operações básicas, como adição, subtração, multiplicação e divisão.
# O programa deve solicitar ao usuário dois números e a operação desejada.
# Em seguida, exiba o resultado da operação solicitada.

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def adicao(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        return self.num1 / self.num2

    def menu(self):
        try:
            while True:
                self.num1 = float(input("digite o primeiro numero: "))
                self.num2 = float(input("digite o segundo numero: "))
                print("digite a operacao que deseja: ")
                print("1 - adicao")
                print("2 - subtracao")
                print("3 - multiplicacao")
                print("4 - divisao")
                print("5 - sair")
                op = int(input("escolha a operacao: "))
                if op == 1:
                    print(f"{self.num1} + {self.num2} = {self.adicao()}")
                elif op == 2:
                    print(f"{self.num1} - {self.num2} = {self.subtracao()}")
                elif op == 3:
                    print(f"{self.num1} * {self.num2} = {self.multiplicacao()}")
                elif op == 4:
                    print(f"{self.num1} / {self.num2} = {self.divisao()}")
                elif op == 5:
                    break
                else:
                    print("opcao invalida")

        except ValueError:
            print("digite um valor valido")

        except ZeroDivisionError:
            print("nao pode dividir por zero")

        except KeyboardInterrupt:
            print("programa encerrado")

        except EOFError:
            print("programa encerrado")

        except:
            print("ocorreu um erro inesperado")

        finally:
            print("programa encerrado")


if __name__ == "__main__":
    calculadora = Calculadora(0, 0)
    calculadora.menu()
