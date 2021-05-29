import requests
from bs4 import BeautifulSoup


def check_hackmd_login(res):
    """
    Checks response content to see if login was succesful
    """
    soup = BeautifulSoup(res.text, "lxml")
    if soup.find(id="hackmd-app"):
        return True
    return False


def authenticate(email, password, url):
    """
    Return an authenticated Session

    Args:
        email: str, email to login with
        password: str, password to login with
        url: str, url to send login request to
    Returns:
        request.Session is login was succesful, otherwise None

    Currently only works for https://hackmd.io/login
    """
    session = requests.Session()
    body = (f"email={requests.utils.quote(email)}&"
            f"password={requests.utils.quote(password)}")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "Python Script"
    }

    # Get CSRF token
    res = session.get(url)
    if res.status_code != 200:
        return None
    soup = BeautifulSoup(res.text, "lxml")
    csrf_token = soup.select_one('meta[name="csrf-token"]')['content']
    headers["X-XSRF-Token"] = csrf_token

    res = session.post(url, data=body, headers=headers)
    if res.status_code == 200 and check_hackmd_login(res):
        return session
    else:
        return None


if __name__ == "__main__":
    print(authenticate("fake@email.com", "password",
                       "https://hackmd.io/login"))
