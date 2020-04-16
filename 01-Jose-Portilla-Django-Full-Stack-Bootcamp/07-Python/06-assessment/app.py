s = 'django'

print(s[0])
print(s[5])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])


lst = [3, 7, [1, 4, 'hello']]
lst[2][2] = 'goodbye'
print(lst)


d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
mySet = set(mylist)
print(mySet)


age = 4
name = 'Summy'
print("Hello my dog's name is {} and he is {} years old.".format(name, age))

