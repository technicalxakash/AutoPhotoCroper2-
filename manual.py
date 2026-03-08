import os
import shutil

input_folder = "input_images"
manual_folder = "manual_crop"
output_folder = "manual_originals"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(manual_folder):

    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    original_path = os.path.join(input_folder, file)

    if os.path.exists(original_path):

        dest_path = os.path.join(output_folder, file)

        shutil.copy(original_path, dest_path)

        print("Copied original:", file)

    else:
        print("Original not found:", file)


print("Done ✅")