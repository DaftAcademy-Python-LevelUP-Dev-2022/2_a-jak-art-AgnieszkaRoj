def greeter(func):
    def inner(*args, **kwargs):
        greet = "Aloha "+func(*args, **kwargs)
        return greet.title()
    return inner


def sums_of_str_elements_are_equal(func):
    def inner_num(*args, **kwargs):
        nonlocal negative
        numbers = func(*args, **kwargs).split()
        numbers = [int(x) for x in numbers]
        if digitSum(numbers[0]) == digitSum(numbers[1]):
            info = f'{digitSum(numbers[0]) == {digitSum(numbers[1])}'
        else:
            info = f'{digitSum(numbers[0]) != {digitSum(numbers[1])}'
        return info
    return inner_num
    def digitSum(n):
        digits = []
        minus = False
        for digit in str(n):
            if digit == '-':
                minus = True
            if minus:
                liczba = -int(digit)
                digits.append(liczba)
            else:
                liczba = int(digit)
                digits.append(liczba)
        return sum(digits)


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
