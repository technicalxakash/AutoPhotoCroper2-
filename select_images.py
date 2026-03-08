import os
import shutil

input_folder = "input_images"
output_folder = "selected_images"
id_file = "selected_ids.txt"

os.makedirs(output_folder, exist_ok=True)

# Read IDs from text file
with open(id_file, "r") as f:
    ids = [line.strip() for line in f if line.strip()]

for img_id in ids:

    found = False

    for ext in [".jpg", ".jpeg", ".png"]:

        filename = img_id + ext
        src = os.path.join(input_folder, filename)

        if os.path.exists(src):

            dst = os.path.join(output_folder, filename)
            shutil.copy(src, dst)

            print("Copied:", filename)

            found = True
            break

    if not found:
        print("Image not found:", img_id)

print("Done ✅")



