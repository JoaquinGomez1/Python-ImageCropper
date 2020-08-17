# Python-ImageCropper"

This script is using PILLOW for the image handling aswell as python-image-cropper (pip install python-image-cropper)

cd into the same folder that contains the .py file and then run the following command to crop the images.

$ python imageCroper.py <images_Width> <images_height> 


NOTE: Before running the script create two folders in the same directory and name them 'images' and 'convertedImages'.

Add the all images that needs to be cropped to the 'images' directory and then run the script.
Once the images have been cropped they will be stored into the convertedImages folder and all of the original images will be deleted.

If there is any images on the convertedImages directory a zip file will be created to store the previously cropped images. 

Dependencies: 
pillow (pip install pillow)
python-resize-image (pip install python-resize-image)
