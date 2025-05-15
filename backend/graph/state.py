from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class ReadmeGraphState(TypedDict):
    repository: str
    context: str                     # The extracted GitHub repo context (source code text)
    history: List[BaseMessage]       # Full conversation history passed to the prompt
    readme: str                      # The latest generated README.md
    needs_rewrite: bool              # Result from reviewer: does it need rewriting?
    turn: int                        # Iteration counter for retry limit
