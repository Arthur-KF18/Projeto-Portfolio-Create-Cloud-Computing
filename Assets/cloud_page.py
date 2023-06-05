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

if __name__=='__main__':
    app.run(debug=True)

