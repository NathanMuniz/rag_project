from crewai import Task
from agentes import especialista

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
