def fib(k):
    # 求第k个数的数值
    assert k > 0, "k的值必须大于0"
    if k in [1, 2]:
        return 1
    return fib(k - 1) + fib(k - 2)


def fib2(k):
    # 依旧求第k个数的数值
    assert k > 0, "k的值必须大于0"
    if k in [1, 2]:
        return 1

    k_1 = 1
    k_2 = 1
    for i in range(3, k + 1):
        tmp = k_1
        k_1 = k_1 + k_2
        k_2 = tmp
    return k_1


if __name__ == "__main__":
    for i in range(1, 10):
        print("递归方式。第{0}位的数的值是{1}。".format(i, fib(i)))
        print("非递归方式。第{0}位的数的值是{1}。".format(i, fib2(i)))
