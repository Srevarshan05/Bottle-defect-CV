import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(folder_path):
    # Optional: Create an output folder
    output_folder = os.path.join(folder_path, "converted_jpgs")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(output_folder, jpg_filename)

            try:
                heif_file = pillow_heif.read_heif(heic_path)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw"
                )
                image.save(jpg_path, "JPEG")
                print(f"Converted: {filename} → {jpg_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

    print("\n✅ All HEIC files converted!")

# 🔁 Change this path to your folder
convert_heic_to_jpg(r"C:\Users\Srevarshan\OneDrive\Desktop\Projects\Yolo_custom\NO Cap Dataser")
