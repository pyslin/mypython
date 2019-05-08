from PIL import Image

# 打开一个jpg图像文件，注意是当前路径
im = Image.open('test.jpg')
w,h = im.size
print('Original image size:X:%s,Y:%s'%(w,h))
im.thumbnail((w//2,h//2))
print('Resize image toX:%s,Y:%s'%(w//2,h//2))

# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg','jpeg')




"""
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
"""
from PIL import Image,ImageFilter
im = Image.open('test.jpg')
im.filter(ImageFilter.BLUR)

# 应用模糊滤镜:

im.save('blur.jpg', 'jpeg')



