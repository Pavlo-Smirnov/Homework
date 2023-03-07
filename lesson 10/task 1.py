a_list = [1, 2, 3, 4, 5]


# def oops():
#         try:
#             print(a_list[7])
#         except IndexError:
#             print("wrong operation")

def oops():
    # task says " function called oops that explicitly raises an IndexError exception when called"
    raise IndexError


b_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def second_option():
    try:
        oops()
    except IndexError:
        print("not working")


second_option()
# but I see you get this topic, nice