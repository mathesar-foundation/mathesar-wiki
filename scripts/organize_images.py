import os
from collections import defaultdict

from actions_toolkit import core

from util.markdown import get_image_links, update_markdown_file
from util.links import get_files, resolve_wiki_link

BASE_IMAGE_DIR = "assets"
UNUSED_IMAGE_DIR = ".unused"
PRIVATE_IMAGE_DIR = "private"
REMOVED_MSG = ("*This image was removed automatically because it was not"
               "uploaded to a public folder. Please contact a [Mathesar core"
               "team member](/team) if you see this on the wiki.*")
IMAGE_EXTS = [".tif", ".tiff", ".bmp", ".jpg", ".jpeg", ".gif", ".png"]


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


def strip_styling(path):
    """
    Remove styling from a relative path
    """
    path = path.split(" ")[0]
    return path


def check_private_paths(files):
    """
    Returns True if there is a mix of public and private paths, else False
    """
    is_private = [f.startswith(PRIVATE_IMAGE_DIR) for f in files]
    # If there is any private, all should be private. Otherwise, we have a mix
    # of public and private paths
    if files and any(is_private) and not all(is_private):
        return False
    else:
        return True


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
    common_path = os.path.commonpath(paths)
    return common_path


def build_image_paths(img, files):
    """
    Given an image and a directory, build a save path and relative link
    """
    if not files:
        if UNUSED_IMAGE_DIR not in img:
            core.warning(f"{img} not used in any files!")
        path = os.path.join(BASE_IMAGE_DIR, UNUSED_IMAGE_DIR)
    else:
        path = build_common_path(files)

    name = os.path.basename(img)
    # Remove styling
    name = name.split(" ")[0]

    save_path = os.path.join(path, name)
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
    Move a file from src to dest
    """
    # Ensure we do not overwrite when we move
    dest = build_unique_path(dest)
    # Move file
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    core.info(f"Moving {src} -> {dest}...")
    os.rename(src, dest)
    return dest


def clean_directories(path):
    """
    Recursively clean up empty directories, starting from the parent of the
    path that is passed
    """
    path = os.path.dirname(path)
    if path and not os.listdir(path):
        core.info(f"Cleaning up {path}...")
        os.rmdir(path)
        clean_directories(path)


def organize_images():
    core.info("Finding markdown files and images...")
    all_files = get_files(".", [".md"] + IMAGE_EXTS)
    md_files = [clean_file_name(f) for f in all_files[".md"]]
    img2files = {
        clean_file_name(img): []
        for ext in IMAGE_EXTS for img in all_files[ext]
    }

    # Check what files each image appears in
    for md_file in md_files:
        links = get_image_links(md_file, filter_relative=True)
        for link in links:
            abs_link = resolve_wiki_link(link, md_file)
            if abs_link not in img2files:
                core.warning(f"Broken link found! {link} in {md_file}")
                continue
            # Store original link as we need to replace it
            img2files[abs_link].append({
                "file": md_file,
                # Strip styling so we only replace the link
                "link": strip_styling(link),
            })

    # Remove links to private images
    private_replacements = defaultdict(list)
    error_message = ""
    for img, files in img2files.items():
        file_paths = [f["file"] for f in files]
        if not check_private_paths(file_paths):
            private_files = [
                f for f in files if f["file"].startswith(PRIVATE_IMAGE_DIR)
            ]
            public_files = [
                f for f in files if not f["file"].startswith(PRIVATE_IMAGE_DIR)
            ]

            # Update links so only references are private files
            img2files[img] = private_files

            for md_file in public_files:
                file, link = md_file["file"], md_file["link"]
                private_replacements[file].append((link, REMOVED_MSG))
                error_message += f"\n- {link} in {file}"

    for md_file, links in private_replacements.items():
        update_markdown_file(md_file,klinks)

    # Move images depending on where they appear
    link_replacements = defaultdict(list)
    for img, files in img2files.items():
        file_paths = [f["file"] for f in files]
        save_path, rel_path = build_image_paths(img, file_paths)
        # If image is not where it should be...
        if img != save_path:
            # Move image
            save_path = move_file(img, save_path)
            rel_path = path2rel(save_path)

            # Remove empty directories
            clean_directories(img)

            # Track moved images
            for md_file in files:
                file, link = md_file["file"], md_file["link"]
                link_replacements[file].append((link, rel_path))

    for md_file, links in link_replacements.items():
        update_markdown_file(md_file, links)

    if error_message:
        print("Public pages pointed to private images:" + error_message)


if __name__ == "__main__":
    organize_images()
