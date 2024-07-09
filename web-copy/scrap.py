import os
import shutil

def move_files(source_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Iterate through files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file is HTML, if not, move it to the destination directory
            if not file.endswith('.html'):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.move(source_path, dest_path)
                print(f"Moved {file} to {dest_dir}")

# Define your source and destination directories
source_directory = 'templates copy'  # Update this with your source directory path
destination_directory = 'statics'  # Update this with your destination directory path

# Call the function to move files
move_files(source_directory, destination_directory)
