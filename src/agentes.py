

from crewai import Agent
from crewai_tools import RagTool



rag_tool = RagTool()
rag_tool.add(data_type="web_page", source="https://moneyp.com.br/sobre/")


especialista = Agent(
        role="Research Analyst",
        goal="Find necessary information to answer the question: {question}",
        backstory="You are an experienced researcher with attention to detail",
        allow_delegation=False,
        tools=[rag_tool]
    )

