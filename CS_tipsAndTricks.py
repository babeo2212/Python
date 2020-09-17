# # 1: Ternary Conditionals:
# condition = False
# x = 1 if condition else 0
# print (x)

# # 2: Underscore Placeholders (working w large numbers)
# num1 = 10_000_000_000
# num2 = 100_000_000

# total = num1 + num2

# print (f'{total:,}')

# 3: Context Managers: opening and closing the file 
## for managing resources
# with open('text.txt', 'r') as f: 
#     file_contents = f.read()

## use this instead of:
# f = open('text.txt', 'r')
# f.read()
# f.close()
# words = file_contents.split(' ')

# # 4: Enumerate: keeping tracks of index while looping
# names = ['Corey', 'Chris', 'Dave', 'Travis']

# for index, name in enumerate(names, start=1):
#     print (index, name)

# # 5: Zip: the zip func will stop at the shortest list exhausted
# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# for name, hero in zip(names, heroes):
#     print(f'{name} is actually {hero}.')

## 6: Unpacking
# a, b = (1, 2)
# print(a)
# print(b)

# a, _ = (1, 2) # using underscore to only unpack a = 1
# print(a)

# a, b, *c = (1, 2, 3, 4, 5)
# print(a) # 1
# print(b) # 2
# print(c) # [3, 4, 5]

# a, b, *c, d = (1, 2, 3, 4, 5)
# print(a) # 1
# print(b) # 2
# print(c) # [3, 4]
# print(d) # 5

# a, b, *_, d = (1, 2, 3, 4, 5)
# print(a) # 1
# print(b) # 2
# print(d) # 5

# # 7: Setattr/Getattr
# class Person():
#     pass

# person = Person()
# person_info = {'first': 'Hung', 'last': 'Vu'}
# for key, value in person_info.items():
#     setattr(person, key, value)
# print(person.first)
# print(person.last)

# for key in person_info.keys():
#     print(getattr(person, key))

# 8: GetPass #use for hiding script while runnning in shell
from getpass import getpass
username = input('Username: ')
password = getpass('Password: ') 
print('Loggin in..')

# 9: Python dash m (- m): running specific module that doesnot in the specific direction


# 10: Help/Dir 
