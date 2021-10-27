import os
import urllib3
from concurrent import futures
import multiprocessing as mp
from collections import defaultdict
import requests

from actions_toolkit import core

from util.markdown import get_image_links, get_links
from util.links import get_files, is_url, resolve_wiki_link
from util.authentication import authenticate_hackmd, USER_AGENT

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SKIP_LINKS = {
    "http://matrix.mathesar.org/",
    "https://staging.mathesar.org/",
    "https://github.com/centerofci/mathesar-ansible",
    "https://github.com/centerofci/mathesar-scripts",
    "https://github.com/centerofci/mathesar-wiki",
    "https://github.com/orgs/centerofci/projects/1",
    "https://github.com/orgs/centerofci/projects/1/views/1",
    "https://github.com/orgs/centerofci/projects/1/views/3",
    "https://github.com/orgs/centerofci/projects/1/views/17",
}
HEADERS = {"User-Agent": USER_AGENT}
TIMEOUT = 10.0


def link2path(link):
    """
    Convert wiki.js style relative link to file path
    """
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
    if return_code >= 200 and return_code < 400:
        return True
    return False


def check_external_link(session, link):
    """
    Checks if an external link exists
    """
    try:
        response = session.get(link,
                               verify=False,
                               headers=HEADERS,
                               timeout=TIMEOUT)
        return response.status_code
    except requests.exceptions.ReadTimeout:
        return 404


def check_local_link(link, file):
    """
    Checks if a local link exists
    """
    link = resolve_wiki_link(link, file)
    if link is not None and os.path.exists(link):
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
    if is_url(link["link"]):
        if link["link"] in cache:
            link["return_code"] = cache[link["link"]]
        else:
            link["return_code"] = check_external_link(session, link["link"])
            cache[link["link"]] = link["return_code"]
    else:
        link["return_code"] = check_local_link(link["link"], link["file"])

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
    Gathers all links (image and otherwise) in the root directory, then
    checks whether they are reachable or not.

    Args:
        skip_links: list of links to skip over
    """
    session = authenticate_hackmd()

    # Get all files
    md_files = get_files(".", [".md"])
    md_files = md_files[".md"]

    # Get all links
    links = []
    for md_file in md_files:
        f = md_file.lstrip("./")
        links += [{"link": l, "file": f} for l in get_links(md_file)]
        links += [{"link": l, "file": f} for l in get_image_links(md_file)]

    # Process links
    skip_links = set(skip_links)
    links = [l for l in links if l["link"] not in skip_links]
    links = check_links(session, links)

    # Map errors to files
    all_errors = defaultdict(list)
    for link in links:
        if not is_success_code(link["return_code"]):
            error = f"[{link['return_code']}] {link['link']}"
            all_errors[link["file"]].append(error)

    # Build final error message
    count = 0
    error_msg = ""
    for md_file, errors in all_errors.items():
        error_msg += f"\n{md_file}:"
        count += len(errors)
        for error in errors:
            error_msg += f"\n  {error}"
    if error_msg:
        error_msg = f"{count} Broken links found!" + error_msg
        core.set_failed(error_msg)


if __name__ == "__main__":
    detect_link_rot(SKIP_LINKS)
