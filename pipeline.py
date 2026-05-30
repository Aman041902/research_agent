from agents import build_search_agent, build_reader_agent, writer_chain,critic_chain
from langchain_core.messages import ToolMessage

def research_pipeline(topic: str) -> dict:
    state = {}

    print(f"Starting research pipeline for topic: {topic}")
    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        "messages": [("user", f"Conduct a web search on the topic: {topic} ")]
    })

    # print("-" * 50)

    # print(search_results['messages'][2])  # Print the ToolMessage object
    # print("-" * 50)

    state['search_results'] = search_results['messages'][2].content
    print("Search completed. Extracting URLs for reading...")

    reader_agent = build_reader_agent()
    reading_tasks = reader_agent.invoke({
        "messages": [("user", f"Extract the URLs from the search results and scrape their content. Search Results: {state['search_results']}")]
    })

    state['reading_results'] = reading_tasks['messages'][-1].content
    print("Reading completed. Generating research report...")

    combined_research = f"Search Results:\n{state['search_results']}\n\nReading Results:\n{state['reading_results']}"

    writer_result = writer_chain.invoke({
        "topic": topic,
        "research": combined_research
    })

    state['report'] = writer_result
    print("Report generation completed. Critiquing the report...")

    critic_result = critic_chain.invoke({
        "report": state['report']
    })

    state['critic'] = critic_result
    


    return state

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    
    research_pipeline(topic)
