from backend.graph.prompts.prompts import readme_reviewer_promt
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from backend.graph.state import ReadmeGraphState

llm = ChatOpenAI(model="gpt-4.1-2025-04-14")

reviewer_chain = readme_reviewer_promt | llm | StrOutputParser()
