"""Prototipo interactivo de investigación.

Usa la API de langchain 1.x: `create_agent(model, system_prompt, response_format)`.
La respuesta estructurada se obtiene de `result["structured_response"]`.
"""

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from langchain.agents import create_agent
from tools import save_tool, search_tool, wiki_tool

load_dotenv()

llm = ChatOpenAI(
    base_url="http://127.0.0.1:8080/v1",
)


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


SYSTEM_PROMPT = (
    "You are a research assistant that helps generate a research paper. "
    "Answer the user query and use necessary tools. "
    "Cite the sources you find."
)


def main():
    tools = [search_tool, wiki_tool, save_tool]
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        response_format=ResearchResponse,
    )

    query = input("What can I help you research? ")
    result = agent.invoke({"messages": [HumanMessage(content=query)]})

    structured_response = result.get("structured_response")
    if structured_response is not None:
        print(structured_response)
    else:
        print("No se pudo obtener una respuesta estructurada.")
        for message in result.get("messages", []):
            print(message)


if __name__ == "__main__":
    main()
