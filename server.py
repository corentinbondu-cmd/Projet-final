from flask import Flask, render_template, jsonify, request, session
import time, csv
from flask_bcrypt import Bcrypt
from UserDAO import UserDAO
from pymongo import *

HTTP = 8080
app = Flask(__name__, static_url_path='/static')
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    '''apiAddUserCSV()'''
    return render_template('index.html')

@app.route("/api/user-login", methods=['POST', 'GET'])
def apiLogin():
    jsDatas = request.get_json()
    hashedPw = bcrypt.generate_password_hash(jsDatas['password'])
    login = jsDatas['login']
    user = UserDAO(MongoClient()).get_one_user_by_login(login)[0]
    if not user:
        return jsonify({'error' : 'User does not exist'})
    else:
        if bcrypt.check_password_hash(user['password'], jsDatas['password']):
            user['password'] = ''
            session['login'] = user['login']
            return jsonify(user)
        else:
            return jsonify({'error' : 'pw does not exist'})

@app.route("/api/add-user-csv/", methods=['POST'])
def apiAddUserCSV():
    with open('users.csv', 'r', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        users = [(row[0], row[1], row[2]) for row in reader]
    newUsers = []
    for x in users:
        newUsers.append(UserDAO(MongoClient()).add_user(x[0], x[1], x[2]))
    return jsonify({'isOk' : True})

@app.route("/api/add-user/", methods=['POST'])
def apiAddUser():
    jsDatas = request.get_json()
    newUser = UserDAO(MongoClient()).add_user(jsDatas['firstname'], jsDatas['lastname'], jsDatas['firstname'][0].lower() + '.' + jsDatas['lastname'].lower())
    return jsonify({'isOk' : True})

@app.route("/api/user-logout")
def apiLogout():
    session.pop('login')
    return jsonify({'isOk' : True})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=HTTP, debug=True)