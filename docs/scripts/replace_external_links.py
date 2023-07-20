import os
import shutil

from actions_toolkit import core

from util.markdown import get_image_links, update_markdown_file
from util.links import get_files
from util.authentication import authenticate_hackmd

BASE_IMAGE_DIR = "assets"


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
        core.info(f"  Saving {link} to {save_path}...")
        response.raw.decode_content = True
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
    else:
        core.warning(f"  Failed to download {link}! "
                     f"Error code {response.status_code}")
    return response.status_code


def replace_links():
    """
    Iterates over markdown files in the root directory, downloading any
    external images and replacing the urls with relative links
    """
    session = authenticate_hackmd()

    core.info("Starting image update process...")
    md_files = get_files(".", [".md"])
    md_files = md_files[".md"]
    for md_file in md_files:
        image_links = get_image_links(md_file, filter_relative=False)
        if image_links:
            core.info(f"External links found in {md_file}!")
            core.info(" Starting image download...")
            replace_links = []
            for link in image_links:
                save_path, rel_path = make_image_paths(md_file, link)
                status_code = download_image(session, link, save_path)
                if status_code == 200:
                    replace_links.append((link, rel_path))
            update_markdown_file(md_file, replace_links)


if __name__ == "__main__":
    replace_links()
