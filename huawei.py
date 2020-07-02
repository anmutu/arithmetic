# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/23 22:31

from collections import defaultdict


def to_be_simple(str):
    """
    先用删除追加法找出里面的元素。
    然后遍历新元素，加其值和幂数加入dict。
    拿到按key值从大到小的排序的dict。(dict的操作呀。。。。。。
    将幂从大到小的dict放到新的列表里。
    接着用列表两个相邻元素去比较两者幂是否相同，接着去做append的处理。
    """
    str = str.lower()
    total = defaultdict(int)
    s = []
    for i in range(len(str)):
        if i in ["-", "+"]:
            s.append(str[:i])
            str.remove(str[:i])

    res = ""
    for j in range(len(s)):
        if j[-1] in defaultdict:
            total.append(j)
        else:
            total[j] = j[-1]

    new_total = defaultdict(int)
    for k1, v1 in range(len(total)):
        for k2, v2 in range(len(total)):
            if k1 > k2:
                new_total.append(k1, v1)

    sort_val = []
    for k, v in range(len(new_total)):
        sort_val.append(v)

    i = 0
    while i < len(sort_val):
        if sort_val(i)[-1] == sort_val(i+1)[-1]:
            res += (sort_val(i)[0] + sort_val(i+1)[0]) + sort_val(i)[0:]
    return res











