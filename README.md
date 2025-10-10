## TG1 – Streaming de Música  
Trabalho da disciplina **Programação Orientada a Dados – PUCRS**

## Descrição  
Sistema de streaming musical simplificado, inspirado em plataformas como o Spotify.  
Permite cadastrar e reproduzir músicas e podcasts, criar playlists personalizadas e gerar relatórios automáticos de uso.

## Alunos e Professor  
**Alunos:** Rafael Magalhães e Sofia Lahham

**Turma:** 11 – Programação Orientada a Dados (POD)  

**Professor:** Me. Otávio Parraga

## Estrutura de Pastas do Projeto

Abaixo está a estrutura principal do repositório, organizada em módulos e subpastas:

<img width="289" height="774" alt="image" src="https://github.com/user-attachments/assets/e028a680-c98c-4d94-93ae-7d5247a3b292" />

**Descrição:**
- `main.py` → ponto de entrada do sistema (onde o programa inicia).  
- `Streaming/` → contém todas as classes principais do sistema.  
- `config/` → arquivos `.md` com dados de exemplo e o script de leitura.  
- `relatorios/` → pasta onde é gerado o relatório final em `.txt`.  
- `logs/` → armazena erros do sistema.  
- `outros/` → arquivos de apoio e enunciado do trabalho.

## Como Executar o Projeto

1. Abra o terminal no diretório principal do projeto.  
2. Execute o comando:
   `python main.py`

## Execução e Importação de Dados (log)

Abaixo, um trecho do log gerado ao iniciar o sistema e importar os `.md` da pasta `config/` (modo `strict=False`):

WARN: Duração inválida para podcast 'Cinema em Debate': '0'. Ignorado (strict=False).

WARN: Playlist 'Relax' tem itens repetidos: ['Shape of You']. Mantendo uma ocorrência de cada.

WARN: Playlist 'Chill' ignorada: usuário 'joão' inexistente no banco de dados.

WARN: Playlist 'Favoritas' contém itens inexistentes: ['Shape of You', 'Música Inexistente']. Ignorados.

WARN: Playlist 'Treino' contém itens inexistentes: ['Rolling in the Deep']. Ignorados.

WARN: Playlist 'Relax' contém itens inexistentes: ['Shape of You']. Ignorados.

ERRO: Playlist 'Favoritas' contém item inexistente 'Shape of You'; removido.

ERRO: Playlist 'Favoritas' contém item inexistente 'Música Inexistente'; removido.

ERRO: Playlist 'Treino' contém item inexistente 'Rolling in the Deep'; removido.

ERRO: Playlist 'Relax' contém item inexistente 'Shape of You'; removido.

--- Importação concluída ---
Novos usuários: 3
Novas músicas: 5
Novos podcasts: 3
Novas playlists: 5

markdown
Copiar código

**Observações técnicas**  
- Os arquivos `.md` com valores inválidos são **ajustados ou ignorados** com aviso (`WARN`).  
- Itens inexistentes em playlists são **removidos** com registro de **erro** (`ERRO`).  
- Usuários referenciados que não existem são **ignorados** na criação de playlists.  
- A importação **continua** mesmo com inconsistências porque o parser está em `strict=False`.

## Menu Inicial

<img width="220" height="114" alt="image" src="https://github.com/user-attachments/assets/f9b98bff-1d92-4a9f-b04d-2e2e086934e6" />

O sistema inicia exibindo o menu principal com as opções:
1) Entrar como usuário, 2) Criar novo usuário, 3) Listar usuários, 4) Sair.


## Menu do Usuário

<img width="369" height="218" alt="image" src="https://github.com/user-attachments/assets/372b6a70-7990-441a-acde-fab040b5a59d" />

Após realizar o login, o sistema exibe o **Menu do Usuário**, responsável pelas principais operações do sistema.  
Cada opção representa uma funcionalidade prevista no TG1:

1. Reproduzir uma música  
2. Listar músicas  
3. Listar podcasts  
4. Listar playlists  
5. Reproduzir uma playlist  
6. Criar nova playlist  
7. Concatenar playlists  
8. Gerar relatório  
9. Carregar dados via arquivos Markdown  
10. Sair  

Essas opções são controladas pela classe `Menu`, localizada no pacote `Streaming/`, que gerencia as interações entre o usuário e as demais classes.


## Relatório Gerado

<img width="560" height="614" alt="image" src="https://github.com/user-attachments/assets/546e16f8-868e-4e27-be60-18214eea5c4e" />

