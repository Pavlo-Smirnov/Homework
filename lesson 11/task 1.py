# some_string = "Hello file world!"
# with open('hello_file.txt', 'w') as file_object:
#     file_object.write(some_string)

with open('hello_file.txt') as file_object:
    some_string = file_object.read()
    print(some_string)

# Does the new file show up in the directory where you ran your scripts? - Yes
# What if you add a different directory path to the filename passed to open? - It raises an error