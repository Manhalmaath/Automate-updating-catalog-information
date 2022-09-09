#! /usr/bin/env python3
import os
import requests

descriptions = os.listdir(os.path.join(os.getcwd(), "supplier-data", "descriptions"))
for filename in descriptions:
    with open(os.path.join(os.getcwd(), "supplier-data", "descriptions", filename), "r") as opened:
        lines = opened.readlines()
        name = lines[0].strip()
        weight = int(lines[1].strip().strip(" lbs"))
        description = lines[2].strip()
        image_name = filename.split(".")[0] + ".jpeg"
        r = requests.post("http://35.193.19.102/fruits/",
                          json={"name": name, "weight": weight, "description": description,
                                "image_name": image_name})
