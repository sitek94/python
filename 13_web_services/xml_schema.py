import xml.etree.ElementTree as ET

data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 733 123 534
        </phone>
        <email hide="yes"/>
    </person>
'''

tree = ET.fromstring(data)

print('Name: ', tree.find('name').text)
print('Email hidden: ', tree.find('email').get('hide'))
