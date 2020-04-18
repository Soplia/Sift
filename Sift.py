import torch
from numpy import *
from PIL import Image
from pylab import *

import os
from matplotlib import pyplot as plt

def draw_circle(w,r):
    m = arange(0,1.01,.01)*2*pi
    x = r*cos(m) + w[0]
    y = r*sin(m) + w[1]
    plot(x, y, 'b', linewidth=2)

file = 'timg.png'
image = array(Image.open(file).convert('L'))
if file[-3:] != 'pgm':
    image_1 = Image.open(file).convert('L')
    image_1.save('sif.pgm')
    image_2 ='sif.pgm'

#在Windows下需要注意：
#sift.exe 而不是sift
#需要注意空格，就像在命令行下输入一样
cmmd = str("sift.exe "+image_2+" --output="+'eigenvalue.sift'+" "+" --edge-thresh 10 --peak-thresh 5")
os.system(cmmd)

read_f = loadtxt('eigenvalue.sift')
descriptor = read_f[:,:4]

figure()
gray()
imshow(image)
circle=True
for i in descriptor:
    draw_circle(i[:2], i[2])
axis('off')
show()