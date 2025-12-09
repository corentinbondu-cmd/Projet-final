from pymongo import MongoClient
import csv


def main():
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
    add_user(db)
    
def add_user(db):
    with open('users.csv', 'r', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        users = [(int(row[0]), row[1], row[2]) for row in reader]
        
        usersToInsert = []

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

main()