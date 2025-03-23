from crewai import Crew, Agent, Task
from crewai_tools import RagTool, WebsiteSearchTool
from dotenv import load_dotenv

load_dotenv()

def run_crew(url, question):
    
    config = {
        "llm": {
        "provider": "google",
        "config": {
            "model": "gemini-1.5-flash",
        }
    }
    }

    rag_tool = RagTool(config=config)

    rag_tool.add(data_type="web_page", source=url)

    # rag_tool = WebsiteSearchTool(website=url)


    especialista = Agent(
        role="Analista de Pesquisa",
        goal=f"Encontrar as informações necessárias para responder à pergunta: {question}",
        backstory="Você é um pesquisador experiente com atenção aos detalhes.",
        allow_delegation=False,
        tools=[rag_tool]
    )

    responder = Agent(
        role="Especislita em responder e explicar",
        goal=f"Entende os conteúdos pesquisados e encontrados e responde a {question}. Responder de forma clara e estrutrua se for necessário",
        backstory="Você é um expert em responder questões.",
        allow_delegation=False,
        tools=[rag_tool]
    )

    research_task = Task(
        description=f"""
            Sempre responda em português
            Use a ferramenta rag_tool para buscar o documento necessário para responder à pergunta: {question}. 
            Traga o trecho relevante para responder a questão
            Sempre chame a Tool e retorne o output da tool
        """,
        expected_output="""Retorne sempre o output da tool""",
        agent=especialista,
        verbose=True
    )

    
    responder_taks = Task(
        description=f"""
            Sempre responda em português
            Use o conteúdo encontrado para responder a questão: {question}
            Responda de forma estutura e clara 
            Usanod título, negrito e espaços e outros recursos se for necessário
        """,
        expected_output="""Uma boa resposta a a questão: {question}""",
        agent=responder,
        verbose=True
    )

    crew = Crew(
        agents=[especialista, responder],
        tasks=[research_task, responder_taks],
        verbose=True
    )
    
    result = crew.kickoff({"question": question})
    return result

