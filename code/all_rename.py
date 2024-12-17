# 所有图片都命名为_afterrain.jpg

# import os

# def process_folders(root_dir):
#     for root, dirs, files in os.walk(root_dir):
#         if 'infrared' in dirs and 'visible' in dirs:
#             infrared_folder = os.path.join(root, 'infrared')
#             visible_folder = os.path.join(root, 'visible')

#             infrared_files = [f for f in os.listdir(infrared_folder) if f.endswith('.jpg')]
#             visible_files = [f for f in os.listdir(visible_folder) if f.endswith('.jpg')]

#             for i, file in enumerate(infrared_files):
#                 old_name = os.path.join(infrared_folder, file)
#                 new_name = os.path.join(infrared_folder, f"{str(i+1).zfill(5)}_afterrain.jpg")
#                 os.rename(old_name, new_name)

#             for i, file in enumerate(visible_files):
#                 old_name = os.path.join(visible_folder, file)
#                 new_name = os.path.join(visible_folder, f"{str(i+1).zfill(5)}_afterrain.jpg")
#                 os.rename(old_name, new_name)

#             print(f"Processed: {infrared_folder} and {visible_folder}")

# # Specify the root directory for recursive traversal
# root_directory = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGB-T234'

# # Call the function to process folders
# process_folders(root_directory)

# print("ALL Rename completed!")




# 命名为_文件夹名.jpg
import os

def process_folders(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'infrared' in dirs and 'visible' in dirs:
            parent_folder_name = os.path.basename(root)
            infrared_folder = os.path.join(root, 'infrared')
            visible_folder = os.path.join(root, 'visible')

            infrared_files = [f for f in os.listdir(infrared_folder) if f.endswith('.jpg')]
            visible_files = [f for f in os.listdir(visible_folder) if f.endswith('.jpg')]

            for file in infrared_files:
                old_name = os.path.join(infrared_folder, file)
                new_name = os.path.join(infrared_folder, file.replace('afterrain', parent_folder_name))
                os.rename(old_name, new_name)

            for file in visible_files:
                old_name = os.path.join(visible_folder, file)
                new_name = os.path.join(visible_folder, file.replace('afterrain', parent_folder_name))
                os.rename(old_name, new_name)

            print(f"Processed: {infrared_folder} and {visible_folder}")

# Specify the root directory for recursive traversal
root_directory = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGB-T234'

# Call the function to process folders
process_folders(root_directory)

print("renew Rename completed!")
