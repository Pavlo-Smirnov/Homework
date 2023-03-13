def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("{0} {1}".format(arg1, arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("{0} {1}".format(city_one, city_two))

cities("", "")





