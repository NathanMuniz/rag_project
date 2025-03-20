from crewai_tools import RagTool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

rag_tool = RagTool()

# rag_tool.add(data_type="file", path="path/to/your/document.pdf")

# rag_tool.add(data_type="web_page", url="https://pt.wikipedia.org/wiki/Stephen_Hawking")

rag_tool.add(data_type="web_page", source="https://docs.crewai.com")

knowledge_expert = Agent(
        role="Research Analyst",
        goal="Find necessary information to answer the question: {question}",
        backstory="You are an experienced researcher with attention to detail",
        allow_delegation=False,
        tools=[rag_tool]
    )


