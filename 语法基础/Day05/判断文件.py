'''
判断传入图片是否为文件类型
'''


def count_image(file_list):
    '''
    判断一组文件中图片的个数
    :param file_list:文件列表
    :return:图片文件数量
    '''
    count = 0
    for file in file_list:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('webp') or \
                file.endswith('bmp') or file.endswith('icon'):
            count = count + 1
    return count


# 调用函数
img_list = ['sh.png', '3.webp', 'op.md', 'ab.mp4', '8.jpg', '4.bmp', 'gh.icon']
result = count_image(img_list)
print('一共有', result, '个图片文件')
