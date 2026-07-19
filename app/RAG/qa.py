from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from app.config import settings
from .prompts import SYSTEM_PROMPT


class QAEngine:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(

            model=settings.MODEL_NAME,

            temperature=0
        )

    def answer(self, query, docs):

        context = "\n\n".join(
            d.page_content for d in docs
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_PROMPT),
                (
                    "human",
                    "Context:\n{context}\n\nQuestion:\n{question}"
                )
            ]
        )

        chain = prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "question": query
            }
        )

        citations = []

        for doc in docs:

            metadata = doc.metadata

            citations.append({

                "document": metadata.get("source"),

                "page": metadata.get("page")
            })

        return {
            "answer": response.content,
            "citations": citations
        }