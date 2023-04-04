import re


class Validation:

    def __init__(self, email):
        self.email = email
        self.validate()

    @staticmethod
    def is_valid_email(email):
        email_check = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
        return re.match(email_check, email)

    def validate(self):
        if not Validation.is_valid_email(self.email):
            raise ValueError(f"Wrong email: {self.email}")
        else:
            return self.email

v = Validation("abcd@gmail.com")
print(v.validate())













#     def __init__(self, email):
#         self.email = email
#         self.validate()
#
#     @staticmethod
#     def is_valid_email(email):
#         email_check = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
#         return re.match(email_check, email)
#
#     def validate(self):
#         if not Validation.is_valid_email(self.email):
#             raise ValueError(f"Wrong {self.email}")
#         else:
#             return self.email
#
#

