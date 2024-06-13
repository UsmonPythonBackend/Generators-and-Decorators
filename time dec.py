import time

def time_of_function(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        result = t2 - t1
        print(f'Xisoblashga {result} secund ketdi')
    return wrapper



@time_of_function
def first_func():
    my_list = [i for i in range(1, 10000000)]


@time_of_function
def second_func():
    my_list = [i for i in range(1, 9999999)]



first_func()
second_func()