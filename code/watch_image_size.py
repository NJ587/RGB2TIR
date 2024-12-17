
from PIL import Image

image_path = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_116649\car4_00044.jpg'

# 读取图片
image = Image.open(image_path)

# 获取尺寸
width, height = image.size

# 获取维度
dimensions = image.mode

# 输出结果
print(image_path)
print("尺寸：{} x {}".format(width, height))
print("维度：{}".format(dimensions))
