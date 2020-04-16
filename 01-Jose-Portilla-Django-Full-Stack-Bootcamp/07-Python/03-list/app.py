mylist = ['a', 'b', 'c']

print(mylist[0])
print(mylist[1])
print(mylist[2])


mylist[2] = 'Cat'
print(mylist)


mylist.append('Dog')
print(mylist)


mylist.append(['Apple', 'Orange'])
print(mylist)


mylist.extend(['Java', 'Golang', 'Python'])
print(mylist)


mylist.pop()
print(mylist)


mylist.reverse()
print(mylist)


mylist = [7, 4, 2, 9, 1, 8, 3, 0, 5, 6]
mylist.sort()
print(mylist)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)
