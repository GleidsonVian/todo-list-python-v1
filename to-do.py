filename = 'todo.txt'

def adicionar_tarefa(tarefa):
    with open(filename, 'a') as f_obj:
        f_obj.write(f"{tarefa}\n")

def listar_tarefa(filename=filename):
    print('')
    with open(filename, 'r') as f_obj:
        tarefa = f_obj.readlines()

    for i,t in enumerate(tarefa):
        print(f"{i+1}. {t.strip()}")
    print('')

def remover_tarefa(filename=filename):
    print('')
    with open(filename, 'r') as f_obj:
        tarefa = f_obj.readlines()

    for i,t in enumerate(tarefa):
        print(f"{i+1}. {t.strip()}")
    print('')

    remover = int(input("Indice da tarefa que deseja remover"))
    del tarefa[remover - 1]

    with open(filename, 'w') as f_obj:
        f_obj.writelines(tarefa)


def menu():
    while True:
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefa')
        print('3 - Remover tarefa')
        print('4 - Sair')
        descisao = input('Opção escolhida: \n')

        if descisao == '1':
            tarefa = input('Digite uma tarefa: \n')
            adicionar_tarefa(tarefa)
        elif descisao == '2':
            listar_tarefa()
        elif descisao == '3':
            remover_tarefa()
        elif descisao == '4':
            break

        else:
            print('Opção inválida, tente novamente.')

menu()

