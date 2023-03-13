def stop_decorator(func):
    def wrapper_accepting_arguments(arg1, arg2):
        print("This guy is driving his {0}, holding a new {1}".format(arg1, arg2))
        func(arg1, arg2)
    return wrapper_accepting_arguments


@stop_decorator
def smt(smt_one, smt_two):
    print("This guy is driving his *, holding a new *")

smt("car", "phone")


