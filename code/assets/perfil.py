import usuario


class Artista(usuario.Usuarios):
    def __init__(self, nickname, email, senha):
        super().__init__(nickname, email, senha)
        self.nomeAlbum = ""
        self.nomeMusica = ""
        self.duracao = ""
        self.nomeArtista = self.nickname

class Ouvinte(usuario.Usuarios):
    def __init__(self, nickname, email, senha):
        super().__init__(nickname, email, senha)
        self.nomeAlbum = ""