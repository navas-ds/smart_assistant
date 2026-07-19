from .vectorstore import VectorStore


class Retriever:

    def __init__(self):

        self.vectorstore = VectorStore()

    def retrieve(self, query):

        retriever = self.vectorstore.as_retriever()

        return retriever.invoke(query)