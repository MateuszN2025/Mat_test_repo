def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return "@" in email and "." in email

# print(is_valid_email('ajk@.com'))
def calc_sum(a:int, b:int):
    return a + b
