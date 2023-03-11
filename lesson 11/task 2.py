# import json
#
# my_application = {}
# my_application['first name'] = 'Pavel'
# my_application['last name'] = 'Smirnov'
# my_application['full name'] = 'Pavel Smirnov'
# my_application['telephone number'] = '0663203207'
# my_application['state'] = 'Zaporizhia'
# my_application['city'] = 'Berdiansk'
#
# with open('my_application.json', 'w') as file_object:
#     json.dump(my_application, file_object)

import sys
import json

with open('my_application.json') as file_object:
    my_application = json.load(file_object)

print("Enter 'f' to search by first name, 'l' for last name, 'fl' for full name, 't' for telephone number, "
      "'c' for city, 's' for state, enter 'x' for exit or 'd' to delete a record\n")

a = input("What do you want to find?: ")
if a == 'f':
    print(my_application['first name'])
elif a == 'l':
    print(my_application['last name'])
elif a == 'fl':
    print(my_application['full name'])
elif a == 't':
    print(my_application['telephone number'])
elif a == 'c':
    print(my_application['city'])
elif a == 's':
    print(my_application['state'])
elif a == 'd':
    del my_application
    print("Your record was deleted")
elif a == 'x':
    print('Good Bye!')
    sys.exit()


