from typing import List

from crewai import Agent, Task, LLM, Crew
from crewai.tools import tool
from crewai_tools import RagTool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

rag_tool = RagTool()
rag_tool.add(data_type="web_page", source="https://moneyp.com.br/sobre/")


inputs={
        'question': 'Quando começou a bmp?',
}



especialista = Agent(
        role="Research Analyst",
        goal="Find necessary information to answer the question: {question}",
        backstory="You are an experienced researcher with attention to detail",
        allow_delegation=False,
        tools=[rag_tool]
    )



research_task = Task(
    description="""
        Use the rag_tool to serach necessary document to reponse the {question}. 
        Resonse the question in a especislit way
    """,
    expected_output="""
        A good aswer for the question. 
    """,
    agent=especialista,
    verbose=True
)

crew = Crew(
    agents=[especialista],
    tasks=[research_task],
    verbose=True
)
result = crew.kickoff(inputs)
print(result)