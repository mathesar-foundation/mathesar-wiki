import os
import re
import sys
import shutil
import logging

import requests

from authentication import authenticate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import get_files, get_image_links, update_markdown_file

BASE_IMAGE_DIR = "assets"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("replace-external-links")

HACKMD_EMAIL = os.environ["HACKMD_EMAIL"]
HACKMD_PASSWORD = os.environ["HACKMD_PASSWORD"]
HACKMD_URL = "https://hackmd.io/login"

def make_image_paths(md_file, link):
    """
    Generate a path to save to and a relative link that points to it

    Args:
        md_file: str, path to a markdown file
        link: str, external image link
    Returns:
        tuple containing:
            save_path: str, path to save image locally
            rel_path: str, relative link that points to save_path
    """
    md_file = md_file.lstrip("./")
    # Remove '.md'
    md_file = md_file[:-3]

    name = link.split("/")[-1]
    name_parts = name.split(" ")
    name = name_parts[0]
    styling = " ".join(name_parts[1:])

    save_path = os.path.join(BASE_IMAGE_DIR, md_file, name)
    rel_path = "/" + save_path + (" " if styling else "") + styling
    return save_path, rel_path

def download_image(session, link, save_path):
    """
    Download an image

    Args:
        session: requests.Session, current session to make requests with
        link: str, external image link
        save_path: str, path to save the image to
    Returns:
        status_code: int, the status code of the request
    """
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

def get_markdown_files(root):
    """
    Gathers markdown file paths recursively
    """
    logger.info("Gathering markdown files...")
    all_files = []
    for dir_path, dirs, files in os.walk(root):
        all_files.extend([os.path.join(dir_path, f) for f in files
                          if f.endswith(".md")])
    return all_files

def replace_links():
    """
    Iterates over markdown files in the root directory, downloading any
    external images and replacing the urls with relative links
    """
    logger.info("Logging into HackMD...")
    session = authenticate(HACKMD_EMAIL, HACKMD_PASSWORD, HACKMD_URL)
    if session is None:
        logger.warning("HackMD log in unsuccesful!")
        session = requests.Session()
    else:
        logger.info("Logged into HackMD")

    logger.info("Starting image update process...")
    md_files = get_files(".", logger, [".md"])
    md_files = md_files[".md"]
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
