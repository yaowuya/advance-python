# 生成器函数，函数里只要有yield关键字

def gen_func():
    yield 1
    yield 2
    yield 3


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


# print (gen_fib(10))
# 斐波拉契 0 1 1 2 3 5 8
# 惰性求值， 延迟求值提供了可能

if __name__ == "__main__":
    # 生成器对象， python编译字节码的时候就产生了
    print(fib(20))
    gen = gen_func()
    for value in gen:
        print(value)

    for data in gen_fib(100):
        print(data)
