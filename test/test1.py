age = int(input('Enter your age: '))
year = 2017
born = year - age
print('You was born in ', born)
i = 0
while born < year - 1:
    born = born + 1

    i = i + 1
    print('In', born, 'you was', i, 'years old')
else :
    print('In this', year, 'year you are', age, 'years old')