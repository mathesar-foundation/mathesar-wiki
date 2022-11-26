import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from actions_toolkit import core

from .links import is_url


def markdown_parse(md_file, extensions):
    with open(md_file, 'r') as f:
        md = markdown.markdown(f.read(), extensions=extensions)
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


def update_markdown_file(md_file, replace_text):
    """
    Replaces urls in a markdown file with relative links

    Args:
        md_file: str, path to a markdown file
        replace_text: list of tuples, where each tuple is of the form (src,
        dest). Each piece of src text will be replaced by its dest text.
    """
    if not replace_text:
        return
    core.info(f" Updating {md_file}...")
    with open(md_file, 'r') as f:
        text = f.read()
    for src, dest in replace_text:
        text = text.replace(src, dest)
        core.info(f"  {src} -> {dest}")
    with open(md_file, 'w') as f:
        f.write(text)
