from agents import build_search_agent, reader_agent, writer_chain,critic_chain


def research_pipeline(topic: str) -> dict:
    state = {}

    print(f"Starting research pipeline for topic: {topic}")
    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        "messages": [("user", f"Conduct a web search on the topic: {topic} ")]
    })

    state['search_results'] = search_results['messages'][-1].content
    print("Search completed. Extracting URLs for reading...")

    reader_agent = reader_agent()
    reading_tasks = reader_agent.invoke({
        "messages": [("user", f"Extract the URLs from the search results and scrape their content. Search Results: {state['search_results'][:800]}")]
    })

    state['reading_results'] = reading_tasks['messages'][-1].content
    print("Reading completed. Generating research report...")
