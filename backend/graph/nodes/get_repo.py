from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers.language.language_parser import LanguageParser
from langchain.text_splitter import Language
from backend.graph.state import ReadmeGraphState
from langchain_core.messages import HumanMessage
import uuid

def get_documents(state:ReadmeGraphState):
    print("---Getting your repository---")
    repo_path = f"./backend/repo/clonedrepo_{uuid.uuid4()}"

    repository = state['repository']
    repo = Repo.clone_from(repository,to_path=repo_path)

    loader = GenericLoader.from_filesystem(
        repo_path,
        glob="**/*",
        suffixes=[
        # Code files
        ".py", ".js", ".ts", ".java", ".cpp", ".c", ".cs", ".go", ".rs", ".rb", ".php", ".swift", ".kt", ".scala",
        # Notebooks and Markdown
        ".ipynb", ".md", ".markdown", ".rst",
        # HTML/CSS and frontend
        ".html", ".css", ".scss", ".sass",
    ],
        parser = LanguageParser(language=Language.PYTHON)
    )

    docs = loader.load()
    context = "\n".join([doc.page_content for doc in docs])
    state["context"] = context
    state["history"]=[HumanMessage(content="Please generate a README for the given context")]
    state["readme"] = ""
    state['needs_rewrite'] = False
    state["turn"] = 0
    print("---Repository fetched successfully---")
    return state