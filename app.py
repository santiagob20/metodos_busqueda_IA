from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# from flask_mysqldb import MySQL
import json
from algorithms import Algorithms

app = Flask(__name__)

# datos de navegacion
app.secret_key = 'mysecretkey'

alg = Algorithms()


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/search_method', methods=['POST'])
def search_method():
    exec_alg= None
    if request.method == 'POST':
        data = json.loads(request.data)
        
        if data['method']=='bpa':
            exec_alg = alg.bpa(data['ei'],data['ef'])
        if data['method']=='bpp':
            exec_alg = alg.bpp(data['ei'],data['ef'],data['bpp_limit'])
        if data['method']=='hill':
            exec_alg = alg.hill_climbing(data['ei'],data['ef'])
        if data['method']=='ram':
            exec_alg = alg.branch(data['ei'],data['ef'])
        if data['method']=='a*':
            exec_alg = alg.asterisk(data['ei'],data['ef'])
        if data['method']=='gen':
            exec_alg = alg.genetic(data['ei'],data['ef'])
    return jsonify(
        code=1,
        description='post 200',
        data= exec_alg
    )


if __name__ == '__main__':
    app.run(port=5000, debug=True)
