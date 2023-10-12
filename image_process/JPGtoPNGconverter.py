# Pillow https://pypi.org/project/Pillow/

# run python3 JPGtoPNGconverter.py Pokedex/original/ new/

import sys
import os
from PIL import Image

def convert_images(original_folder, new_folder):
    if not os.path.exists(original_folder):
        print(f"The original folder at '{original_folder}' does not exist.")
        return

    if not os.path.exists(new_folder):
        os.mkdir(new_folder) 
        
    original_files = os.listdir(original_folder)

    for file in original_files:
        clean_name, file_extension = os.path.splitext(file)
        if file_extension.lower() in (".jpg", ".png", ".jpeg", ".gif"):
            img = Image.open(os.path.join(original_folder, file))
            img.save(os.path.join(new_folder, f"{clean_name}.png"), "PNG")
            print(f"Converted: {file} -> {clean_name}.png")
    print('all done!!')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <original_folder> <new_folder>")
    else:
        original_folder = sys.argv[1]
        new_folder = sys.argv[2]
        convert_images(original_folder, new_folder)
