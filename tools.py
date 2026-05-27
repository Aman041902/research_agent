from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
  """Search the web for the given query and return the Titles,URLs and descriptions."""
  results = tavily.search(query,max_results=3)
  out = []
  for r in results['results']:
    out.append(f"Title: {r['title']}\nURL: {r['url']}\nDescription: {r['content']}\n")

  return out

@tool
def scrape_url(url:str) -> str:
  """Scrape the content of the given URL and return the text."""
  try:
    response = requests.get(url,timeout=10,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
        tag.decompose()
    
    return soup.get_text(separator=' ', strip=True)[:1000]
  except Exception as e:
    return f"Error scraping the URL: {e}"




