import yaml
import json

with open('data_test.json', 'r') as file:
    data = json.load(file)

user = data['user']
print(type(user))
print(user)
print(user['name'])

for role in user['roles']:
    print(role)

user['location']['state'] = 'Bangalore'
with open('data_test_edited.json' , 'w') as file:
    json.dump(user,file,indent=4)


