import os
import re

def remove_invalid_links(html_content):
    # Define regex pattern to match link tags with href attributes
    pattern = re.compile(r'<link\s+[^>]*?href\s*=\s*["\']([^"\']+)["\'][^>]*?>')

    # Function to remove invalid link tags
    def remove_link(match):
        full_tag = match.group(0)
        href = match.group(1)
        # Check if the href attribute is in the {% static 'filename' %} format
        if '{% static' in href:
            return full_tag  # Skip the link if already in the correct format
        valid_extensions = (
            '.jpg', '.jpeg', '.png', '.gif', '.svg',  # image formats
            '.css', '.js',  # stylesheet and script formats
            '.woff2', '.woff', '.ttf', '.eot',  # font formats
            '.ico', '.webp',  # other web-related formats
            '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',  # document formats
            '.mp3', '.ogg', '.wav', '.aac',  # audio formats
            '.mp4', '.webm', '.mov', '.avi', '.mkv',  # video formats
        )
        if not href.endswith(valid_extensions):
            print(f"Removing invalid link tag: {full_tag}")
            return ''  # Replace the tag with an empty string
        else:
            return full_tag  # Keep the tag unchanged if href ends with a valid file format

    # Perform the removal
    cleaned_content = re.sub(pattern, remove_link, html_content)
    return cleaned_content

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
                
                # Remove invalid link tags
                cleaned_html = remove_invalid_links(html_content)
                
                # Write the modified content back to the file if changes are made
                if cleaned_html != html_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(cleaned_html)
                    print(f"Modification completed for file: {file_path}")

# Define the directory containing HTML files
templates_directory = 'templates'  # Update this with the path to your "templates" folder

# Call the function to process HTML files
process_html_files(templates_directory)
