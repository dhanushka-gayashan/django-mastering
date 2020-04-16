mystring = 'Dhanushka'

print(mystring[0])
print(mystring[-1])
print(mystring[:5])
print(mystring[2:])
print(mystring[::2])
print(mystring.upper())
print(mystring.lower())


mystring = 'Hello World'

x = mystring.split(' ')
print(x[0])
print(x[1])


mystring = '{} is {} years old'.format('dhanushka', 33)
print(mystring)

mystring = '{name} is {age} years old'.format(age=33, name='dhanushka')
print(mystring)
