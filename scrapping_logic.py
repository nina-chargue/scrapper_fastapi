from bs4 import BeautifulSoup
from typing import List

# Website scraping functions
def extract_body_content(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return None

def clean_body_content(body_content: str) -> str:
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(["script", "style", "header", "footer", "nav", "aside"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content

def split_dom_content(dom_content: str, max_length: int = 4000) -> List[str]:
    if len(dom_content) <= max_length:
        return [dom_content]
    
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]