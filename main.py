from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime
import os

template_dir = os.path.abspath('.')
static_dir = os.path.abspath('.')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return redirect(url_for('pedido'))

@app.route('/pedido/', methods=["POST", "GET"])
def pedido():
    if request.method == "POST":
        data = datetime.now()
        data = str(data.day) + '/0' + str(data.month) + '/' + str(data.year)
        f = open('./pedido.txt', "w")
        f.write(f'{data}')
        f.close
        return render_template('aceito.html', data=str(data))
    else:
        f = open('./pedido.txt', "r")
        pedido = str(f.read())
        if pedido == 'nao-aceito':
            f.close
            return render_template('nao-aceito.html')
        else:
            f.close
            return render_template('aceito.html', data=pedido)

app.run(host='0.0.0.0', port=80)
