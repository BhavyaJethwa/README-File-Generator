from backend.graph.state import ReadmeGraphState
from backend.graph.chains.generate_chain import generate_chain
from langchain_core.messages import HumanMessage



def generate_readme(state:ReadmeGraphState):
    print("---Generating README---")
    context = state["context"]
    history = state["history"]
    readme = generate_chain.invoke({"context":context, "history":history})
    state["readme"] = readme
    state["history"].append(HumanMessage(content=f"Generated README:\n{readme}"))
    state["needs_rewrite"] = False 
    print("---Generation Complete---")
    return state
