import requests

from bs4 import BeautifulSoup
from smolagents import tool


@tool
def fetch_webpage(url: str) -> str:
    """
    Fetches and extracts text content from a webpage.

    Args:
        url: Webpage URL to fetch and parse.

    Returns:
        Extracted webpage text content limited to 5000 characters.
    """

    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    return soup.get_text(separator="\n")[:5000]


@tool
def get_status_code(url: str) -> str:
    """
    Retrieves the HTTP status code of a webpage.

    Args:
        url: Webpage URL to check.

    Returns:
        HTTP status code as a formatted string.
    """

    response = requests.get(url, timeout=10)

    return f"Status Code: {response.status_code}"


@tool
def extract_links(url: str) -> str:
    """
    Extracts hyperlinks from a webpage.

    Args:
        url: Webpage URL to scan for links.

    Returns:
        Newline-separated list of extracted links.
    """

    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        links.append(a["href"])

    return "\n".join(links[:100])