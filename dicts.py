import subprocess
import time
def cadastrarAluno():
    nomeAluno = input("Nome do aluno: ")
    while True:
        matricula = input("Matricula: ")
        if matricula in alunos:
            print("Matricula ja cadastrada!")
            time.sleep(3)
            subprocess.run('cls', shell=True)
        else:
            break
    curso = input("Curso: ")
    notas = []
    i = 0
    while True:
        i = i + 1
        nota = float(input(f"Nota {i}: "))
        if nota > 10 or nota < 0:
            print("Nota fora do escopo")
            i = i-1
        else:
            notas.append(nota)
            if i == 3:
                break
    #time.sleep(1)
    subprocess.run('cls', shell=True)
    return nomeAluno, matricula, curso, notas

def consultarAluno(consulta):
    if consulta in alunos:
        dados = alunos[consulta]
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")


if __name__ == "__main__":
    alunos = {}
    while True:
        nome, matr, curso,  notas = cadastrarAluno()
        novoAluno = {
            "nome": nome,
            "curso": curso,
            "notas": notas,
        }
        alunos[matr] = novoAluno
        resp = input("Cadastrar outro aluno? s/n \n")
        if resp == 'n':
            break
        print("Consultar alunos cadastrados (por matriucla)? s/n")
        resp = input()
        if resp == 's':
         consulta = input("Informar matriucla: ")
         consultarAluno(consulta)
    '''print("Alunos:")
    for matr, dados in alunos.items():
        print(f"{matr}: " + f"{dados['nome']} " + f"Curso {curso}" + f"Notas: {dados['notas']}")'''
    