class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie(Programa):
    def __init__(self, nome, ano, temporadas, likes):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)

print(
    f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}')