O arquivo `relatorios/relatorio.txt` é gerado automaticamente pela classe `Analises`.  
Ele consolida todas as informações do sistema, apresentando:

- Total de usuários, músicas e playlists.  
- Top 10 músicas mais reproduzidas.  
- Playlist mais popular, com nome, criador e número de itens.  
- Usuário mais ativo, com base no histórico de reproduções.  
- Média de avaliações de cada música cadastrada.  

O relatório é criado no formato `.txt` e atualizado a cada nova execução do sistema.

## Funcionalidades do Sistema

O sistema implementa as funcionalidades exigidas no TG1, organizadas em categorias.

### Usuários
- Criação e login de usuários.
- Registro do histórico de mídias reproduzidas.
- Associação de playlists ao usuário logado.
- Implementado em `Streaming/usuario.py`.

### Mídias (músicas e podcasts no mesmo módulo)
- As classes `Musica` e `Podcast` são definidas no **mesmo arquivo**: `Streaming/arquivo_midia.py`.
- Ambas herdam de `ArquivoDeMidia`, compartilhando atributos e métodos como `reproduzir()`, `__str__` e `__repr__`.
- `Musica` possui sistema de **avaliações** (0 a 5).
- Durante a reprodução de músicas, o sistema exibe a **letra completa** da faixa (arquivos `.txt` em `config/`).

### Playlists
- Criação de playlists personalizadas por usuário.
- Adição e remoção de mídias por título (busca em `ArquivoDeMidia.registroMidia`).
- Reprodução completa da playlist.
- Concatenação de duas playlists com o operador `+`, unindo as mídias e somando as reproduções.
- Implementado em `Streaming/playlist.py`.

### Análises e Relatórios
- Top músicas por reproduções.
- Playlist mais popular.
- Usuário mais ativo (pelo histórico).
- Média de avaliações por música.
- Geração automática de `relatorios/relatorio.txt`.
- Implementado em `Streaming/analises.py`.

### Importação de Dados (Markdown)
- Leitura dos arquivos `.md` em `config/` para cadastrar usuários, mídias e playlists.
- Deduplicação por chave (nome/título) e validação com avisos/erros.
- Controlado por `config/lermarkdown.py` e pela função `importar_markdowns_para_main` em `main.py`.

### Inovação

Durante a reprodução de músicas, o sistema exibe a **letra completa da faixa** diretamente no terminal, tornando a experiência mais interativa e visual.  
Além disso, o programa utiliza leitura de arquivos Markdown para cadastrar automaticamente usuários, playlists e mídias, garantindo flexibilidade e escalabilidade no carregamento de dados.



## Demonstrações do Sistema

### Reprodução de Música
Abaixo estão alguns exemplos visuais do sistema em execução, ilustrando as principais etapas de funcionamento do projeto TG1 – Streaming de Música.

<img width="809" height="906" alt="image" src="https://github.com/user-attachments/assets/f5c3705f-1b0d-448e-a9ab-88a93dab1a1a" />

<img width="642" height="903" alt="image" src="https://github.com/user-attachments/assets/9ee24eff-42ab-40ec-84d7-070a6f407e68" />

<img width="564" height="306" alt="image" src="https://github.com/user-attachments/assets/d27692f7-6e20-4f83-99ec-92c658b1e4e2" />


Durante a execução de uma música, o sistema exibe o título, artista, duração e letra completa da faixa — recurso desenvolvido como inovação no projeto.  
Ao final da reprodução, o usuário é convidado a **avaliar a música** com uma nota de 0 a 5, registrada automaticamente no atributo `avaliacoes` da classe `Musica`.

Este comportamento é implementado no arquivo `Streaming/arquivo_midia.py`, dentro dos métodos:
- `reproduzir()` → responsável por imprimir a letra e incrementar o contador de reproduções;  
- `avaliar()` → solicita a avaliação do usuário e atualiza a média da faixa.


### Criação de Nova Playlist

O usuário logado pode criar uma nova playlist personalizada informando um nome.  
Após a confirmação, o sistema pergunta se o usuário deseja **adicionar mídias imediatamente**, permitindo incluir músicas ou podcasts existentes por título.

Neste exemplo, foi criada a playlist `PlaylistTeste` com a música “Shape of You”.  
Essa funcionalidade é implementada no método `criar_playlist()` da classe `Usuario` e controlada pela opção **6** do menu do usuário no `main.py`.

<img width="495" height="335" alt="image" src="https://github.com/user-attachments/assets/40f485e0-9011-4927-9a12-3168f77beec0" />
