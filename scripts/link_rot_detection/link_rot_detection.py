import os
import sys
import logging

from actions_toolkit import core

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import get_files, get_image_links, get_links, is_url
from authentication import authenticate_hackmd, USER_AGENT

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("link-rot-detection")

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
    link = link.lstrip("/")
    if not link.endswith(".md"):
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


def check_link(session, link):
    """
    Checks to see if a link is valid

    Args:
        session: requests.Session, current session to make requests with
        link: str, the link to check
    Returns:
        status_code: int, the status code of the request
    """
    if is_url(link):
        return check_external_link(session, link)
    else:
        return check_relative_link(link)


def check_links(session, links, cache):
    """
    Checks a list of links and returns a list of errors

    Args:
        session: requests.Session, current session to make requests with
        link: list of strs, where each str is a link
        cache: dict, that maps links to return codes
    Returns:
        errors: list of strs, where each str is an error message for a link
    """
    errors = []
    for link in links:
        if link in cache:
            continue
        return_code = check_link(session, link)
        cache[link] = return_code
        log_msg = f"[{return_code}] {link}"
        if is_success_code(return_code):
            core.info(f"  {log_msg}")
        else:
            core.error(f"  {log_msg}")
            errors.append(log_msg)
    return errors


def detect_link_rot(skip_links):
    """
    Iterates over markdown files in the root directory, downloading any
    external images and replacing the urls with relative links

    Args:
        skip_links: Set of links to skip over
    """
    session = authenticate_hackmd(logger)

    md_files = get_files(".", logger, [".md"])
    md_files = md_files[".md"]
    all_errors = {}
    cache = {}
    for md_file in md_files:
        core.info(f"Checking {md_file}...")
        links = get_links(md_file)
        links += get_image_links(md_file)
        links = list(filter(lambda x: x not in skip_links, links))
        all_errors[md_file] = check_links(session, links, cache)

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
