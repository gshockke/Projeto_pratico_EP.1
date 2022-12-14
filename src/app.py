from flask import Flask, render_template
# from dotenv import load_dotenv
# import os
# load_dotenv()

app = Flask(__name__)


# @app.route("/")
# def base():
#     return render_template("base.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/resumo')
def resumo():
    return render_template("resumo.html")

@app.route('/formacao')
def formacao():
    return render_template("formacao.html")

@app.route('/historico')
def historico():
    return render_template("historico.html")

if __name__=='__main__':
    app.run(host='0.0.0.0')  
