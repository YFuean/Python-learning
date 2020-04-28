'''
用myqr库制作二维码
'''
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont


def img_code():
    myqr.run(
        words='https://yfuean-student-manager.oss-cn-shanghai.aliyuncs.com/img/carbon.png',
        # 设置容错率为最高
        version=1,
        # 控制纠错水平，范围是l、M、Q、H，从左到右依次升高
        level='H',
        # 背景图
        picture='./res/img/bg3.jpg',
        # 彩色二维码
        colorized=True,
        # 用以调节图片的对比度，1.0表示原始图片，更小的值表示更低的对比度，反之更大
        contrast=1.2,
        # 用来调节图片宽度，其余用法和取值同上
        brightness=1.0,
        # 保存文件名字
        save_name='code2.png',
        # 保存位置
        save_dir=os.getcwd()+'/res/img/')


def draw():
    img = Image.open('./res/img/code2.png')
    w, h = img.size
    txt = '云上的日子'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./res/fonts/SimHei.ttf', 26)
    draw.text((w/2-100, 10), txt, (0, 0, 0), font=font)
    img.save('./res/img/code3.png')


if __name__ == '__main__':
    img_code()
    draw()
