# midia.py

from datetime import datetime
from pathlib import Path

# =========================
# Utilitário simples de log
# =========================
_LOG_PATH = Path("logs") / "erros.log"

def _log_error(msg: str) -> None:
    """Registra mensagens de erro em logs/erros.log com timestamp."""
    try:
        _LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        carimbo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with _LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(f"[{carimbo}] {msg}\n")
    except Exception:
        # Falha silenciosa de log para não quebrar o fluxo do programa.
        pass


def _fmt_duracao(segundos: int) -> str:
    """Formata duração em segundos para mm:ss (ou hh:mm:ss se > 1h)."""
    if segundos < 0:
        segundos = 0
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    if h > 0:
        return f"{h:01d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


# ======================
# Classe base: Mídia
# ======================
class ArquivoDeMidia:
    """
    Classe de um arquivo de mídia genérico (música, podcast, álbum, etc.)
    A igualdade (__eq__) considera apenas título e artista, sendo case insensitive.
    Duração em segundos (int). Reproduções (int) inicia em zero.
    Atributos adicionais são definidos nas subclasses.
    """

    def __init__(self, titulo: str, duracao: int, artista: str, reproducoes: int = 0):
        
        # Realizando validações e registrando os problemas em log
        titulo_norm = (titulo or "").strip()
        artista_norm = (artista or "").strip()

        if not titulo_norm:
            _log_error("ArquivoDeMidia: título vazio informado; usando 'Não informado'.")
            titulo_norm = "Não informado"

        if not artista_norm:
            _log_error("ArquivoDeMidia: artista vazio informado; usando 'Não informado'.")
            artista_norm = "Não informado"

        if not isinstance(duracao, int):
            _log_error(f"ArquivoDeMidia: duração não inteira '{duracao}'; convertendo para inteiro.")
            duracao = int(duracao)

        if duracao < 0:
            _log_error(f"ArquivoDeMidia: duração negativa {duracao}; ajustando valor para 0.")
            duracao = 0
                
        self.titulo = titulo_norm
        self.duracao = duracao               # duração em segundos (int)
        self.artista = artista_norm
        self.reproducoes = reproducoes       # contador de execuções iniciado em zero

    # Métodos obrigatórios especiais
    #  simula a execução do arquivo de mídia, mostra na tela as informações contendo título, artista e duração
    def reproduzir(self) -> None:
        """Simula a execução do arquivo de mídia, incrementando reproduções e exibindo info."""
        self.reproducoes += 1
        print(f"-> Reproduzindo: '{self.titulo}' — {self.artista} [{_fmt_duracao(self.duracao)}]")

    #  Compara dois arquivos de mídia (mesmo título e artista).
    def __eq__(self, other) -> bool:
        """Dois arquivos são iguais se título e artista forem iguai, ignora espaços e case."""
        # Trata comparação com outros tipos 
        if not isinstance(other, ArquivoDeMidia):
            return NotImplemented
        
        #Retorna True se título e artista forem iguais, ignorando espaços e case
        return (self.titulo.strip().lower() == other.titulo.strip().lower() and
                self.artista.strip().lower() == other.artista.strip().lower())

    # Métodos obrigatórios para todos 
    # ToString
    def __str__(self) -> str:
        return (f"A midia {self.titulo} do artista {self.artista} | "
                f" com duração de {self.duracao} segundos | "
                f" tocou: {self.reproducoes} vezes")

    # Representação oficial
    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return (f"{cls}(titulo='{self.titulo}', duracao={self.duracao}, "
                f"artista='{self.artista}', reproducoes={self.reproducoes})")


# Subclasse obrigatória: Música
class Musica(ArquivoDeMidia):
    """
    Classe música.
    - genero: string (Rock, Pop, Rap, Clássico, etc.)
    - avaliacoes: lista com notas inteiras de 0 a 5
    """

    def __init__(self, titulo: str, duracao: int, artista: str,
                 genero: str = "Desconhecido", reproducoes: int = 0,
                 avaliacoes=None):
        super().__init__(titulo, duracao, artista, reproducoes)
        self.genero = (genero or "Não informado").strip().title()
        self.avaliacoes = list(avaliacoes) if isinstance(avaliacoes, list) else []

    def avaliar(self, nota: int) -> bool:
        """
        Adiciona uma nota de 0 a 5. Caso fora do intervalo ou inválida, registra erro no log.
        Retorna True se adicionou; False caso contrário.
        """
        if not isinstance(nota, int):
            _log_error(f"Musica.avaliar: nota não inteira '{nota}' para '{self.titulo}'.")
            return False
      
        if nota < 0 or nota > 5:
            _log_error(f"Musica.avaliar: nota fora do intervalo 0 a 5 ({nota}) para '{self.titulo}'.")
            return False
       
        self.avaliacoes.append(nota)
        return True

    # Métodos obrigatórios gerais
    # ToString
    def __str__(self) -> str:
       # Calcula a média das avaliações
        if self.avaliacoes:
            avg = sum(self.avaliacoes) / len(self.avaliacoes)
        else:
            avg = 0
       
        return (f"A música {self.titulo} do {self.artista}, |"
               f"estilo {self.genero} com duração de {self.duracao} segundos. |"
               f"Possui {len(self.avaliacoes)} avaliações com média de: {avg:.2f}")

    # Representação oficial
    def __repr__(self) -> str:
        return (f"Musica(titulo='{self.titulo}', duracao={self.duracao}, artista='{self.artista}', "
                f"genero='{self.genero}', reproducoes={self.reproducoes}, "
                f"avaliacoes={self.avaliacoes})")


# Subclasse obrigatória: Podcast
class Podcast(ArquivoDeMidia):
    """
    Classe de episódio de podcast.
    - episodio: inteiro com o número do episódio
    - temporada: string com o nome da temporada
    - host: string com o nome do apresentador
    """

    def __init__(self, titulo: str, duracao: int, artista: str,
                 episodio: int, temporada: str, host: str,
                 reproducoes: int = 0):
        super().__init__(titulo, duracao, artista, reproducoes)

        if not isinstance(episodio, int) or episodio < 1:
            _log_error(f"Podcast: número de episódio inválido '{episodio}' para '{self.titulo}'; ajustando para 1.")
            episodio = 1

        self.episodio = episodio
        self.temporada = (temporada or "Temporada").strip()
        self.host = (host or "Não informado").strip()

    # Métodos obrigatórios gerais
    # ToString
    def __str__(self) -> str:
        return (f"O Podcast {self.titulo} do artista {self.artista} |"
                f"Temporada:{self.temporada}, Episódio:{self.episodio} |"
                f"Apresentado por {self.host} |"
                f"Duração de {self.duracao} segundos, tocou: {self.reproducoes} vezes")

    # Representação oficial
    def __repr__(self) -> str:
        return (f"Podcast(titulo='{self.titulo}', duracao={self.duracao}, artista='{self.artista}', "
                f"episodio={self.episodio}, temporada='{self.temporada}', host='{self.host}', "
                f"reproducoes={self.reproducoes})")
