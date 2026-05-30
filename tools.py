from langchain.tools import tool
import requests
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str):
    """Search the web and return structured results."""
    
    results = tavily.search(query, max_results=3)

    out = []

    for r in results["results"]:
        out.append({
            "title": r["title"],
            "url": r["url"],
            "description": r["content"]
        })

    return out

@tool
def scrape_url(url: str) -> dict:
    """Scrape a URL via Jina Reader (handles JS-rendered pages)."""
    try:
        jina_url = f"https://r.jina.ai/{url}"
        response = requests.get(
            jina_url,
            timeout=30,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        # Jina returns clean markdown text directly
        text = response.text
        title_line = next(
            (l for l in text.splitlines() if l.startswith("Title:")), ""
        )
        title = title_line.replace("Title:", "").strip() or "No title"

        return {"url": url, "title": title, "content": text[:5000]}

    except Exception as e:
        return {"url": url, "error": str(e)}
