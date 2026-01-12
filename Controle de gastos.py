import json
from time import sleep
gastos = []

def salvar_gastos():
    with open("gastos.json", "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, ensure_ascii=False, indent=4)


def carregar_gastos():
    global gastos
    try:
        with open("gastos.json", "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
    except FileNotFoundError:
        gastos = []





def gasto():
    nome = input("Diga o nome do gasto: ").strip().lower()
    try:
        preço = float(input("Diga o valor do gasto: "))
    except ValueError:
        print("Digite um valor !")
        return
    
    lista = {'nome': nome, 'preço': preço}
    gastos.append(lista)
    salvar_gastos()
    print(gastos)
    sleep(1)


def remover_gasto():
    if not gastos:
        print("Nao tem nenhum gasto")
        sleep(1)
        return
    
    print(gastos)
    remover = input("Diga o nome do gasto: ").strip().lower()
    for i in gastos:
        if i['nome'].lower() == remover:
            gastos.remove(i)
            salvar_gastos()
            print("Remoção bem sucedida !")
            return
    print(f"Nao foi possivel indentificar {remover}")
    sleep(1)


def ver_gastos():
    if not gastos:
        print("Nao tem nenhum gasto")
        sleep(1)
        return
    for i in gastos:
        print(f"{i['nome']} - R$ {i['preço']}")
        sleep(1)


def menu():
    while True:
        print("1 - Adicionar gastos")
        print("2 - Remover gastos")
        print("3 - Ver gastos")
        print("0 - sair")
        escolha = input("Oq deseja fazer?: ")

        if escolha == '0':
            break



        if escolha == '1':
            gasto()

        elif escolha == '2':
            remover_gasto()

        elif escolha == '3':
            ver_gastos()
        else:
            print("Escolha algo valido !")
            sleep(1)
            continue
            


carregar_gastos()
menu()


    
        


