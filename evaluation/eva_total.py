import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
import cv2
from skimage.metrics import structural_similarity
from skimage.metrics import peak_signal_noise_ratio

# FID 测量方法
def calculate_fid_score(fake_folder, real_folder):
    os.system(f"python -m pytorch_fid {fake_folder} {real_folder}")

# IS 测量方法
def calculate_is_score(fake_folder):
    # 加载预训练的InceptionV3模型
    inception_model = InceptionV3(include_top=False, weights='imagenet')

    # 加载生成图像
    def load_images_from_folder(folder):
        images = []
        for filename in os.listdir(folder):
            img = Image.open(os.path.join(folder, filename))
            img = img.resize((299, 299))  # 将图像大小调整为InceptionV3所需的大小
            img = np.array(img)
            images.append(img)
        return np.array(images)

    # 加载生成图像
    fake_images = load_images_from_folder(fake_folder)

    # 预处理图像数据
    fake_images = preprocess_input(fake_images)

    # 提取生成图像的特征
    fake_features = inception_model.predict(fake_images)

    # 平滑特征以避免零值
    epsilon = 1e-10
    fake_features += epsilon

    # 计算IS分数
    def calculate_is_score(features):
        preds = features.mean(axis=0)
        kl_divergence = (features * (np.log(features) - np.log(preds))).mean(axis=1)
        is_score = np.exp(kl_divergence.mean())
        return is_score

    fake_is_score = calculate_is_score(fake_features)

    print(f"Fake IS Score: {fake_is_score}")

# SSIM、PSNR测量方法
def calculate_ssim(folder1, folder2):
    """
    计算两个文件夹中所有图像的SSIM值。
    :param folder1: 第一个文件夹路径
    :param folder2: 第二个文件夹路径
    :return: None
    """
    # 获取文件夹中所有图像文件的路径
    images1 = [os.path.join(folder1, file) for file in os.listdir(folder1) if file.endswith('.png')]
    images2 = [os.path.join(folder2, file) for file in os.listdir(folder2) if file.endswith('.png')]

    # 确保两个文件夹中有相同数量的图像
    if len(images1) != len(images2):
        print("Error: 两个文件夹中图像数量不一致")
        return

    # 遍历图像并计算SSIM值
    total_ssim = 0
    for img1_path, img2_path in zip(images1, images2):
        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)

        # 转换图像为灰度图像
        gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # 计算SSIM值
        ssim = structural_similarity(gray_img1, gray_img2)
        total_ssim += ssim

    # 计算平均SSIM值
    avg_ssim = total_ssim / len(images1)
    print(f"Average SSIM: {avg_ssim}")

if __name__ == "__main__":

    fake_folder = "/home/huison/ai/total_real_and_fake/fake_B/total"
    real_folder = "/home/huison/ai/total_real_and_fake/real_B/total"

    # 计算FID分数
    # calculate_fid_score(fake_folder, real_folder)

    # 计算IS分数
    calculate_is_score(fake_folder)

    # 计算SSIM分数
    # calculate_ssim(real_folder, fake_folder)
