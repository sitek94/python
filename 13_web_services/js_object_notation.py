import json

data = '''
    {
        "name": "Maciek",
        "age": 25,
        "isAuthorized": true,
        "roles": ["user", "admin"]
    }
'''

info = json.loads(data)

print('Name: ', info['name'])
print('Age: ', info['age'])
print('Authorized: ', info['isAuthorized'])
print('roles: ', info['roles'])
