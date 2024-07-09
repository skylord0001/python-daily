import os
import re

def replace_src_with_static(html_content):
    # Define regex pattern to match src attributes in script, img, link, and svg tags
    pattern = re.compile(r'<(script|img|link|svg)\s+[^>]*?(src|href)\s*=\s*["\']([^"\']+)["\'][^>]*?>')

    # Function to replace matched src or href paths with {% static 'filename' %}
    def replace_path(match):
        tag = match.group(1)
        attr = match.group(2)
        src_path = match.group(3)

        # Print the path before processing
        print(f"Found path: {src_path}")

        # Check if the path is not already in the correct format
        if 'static' not in src_path or src_path.count('/') > 1:
            file_name = src_path.split('/')[-1]  # Extract filename from the path
            return f"<{tag} {attr}=\"{{% static '{file_name}' %}}\">"
        else:
            return match.group(0)  # No need to replace if already in correct format

    # Perform the replacement
    replaced_content = re.sub(pattern, replace_path, html_content)
    return replaced_content

def process_html_files(directory):
    print(f"Processing HTML files in directory: {directory}")
    # Traverse through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                # Read HTML content from the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Perform the replacement
                replaced_html = replace_src_with_static(html_content)
                
                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(replaced_html)
                print(f"Replacement completed for file: {file_path}")

# Define the directory containing HTML files
templates_directory = 'templates'  # Update this with the path to your "templates" folder

# Call the function to process HTML files
process_html_files(templates_directory)
