# Strings
variable = None
num = 0
name = ""

name = "gramsci hermozo"
print(name.title())
print(name.upper())
print(name.lower())

# Combining
age = 32
firts_name = "Gramsci"
last_name = "Hermozo"
full_name = firts_name + " " + last_name

# msg = "Hello, My name is " + firts_name + "I am " + age + "years old." # Invalid operation
# print(msg)

msg = "Hello, My name is " + firts_name + "I am " + str(age) + "years old."
print(msg)

print("This is the full name: ", full_name)
print("{} {} {}".format(firts_name, last_name, age))
print(f"{last_name} {firts_name}")
print("%s %s" % (last_name, firts_name))  # old mode

# tab & new line
print("Languges: \n\tPython \n\tjavascript \n\tc++")
print('Someone say "Hello"')
long_str = """sadfjasdjflsdjflasdkjflskajdflasjdflkjsadfkljasdlkfjlkasdjflkasdj
flksagjhlsdfjglsakjglksajdlfjaslkdjflsakjdflksjdflksjadf
lsdjkflskdjflksjdflskjdflsjdflsjdflsdjflsjdflsdjf
sldkjfslkjdflsjdflsjfdlsjdflsjdflsjfdlksdflsdfj"""

favorite_language = '    Python    '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# Numbers

nums = 1234567890

# Floats
flts = 1.2345656

# inputs
# name = input('Enter your name: ')
# print("Hello {}".format(name))

# Conditionals if ... else

number = 4

if number > 2:
	print("Number is bigger than 2.")
elif number < 2:
	print("Number is smaller than 2.")
else:
	print("Number is 2.")

msg = "Greter that 2" if number > 2 else "Smaller than 2."
print(msg)
