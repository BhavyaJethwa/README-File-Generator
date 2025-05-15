from backend.graph.prompts.prompts import readme_generator_promt
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from backend.graph.state import ReadmeGraphState

llm = ChatOpenAI(model="gpt-4.1-2025-04-14")

generate_chain = readme_generator_promt | llm | StrOutputParser()




