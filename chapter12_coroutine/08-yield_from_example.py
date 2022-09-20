"""
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    main()
"""

final_result = {}


# 子生成器
def sales_sum(pro_name):
    total = 0
    nums = []
    while 1:
        x = yield
        print(pro_name + "销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    # 每一次return，都意味着当前协程结束。
    return total, nums


# 委托生成器
def middle(key):
    while 1:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成！！.")


# 调用方
def main():
    data_sets = {
        "bobby牌面膜": [1200, 1500, 3000],
        "bobby牌手机": [28, 55, 98, 108],
        "bobby牌大衣": [280, 560, 778, 70],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None)  # 预激middle协程
        for value in data_set:
            m.send(value)  # 给协程传递每一组的值
        m.send(None)  # 结束协程
    print("final_result:", final_result)


"""
1、调用方：调用委派生成器的客户端（调用方）代码 
2、委托生成器：包含yield from表达式的生成器函数 
3、子生成器：yield from后面加的生成器函数

委托生成器的作用是：在调用方与子生成器之间建立一个双向通道
所谓的双向通道是什么意思呢？ 调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方。
"""

if __name__ == '__main__':
    main()

"""
3. 为什么要使用yield from
学到这里，我相信你肯定要问，既然委托生成器，起到的只是一个双向通道的作用，我还需要委托生成器做什么？我调用方直接调用子生成器不就好啦？

高能预警~

下面我们来一起探讨一下，到底yield from 有什么过人之处，让我们非要用它不可。

3.1 因为它可以帮我们处理异常
如果我们去掉委托生成器，而直接调用子生成器。那我们就需要把代码改成像下面这样，我们需要自己捕获异常并处理。而不像使yield from那样省心。
"""
"""
def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name+"销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

if __name__ == "__main__":
    my_gen = sales_sum("bobby牌手机")
    my_gen.send(None)
    my_gen.send(1200)
    my_gen.send(1500)
    my_gen.send(3000)
    try:
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
"""
