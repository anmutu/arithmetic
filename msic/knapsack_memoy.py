# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/11 11:05'

info = [
    [3, 8],
    [2, 5],
    [5, 12]
]


def search(depth, rest):
    if depth == 2:
        return info[depth][1] if rest >= info[depth][0] else 0
    else:
        value = []
        # 选还是不选.选的逻辑和不选的逻辑,其中选的逻辑要判断剩余大于当前的
        value.append(search(depth, rest+1))
        if rest > info[depth][0]:
            value.append(search(depth+1, rest-info[depth][0])+info[depth][1])
            return max(value)


if __name__ == "__main__":
    search(0, 5)