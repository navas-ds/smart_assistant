from langchain_chroma import Chroma

from app.config import settings

from .embeddings import get_embedding_model


class VectorStore:

    def __init__(self):

        self.embedding = get_embedding_model()

        self.db = Chroma(

            persist_directory=settings.VECTOR_DB_PATH,

            embedding_function=self.embedding
        )

    def add_documents(self, docs):

        self.db.add_documents(docs)

    def as_retriever(self):

        return self.db.as_retriever(

            search_kwargs={
                "k": settings.TOP_K
            }
        )