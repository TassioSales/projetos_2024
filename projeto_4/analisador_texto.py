import re


class AnalisadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palavras(self):
        return len(self.texto.split())

    # fazer tratamento de caracteres especiais usando a blibioteca re
    def remover_caracteres_especiais(self):
        return re.sub(r'[^A-Za-z0-9\s]', '', self.texto)

    def freq_palavras(self):
        texto_tratado = self.remover_caracteres_especiais()
        palavras = texto_tratado.split()
        freq = {}
        for palavra in palavras:
            if palavra in freq:
                freq[palavra] += 1
            else:
                freq[palavra] = 1
        return freq

    def palavras_unicas(self):
        palavras = self.texto.split()
        unicas = []
        for palavra in palavras:
            if palavra not in unicas:
                unicas.append(palavra)
        return unicas

    def contar_frases(self):
        return self.texto.count('.') + self.texto.count('!') + self.texto.count('?')

    def contar_caracteres(self):
        return len(self.texto)

    def palavras_longas(self):
        palavras = self.texto.split()
        longas = []
        for palavra in palavras:
            if len(palavra) > 5:
                longas.append(palavra)
        return longas

    def palavras_curta(self):
        palavras = self.texto.split()
        curtas = []
        for palavra in palavras:
            if len(palavra) < 3:
                curtas.append(palavra)
        return curtas

    def execute(self):
        print(f'Palavras: {self.contar_palavras()}')
        print(f'Frases: {self.contar_frases()}')
        print(f'Caracteres: {self.contar_caracteres()}')
        print(f'Palavras curtas: {self.palavras_curta()}')
        print(f'Palavras Longas: {self.palavras_longas()}')
        print(f'Palavras unicas: {self.palavras_unicas()}')
        print(f'Frequencia das palavras: {self.freq_palavras()}')


if __name__ == '__main__':
    texto = "Python é uma linguagem de programação poderosa. Fácil de aprender e divertida de usar! Você vai adorar programar em Python."
    analisador = AnalisadorTexto(texto)
    analisador.execute()
