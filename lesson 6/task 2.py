#Generate 2 lists with the length of 10 with random integers from 1 to 10,
#and make a third list containing the common integers between the 2 initial lists without any duplicates.

from random import randint

list1 = [randint(1, 10) for i in range(10)]
list2 = [randint(1, 10) for i in range(10)]
d1 = set(list1)
d2 = set(list2)
i = 0

while d1 & d2:
    print(list1, list2)
    print(list(d1 & d2))
    i += 1
    break
else:
    print("No common elements")









