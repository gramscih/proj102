# function

def print_pet_information(pet_type):
	print(f'I have my pet that is a {pet_type}')

print_pet_information('dog')
print_pet_information('cat')

# def make_full_name(firts_name: str, last_name: str) -> str:
# 	return firts_name + " " + last_name

def make_full_name(firts_name, last_name):
	if middle_name:
		return firts_name + " " + middle_name + " " + last_name
	else:
		return firts_name + " " + last_name

full_name = make_full_name('Gramsci', 'Hermozo')
print(full_name)

full_name = make_full_name('Gramsci', 'Hermozo', middle_name='Jaime')
print(full_name)

def make_pizza(*args, **kargs):
	print(args)
	print(kargs)

# make_pizza('pepperoni')
# make_pizza('extra cheese', 'green peppers', 'mushrooms')

make_pizza('for extra toppigs', 'other paramether', toppigs='chesse', toppigs2='mushrooms', toppigs3=['extra cheese', 'green peppers', 'mushrooms'])