from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import shutil
import os

from app.rag.loader import DocumentLoader
from app.rag.chunker import Chunker
from app.rag.vectorstore import VectorStore

from app.agent.agent import executor
from app.memory.memory import get_history

router = APIRouter()

UPLOAD_FOLDER = "documents"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):

    path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    docs = DocumentLoader().load_document(path)

    chunks = Chunker().split(docs)

    VectorStore().add_documents(chunks)

    return {

        "filename": file.filename,

        "status": "uploaded"
    }



@router.get("/documents")

def list_documents():

    return os.listdir("documents")




@router.post("/chat")

def chat(request):

    history = get_history(request.session_id)

    history.add_user_message(request.message)

    result = executor.invoke(

        {

            "input": request.message

        }

    )

    history.add_ai_message(

        result["output"]

    )

    return {

        "answer": result["output"],

        "reasoning": result["intermediate_steps"]
    }

@router.get("/chat/{session_id}/history")

def history(session_id: str):

    chat_history = get_history(session_id)

    return [

        {

            "type": msg.type,

            "content": msg.content

        }

        for msg in chat_history.messages

    ]
