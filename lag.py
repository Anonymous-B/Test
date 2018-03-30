#strings
print('Hello World')
msg = 'Hello World'
print(msg)
firstName = 'Bilal'
lastName = 'Ahmed'
fullName = firstName + ' ' + lastName
print(fullName)

#lists
bikes = ['trek', 'redline', 'gaint']
firstBike = bikes[0]
lastBike = bikes[-1]

for bike in bikes:
    print(bike)

square = []
for x in range(1, 11):
    square.append(x**2)

print(square)

square = [x**2 for x in range(1, 11)]
print(square)

finsher = ['bil', 'mon','pola']
firstTwo = finsher[:2]
print(firstTwo)

bikez = bikes[:]

print(bikez)

dim = (1920, 1080)
x = 1
if x == 1:
    print(dim)


if 'do' not in bikes:
    print('trek')

dic ={'key1': 1, 'key2': 2}
print(dic)

print(dic['key1'])

