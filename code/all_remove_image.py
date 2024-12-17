import os
import shutil

def process_folders(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'infrared' in dirs and 'visible' in dirs:
            visible_folder = os.path.join(root, 'visible')
            infrared_folder = os.path.join(root, 'infrared')

            # Copy files from visible folder to target visible directory
            target_visible_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\visible'
            for file_name in os.listdir(visible_folder):
                source_file = os.path.join(visible_folder, file_name)
                target_file = os.path.join(target_visible_folder, file_name)
                shutil.copy(source_file, target_file)

            # Copy files from infrared folder to target infrared directory
            target_infrared_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared'
            for file_name in os.listdir(infrared_folder):
                source_file = os.path.join(infrared_folder, file_name)
                target_file = os.path.join(target_infrared_folder, file_name)
                shutil.copy(source_file, target_file)

            print(f"Copied files from {visible_folder} to {target_visible_folder}")
            print(f"Copied files from {infrared_folder} to {target_infrared_folder}")

# Specify the root directory for traversal
root_directory = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGB-T234'

# Call the function to process folders
process_folders(root_directory)

print("Copying completed!")
