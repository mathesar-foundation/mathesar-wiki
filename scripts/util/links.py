import os
import urllib.parse

from actions_toolkit import core


def is_url(link):
    """
    Checks if a link is a url or relative link
    """
    # Don't check for linkrot if link is a fragment
    if link.startswith('#'):
        return False
    parse_result = urllib.parse.urlparse(link)
    if parse_result.netloc:
        return True
    else:
        return False


def resolve_dot_path(link, file):
    """
    Resolves paths that start with dots
    """
    file = os.path.dirname(file)
    while link and link.startswith("./") or link.startswith("../"):
        if link.startswith("./"):
            link = link[2:]
        elif link.startswith("../"):
            link = link[3:]
            file = os.path.dirname(file)
    return os.path.join(file, link)


def resolve_dir_path(link, file):
    """
    Resolves paths that search from a directory
    """
    # Directory name would be filename without extension
    dir_name = os.path.splitext(file)[0]
    if os.path.exists(dir_name):
        n_link = os.path.join(dir_name, link)
        if os.path.exists(n_link):
            return n_link

    # If dir doesn't exist, or if it does exist but the file isn't inside of
    # it, we assume we search from current directory
    parent_dir = os.path.dirname(file)
    return os.path.join(parent_dir, link)


def resolve_relative_link(link, file):
    """
    Converts a relative link to an absolute link

    Three modes of relative path:
        './': Search from parent directory of file
        '../': Search from parent of parent directory of file
        No prefix: Search inside directory of same name as file
    """
    if link.startswith("./") or link.startswith("../"):
        return resolve_dot_path(link, file)
    else:
        return resolve_dir_path(link, file)


def resolve_wiki_link(link, file):
    """
    Converts wiki.js link to usable local path
    """
    # Remove styling that might be part of image links (e.g. "x.png =240x")
    link = link.split(" =")[0]
    # Remove fragments if they exist
    link = link.split("#")[0]
    
    # Remove "/en" from paths if they exist, since English is the default
    if link.startswith('/en/'):
        link = link[3:]
    # Add .md extension is there is no extension
    _, ext = os.path.splitext(link)
    if not ext:
        link += ".md"
    
    if link.startswith("/"):
        return link.lstrip("/")
    if link.startswith("#"):
        print('\n\n', link, '\n', file, '\n\n')
        return file
    else:
        return resolve_relative_link(link, file)


def get_files(root, extensions=None):
    """
    Gathers file of given extensions recursively

    Args:
        root: Root directory to search from
        extensions: A list of strings, where each string is an extension of the
        form ".ext". Ex: ".txt", ".md", ".pdf". If not passed, all files are
        returned
    """
    core.info("Gathering files...")
    if extensions:
        all_files = {ext: [] for ext in extensions}
    else:
        all_files = []

    for dir_path, _, files in os.walk(root):
        for f in files:
            full_path = os.path.join(dir_path, f)
            _, file_ext = os.path.splitext(f)
            if extensions is None:
                all_files.append(full_path)
            elif file_ext in all_files:
                all_files[file_ext].append(full_path)

    return all_files
