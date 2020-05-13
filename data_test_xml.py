import xml.etree.ElementTree as ET
with open('data_test.xml','r') as file:
    mytree= ET.parse(file)
    myroot= mytree.getroot()

user= myroot.find('user')
print(user.find('name').text)

for role in user.findall('roles'):
    print(role.text)

user.find('location').find('city').text = 'Bangalore'
user.find('location').find('state').text = 'Karnataka'
with open('data_test_edited.xml','w') as file:
    mytree.write(file, encoding='uncode')