import xml.etree.ElementTree as ET

data = '''
    <stuff>
        <users>
            <user>
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user>
                <id>002</id>
                <name>John</name>
            </user>
            <user>
                <id>003</id>
                <name>Mary</name>
            </user>
        </users>
    </stuff>
'''

tree = ET.fromstring(data)

users = tree.findall('users/user')
for user in users:
    user_id = user.find('id').text
    user_name = user.find('name').text
    print('{ id: %s, name: %s }' % (user_id, user_name))
