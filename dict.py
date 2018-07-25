
person = {'name':'Donghee', 'address':'cheonan','e-mail':'jdhee4@naver.com'}
print(person)
print(person['name'])
print(person['e-mail'])
print(person.items())
for key, value in person.items():
    print("\n Key : " + key)
    print("\n value : " + value)

# key \ 'name'
# value \ 'Donghee'

for key, value in person.items():
    print("\n Key \ '" + key + "'")
    print("\n value \ '" + value + "'")
