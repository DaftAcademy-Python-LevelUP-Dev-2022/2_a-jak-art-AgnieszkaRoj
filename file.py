def greeter(func):
    def inner(*args, **kwargs):
        greet = "Aloha "+func(*args, **kwargs)
        return greet.title()
    return inner


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
