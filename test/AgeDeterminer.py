import datetime

adultAge = 29

age = input('Your age: ')
yearOfBirthday = datetime.datetime.now().year - int(age)
print(f'You was born on {yearOfBirthday} or {yearOfBirthday - 1}')

print(f"You are so {('young', 'old')[int(age) > adultAge]}.")
















