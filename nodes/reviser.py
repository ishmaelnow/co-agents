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

def revise(state: SecretaryState) -> SecretaryState:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a reviser agent."),
        ("human", "Revise the following letter based on the reflection.\n\nTask: {task}\nLetter: {letter}\nReflection: {reflection}")
    ])
    chain = prompt | llm
    response = chain.invoke({
        "task": state.task,
        "letter": state.letter,
        "reflection": state.reflection
    })
    return state.copy(update={"letter": response.content})  # ✅ Extract .content