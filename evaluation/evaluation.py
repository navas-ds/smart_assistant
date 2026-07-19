import json

from app.rag.qa import QAEngine
from app.rag.retriever import Retriever

qa = QAEngine()

retriever = Retriever()

with open("evaluation/dataset.json") as f:

    dataset = json.load(f)

score = 0

for item in dataset:

    docs = retriever.retrieve(item["question"])

    answer = qa.answer(
        item["question"],
        docs
    )

    if item["expected"].lower() in answer["answer"].lower():

        score += 1

print(score / len(dataset))
