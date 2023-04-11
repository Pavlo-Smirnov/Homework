"""In this task I tried two sultions. The first one I found in the articles atteched to the lesson.
And the 2nd one I tried to make with classes, as it seemed easier for me. Which one is right? Or I didn't
understand the task?"""


# def in_range():
#     for i in range(1, 20, 2):
#         yield i
#
# my_function = in_range()
# for i in my_function:
#     print(i)


class MyRange:

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def in_range(self):
        for i in range(self.start, self.stop, self.step):
            yield i

mr = MyRange(1, 10, 2)
for i in mr.in_range():
    print(i)




