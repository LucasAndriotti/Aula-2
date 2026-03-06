from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def inicio():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/sobre/fatec')
def sobre_fatec():
    return '''
    <h1>Página sobre a Fatec</h1>
    <p>Desenvolvida na Fatec</p>
    '''

@app.route('/cor/<cor1>')
def exibe_cor(cor1):
    return f'<h1 style="color:{cor1}">A cor escolhida foi: {cor1}</h1>'

@app.route('/cor/<cor1>/<cor2>')
def exibe_cor2(cor1, cor2):
    return f'<h1 style="color:{cor1}">A cor foi: {cor1} e <b style="color:{cor2}">{cor2}</b></h1>'

@app.route('/codigos/<int:ano_nascimento>')
def exibe_codigos(ano_nascimento):
    dados = {
        'nome' : "Lucas",
        'ano_nascimento' : ano_nascimento,
        'idade' : (2026 - ano_nascimento),
        'texto' : "Vamos escrever um texto bem longo para que o truncate funcione!",
        'ativo' :'erro',
        'pessoas' : ['Lucas', 'Rafel', 'Douglas']
    }

    return render_template('codigos.html', **dados)

@app.route('/home')
def home():
    return render_template('blocos/home.html')

@app.route('/produtos')
def produtos():
    return render_template('blocos/produtos.html')

@app.route('/perfil')
def perfil():
    return render_template('blocos/perfil.html')

if __name__ == '__main__':
    app.run(debug=True)