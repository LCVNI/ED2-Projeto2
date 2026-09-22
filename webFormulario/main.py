from flask import Flask, render_template, request, redirect

app = Flask(__name__)

alunos = {}


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    matriucla = request.form["matricula"]
    aluno = {
        "nome": request.form["nome"],
        "matricula": matriucla,
        "curso": request.form["curso"],
        "semestre": request.form["semestre"],
        "email": request.form["email"]
    }

    alunos[matriucla] = aluno

    return redirect("/alunos") 


@app.route("/alunos")
def listar_alunos():

    return render_template(
        "alunos.html",
        alunos=alunos
    )

#def editar(matricula):
@app.route("/deletar", methods = ["POST"])
def deletar(matriucla):
    alunos.pop(matriucla)
    return alunos

if __name__ == "__main__":
    app.run(debug=True)