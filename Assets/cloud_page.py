from flask import Flask, render_template, request, redirect, session, flash, url_for
import sqlite3


app = Flask(__name__)
app.secret_key = 'best-cloud'

db = sqlite3.connect('cadastro.db', check_same_thread=False)
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL             )
''')

db.commit()

@app.route('/')

def home():
    session['usuario_logado'] = None
    return render_template('index.html')

@app.route('/sobre')

def sobre():
    return render_template('sobre.html')

@app.route('/servico')

def servico():
    return render_template('servicos.html')

@app.route('/central_login')

def central_login():
    return render_template('login.html')

@app.route('/ajuda')

def ajuda():
    return render_template('ajuda.html')

@app.route('/cadastro')

def cadastro():
    return render_template('criar_conta.html')

@app.route("/pagamento")

def cadastar_cartao():
    return render_template("forma_pagamento.html")

@app.route('/cadastrar_user',methods=['POST','GET'],)    
def cadastrar_user():
    email = request.form['email']
    senha = request.form['senha']

    cursor.execute('''
        INSERT INTO usuarios (email, senha)
        VALUES (?, ?)
    ''', (email, senha))
    db.commit()

    return redirect(url_for('cadastar_cartao'))



@app.route("/login")

def login():
    return render_template('acessar_conta.html')

@app.route('/autenticar', methods=['POST','GET'])
def autenticar():

    email = request.form['email']
    senha = request.form['senha']

    # Verifica se o email e senha estão cadastrados no banco de dados
    cursor.execute('''
        SELECT * FROM usuarios WHERE email = ? AND senha = ?
    ''', (email, senha))
    usuario = cursor.fetchone()

    if usuario:
        session['usuario_logado'] = email
        flash(' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        if proxima_pagina == '/':
            proxima_pagina = '/home'
        return redirect(proxima_pagina)
    else:
        flash('E-mail ou Senha invalido')
        return redirect(url_for('login'))

@app.route('/home')

def home_logged():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('home_logged')))
    return render_template('pag_logada.html')

@app.route('/my_account')

def my_account():
    return render_template('minha_conta.html')

if __name__=='__main__':
    app.run(debug=True)

