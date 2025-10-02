
    # ---------------------- Carregamento via Markdown ---------------------- #
    @classmethod
    def carregar_Markdown(cls, caminho_markdown, catalogo: dict):
        """
        Lê um arquivo .md e retorna uma LISTA de objetos Playlist.

        Formatos aceitos (tolerantes):
        1) Blocos iniciados por um cabeçalho contendo 'playlist' (ex.: '## Playlist', '### PLAYLIST').
           Dentro do bloco, chaves simples:
              nome: Minha Mix
              usuario: Rafael
              itens: [Titulo 1; Titulo 2; Titulo 3]
           - 'itens' pode estar em linha única (entre []), separados por ',' ou ';'
           - OU em linhas abaixo com '-' (bullets), até linha em branco ou próxima chave/cabeçalho.

        2) Também aceita bullets após a linha 'itens:' assim:
              itens:
                - Titulo 1
                - Titulo 2
        """
        playlists = []
        p = Path(caminho_markdown)
        if not p.exists():
            _log_erro(f"carregar_Markdown: arquivo não encontrado: {caminho_markdown}")
            return playlists

        try:
            linhas = p.read_text(encoding="utf-8").splitlines()
        except Exception as e:
            _log_erro(f"carregar_Markdown: erro ao ler '{caminho_markdown}': {e}")
            return playlists

        def is_header_playlist(linha: str) -> bool:
            s = (linha or "").strip().lower()
            if not s.startswith("#"):
                return False
            return "playlist" in s

        def parse_list_inline(payload: str):
            # Ex.: "[a, b; c]" => ["a","b","c"]
            s = (payload or "").strip()
            if s.startswith("[") and s.endswith("]"):
                s = s[1:-1]
            # separa por ';' ou ','
            partes = []
            for chunk in s.replace(";", ",").split(","):
                t = chunk.strip()
                if t:
                    partes.append(t)
            return partes

        i = 0
        n = len(linhas)
        while i < n:
            linha = linhas[i]
            if is_header_playlist(linha):
                # novo bloco
                i += 1
                nome = ""
                usuario = ""
                itens_nomes = []

                # lê até próximo cabeçalho ou EOF
                while i < n and not is_header_playlist(linhas[i]):
                    atual = linhas[i].strip()

                    # chaves simples "nome:" / "usuario:" / "itens:"
                    if atual.lower().startswith("nome:"):
                        nome = atual.split(":", 1)[1].strip()
                    elif atual.lower().startswith("usuario:"):
                        usuario = atual.split(":", 1)[1].strip()
                    elif atual.lower().startswith("itens:"):
                        resto = atual.split(":", 1)[1].strip()
                        if resto:  # pode ser inline [a, b; c]
                            itens_nomes.extend(parse_list_inline(resto))
                        else:
                            # ler bullets seguintes
                            j = i + 1
                            while j < n:
                                prox = linhas[j].strip()
                                if not prox:  # linha em branco termina a lista
                                    break
                                if prox.lower().startswith(("nome:", "usuario:", "itens:")):
                                    break
                                if prox.startswith("-"):
                                    titulo = prox[1:].strip()
                                    if titulo:
                                        itens_nomes.append(titulo)
                                    j += 1
                                    continue
                                # parou se não é bullet e não é chave
                                break
                            i = j - 1  # o loop externo vai fazer i += 1
                    i += 1

                # construir objeto
                pl = cls(nome=nome, usuario=usuario)
                # resolver itens via catálogo
                for titulo in itens_nomes:
                    if not pl.adicionar_midia(titulo, catalogo):
                        # erro já logado por adicionar_midia
                        pass
                playlists.append(pl)
                continue

            i += 1

        if not playlists:
            _log_erro(f"carregar_Markdown: nenhum bloco de playlist encontrado em '{caminho_markdown}'.")
        return playlists
