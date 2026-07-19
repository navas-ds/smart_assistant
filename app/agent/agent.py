from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent

from langchain_core.prompts import ChatPromptTemplate

from app.config import settings

from .tools import TOOLS

llm = ChatGoogleGenerativeAI(

    model=settings.MODEL_NAME,

    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Smart Document Assistant.

Always decide which tools are needed.

If document information is required,
use document_search.

If calculations are needed,
use calculator.

If user asks for current time,
use datetime_tool.

Explain answers clearly.
"""
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)

agent = create_tool_calling_agent(

    llm,

    TOOLS,

    prompt
)

executor = AgentExecutor(

    agent=agent,

    tools=TOOLS,

    verbose=True,

    return_intermediate_steps=True
)
