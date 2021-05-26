import os
import re
import shutil
import logging

import requests

from authentication import authenticate

BASE_IMAGE_DIR = "assets"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("image_automation")

HACKMD_EMAIL = os.environ["HACKMD_EMAIL"]
HACKMD_PASSWORD = os.environ["HACKMD_PASSWORD"]
HACKMD_URL = "https://hackmd.io/login"

def get_image_links(md_file):
    with open(md_file, 'r') as f:
        # Matches markdown image syntax, capturing image link and image name
        pattern = r'!\[[^\]]*\]\((.*?)\s*("(?:.*[^"])")?\s*\)'
        links = re.findall(pattern, f.read())
    # Currently throw out names, consider using down the line
    links = [link for link, name in links]
    links = list(filter(is_url, links))
    return links

def make_image_paths(md_file, link):
    md_dir, md_base = os.path.split(md_file)
    md_dir = md_dir.lstrip("./")
    # Remove '.md'
    md_base = md_base[:-3]

    name = link.split("/")[-1]
    name_parts = name.split(" ")
    name = name_parts[0]
    styling = " ".join(name_parts[1:])

    save_path = os.path.join(BASE_IMAGE_DIR, md_dir, md_base, name)
    rel_path = "/" + save_path + " " + styling
    return save_path, rel_path

def download_image(session, link, save_path):
    response = session.get(link, stream=True)
    if response.status_code == 200:
        logger.info(f"  Saving {link} to {save_path}...")
        response.raw.decode_content = True
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
    else:
        logger.warning(f"  Failed to download {link}! "
                       f"Error code {response.status_code}")
    return response.status_code

def is_url(link):
    # Looks for text followed by '://' to identify a URL
    pattern = r'^[a-z0-9]*:\/\/.*$'
    if re.search(pattern, link):
        return True
    else:
        return False

def get_markdown_files(root):
    logger.info("Gathering markdown files...")
    all_files = []
    for dir_path, dirs, files in os.walk(root):
        all_files.extend([os.path.join(dir_path, f) for f in files
                          if f.endswith(".md")])
    return all_files

def update_markdown_file(md_file, replace_links):
    if not replace_links:
        return
    logger.info(f" Replacing links...")
    with open(md_file, 'r') as f:
        text = f.read()
    for link, rel_link in replace_links:
        text = text.replace(link, rel_link)
        logger.info(f"  {link} -> {rel_link}")
    with open(md_file, 'w') as f:
        f.write(text)

def replace_links():
    logger.info("Logging into HackMD...")
    session = authenticate(HACKMD_EMAIL, HACKMD_PASSWORD, HACKMD_URL)
    if session is None:
        logger.warning("HackMD log in unsuccesful!")
        session = requests.Session()
    else:
        logger.info("Logged into HackMD")

    logger.info("Starting image update process...")
    md_files = get_markdown_files(".")
    for md_file in md_files:
        image_links = get_image_links(md_file)
        if image_links:
            logger.info(f"External links found in {md_file}!")
            logger.info(" Starting image download...")
            replace_links = []
            for link in image_links:
                save_path, rel_path = make_image_paths(md_file, link)
                status_code = download_image(session, link, save_path)
                if status_code == 200:
                    replace_links.append((link, rel_path))
            update_markdown_file(md_file, replace_links)

if __name__ == "__main__":
    replace_links()
