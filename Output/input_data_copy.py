import os
import shutil
import uuid
from ipywidgets import interact, interactive, fixed, interact_text

def copy_files(source_folder, destination_folder):
    # Get the parent folder of the destination folder
    parent_folder = os.path.dirname(destination_folder)

    # Get the path of the input folder relative to the parent folder
    input_folder = os.path.join(parent_folder, 'Input')

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Create the data folder in the destination folder if it doesn't exist
    data_folder = os.path.join(destination_folder, 'data')
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Iterate over each file
    for file in files:
        # Check if the file is a CSV or XLSX file
        if file.endswith('.csv') or file.endswith('.xlsx'):
            # Check if the file has already been copied
            if os.path.exists(os.path.join(data_folder, file)):
                # Get the new file name from the user
                new_name = interact_text(value=file, description=file)
                unique_name = str(uuid.uuid4()) + os.path.splitext(file)[1]
            else:
                # Generate a unique name for the file
                unique_name = str(uuid.uuid4()) + os.path.splitext(file)[1]

                # Prompt the user to rename the file
                new_name = interact_text(value=unique_name, description=file)

            # Copy the file to the data folder with the new name
            shutil.copy(os.path.join(input_folder, file), os.path.join(data_folder, new_name))

# Get the current folder
current_folder = os.getcwd()

# Set the destination folder to the current folder
destination_folder = current_folder

# Call the copy_files function with the appropriate source and destination folders to copy the files
copy_files(destination_folder, current_folder)