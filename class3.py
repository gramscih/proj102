# List

my_list = list()
my_list = []

names = ["jose", 'jaime', 'karla', 12] # 0, 1, 2 -> len = 3
# print(names[0].title())
# print(names[1])
# print(names[2])

# print(names[-1])
# print(names[-2])
# print(names[-3])

# Changing & Adding 
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati' # update
# print(motorcycles)
motorcycles.append('BMW')
# print(motorcycles)
motorcycles.insert(1, 'ktm')
# print(motorcycles)

# Removing
# print(motorcycles)
del motorcycles[0] # Take care with del keyword since if don;t define the index the varibale would be removed from the memory
# print(motorcycles)
motorcycles.remove('BMW') # Need to validate if the item is in the list
# print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'BMW']
motorcycles.sort()
print(motorcycles)
sorted_list = sorted(motorcycles)
sorted_str = sorted('bca')
# print(sorted_str)
# print(sorted_list)

# iteration List

# for motorcycle in motorcycles:
# 	print(motorcycle)


# for index in range(0, len(motorcycles)):
# 	print(motorcycles[index])

# Comprenhension List

upper_list = [item.upper() for item in motorcycles if item != 'BMW']
# print(upper_list)

# Tuple

tpl = tuple(upper_list)
# print(tpl)
tpl = ('elem1', 'elem2', 'elem3')

# print(tpl[1])
# print(tpl[-1])

# Accessing STR, LIST, TUPLE

names = ['Jose', 'Miguel', 'Carlos']
tpl = ('elem1', 'elem2', 'elem3')
my_str = 'Hello World'

# print(names[1:])
# print(names[:2])

# print(tpl[1:])
# print(tpl[:2])

# print(my_str[5:])
# print(my_str[:5])

new_str = [item for item in my_str if item != ' ']
# print(new_str)

# File Reader

# One way
file = open('txt_for_class3.txt')
#process
file.close()

# print(file.read())

# Sencond Way

with open('txt_for_class3.txt') as file:
	for line in file:
		print('***************************************************')
		print(line)



print(__name__ == '__main__')