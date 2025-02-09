import os
import json

GALLERY_DIR = "gallery"


def scan_directory(directory):
    result = {}
    for item in sorted(os.listdir(directory)):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            result[item] = scan_directory(path)
        elif item.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            result.setdefault(os.path.basename(directory), []).append(item)
    return result


gallery_structure = scan_directory(GALLERY_DIR)

with open("galleryStructure.json", "w") as f:
    json.dump(gallery_structure, f, indent=4)

print("✅ Generated galleryStructure.json")
