from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def pag_cadastro():
    return render_template("cadastro.html")

app.run(debug=True)