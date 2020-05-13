import yaml

with open('data_test.yaml', 'r') as file:
    data = yaml.safe_load(file)

user = data['user']
print(type(user))
print(user)
print(user['name'])

for role in user['roles']:
    print(role)

user['location']['state'] = 'Bangalore'
with open('data_test_edited.yaml' , 'w') as file:
    yaml.dump(user,file, default_flow_style=False)