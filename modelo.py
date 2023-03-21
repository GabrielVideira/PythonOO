class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas, likes):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0


vingadores = Filme()
print(vingadores.nome)
