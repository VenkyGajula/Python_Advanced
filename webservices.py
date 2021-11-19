import xml.etree.ElementTree as ET

data = '''
<person>
  <name>venky</name>
  <phone type="intl">+1 8899556622</phone>
  <email hide="Venky@0123" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('mobile:',tree.find('phone').text)
print('Email:', tree.find('email').get('hide'))

print("Looping through nodes")
input = '''
<stuff>
  <users>
    <user x="1">
      <id>01</id>
      <name>Venkatesh</name>
    </user>
    <user x="2">
      <id>02</id>
      <name>Ravi</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

print("***JSON(javaScript object-notation)")
import json
infor = '''
[
  { "id" : "101",
    "x" : "01",
    "name" : "venkatesh"
  } ,
  { "id" : "102",
    "x" : "02",
    "name" : "Hari"
  }
]'''

info = json.loads(infor)
print('User count:', len(info))

for item in info:
    print('Name :', item['name'])
    print('Id :', item['id'])
    print('Attribute :', item['x'])
