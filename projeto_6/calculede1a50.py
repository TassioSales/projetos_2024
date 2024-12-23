from InquirerPy import prompt
from math import prod

def pergunta():
    """Exibe uma pergunta para o usuário selecionar uma operação."""
    perguntas = [
        {
            "type": "list",
            "message": "Qual operação deseja realizar?",
            "name": "operacao",
            "choices": ["Multiplicação", "Soma"],
        }
    ]
    return prompt(perguntas)

def calculo_de_1_a_50():
    """Realiza o cálculo com base na operação selecionada pelo usuário."""
    resposta = pergunta()
    operacao = resposta["operacao"]

    if operacao == "Multiplicação":
        resultado = prod(range(1, 51))  # Multiplica de 1 a 50
        print(f"Resultado da multiplicação de 1 a 50: {resultado}")
    elif operacao == "Soma":
        resultado = sum(range(1, 51))  # Soma de 1 a 50
        print(f"Resultado da soma de 1 a 50: {resultado}")
    else:
        print("Operação não suportada no momento.")

def main():
    calculo_de_1_a_50()

if __name__ == "__main__":
    main()
