'''
列表的综合操作
'''


# 判断重复元素的两种方法：遍历、set
def is_duplicated(list):
    for x in list:
        if list.count(x) > 1:
            return True
    return False


def is_duplicated1(lst):
    return len(lst) != len(set(lst))


# 列表翻转
def reverse(lst):
    return lst[::-1]


# 找出重复元素
def find_duplicate(lst):
    ret = []
    for x in lst:
        if lst.count(x) > 1 and x not in ret:
            ret.append(x)
    return ret


# 找出现次数量最多的元素
def mode(lst):
    if lst is None or len(lst) == 0:
        return None
    return max(lst, key=lambda v: lst.count(v))


if __name__ == '__main__':
    a = [1, -3, 2, 4, 2, 5, 3]
    print(is_duplicated(a))
    print(is_duplicated1(a))
    r = reverse([1, -2, 3, 4, 1, 2])
    print(r)
    r = find_duplicate([1, 2, 3, 4, 5, 2, ])
    print(r)
    lst = [1, 3, 3, 2, 2, 1, 1]
    r = mode(lst)
    print(f'{lst}中出现次数最多的元素为：{r}')
