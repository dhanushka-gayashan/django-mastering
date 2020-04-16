x = 110
if x > 100:
    print("Hurraaaa....")
elif x > 50:
    print('Not bad')
else:
    print('So Bad')


seq = [1, 2, 3, 4, 5]
for i in seq:
    print(i)


marks = {"Dhanushka": 90, "Gayashan": 80, 'Chamari': 95}
for k in marks:
    print(marks[k])


mypairs = [(1, 2), (3, 4), (5, 6)]
for v1, v2 in mypairs:
    print(str(v1) + " " + str(v2))


i = 1
while i < 5:
    print(i)
    i += 1


for i in range(1, 10):
    print(i)

for i in range(1, 10, 3):
    print(i)


for i in range(10):
    print(i)


x = range(21)
out = [i*2 for i in x if i % 2 == 0]
print(out)
