import sys
import os
from PIL import Image #use pip install Pillow in command line.



#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check that the output_folder exists, if not then create a new folder

if not os.path.exists(output_folder):
	os.makedirs(output_folder)


#loop through pokedex

for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0] #this line is use to remove .jpg from image name
	img.save(f'{output_folder}{clean_name}.png','png')
	print('all done')


# use this on command line to run the file python JPG-to-PNG-converter.py pokedex\ pngfolder\
