import os
import json

GALLERY_DIR = "gallery"


def scan_directory(directory):
    result = {}
    for item in sorted(os.listdir(directory)):
        path = os.path.join(directory, item)

        if os.path.isdir(path):
            # Keep subdirectory structure
            result[item] = scan_directory(path)
        elif item.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Ensure images are correctly assigned to the current directory key
            if "images" not in result:
                result["images"] = []
            result["images"].append(item)

    return result


# Scan the gallery directory
gallery_structure = scan_directory(GALLERY_DIR)

# Write to JSON file
with open("galleryStructure.json", "w") as f:
    json.dump(gallery_structure, f, indent=4)

print("✅ Successfully fixed galleryStructure.json")
