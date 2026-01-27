import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code != 200:
        raise RuntimeError(
            f"Website blocked or unavailable (status {response.status_code})"
        )

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    return " ".join(soup.get_text(separator=" ").split())
