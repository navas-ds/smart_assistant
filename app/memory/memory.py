from langchain_community.chat_message_histories import ChatMessageHistory

history_store = {}


def get_history(session_id):

    if session_id not in history_store:

        history_store[session_id] = ChatMessageHistory()

    return history_store[session_id]
