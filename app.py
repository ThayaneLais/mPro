from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/prioridades")
def prioridades():
    return render_template('prioridades/prioridades.html')

@app.route("/resultados")
def resultados():
    return render_template('resultados/resultados.html')

app.run()