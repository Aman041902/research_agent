from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url 
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.1,
)

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a professional research analyst and technical writer. "
        "Create well-structured, accurate, and insightful research reports "
      
    ),
    (
        "human",
        """Prepare a comprehensive research report based on the information provided below.

Topic:
{topic}

Collected Research:
{research}

Requirements:
- Write in a professional, factual, and analytical style.
- Explain concepts clearly with supporting details and examples where relevant.
- Organize the report using the following structure:

1. Introduction
   - Brief overview of the topic
   - Importance and context

2. Key Findings
   - Include at least 3 detailed findings
   - Each finding should have its own heading and explanation
   - Highlight trends, insights, comparisons, or notable observations

3. Conclusion
   - Summarize the major insights
   - Provide a concise final assessment

4. Sources
   - List all source URLs referenced in the research
"""
    )
])

writer_chain = writer_prompt | llm | StrOutputParser() 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:

Areas to Improve:

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()