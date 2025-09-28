# main.py

import sys
from menu import Menu  # se a classe Menu estiver no mesmo arquivo, pode remover este import

def main():
    menu = Menu()
    usuarios = []  # lista inicial de usuários (será melhorada futuramente)
    usuario_logado = None

    while True:
        if not usuario_logado:
            # Exibe menu inicial
            opcao = menu.exibir_menu_inicial()

            match opcao:
                case "1":
                    if not usuarios:
                        print("Nenhum usuário cadastrado. Crie um novo usuário primeiro.")
                    else:
                        print("Usuários disponíveis:")
                        for i, u in enumerate(usuarios, start=1):
                            print(f"{i} - {u}")
                        try:
                            escolha = int(input("Digite o número do usuário: "))
                            if 1 <= escolha <= len(usuarios):
                                usuario_logado = usuarios[escolha - 1]
                                print(f"Usuário '{usuario_logado}' logado com sucesso!")
                            else:
                                print("Opção inválida.")
                        except ValueError:
                            print("Entrada inválida. Digite apenas números.")

                case "2":
                    novo_usuario = input("Digite o nome do novo usuário: ").strip()
                    if novo_usuario:
                        usuarios.append(novo_usuario)
                        print(f"Usuário '{novo_usuario}' criado com sucesso!")
                    else:
                        print("Nome de usuário não pode ser vazio.")

                case "3":
                    if not usuarios:
                        print("Nenhum usuário cadastrado.")
                    else:
                        print("=== LISTA DE USUÁRIOS ===")
                        for u in usuarios:
                            print("-", u)

                case "4":
                    print("Saindo do sistema...")
                    sys.exit()

                case _:
                    print("Opção inválida. Tente novamente.")

        else:
            # Exibe menu do usuário logado
            opcao = menu.exibir_menu_usuario(usuario_logado)

            match opcao:
                case "1":
                    print("Reproduzir uma música (função ainda não implementada)")
                case "2":
                    print("Listar músicas (função ainda não implementada)")
                case "3":
                    print("Listar podcasts (função ainda não implementada)")
                case "4":
                    print("Listar playlists (função ainda não implementada)")
                case "5":
                    print("Reproduzir uma playlist (função ainda não implementada)")
                case "6":
                    print("Criar nova playlist (função ainda não implementada)")
                case "7":
                    print("Concatenar playlists (função ainda não implementada)")
                case "8":
                    print("Gerar relatório (função ainda não implementada)")
                case "9":
                    print(f"👤 Usuário '{usuario_logado}' saiu da conta.")
                    usuario_logado = None
                case _:
                    print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

