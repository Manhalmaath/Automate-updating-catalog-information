import os
from PIL import Image

images = os.listdir(os.path.join(os.getcwd(), "supplier-data", 'images'))

for image in images:
    if image.endswith(".tiff"):
        with Image.open(os.path.join(os.getcwd(), "supplier-data", 'images', image)) as img:
            img.convert("RGB").resize((600, 400)).save(os.path.join(os.getcwd(), "supplier-data", 'images', image.split('.')[0] + '.jpeg'), "JPEG")
