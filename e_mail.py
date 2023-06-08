import random
import string


class EmailValidator:
    LIBRARY_SYMBOLS = string.ascii_letters + string.digits + "_.@"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        prefix = ""
        random_int = random.randint(1, 98)
        for i in range(random_int):
            prefix += random.choice(cls.LIBRARY_SYMBOLS[:-1])
        return prefix + "@gmail.com"

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count("@") != 1:
            return False
        first_part, last_part = email.split("@")
        if len(first_part) >= 100 or len(last_part) >= 50:
            return False
        elif ".." in email:
            return False
        elif "." not in last_part:
            return False
        for sym in email:
            if sym not in cls.LIBRARY_SYMBOLS:
                return False
        return True

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
