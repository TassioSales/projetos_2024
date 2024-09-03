import re
import unicodedata
from collections import Counter

class AnalisadorTexto:
    def __init__(self, texto):
        self.texto = texto.lower()  # Convertendo o texto para minúsculas
        self.texto_tratado = self.remover_caracteres_especiais()

    def contar_palavras(self):
        return len(self.texto_tratado.split())

    def remover_caracteres_especiais(self):
        texto_sem_acento = unicodedata.normalize('NFKD', self.texto).encode('ASCII', 'ignore').decode('ASCII')
        return re.sub(r'[^a-z0-9\s]', '', texto_sem_acento)

    def freq_palavras(self):
        palavras = self.texto_tratado.split()
        return dict(Counter(palavras))

    def palavras_unicas(self):
        freq = self.freq_palavras()
        return [palavra for palavra, contagem in freq.items() if contagem == 1]

    def contar_frases(self):
        return self.texto.count('.') + self.texto.count('!') + self.texto.count('?')

    def contar_caracteres(self):
        return len(self.texto)

    def palavras_longas(self, limite=5):
        palavras = self.texto_tratado.split()
        palavras_longas_unicas = set([palavra for palavra in palavras if len(palavra) > limite])
        return list(palavras_longas_unicas)

    def palavras_curtas(self, limite=3):
        palavras = self.texto_tratado.split()
        palavras_curtas_unicas = set([palavra for palavra in palavras if len(palavra) < limite])
        return list(palavras_curtas_unicas)

    def execute(self):
        print(f'Palavras: {self.contar_palavras()}')
        print(f'Frases: {self.contar_frases()}')
        print(f'Caracteres: {self.contar_caracteres()}')
        print(f'Palavras curtas: {self.palavras_curtas()}')
        print(f'Palavras longas: {self.palavras_longas()}')
        print(f'Palavras únicas: {self.palavras_unicas()}')
        print(f'Frequência das palavras: {self.freq_palavras()}')


if __name__ == '__main__':
    texto = """
    Era uma vez, em uma terra distante, um jovem chamado Leonardo. Ele vivia em uma pequena aldeia cercada por montanhas majestosas e rios cristalinos. Leonardo sempre foi curioso e apaixonado por descobrir novos conhecimentos. Desde criança, passava horas explorando a floresta ao redor da aldeia, observando os animais e as plantas, e tentando entender como tudo funcionava.
    Um dia, enquanto explorava uma caverna que havia encontrado na floresta, Leonardo descobriu um antigo livro de alquimia. O livro estava coberto de poeira, e as páginas estavam amareladas pelo tempo, mas Leonardo ficou fascinado pelas fórmulas e experimentos descritos nele. Ele decidiu que queria se tornar um alquimista e dedicar sua vida a transformar materiais comuns em ouro e descobrir o elixir da vida eterna.
    Determinado a seguir esse novo caminho, Leonardo começou a estudar o livro todas as noites, experimentando com diferentes ingredientes e substâncias que encontrava na floresta. Ele falhou inúmeras vezes, mas a cada erro, aprendia algo novo e ficava mais perto de alcançar seu objetivo. Sua determinação era tão grande que, eventualmente, ele conseguiu criar uma poção que fazia as plantas crescerem duas vezes mais rápido.
    A notícia da descoberta de Leonardo se espalhou rapidamente pela aldeia, e logo pessoas de lugares distantes começaram a visitá-lo, buscando sua ajuda. Algumas queriam poções para curar doenças, outras desejavam melhorar suas colheitas, e havia até mesmo aqueles que queriam a poção para prolongar suas vidas.
    Apesar de todos os pedidos, Leonardo nunca esqueceu seu verdadeiro objetivo: encontrar o segredo do ouro e da vida eterna. Ele continuou a estudar e a experimentar, convencido de que um dia faria a maior descoberta da história.
    No entanto, ao longo dos anos, Leonardo começou a perceber algo importante. Embora suas poções pudessem trazer benefícios temporários, elas não eram a resposta para os mistérios mais profundos da vida. Ele viu que a busca pelo ouro e pela imortalidade não era o que realmente importava. O verdadeiro valor estava em ajudar os outros e em compartilhar o conhecimento que havia adquirido.
    Com essa nova compreensão, Leonardo começou a ensinar alquimia para as crianças da aldeia, passando seus conhecimentos para a próxima geração. Ele deixou de lado a busca pelo ouro e pela vida eterna, dedicando-se a ajudar sua comunidade a prosperar. E assim, ele viveu uma vida longa e plena, não por causa de uma poção mágica, mas por causa do impacto positivo que teve na vida dos outros.
    """

    analisador = AnalisadorTexto(texto)
    analisador.execute()
