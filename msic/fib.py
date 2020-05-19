from collections import defaultdict
from datetime import datetime

total = defaultdict(int)


def fib(k):
    # 求第k个数的数值，用递归实现。
    assert k > 0, "k的值必须大于0"
    if k in [1, 2]:
        return 1
    global total
    total[k] += 1
    return fib(k - 1) + fib(k - 2)


def fib2(k):
    # 依旧求第k个数的数值，不用递归实现。
    assert k > 0, "k的值必须大于0"
    if k in [1, 2]:
        return 1

    # k_1 = 1
    # k_2 = 1
    k_1 = k_2 = 1
    for i in range(3, k + 1):
        k_1, k_2 = k_2, k_1+k_2
        # tmp = k_1
        # k_1 = k_1 + k_2
        # k_2 = tmp

    return k_1


if __name__ == "__main__":
    start_time = datetime.now()
    print("递归方式。第{0}位的数的值是{1}".format(35, fib(35)))
    print("此次递归耗时{0}".format((datetime.now()-start_time).total_seconds()))
    print("递归的次数也是一个斐波拉契数列,比如你看:{0}".format(total))

    start_time1 = datetime.now()
    print("非递归方式。第{0}位的数的值是{1}".format(35, fib(35)))
    print("此次耗时{0}".format((datetime.now() - start_time1).total_seconds()))

    for i in range(1, 10):
        print("递归方式。第{0}位的数的值是{1}。".format(i, fib(i)))
        print("非递归方式。第{0}位的数的值是{1}。".format(i, fib2(i)))
