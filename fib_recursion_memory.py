# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/6 2:01'

from collections import defaultdict
from datetime import datetime

total = defaultdict(int)
total_memory = defaultdict(int)



def fib_recusion(k):
    assert k > 0, "k的值必须大于0"
    if k in [1, 2]:
        return 1
    else:
        global total
        total[k] += 1
        return fib_recusion(k - 2) + fib_recusion(k - 1)


# 将值存到total里,在递归前判断是否在这个total里,如果在就取total里的值,如果不在就将新值存到total里.
def fib_recursion_memory(k):
    assert k > 0, "k的值必须大于0"
    if k in [1, 2]:
        return 1
    global total_memory
    if k in total_memory:
        result = total_memory[k]
    else:
        result = fib_recursion_memory(k - 2) + fib_recursion_memory(k - 1)
        total_memory[k] = result
    return result


if __name__ == "__main__":
    start_time = datetime.now()
    print("普通递归方式。第{0}位的数的值是{1},此次递归耗时{2}".format(35, fib_recusion(35), (datetime.now()-start_time).total_seconds()))
    start_time_memory = datetime.now()
    print("采用记忆搜索的递归方式。第{0}位的数的值是{1},递归耗时{2}".format(35, fib_recursion_memory(35), (datetime.now()-start_time_memory).total_seconds()))
    print("递归的次数也是一个斐波拉契数列,比如你看:{0}".format(total))
