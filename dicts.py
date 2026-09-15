def cadastrarAluno():
    nomeAluno = input("Nome do aluno: ")
    matricula = input("Matricula: ")
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
        resp = input("Cadastrar outra nota? s/n")
        if resp == "n":
            break
    return nomeAluno, matricula, notas

if __name__ == "__main__":
    alunos = []
    while True:
        nome, matr, notas = cadastrarAluno()
        novoAluno = {
            "nome": nome,
            "matricula": matr,
            "notas": notas,
        }
        alunos.append(novoAluno)
        resp = input("Cadastrar outro aluno? s/n")
        if resp == 'n':
            break
    
        