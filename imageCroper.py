from PIL import Image
from resizeimage import resizeimage
from os import listdir	
import os
from zipfile import ZipFile
import sys

try:
	converted_images_list = listdir('./convertedImages')
	if len(converted_images_list) != 0:
		zipObj = ZipFile('previousConvertedImages.zip', 'w')
		for image in converted_images_list:
			zipObj.write('./convertedImages/' + image)
		 
		zipObj.close()

	list_of_images = listdir('./Images')
	image_width = int(sys.argv[1])
	image_height = int(sys.argv[2])
	print(list_of_images)

	for i in range(len(list_of_images)):
		image_name = './Images/' + list_of_images[i]

		fd_img = open(image_name, 'rb')
		img = Image.open(fd_img)
		img = resizeimage.resize_cover(img, [image_width, image_height])

		if img.mode in ("RGBA", "P"):  # RGBA is not supported so it needs to get converted into RGB
			img = img.convert("RGB")

		img.save('./convertedImages/' + list_of_images[i] , img.format)
		fd_img.close()
		print(image_name + ': done')
		
		os.remove(image_name)


except IndexError:
	print('Index Error: Probably forgot to add <width> and <height> parameters')