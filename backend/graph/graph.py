from dotenv import load_dotenv
from langgraph.graph import START,END , StateGraph
from backend.graph.nodes.get_repo import get_documents
from backend.graph.nodes.generate import generate_readme
from backend.graph.nodes.review import review_readme
from backend.graph.state import ReadmeGraphState

workflow = StateGraph(ReadmeGraphState)

workflow.add_node("get_repo", get_documents)
workflow.add_node("generate", generate_readme)
workflow.add_node("review" , review_readme)

MAX_ITERATIONS = 2
def route_review(state:ReadmeGraphState):
    if not state["needs_rewrite"]:
        print("Review passed")
        return END
    elif state["turn"] >= MAX_ITERATIONS:
        print("MAX iterations done")
        return END
    else:
        print("README Generation count:", state["turn"])
        return "generate"

workflow.add_edge(START, "get_repo")
workflow.add_edge("get_repo", "generate")
workflow.add_edge("generate", "review")
workflow.add_conditional_edges(
    "review",
    route_review,
    path_map={
        "generate": "generate",
        END : END
    }
)
workflow.add_edge("review",END)
graph = workflow.compile()


