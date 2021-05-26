import os
import re
import shutil

import requests

BASE_IMAGE_DIR = "assets"

def get_image_links(md_file):
    with open(md_file, 'r') as f:
        # Matches markdown image syntax, capturing image link and image name
        pattern = r'!\[[^\]]*\]\((.*?)\s*("(?:.*[^"])")?\s*\)'
        links = re.findall(pattern, f.read())
    # Currently throw out names, consider using down the line
    links = [link for link, name in links]
    return links

def make_image_path(md_file, link):
    md_dir, md_base = os.path.split(md_file)
    md_dir = md_dir.lstrip("./")
    # Remove '.md'
    md_base = md_base[:-3]

    name = link.split("/")[-1]
    # Remove any styling after image name
    name = name.split(" ")[0]

    save_path = os.path.join(BASE_IMAGE_DIR, md_dir, md_base, name)
    return save_path

def download_image(link, save_path):
    response = requests.get(link, stream=True)
    if response.status_code == 200:
        response.raw.decode_content = True
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
    else:
        print(f"{link} could not be downloaded!")
    return response.status_code

def is_url(link):
    # Looks for text followed by '://' to identify a URL
    pattern = r'^[a-z0-9]*:\/\/.*$'
    if re.search(pattern, link):
        return True
    else:
        return False

def get_markdown_files(root):
    all_files = []
    for dir_path, dirs, files in os.walk(root):
        all_files.extend([os.path.join(dir_path, f) for f in files
                          if f.endswith(".md")])
    return all_files

def save_2_rel(save_path):
    # Ensure rel link starts with single '/'
    return "/"  + save_path.lstrip("/")

def update_markdown_file(md_file, replace_links):
    with open(md_file, 'r') as f:
        text = f.read()
    for link, save_path in replace_links:
        rel_link = save_2_rel(save_path)
        text = text.replace(link, rel_link)
    with open(md_file, 'w') as f:
        f.write(text)

def check_and_update_images():
    md_files = get_markdown_files(".")
    for md_file in md_files:
        image_links = get_image_links(md_file)
        replace_links = []
        for link in image_links:
            if is_url(link):
                save_path = make_image_path(md_file, link)
                status_code = download_image(link, save_path)
                if status_code == 200:
                    replace_links.append((link, save_path))
        update_markdown_file(md_file, replace_links)

if __name__ == "__main__":
    check_and_update_images()
