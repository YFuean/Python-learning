'''
对字符串进行32位加密
'''
import hashlib


def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('utf-8')))
    return m.hexdigest()


print(hash_cry32(123))
print(hash_cry32('hello123'))
