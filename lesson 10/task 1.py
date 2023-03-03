a_list = [1, 2, 3, 4, 5]

def oops():
        try:
            print(a_list[7])
        except IndexError:
            print("wrong operation")


b_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def second_option():
    try:
        oops()
        print(b_list[7])
    except IndexError:
        print("not working")


second_option()