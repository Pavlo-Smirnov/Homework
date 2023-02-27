my_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = {1: (my_list[0]), 2: (my_list[1]), 3: (my_list[2]), 4: (my_list[3]), 5: (my_list[4]), 6: (my_list[5]),
        7: (my_list[6])}
print(days)

make_opposite = {v: k for k, v in days.items()}
print(make_opposite)
