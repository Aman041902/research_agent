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

results = web_search.invoke("Recent development in Open-Source LLMs")


for i in results:
  print(i)
  print("\n\n")

