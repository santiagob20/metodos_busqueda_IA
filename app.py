from flask import Flask, render_template, request, redirect, url_for,flash,jsonify
from flask_mysqldb import MySQL
from flask_materialize import Material
import json


app = Flask(__name__)

# mysql connection
# app.config['MYSQL_HOST']= '10.32.3.6'
# app.config['MYSQL_USER']= 'root'
# app.config['MYSQL_PASSWORD']= 'Identidad2018@.'
# app.config['MYSQL_DB']= 'test'
# mysql = MySQL(app)

# datos de navegacion
app.secret_key='mysecretkey'

@app.route('/')
def Index():
    # cur =mysql.connection.cursor()
    # cur.execute('SELECT * FROM info')
    # data = cur.fetchall()
    # print(data)
    return render_template('index.html')
    # return render_template('index.html', contacts= data)


@app.route('/search_method', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        data = request.get_json()
        # flash('Contact added succesfully')
        # return jsonify(
        #     code=1,
        #     description='post 200',
        #     data= data
        # )
        print(data)
    return render_template('index.html')

# @app.route('/edit/<id>')
# def edit_contact(id):
#     cur = mysql.connection.cursor()
#     cur.execute('select * from info where id = %s',(id))
#     data = cur.fetchall()
#     return render_template('editcontact.html', contact= data[0])


# @app.route('/delete/<string:id>')
# def delete_contact(id):
#     cur = mysql.connection.cursor()
#     cur.execute('DELETE FROM info WHERE id = {0}'.format(id))
#     mysql.connection.commit()
#     flash('Contact deleted succesfully')
#     return redirect(url_for('Index'))

# @app.route('/update/<id>', methods=['POST'])
# def update(id):
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         phone = request.form['phone']
#         email = request.form['email']
#     cur = mysql.connection.cursor()
#     cur.execute("""UPDATE info 
#                 SET name = %s,
#                 email=%s,
#                 phone= %s 
#                 WHERE id = %s""",
#                 (fullname,email,phone,id))
#     mysql.connection.commit()
#     flash('Contact updated succesfully')
#     return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)
