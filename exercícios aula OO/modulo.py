class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def darLike(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, playlist):
        self.nome = nome.title()
        self._playlist = playlist

    def __getitem__(self, item):
        return self._playlist[item]

    def __len__(self):
        return len(self._playlist)

    def __str__(self):
        return f'{playlist_fim_de_semana}'

    @property
    def listagem(self):
        return self._playlist

    @property
    def tamanho(self):
        return len(self._playlist)


vingadores = Filme("vingadores: guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
atlanta.darLike()
atlanta.darLike()
vingadores.darLike()

filmes_e_series = [vingadores, atlanta]
playlist_fim_de_semana = Playlist('Playlist para o final de semana', filmes_e_series)

print(playlist_fim_de_semana.nome)
print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana.listagem:
    print(programa)