from flask import Flask, render_template, jsonify, request
import time, csv
from UserDAO import UserDAO
from pymongo import *

HTTP = 8080
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    users = UserDAO(MongoClient()).get_users()
    return render_template('oui.html', users = users)

@app.route("/api/user-login", methods=['POST', 'GET'])
def apiLogin():
    jsDatas = request.get_json()
    errors = {}
    if jsDatas['name'] != 'Cuvelier' and jsDatas['pw'] != 'aaaaa':
        errors['error_id'] = True
    return jsonify(errors)

'''@app.route("/api/add-user/", methods=['POST'])
def apiAddUser():
    csvPath = request.json
    print(csvPath)
    print("Script gestion de la BDD Mongo.")
    client = MongoClient()
    db = client['Project']
    collToAdd = ['users', 'missions', 'userMission']
    for i in range(len(collToAdd)):
        try: 
            db.create_collection(collToAdd[i])
            print(f'collection {collToAdd[i]} created')
        except Exception as ex:
            print(ex)
    with open('users.csv', 'r', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        users = [(int(row[0]), row[1], row[2]) for row in reader]

    for x in users:
        newUser = {}
        newUser['_id'] = x[0]
        newUser['firstname'] = x[1]
        newUser['lastname'] = x[2]
        try:
            db.users.insert_one(newUser)
            print(f'{newUser} added')
        except:
            print(f'{newUser} already exists')
    return jsonify({'isOk' : True})'''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=HTTP, debug=True)