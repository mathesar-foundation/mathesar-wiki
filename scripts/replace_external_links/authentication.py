import requests
from bs4 import BeautifulSoup

def authenticate(email, password, url):
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
    if res.status_code == 200:
        return session
    else:
        return None
