# -*- coding: utf-8 -*-
# @Time : 2020/5/19 11:54
# @Author : Fan
import os
import paddlehub as hub

human = hub.Module(name='deeplabv3p_xception65_humanseg')
base_dir = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(base_dir,'images/')
files = [path + i for i in os.listdir(path)]
print(files)

results = human.segmentation(data = {'image':files})
for result in results:
    print(result)