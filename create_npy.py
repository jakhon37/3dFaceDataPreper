

import os
import numpy as np

def create_npy_from_folder(folder_path, output_npy_path):
    # List all subdirectories or files inside the custom folder
    items = os.listdir(folder_path)
    
    # Create a dictionary. Here, I'm assuming each item is a key with an empty list as its value.
    # Modify this as per your requirements.
    custom_dict = {item: [] for item in items}
    
    # Save the dictionary as a .npy file
    np.save(output_npy_path, custom_dict)



if __name__ == '__main__':
    
    # folder_path = "/path/to/your/custom/folder"
    # output_npy_path = "/path/to/save/your/output.npy"
    root = os.path.abspath(os.path.dirname(__file__))
    
    image_folder = os.path.join(root, 'image_paths')
    
    output_npy_path = os.path.join('image_paths', 'KR_FACE.npy')
    
    
    create_npy_from_folder(image_folder, output_npy_path)
