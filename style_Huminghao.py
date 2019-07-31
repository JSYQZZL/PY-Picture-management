from PIL import Image
from PIL import ImageFilter


def blurPic(Imf):
    Im2 = Imf.filter(ImageFilter.BLUR)  # 图像模糊
    return Im2

def edge(Imf):
    Im4 = Imf.filter(ImageFilter.EDGE_ENHANCE)  # 边界增强
    return Im4

def gaussianBlur(Imf):
    Im6 = Imf.filter(ImageFilter.GaussianBlur)  # 高斯模糊
    return Im6

def emboss(Imf):
    Im8 = Imf.filter(ImageFilter.EMBOSS)  # 浮雕滤镜，
    return Im8

def ffind_edeges(Imf):
    Im10 = Imf.filter(ImageFilter.FIND_EDGES)  # 边界滤镜，相当于背景涂黑，线条白色
    return Im10

