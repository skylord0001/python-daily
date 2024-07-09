import os
import re
from multiprocessing import Pool

def replace_filenames_in_js(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        modified_lines = []
        for line in lines:
            if '//' in line or '/*' in line:
                modified_lines.append(line)  # Skip replacement for lines containing comments
            else:
                # Replace filenames with only filename without path in JavaScript content
                modified_line, num_replacements = re.subn(r"(?<![\'\"`])(?:https?:\/\/[^\'\"`\s]*\/)?(?:\.\.\/)*(?:([^\'\"`\s]+(?:\.js|\.css))(?=[\'\"`]))", lambda match: os.path.basename(match.group(1)) if match.group(1) else '', line)
                modified_line = modified_line.lstrip('/')  # Remove leading slash
                modified_lines.append("static/")
                modified_lines.append(modified_line)

                # Print what is being replaced
                if num_replacements > 0:
                    for match in re.finditer(r"(?<![\'\"`])(?:https?:\/\/[^\'\"`\s]*\/)?(?:\.\.\/)*(?:([^\'\"`\s]+(?:\.js|\.css))(?=[\'\"`]))", line):
                        original_filename = match.group(0)
                        new_filename = os.path.basename(match.group(1))
                        if original_filename != new_filename:
                            print(f"Replaced '{original_filename}' with '{new_filename}' in file '{file_path}'")

        # Write the modified content back to the file if changes are made
        if any(modified_lines):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(modified_lines)
            print(f"Modification completed for file: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def main():
    # Define the directory containing JavaScript files
    statics_directory = 'statics'  # Update this with the path to your "statics" folder

    # Get a list of JavaScript files
    js_files = [os.path.join(root, file) for root, _, files in os.walk(statics_directory) for file in files if file.endswith('.js')]

    # Process files in parallel
    with Pool() as pool:
        pool.map(replace_filenames_in_js, js_files)

if __name__ == "__main__":
    main()
