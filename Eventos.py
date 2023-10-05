import os

from util import inscricao


def inscrever(matricula, nome, email):
    with open("inscricoes.dat", "a") as file:
        file.write(f"{matricula}; {nome}; {email}\n")

def listar_inscritos():
    with open("inscricoes.dat", "r") as file:
        for line in file:
            matricula, nome, email = line.strip().split("; ")
            print(f"Matrícula: {matricula}, Nome: {nome}, Email: {email}")

def entrar_evento(matricula, horario):
    with open("entradas.dat", "a") as file:
        file.write(f"{matricula}; {horario}\n")

while True:
    print("1- Inscrições")
    print("2- Listar Inscritos")
    print("3- Entrar no Evento")
    print("4- Saída do Evento")
    print("5- Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        matricula = input("Digite a matrícula: ")
        nome = input("Digite o nome completo: ")
        email = input("Digite o email: ")
        inscrever(matricula, nome, email)
        print("Inscrição realizada com sucesso!")
    elif escolha == "2":
        listar_inscritos()
    elif escolha == "3":
        matricula = input("Digite a matrícula do participante: ")
        horario = input("Digite o horário de entrada: ")
        entrar_evento(matricula, horario)
        print("Entrada registrada com sucesso!")
    elif escolha == "4":  
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
