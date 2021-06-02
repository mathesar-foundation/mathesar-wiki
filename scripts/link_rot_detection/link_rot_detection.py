import os
import sys
import logging
import urllib3
from concurrent import futures
import multiprocessing as mp
from collections import defaultdict

from actions_toolkit import core

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import get_files, get_image_links, get_links, is_url
from authentication import authenticate_hackmd, USER_AGENT

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("link-rot-detection")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SKIP_LINKS = {
    "http://matrix.mathesar.org/",
    "https://github.com/centerofci/mathesar-wiki"
}
HEADERS = {"User-Agent": USER_AGENT}
TIMEOUT = 10.0


def link2path(link):
    """
    Convert wiki.js style relative link to file path
    """
    # Remove leading slash from relative path
    link = link.lstrip("/")
    # Remove styling that might be part of image links
    link = link.split(" ")[0]
    # Add .md extension is there is no extension
    _, ext = os.path.splitext(link)
    if not ext:
        link += ".md"
    return link


def is_success_code(return_code):
    """
    Returns true if return_code is a success code, otherwise false
    """
    if return_code >= 200 and return_code < 300:
        return True
    return False


def check_external_link(session, link):
    """
    Checks if an external link exists
    """
    response = session.head(link,
                            verify=False,
                            headers=HEADERS,
                            timeout=TIMEOUT)
    # Page might not like head requets, try get instead
    if response.status_code == 405:
        response = session.get(link,
                               verify=False,
                               headers=HEADERS,
                               timeout=TIMEOUT)
    return response.status_code


def check_relative_link(link):
    """
    Checks if a relative link exists
    """
    link = link2path(link)
    if os.path.exists(link):
        return 200
    else:
        return 404


def check_link(session, cache, link):
    """
    Checks to see if a link is valid

    Args:
        session: requests.Session, current session to make requests with
        cache: dict, a cache of links mapped to their responses
        link: dict, link of the form:
            {"link": "link.com", "file": "parent.md"}
    Returns:
        link: dict, link of the form:
            {"link": "link.com", "file": "parent.md", "return_code": 200}
    """
    if link["link"] in cache:
        link["return_code"] = cache[link["link"]]
    else:
        if is_url(link["link"]):
            link["return_code"] = check_external_link(session, link["link"])
        else:
            link["return_code"] = check_relative_link(link["link"])
        cache[link["link"]] = link["return_code"]

    core.info(f"[{link['return_code']}] link: {link['link']} | "
              f"parent: {link['file']}")
    return link


def check_links(session, links):
    """
    Checks a list of links and returns a dict of errors

    Args:
        session: requests.Session, current session to make requests with
        links: list of dicts, where each dict is a link of the form:
            {"link": "link.com", "file": "parent.md"}
    Returns:
        links: list of dicts, where each dict is a link of the form:
            {"link": "link.com", "file": "parent.md", "return_code": 200}
    """
    cache = {}
    num_threads = mp.cpu_count() * 4
    with futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        links = executor.map(lambda link: check_link(
            session,
            cache,
            link,
        ), links)
    return links


def detect_link_rot(skip_links):
    """
    Iterates over markdown files in the root directory, downloading any
    external images and replacing the urls with relative links

    Args:
        skip_links: list of links to skip over
    """
    session = authenticate_hackmd(logger)

    # Get all files
    md_files = get_files(".", logger, [".md"])
    md_files = md_files[".md"]

    # Get all links
    links = []
    for md_file in md_files:
        f = md_file.lstrip("./")
        links += [{"link": l, "file": f} for l in get_links(md_file)]
        links += [{"link": l, "file": f} for l in get_image_links(md_file)]

    # Process links
    skip_links = set(skip_links)
    links = list(filter(lambda x: x["link"] not in skip_links, links))
    links = check_links(session, links)

    # Map errors to files
    all_errors = defaultdict(list)
    for link in links:
        if not is_success_code(link["return_code"]):
            error = f"[{link['return_code']}] {link['link']}"
            all_errors[link["file"]].append(error)

    # Build final error message
    error_msg = ""
    for md_file, errors in all_errors.items():
        error_msg += f"\n{md_file}:"
        for error in errors:
            error_msg += f"\n  {error}"
    if error_msg:
        error_msg = "Broken links found!" + error_msg
        core.set_failed(error_msg)


if __name__ == "__main__":
    detect_link_rot(SKIP_LINKS)
