import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from state import SecretaryState

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def generate(state: SecretaryState) -> SecretaryState:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a company secretary."),
        ("human", """Write a professional letter for the following task.

Task: {task}

If available, incorporate relevant insights from this search reflection:
{search_reflection}""")
    ])
    chain = prompt | llm
    response = chain.invoke({
        "task": state.task,
        "search_reflection": state.search_reflection or "No external insights available."
    })
    return state.copy(update={"letter": response.content})