from unicodedata import name



name = input('Name of the first person: ')
age = int(input('Age: '))
name2 = input('Name of the second person: ')
age2 = int(input('Age: '))

if age < age2:
    print(name + ' is younger than ' + name2)
elif age == age2:
    print(name  + 'is the same age than ' + name2 )
else:
    print(name + ' is older than ' + name2)

