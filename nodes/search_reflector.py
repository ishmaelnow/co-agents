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

def reflect_search(state: SecretaryState) -> SecretaryState:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a search reflection agent."),
        ("human", "Analyze the following search result for clarity, relevance, and usefulness:\n\nTask: {task}\nSearch Result: {search_result}")
    ])
    chain = prompt | llm
    response = chain.invoke({
        "task": state.task,
        "search_result": state.search_result
    })
    return state.copy(update={"search_reflection": response.content})