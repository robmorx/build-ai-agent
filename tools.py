"""Herramientas del prototipo de investigación.

`langchain_community` está descontinuado, así que las herramientas se
construyen con `langchain_core` sobre `ddgs` (buscador web) y el paquete
`wikipedia`.
"""

from datetime import datetime

from ddgs import DDGS
from langchain_core.tools import Tool
from wikipedia import summary as wiki_summary


def search_to_text(query: str, max_results: int = 5) -> str:
    """Busca en la web con DuckDuckGo y devuelve título, URL y resumen de cada resultado."""
    results = DDGS().text(query, max_results=max_results)
    if not results:
        return "No se encontraron resultados."
    lines = []
    for result in results:
        title = result.get("title", "")
        url = result.get("href", "")
        body = result.get("body", "")
        lines.append(f"- {title}\n  {url}\n  {body}")
    return "\n".join(lines)


def wiki_to_text(query: str, sentences: int = 5) -> str:
    """Devuelve el resumen de una página de Wikipedia (paquete `wikipedia`)."""
    try:
        return wiki_summary(query, sentences=sentences)
    except Exception as exc:
        return f"No se encontró una página de Wikipedia para '{query}': {exc}"


search_tool = Tool(
    name="search",
    func=search_to_text,
    description="Search the web for information",
)

wiki_tool = Tool(
    name="wiki",
    func=wiki_to_text,
    description="Get a summary from Wikipedia",
)


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)
