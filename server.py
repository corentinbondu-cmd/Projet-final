from flask import Flask, render_template, jsonify, request, session
import time, csv
from flask_bcrypt import Bcrypt
from UserDAO import UserDAO
from MissionDAO import MissionDAO
from SymbolDAO import SymbolDAO
from pymongo import *

HTTP = 8080
app = Flask(__name__, static_url_path='/static')
app.secret_key = b'Y\xf1Xz\x00\xad|a\x1a\x10K'
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    SymbolDAO(MongoClient()).add_symbol("otan")
    return render_template('index.html')

@app.route("/map/")
def map():
    missions = MissionDAO(MongoClient()).get_all_mission()
    return render_template('map.html', missions = missions, missionsLen = len(missions))

@app.route("/liste-missions/")
def missions():
    missions = MissionDAO(MongoClient()).get_all_mission()
    return render_template('missions.html', missions = missions, longueur = len(missions))

@app.route("/admin/dashboard/")
def admIndex():
    if session :
        if int(session['rank']) == 0:
            print(UserDAO(MongoClient()).get_mission(session['login']))
            return render_template('admIndex.html')
    return render_template('500.html'), 500
    
@app.route("/admin/liste-missions/")
def admMissions():
    missions = MissionDAO(MongoClient()).get_all_mission()  
    return render_template('admMissions.html', missions = missions, longueur = len(missions))

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
            session['rank'] = user['rank']
            return jsonify(user)
        else:
            return jsonify({'error' : 'pw does not exist'})

@app.route("/api/add-user-csv/", methods=['POST'])
def apiAddUserCSV():
    with open('users.csv', 'r', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        users = [(row[0], row[1], int(row[2]), row[3], row[4], row[5], row[6]) for row in reader]
    newUsers = []
    for x in users:
        tmpPw = bcrypt.generate_password_hash(x[6])
        newUsers.append(UserDAO(MongoClient()).add_user(x[0], x[1], x[2], x[3], x[4], x[5], tmpPw))
    return jsonify({'isOk' : True})

@app.route("/api/add-user/", methods=['POST'])
def apiAddUser():
    jsDatas = request.get_json()
    tmpPw = bcrypt.generate_password_hash(jsDatas['password'])
    newUser = UserDAO(MongoClient()).add_user(jsDatas['firstname'], jsDatas['lastname'], jsDatas['rank'],  jsDatas['grade'], '',  jsDatas['login'], tmpPw)
    return jsonify({'isOk' : True})

@app.route("/api/user-logout")
def apiLogout():
    session.pop('login')
    return jsonify({'isOk' : True})

@app.route("/api/add-mission/", methods=['POST'])
def apiAddMission():
    jsDatas = request.get_json()
    users = UserDAO(MongoClient()).get_users()
    userLogin = []
    for x in range(len(users)):
        userLogin.append(users[x].get_login())
    newMission = MissionDAO(MongoClient()).add_mission(jsDatas['name'], jsDatas['country'], session['login'],  userLogin, [])
    return jsonify({'isOk' : True})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=HTTP, debug=True)