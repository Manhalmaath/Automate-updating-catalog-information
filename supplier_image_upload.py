import os
import requests

images = os.listdir(os.path.join(os.getcwd(), "supplier-data", "images"))
for image in images:
    if ".jpeg" in image:
        with open(os.path.join(os.getcwd(), "supplier-data", "images", image), "rb") as opened:
            r = requests.post("http://localhost/upload/", files={"file": opened})