# -*- coding: utf-8 -*-
# @Time : 2020/8/3 16:24
# @Author : Fan
#抖音封面三张或六张
import os
from PIL import Image
#切成的行列数
def splitimage(src,row,col,dst):    #打开起始图片
    img = Image.open(src)

    #获取图片的宽高
    w,h = img.size
    if row <= h and col <= w:
        print('原图片信息:%sx%s,%s,%s'%(w,h,img.format,img.mode))
        print('开始处理图片。。')

        s = os.path.split(src)
        if dst == '':
            dst = s[0]
        #获取命名
        fn = s[1].split('.')
        basename = fn[0]
        ext= fn[-1]

        num = 0
        rowheight = h //row
        colwidth  = w //col
        for r in range(row):
            for c in range(col):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                f = 'JPEG' if ext.lower() == 'jpg' else ext.upper()
                img.crop(box).save(os.path.join(dst, basename + '-'+ str(num) +'.'+ ext), f)
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')

src = input('请输入图片文件路径：')
if os.path.isfile(src):
    dstpath = input('请输入图片输出目录（不输入路径则表示使用源图片所在目录）：')
    if (dstpath == '') or os.path.exists(dstpath):
        row = int(input('请输入切割行数：'))
        col = int(input('请输入切割列数：'))
        if row > 0 and col > 0:
            splitimage(src, row, col, dstpath)
        else:
            print('无效的行列切割参数！')
    else:
        print('图片输出目录 %s 不存在！' % dstpath)
else:
    print('图片文件 %s 不存在！' % src)
