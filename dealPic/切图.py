# -*- coding: utf-8 -*-
# @Time : 2020/6/9 13:10
# @Author : Fan
from PIL import Image
import sys

#图片填充为正方形
def fill_image(image):
    width,height =  image.size
    #选图片最大的边
    n_image_length = width if width > height else height
    #填充为白色
    n_image = Image.new(image.mode,(n_image_length,n_image_length),color='white')
    if width >height:
        n_image.paste(image,(0,int((n_image_length - height)/2)))
    else:
        n_image.paste(image,(int((n_image_length - width)/2),0))
    return n_image

def cut_image(image):
    width,height = image.size
    item_width = int(width/3)
    box_list = []
    for i in range(0,3):
        for j in range(0,3):
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list

def save(image_list):
    index = 1
    for image in image_list:
        image.save('./images'+str(index)+'.png','PNG')
        index += 1

if __name__ == '__main__':
    file_path = './images/1.jpg'
    image = Image.open(file_path)
    image = fill_image(image)
    image_list = cut_image(image)
    save(image_list)

