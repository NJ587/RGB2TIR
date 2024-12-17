import os

def count_images_by_category(directory):
    category_counts = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            category = filename.split("_")[0]  # 提取类别名
            category_counts[category] = category_counts.get(category, 0) + 1
    
    return category_counts

directory = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_116649"
category_counts = count_images_by_category(directory)

for category, count in category_counts.items():
    print(f"Category '{category}' has {count} images.")

