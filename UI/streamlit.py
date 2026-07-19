import uuid

import requests
import streamlit as st

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Smart Document Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart Document Assistant")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("Upload Documents")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF or TXT",
    type=["pdf", "txt", "md"]
)


if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    if st.sidebar.button("Upload"):

        response = requests.post(
            f"{API_URL}/documents/upload",
            files=files
        )

        if response.status_code == 200:
            st.sidebar.success("Document Uploaded")

        else:
            st.sidebar.error("Upload Failed")


st.sidebar.subheader("Uploaded Documents")

documents = requests.get(
    f"{API_URL}/documents"
).json()

for doc in documents:
    st.sidebar.write(doc)

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


prompt = st.chat_input(
    "Ask a question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)



response = requests.post(

    f"{API_URL}/chat",

    json={

        "session_id": st.session_state.session_id,

        "message": prompt

    }

).json()


answer = response["answer"]

st.session_state.messages.append(
    {
        "role": "assistant",
        "content": answer
    }
)

with st.chat_message("assistant"):

    st.markdown(answer)


with st.expander("📚 Sources"):

    for source in response["citations"]:

        st.write(source)


with st.expander("🧠 Agent Reasoning"):

    st.json(
        response["reasoning"]
    )


if st.sidebar.button("Load History"):

    history = requests.get(

        f"{API_URL}/chat/"

        f"{st.session_state.session_id}/history"

    ).json()

    st.sidebar.json(history)
