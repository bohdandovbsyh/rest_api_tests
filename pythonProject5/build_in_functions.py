"""

My beautiful code

"""

# print(abs(5))


# print(all(names))
# print(any(names))
# print(bin(9999990))
# print(bool(1))
# print(bin(10))
# print(bytes(10))

# def my_string_function():
#     pass
# print(callable(my_string_function))
# print(chr(45987))
# my_new_dict_1 = {'name': 'Viktor', 'age': 45}
# my_new_dict = dict(my_new_dict_1)
# print(my_new_dict)
# my_another_var = 0
# # print(__doc__)
# print(dir(my_another_var))

# print(list(enumerate(names)))
# for index, name in enumerate(names):
#     print(f'{index}: {name}')
# eval('1 + 2 /0')
names = ['Victor', 'Peter', 'Homer', 'Vanessa', 'Volodymir']
salaries = [5000, 4000, 3000, 5500, 9000, 10]

# my_dict = {'name': 'Oleh', 'age': 45}
# list(filter(lambda salary: salary >= 5000, salaries))
# print(salaries)
# print(frozenset([1, 2, 3, 1]))
# print(globals())
# print(help('random'))
# print(hex(7800))
# print(int(1.9))
# print(len(salaries))
# def my_func():
#     a = 0
#     b = 1
#     print(locals())
# my_func()

# salaries = [5000, 4000, 3000, 5500, 6500, 10]
# salaries.sort()
#
# sorted_salaries = sorted(salaries, key=lambda salary: salary > 1000, reverse=True)
# sorted_salaries_2 = sorted(salaries, key=lambda salary: salary > 2000, reverse=True)
# sorted_salaries_3 = sorted(salaries, key=lambda salary: salary > 4000, reverse=True)
#
# print(sorted_salaries)
# print(sorted_salaries_2)
# print(sorted_salaries_3)

# print(list(reversed(salaries)))
# print(salaries[::-1])

# print(salaries)
# print(list(map(lambda salary: salary + 100, salaries)))
# print(max(salaries))
# print(min(salaries))
# salaries_iterator = iter(salaries)
# print(next(salaries_iterator))
# print(next(salaries_iterator))
# print(next(salaries_iterator))
# print(next(salaries_iterator))
# print(next(salaries_iterator))
# print(next(salaries_iterator))
# print(next(salaries_iterator))
# a = ord('눴')
# print(chr(a))
# print(round(1.10000000000000000, 5))

# person_1 = {'name': 'Peter', 'age': 45}
# person_2 = {'name': 'Alfred', 'age': 15}
# person_3 = {'name': 'Zarina', 'age': 65}
#
# peoples = [person_1, person_2, person_3]
# print(peoples)
# sorted_people = list(sorted(peoples, key=lambda man: man['name'], reverse=False))
# print(sorted_people)


# print(sum([1, 2, 3, 4, 5]))

# print(type([1]))

first_list = ['Name_1', 'Name_2']
second_list = ['James', 'Homer']
my_dict = {}

# my_dict['key'] = 'new_value'
# my_dict.get()

for name, age in zip(first_list, second_list):
    my_dict[name] = age

print(my_dict)