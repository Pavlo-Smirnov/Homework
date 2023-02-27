#Task 3 Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10
# and `j` is corresponding to `i` squared.

def squares(j, i):
    squares = [value ** 2 for value in range(j, i+1)]
    return squares

print(squares(1, 11))