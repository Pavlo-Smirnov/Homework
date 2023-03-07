import random

range_len = 1
range_object = [random.randint(0, 10) for i in range(10)]
i = 0
while i < range_len:
    print(range_object)
    i += 1
    print(max(range_object))

# Why not just? :
print(max(range_object))