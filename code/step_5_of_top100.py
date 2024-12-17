import os
import shutil

def copy_images(source_dir, dest_dir_train, dest_dir_test, classes, step=5):
    for class_name in classes:
        class_images = [f for f in os.listdir(source_dir) if f.startswith(class_name)]
        class_images.sort()  # Ensure consistent order

        # Calculate number of images to copy to test set
        num_test_images = len(class_images) // step

        # Copy images to train and test directories
        for i, image in enumerate(class_images):
            if i % step == 0:  # Every 5th image goes to test set
                shutil.copy(os.path.join(source_dir, image), os.path.join(dest_dir_test, image))
            else:
                shutil.copy(os.path.join(source_dir, image), os.path.join(dest_dir_train, image))

# Define source and destination directories for infrared images
source_dir_ir = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_116649"
dest_dir_train_ir = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\train_B"
dest_dir_test_ir = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\test_B"

# Define source and destination directories for visible images
source_dir_visible = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\visible_116649"
dest_dir_train_visible = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\train_A"
dest_dir_test_visible = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\test_A"

# Define classes
classes = ["car4", "walkingwoman", "walkingmantiny", "kite2", "walkingtogether1", "twoelecbike1",
           "blackwoman", "bicyclecity", "cycle4", "tree2", "oldwoman", "child1", "walkingwithbag1",
           "push", "walkingwithbag2", "hotkettle", "kite4", "toy3", "playsoccer", "nightthreepeople",
           "soccerinhand", "crossroad", "manoccpart", "redmanchange", "graycar2", "womanfaraway",
           "aftertree", "tallman", "car3", "tricycle", "woman89", "elecbikewithlight1", "maninred",
           "car", "manwithumbrella", "fog", "children4", "man2", "redcar", "toy4", "walkingtogether",
           "diamond", "kettle", "whiteman1", "whitecar4", "children2", "face1", "twowoman1", "oldman2",
           "dog1", "stroller", "man69", "redcar2", "redbag", "boundaryandfast", "woman4", "cycle1",
           "child3", "manypeople", "yellowcar", "tree3", "carnotmove", "car66", "luggage", "orangeman1",
           "cycle3", "bike", "man24", "threeman2", "carLight", "people", "notmove", "maninglass", "man8",
           "man29", "man7", "child", "elecbike2", "man88", "whitebag", "walkingman1", "woman3", "woman2",
           "woman", "manafterrain", "glass", "run2", "manwithbag4", "cycle2", "maninblack", "balancebike",
           "rmo", "straw", "man28", "call", "whitecarafterrain", "bikemove1", "baketballwaliking",
           "blueCar", "manwithbasketball"]

# Copy infrared images
copy_images(source_dir_ir, dest_dir_train_ir, dest_dir_test_ir, classes)

# Copy visible images
copy_images(source_dir_visible, dest_dir_train_visible, dest_dir_test_visible, classes)
