import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import get_files, get_image_links, update_markdown_file

BASE_IMAGE_DIR = "assets"
UNUSED_IMAGE_DIR = ".unused"
IMAGE_EXTS = [".tif", ".tiff", ".bmp", ".jpg", ".jpeg", ".gif", ".png"]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("organize-images")

def rel2path(link):
    """
    Converts a relative path to a path we can save to and read from
    """
    path, *_ = link.split(" ")
    path = path.lstrip("/")
    return path

def path2rel(link):
    """
    Converts a system path to a relative path
    """
    path = "/" + link
    return path

def clean_file_name(path):
    """
    Removes the initial directory added by get_files()
    """
    path = path.lstrip("./")
    return path

def build_path(markdown_file):
    """
    Given a markdown file an image was referenced in, build a path to the
    directory we woulds save the image in
    """
    # Remove '.md'
    markdown_file = markdown_file[:-3]
    path = os.path.join(BASE_IMAGE_DIR, markdown_file)
    return path

def build_common_path(files):
    """
    Given a list of markdown files that all reference an image, build the path
    to the directory we would save the image in
    """
    paths = [build_path(f) for f in files]
    try:
        common_path = os.path.commonpath(paths)
    except:
        import pdb; pdb.set_trace()
    return common_path

def build_image_paths(img, path):
    """
    Given an image and a directory, build a save path and relative link
    """
    name = img.split("/")[-1]
    name, *styling = name.split(" ")
    styling = " ".join(styling)

    save_path = os.path.join(path, name)
    # rel_path = "/" + save_path + (" " if styling else "") + styling
    # Ignore styling, since we just replace the first part of the link
    rel_path = path2rel(save_path)
    return save_path, rel_path

def build_unique_path(file_name):
    """
    Given a file name, build a unique name if the current one is taken
    """
    i = 1
    name, ext = os.path.splitext(file_name)
    ret_name = file_name
    while os.path.isfile(ret_name):
        ret_name = name + f"({i})" + ext
        i += 1
    return ret_name

def move_file(src, dest):
    """
    Move a file
    """
    # Ensure we do not overwrite when we move
    dest = build_unique_path(dest)
    # Move file
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    logger.info(f"Moving {src} -> {dest}...")
    os.rename(src, dest)
    return dest

def clean_directories(path):
    """
    Recursively clean up empty directories, starting from the parent of the
    path that is passed
    """
    path = os.path.dirname(path)
    if path and not os.listdir(path):
        logger.info(f"Cleaning up {path}...")
        os.rmdir(path)
        clean_directories(path)

def organize_images():
    logger.info("Finding markdown files and images...")
    all_files = get_files(".", logger, [".md"] + IMAGE_EXTS)
    md_files = [clean_file_name(f) for f in all_files[".md"]]
    file2links = {md_file: [] for md_file in md_files}
    img2files = {clean_file_name(img): []
                 for ext in IMAGE_EXTS for img in all_files[ext]}

    # Check what files each image appears in
    for md_file in md_files:
        links = get_image_links(md_file, filter_relative=True)
        for link in links:
            link = rel2path(link)
            if link not in img2files:
                logger.warn(f"Broken link found! {link} in {md_file}")
                continue
            img2files[link].append(md_file)

    # Move images depending on where they appear
    for img, files in img2files.items():
        if not files and UNUSED_IMAGE_DIR not in img:
            logger.warn(f"{img} not used in any files!")
            path = os.path.join(BASE_IMAGE_DIR, UNUSED_IMAGE_DIR)
        else:
            path = build_common_path(files)
        save_path, rel_path = build_image_paths(img, path)
        # If image is not where it should be...
        if img != save_path:
            # Move image
            save_path = move_file(img, save_path)
            rel_path = path2rel(save_path)

            # Remove empty directories
            clean_directories(img)

            # Track moved images
            rel_img = path2rel(img)
            for md_file in files:
                file2links[md_file].append((rel_img, rel_path))
    
    # Update markdown files
    for md_file, links in file2links.items():
        update_markdown_file(logger, md_file, links)

if __name__ == "__main__":
    organize_images()
