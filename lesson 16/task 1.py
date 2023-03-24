class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Student(Person):

    def __init__(self, name, surname, age, subject, graduated):
        super().__init__(name, surname, age)
        self.subject = subject
        self.graduated = graduated

    def square_numbers(self, x, y):
        self.x = x
        self.y = y
        a = x**2 + y**2
        print(a)

class Teacher(Person):

    def __init__(self, name, surname, age, salary, teaching_since):
        super().__init__(name, surname, age)
        self.salary = salary
        self.teaching_since = teaching_since

    def check_students(self, x):
        self.x = x
        if x == 15:
            print("All student are at the lesson")
        elif x < 15:
            print("Somebody is missing")

    def calculate_salary(self, number_of_days_worked):
        """this function is to calculate the salary of days worked. First, I need find the salary/per day by 6500//30
         Then, I multiply it by the number of days worked."""
        self.number_of_days_worked = number_of_days_worked
        salary_per_day = 6500 // 30
        x = salary_per_day * number_of_days_worked
        print(x)

my_student = Student('Pavel', 'Smirnov', 25, 'Math', 2023)
print({"Name":my_student.name, "Surname":my_student.surname, "Age":my_student.age,
       "Subject":my_student.subject, "Graduate":my_student.graduated})
my_student.square_numbers(4, 6)

print('*' * 15)

my_teacher = Teacher('Ivan', 'Ivanov', 35, 6500, 2018)
print({"Name":my_teacher.name, "Surname":my_teacher.surname, "Age":my_teacher.age, "Monthly salary":my_teacher.salary,
       "Teaching since" : my_teacher.teaching_since})
my_teacher.check_students(14)
my_teacher.calculate_salary(20)
