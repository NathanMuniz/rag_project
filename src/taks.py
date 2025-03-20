from crewai import Task
from agentes import knowledge_expert
from crewai.project import CrewBase, agent, crew, task


reserach_task = Task(
        description="""
            Use the document to response the quesiton: {question}.
        """,
        expected_output="""
          A response of the {question}
        """,
        agent=knowledge_expert
    )