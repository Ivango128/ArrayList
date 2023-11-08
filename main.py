from ArrayList import ArrayList

my_list = ArrayList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)  # Вывод: [1, 2, 3]

my_list.insert(1, 4)
print(my_list)  # Вывод: [1, 4, 2, 3]

my_list.pop()
print(my_list)  # Вывод: [1, 4, 2]

my_list.pop(1)
print(my_list)