from crewai import  Crew
from agentes import especialista
from taks import research_task

inputs={
        'question': 'Quando começou a bmp?',
}

crew = Crew(
    agents=[especialista],
    tasks=[research_task],
    verbose=True
)
result = crew.kickoff(inputs)
print(result)