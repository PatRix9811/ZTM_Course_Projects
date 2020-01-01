from PIL import Image
import os
import sys

try:
    first_folder = sys.argv[1]
    second_folder = sys.argv[2]
except IndexError:
    exit('Please give a paths')

if not os.path.isdir(second_folder):
    os.mkdir(second_folder)

files_paths = [f for f in os.listdir(first_folder)]


for path in files_paths:
    name = os.path.splitext(path)[0]
    img = Image.open(f'{first_folder}\\{path}')
    img.save(f'{second_folder}\\{name}.png', 'png')
