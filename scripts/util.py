import os
import urllib.parse

import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension


def is_url(link):
    """
    Checks if a link is a url or relative link
    """
    parse_result = urllib.parse.urlparse(link)
    if parse_result.netloc:
        return True
    else:
        return False


def markdown_parse(md_file, extensions):
    with open(md_file, 'r') as f:
        md = markdown.Markdown(extensions=extensions)
        md.convert(f.read())
    return md


class ImgExtractor(Treeprocessor):
    def run(self, doc):
        """
        Gather all images in XML tree and store in markdown.images attribute
        """
        self.markdown.images = []
        for image in doc.findall('.//img'):
            self.markdown.images.append(image.get('src'))


class ImgExtExtension(Extension):
    def extendMarkdown(self, md, _):
        """
        Register ImageExtractor as an extension
        """
        img_ext = ImgExtractor(md)
        md.treeprocessors.add('imgext', img_ext, '>inline')


def get_image_links(md_file, filter_relative=None):
    """
    Given a markdown file, find all image links

    Args:
        md_file: str, path to a markdown file
        filter_relative: bool, if True return only relative links, if false
        return only external links and if None return all
    Returns:
        links: list of external image link strings
    """
    md = markdown_parse(md_file, extensions=[ImgExtExtension()])
    links = md.images
    if filter_relative is None:
        return links
    elif filter_relative:
        return list(filter(lambda x: not is_url(x), links))
    else:
        return list(filter(is_url, links))


class LinkExtractor(Treeprocessor):
    def run(self, doc):
        """
        Gather all links in XML tree and store in markdown.links attribute
        """
        self.markdown.links = []
        for link in doc.findall('.//a'):
            self.markdown.links.append(link.get('href'))


class LinkExtExtension(Extension):
    def extendMarkdown(self, md, _):
        """
        Register LinkExtractor as an extension
        """
        link_ext = LinkExtractor(md)
        md.treeprocessors.add('linkext', link_ext, '>inline')


def get_links(md_file, filter_relative=None):
    """
    Given a markdown file, find (non-image) links

    Args:
        md_file: str, path to a markdown file
        filter_relative: bool, if True return only relative links, if false
        return only external links and if None return all
    Returns:
        links: list of external image link strings
    """
    md = markdown_parse(md_file, extensions=[LinkExtExtension()])
    links = md.links
    if filter_relative is None:
        return links
    elif filter_relative:
        return list(filter(lambda x: not is_url(x), links))
    else:
        return list(filter(is_url, links))


def update_markdown_file(logger, md_file, replace_text):
    """
    Replaces urls in a markdown file with relative links

    Args:
        md_file: str, path to a markdown file
        replace_text: list of tuples, where each tuple is of the form (src,
        dest). Each piece of src text will be replaced by its dest text.
    """
    if not replace_text:
        return
    logger.info(f" Updating {md_file}...")
    with open(md_file, 'r') as f:
        text = f.read()
    for src, dest in replace_text:
        text = text.replace(src, dest)
        logger.info(f"  {src} -> {dest}")
    with open(md_file, 'w') as f:
        f.write(text)


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

    for dir_path, _, files in os.walk(root):
        for f in files:
            full_path = os.path.join(dir_path, f)
            _, file_ext = os.path.splitext(f)
            if extensions is None:
                all_files.append(full_path)
            elif file_ext in all_files:
                all_files[file_ext].append(full_path)

    return all_files
