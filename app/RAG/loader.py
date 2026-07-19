from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)


class DocumentLoader:

    def load_document(self, file_path: str):

        suffix = Path(file_path).suffix.lower()

        if suffix == ".pdf":
            loader = PyPDFLoader(file_path)

        elif suffix in [".txt", ".md"]:
            loader = TextLoader(file_path, encoding="utf-8")

        else:
            raise ValueError("Unsupported file format")

        return loader.load()