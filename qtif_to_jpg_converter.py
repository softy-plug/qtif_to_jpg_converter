import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Prompt user for folders
Tk().withdraw()
qtif_folder = askdirectory(title='Choose the folder with QTIF images:')
jpg_folder = askdirectory(title='Choose the folder to save converted JPG images:')

# Check if folders exist, create if they don't
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Loop through all files in QTIF folder
for file_name in os.listdir(qtif_folder):
    if file_name.endswith('.qtif'):
        # Open QTIF image and convert to JPG
        qtif_file_path = os.path.join(qtif_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        qtif_image = Image.open(qtif_file_path)

        # Save JPG image with maximum quality
        qtif_image.save(jpg_file_path, 'JPEG', quality=100)

print(f"All QTIF images in {qtif_folder} converted to JPG and saved in {jpg_folder}.")

#softy_plug