# Dictionary

my_dict = dict()
my_dict = {}

person = {'name': 'Gramsci', 'last_name': 'Hermozo', 2: 'two'}
print(person['name'])
last_name = person.get('last_namee', 'This person not have a last name')
print(last_name)
print(person[2])

print(person.keys())
print(person.values())

person['name'] = 'Alvaro'
person['age'] = 32
print(person)

for key, value in person.items():
	print(key, value)

for key in person.keys():
	print(key)

for value in person.values():
	print(value)

# Set
my_set = set() # {}

my_set.add(3)
my_set.add(5)
my_set.add(5)
my_set.add(7)
my_set.add(9)
print(my_set)
my_set.remove(9)
print(my_set)
