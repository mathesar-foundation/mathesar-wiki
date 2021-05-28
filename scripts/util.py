import os
import re

def is_url(link):
    """
    Checks if a link is a url or relative link
    """
    # Looks for text followed by '://' to identify a url
    pattern = r'^[a-z0-9]*:\/\/.*$'
    if re.search(pattern, link):
        return True
    else:
        return False

def get_image_links(md_file, filter_relative=False):
    """
    Given a markdown file, find all image links

    Args:
        md_file: str, path to a markdown file
        filter_relative: bool, if True return only relative links. Else, return
        only external links
    Returns:
        links: list of external image link strings
    """
    with open(md_file, 'r') as f:
        # Matches markdown image syntax, capturing image link and image name
        pattern = r'!\[[^\]]*\]\((.*?)\s*("(?:.*[^"])")?\s*\)'
        links = re.findall(pattern, f.read())
    # Currently throw out names, consider using down the line
    links = [link for link, name in links]

    if filter_relative:
        links = list(filter(lambda x: not is_url(x), links))
    else:
        links = list(filter(is_url, links))

    return links

def get_files(root, logger, extensions=None):
    """
    Gathers file of given extensions recursively

    Args:
        root: Root directory to search from
        logger: Logger to log with
        extensions: A list of strings, where each string is an extension of the
        form ".ext". Ex: ".txt", ".md", ".pdf". If not passed, all files are
        returned
    """
    logger.info("Gathering files...")
    if extensions:
        all_files = {ext: [] for ext in extensions}
    else:
        all_files = []

    for dir_path, dirs, files in os.walk(root):
        for f in files:
            full_path = os.path.join(dir_path, f)
            _, file_ext = os.path.splitext(f)
            if extensions is None:
                all_files.append(full_path)
            elif file_ext in all_files:
                all_files[file_ext].append(full_path)

    return all_files
