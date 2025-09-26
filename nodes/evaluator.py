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

def evaluate(state: SecretaryState) -> SecretaryState:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an evaluator."),
        ("human", "Score the letter out of 10 and explain briefly:\nTask: {task}\nLetter: {letter}")
    ])
    chain = prompt | llm
    response = chain.invoke({
        "task": state.task,
        "letter": state.letter
    })
    return state.copy(update={"evaluation": response.content})  # ✅ Extract .content