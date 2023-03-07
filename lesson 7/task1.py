# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
# and the number of occurrences as values.

str1 = "Ukraine is beautiful"
my_dict = {}
for word in str1:  # look fir .split() method it will help you
    my_dict[word] = my_dict.get(word, 0) + 1
    print(my_dict)


