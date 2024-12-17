import os

directory = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\RGB_T234\afterrain'

infrared_files = [f for f in os.listdir(os.path.join(directory, 'infrared')) if f.endswith('.jpg')]
visible_files = [f for f in os.listdir(os.path.join(directory, 'visible')) if f.endswith('.jpg')]

for i, file in enumerate(infrared_files):
    old_name = os.path.join(directory, 'infrared', file)
    new_name = os.path.join(directory, 'infrared', f"{str(i+1).zfill(5)}_afterrain.jpg")
    os.rename(old_name, new_name)

for i, file in enumerate(visible_files):
    old_name = os.path.join(directory, 'visible', file)
    new_name = os.path.join(directory, 'visible', f"{str(i+1).zfill(5)}_afterrain.jpg")
    os.rename(old_name, new_name)

print("rename completed!")
