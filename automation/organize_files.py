import os
import shutil


def organize_files(input_folder, output_folder):
    """
    Moves files from the input folder to the output folder.
    Creates the output folder if it does not exist.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        source_path = os.path.join(input_folder, filename)

        if os.path.isfile(source_path):
            destination_path = os.path.join(output_folder, filename)
            shutil.move(source_path, destination_path)


def main():
    input_folder = "files_input"
    output_folder = "files_output"

    organize_files(input_folder, output_folder)
    print("Files organized successfully.")


if __name__ == "__main__":
    main()
