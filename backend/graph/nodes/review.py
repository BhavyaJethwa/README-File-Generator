from backend.graph.state import ReadmeGraphState
from backend.graph.chains.review_chain import reviewer_chain
from langchain_core.messages import HumanMessage

def review_readme(state: ReadmeGraphState) -> ReadmeGraphState:
    print("---Reviewing the README---")
    """
    Reviews the README and determines if it needs to be rewritten.
    Updates the state with the review result and any suggested changes.
    """
    readme = state['readme']
    history = state["history"]
    context = state['context']
    response = reviewer_chain.invoke({
        "readme": readme,
        "history": history
    })

    # Basic heuristic: if response contains "missing", "should", or "suggest", we assume rewrite is needed
    trigger_words = ["missing", "should", "suggest", "recommend", "could improve"]
    needs_rewrite = any(word in response.lower() for word in trigger_words)

    # Append review message to history
    state["history"].append(HumanMessage(content=f"Review:\n{response}"))
    state["needs_rewrite"] = needs_rewrite
    state["turn"] += 1
    print("State turn value",state["turn"])
    print("---Review Complete---")
    return state
