# ALL操作

import os

def process_folders(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'infrared' in dirs and 'visible' in dirs:
            visible_folder = os.path.join(root, 'visible')
            infrared_folder = os.path.join(root, 'infrared')

            visible_files = os.listdir(visible_folder)
            infrared_files = os.listdir(infrared_folder)

            visible_files_set = set(visible_files)
            infrared_files_set = set(infrared_files)

            for file_name in visible_files_set.symmetric_difference(infrared_files_set):
                if file_name in visible_files_set:
                    os.remove(os.path.join(visible_folder, file_name))
                if file_name in infrared_files_set:
                    os.remove(os.path.join(infrared_folder, file_name))

            print(f"Processed: {visible_folder} and {infrared_folder}")

# Specify the root directory for traversal
root_directory = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\RGB_T234'

# Call the function to process folders
process_folders(root_directory)

print("Delete unpaired completed!")
