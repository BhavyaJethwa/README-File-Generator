from fastapi import FastAPI, Request
from pydantic import BaseModel
from backend.graph.graph import graph
from backend.graph.state import ReadmeGraphState
from langchain.schema import BaseMessage
import re
from dotenv import load_dotenv
import os
load_dotenv()
from fastapi.middleware.cors import CORSMiddleware

# Replace this with your actual LangGraph logic
def run_langgraph_agent(repo_url: str) -> str:
    print("Running README Generator...")

    initial_state: ReadmeGraphState = {
        "repository": repo_url,
        "context": "",             # Start with empty context
        "history": [],             # Start with empty message history
        "readme": "",              # Empty until generated
        "needs_rewrite": False,
        "turn": 0
    }

    final_state: ReadmeGraphState = graph.invoke(initial_state)

    print("Graph execution completed.")
    return final_state["readme"]
    

def clean_markdown_wrapping(text: str) -> str:
    # Remove starting and ending triple backticks and optional language tag
    return re.sub(r"^```(?:\w+)?\s*|\s*```$", "", text.strip())

app = FastAPI()

# Allow CORS so Streamlit can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    repo_url: str

@app.post("/generate_readme")
async def generate_readme(request: RepoRequest):
    raw_readme = run_langgraph_agent(request.repo_url)
    cleaned_readme = clean_markdown_wrapping(raw_readme)
    return {"readme": cleaned_readme} 
