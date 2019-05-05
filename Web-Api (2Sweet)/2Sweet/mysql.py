from flask import Flask, jsonify, request, json 
from flask_mysqldb import MySQL 
from datetime import datetime
from flask_cors import CORS 
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root1'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '2sweet'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

@app.route('/users/register', methods=['POST'])
def register():
    cur         = mysql.connection.cursor()
    email       = request.get_json()['email']
    password    = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    fullname    = request.get_json()['fullname']
    gender      = request.get_json()['gender']
    birthday    = request.get_json()['birthday']
    pic         = request.get_json()['pic']

    cur.execute("INSERT INTO users (email, password, fullname, gender, birthday, pic ) VALUES ('" +
        str(email)    + "','" +
        str(password) + "','" +
        str(fullname) + "','" +
        str(gender)   + "','" +
        str(birthday) + "','" +
        str(pic)      + "')")
    
    mysql.connection.commit()

    result = {
        'email'   : email,
        'password': password,
        'fullname': fullname,
        'gender'  : gender,
        'birthday': birthday,
        'pic'     : pic
    }

    return jsonify({'result': result})

@app.route('/users/login', methods=['POST'])


def login():
    cur = mysql.connection.cursor()
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""

    cur.execute("SELECT * FROM users where email = '" + str(email) + "'")
    rv = cur.fetchone()

    if bcrypt.check_password_hash(rv['password'], password):
        access_token = create_access_token(identity = {'fullname': rv['fullname'], 'gender': rv['gender'], 'email': rv['email']})
        result = jsonify({"token":access_token})
    else:
        result = jsonify({"error": "Invalid username and password"})
    
    return result 

if __name__ == '__main__':
    app.run(debug=True)