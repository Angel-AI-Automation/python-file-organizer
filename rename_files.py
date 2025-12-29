import os

folder = "files_to_rename"

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    if os.path.isfile(old_path):
        new_name = filename.replace(" ", "_").lower()
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)

print("Files renamed successfully!")
