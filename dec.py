import time

def task_2(a):
    print("start task_2")
    yield "a"
    yield "aa"
    yield "aaa"

def task_3(b):
    print("start task_3")
    yield "b"
    yield "bb"
    yield "bbb"

def task_4(c):
    print("start task_4")
    yield "c"
    yield "cc"
    yield "ccc"

def task_5(d):
    yield "d"
    yield "dd"
    yield "ddd"

def task_6(a, b, c, d):
    yield "abcd"
    yield "abcdabcd"



def test():
    # a = yield task_2(2)
    # b = yield task_3(2)
    # yield task_4(2, 8)
    yield task_2(2)
    yield task_3(2)
    yield task_4(2)
    yield task_5(2)
    yield task_6(2, 3, 4, 5)

for i in test():
    print("next")
    time.sleep(1)
    for j in i:
        time.sleep(1)
        print(j)


