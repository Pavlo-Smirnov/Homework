class CustomException(Exception):
    def __init__(self, msg):
        with open("logs.txt", "a") as file:
            file.write(f"{msg}")

salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise CustomException("Salary is in the wrong range")













