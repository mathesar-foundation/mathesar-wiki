import requests
from bs4 import BeautifulSoup

def check_login(res):
    content = str(res.content)
    if "User not found or password not set." in content:
        return False
    return True

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
    if res.status_code == 200 and check_login(res):
        return session
    else:
        return None

if __name__ == "__main__":
    print(authenticate("fake@email.com", "password",
                       "https://hackmd.io/login"))
