# Streaming_POD_Rafael_Sofia

Sistema de streaming musical simplificado, inspirado em plataformas como o Spotify.

Alunos: Rafael Magalhães e Sofia Lahham

Turma 11 - Programação Orientada a Dados (POD)

Professor: Me. Otávio Parraga

**Inovação:**  
Durante a reprodução de músicas, o sistema exibe a letra completa da faixa na tela.


## Estrutura de Pastas do Projeto

Abaixo está a estrutura principal do repositório, organizada em módulos e subpastas:


<img width="433" height="658" alt="image" src="https://github.com/user-attachments/assets/6da4e6bc-d98c-46d6-b7bd-23045505bbbd" />

**Descrição:**
- `main.py` → ponto de entrada do sistema (onde o programa inicia).  
- `Streaming/` → contém todas as classes principais do sistema.  
- `config/` → arquivos `.md` com dados de exemplo e o script de leitura.  
- `Relatório/` → pasta onde é gerado o relatório final em `.txt`.  
- `outros/` → arquivos de apoio e enunciado do trabalho.

## Funcionalidades do Sistema

O projeto implementa as principais funcionalidades solicitadas no TG1, organizadas por categoria:

### Usuários
- Criação de novos usuários.  
- Login e gerenciamento do usuário ativo.  
- Histórico de músicas reproduzidas.

### Músicas e Podcasts
- Cadastro e reprodução de músicas e episódios de podcast.  
- Armazenamento de informações como título, artista, duração e gênero.  
- Sistema de avaliação de músicas (notas de 0 a 5).  

### Playlists
- Criação de playlists personalizadas associadas a cada usuário.  
- Adição e remoção de mídias dentro das playlists.  
- Reprodução completa das playlists.  
- Concatenação de duas playlists com o operador `+`, unindo as mídias e somando as reproduções.  

### Análises e Relatórios
- Identificação das músicas mais reproduzidas.  
- Usuário mais ativo do sistema.  
- Playlist mais popular.  
- Média de avaliações das músicas.  
- Geração automática de relatório em `Relatório/relatorio.txt`.  

### Inovação
Durante a reprodução de músicas, o sistema exibe a **letra completa da faixa** na tela, tornando a experiência mais envolvente e interativa.
